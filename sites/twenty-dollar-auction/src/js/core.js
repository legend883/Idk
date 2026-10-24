/* Core: mode registry, game state, and the auction rules.
   Every money change goes through the functions in this file so the rules live in one place. */
window.TDA = (function () {
  'use strict';

  var T = { modes: [], modeById: {}, START_MONEY: 20 };

  var CATS = {
    dream: 'Build Your Dream',
    food: 'Food & Entertainment',
    action: 'Action & Imagination',
    custom: 'Your Own Modes'
  };
  T.CATS = CATS;

  // Player ink colors: picked to stay distinct from each other on newsprint white.
  T.PLAYER_COLORS = ['#E4002B', '#0072CE', '#00A651', '#FF8200', '#7B2CBF', '#00B5B8', '#E6007E', '#6B4226'];

  /* ---------- mode registry ---------- */

  function parseItem(s) {
    var p = String(s).split('|');
    var item = { name: (p[0] || '').trim(), desc: (p[1] || '').trim(), emoji: (p[2] || '').trim() || '⭐', color: null, shape: null };
    if (item.desc === 'Name') item.desc = 'A name worth fighting for';
    if (p[3]) p[3].split(':').forEach(function (bit) {
      bit = bit.trim();
      if (!bit) return;
      if (bit.charAt(0) === '#') item.color = bit; else item.shape = bit;
    });
    return item;
  }

  function normalizeMode(m) {
    var mode = {
      id: m.id, name: m.name, cat: m.cat || 'custom', kind: m.kind || 'collage', skin: m.skin || m.kind,
      blurb: m.blurb || '', ai: m.ai || ('a dream ' + m.name.replace(/^Dream /, '')),
      cover: m.cover || ['⭐'], color: m.color || '#00A6E8', custom: !!m.custom,
      rounds: m.rounds.map(function (r) {
        return { label: r[0], part: r[1] || 'spot', items: r[2].map(parseItem) };
      })
    };
    return mode;
  }

  T.addModes = function (list) {
    list.forEach(function (m) {
      var mode = normalizeMode(m);
      if (T.modeById[mode.id]) T.modes = T.modes.filter(function (x) { return x.id !== mode.id; });
      T.modes.push(mode);
      T.modeById[mode.id] = mode;
    });
  };
  T.removeMode = function (id) {
    delete T.modeById[id];
    T.modes = T.modes.filter(function (x) { return x.id !== id; });
  };

  /* ---------- storage (always optional) ---------- */

  T.store = {
    get: function (k, fallback) {
      try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : fallback; } catch (e) { return fallback; }
    },
    set: function (k, v) {
      try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; }
    },
    del: function (k) { try { localStorage.removeItem(k); } catch (e) { /* storage blocked */ } }
  };

  /* ---------- small utilities ---------- */

  T.uid = function () { return Math.random().toString(36).slice(2, 9); };
  T.hash = function (s) {
    var h = 2166136261;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  };
  T.rng = function (seed) {
    var a = seed >>> 0 || 1;
    return function () {
      a |= 0; a = a + 0x6D2B79F5 | 0;
      var t = Math.imul(a ^ a >>> 15, 1 | a);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  };
  T.esc = function (s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  };

  /* ---------- game setup ---------- */

  // Pick which rounds are played (keeping the mode's order) and one random item per round.
  function drawRounds(mode, count, rand) {
    var idx = mode.rounds.map(function (_, i) { return i; });
    while (idx.length > count) idx.splice(Math.floor(rand() * idx.length), 1);
    return idx.map(function (i) {
      var r = mode.rounds[i];
      var item = r.items[Math.floor(rand() * r.items.length)];
      return { label: r.label, part: r.part, item: JSON.parse(JSON.stringify(item)) };
    });
  }

  T.newGame = function (modeId, names, opts) {
    var mode = T.modeById[modeId];
    if (!mode) throw new Error('Unknown mode');
    opts = opts || {};
    var rand = T.rng(Date.now() ^ T.hash(modeId + names.join()));
    var count = Math.min(opts.rounds || mode.rounds.length, mode.rounds.length);
    return {
      v: 1,
      id: T.uid(),
      started: Date.now(),
      modeId: modeId,
      bidStyle: opts.bidStyle === 'secret' ? 'secret' : 'live',
      players: names.map(function (n, i) {
        return {
          id: 'p' + i + T.uid(), name: n, color: T.PLAYER_COLORS[i % T.PLAYER_COLORS.length],
          balance: T.START_MONEY, wins: [], missed: [],
          ai: { status: 'idle', url: null, sig: null, error: null }
        };
      }),
      rounds: drawRounds(mode, count, rand),
      roundIndex: 0,
      phase: 'curtain',          // curtain -> preview -> bidding -> sold | unclaimed | skipped -> (next) curtain ... -> over
      auction: freshAuction(),
      history: [],
      votes: {},
      over: false
    };
  };

  function freshAuction() {
    return { log: [], secret: null, tieWith: null };
  }

  T.mode = function (g) { return T.modeById[g.modeId]; };
  T.currentRound = function (g) { return g.rounds[g.roundIndex] || null; };
  T.player = function (g, id) {
    for (var i = 0; i < g.players.length; i++) if (g.players[i].id === id) return g.players[i];
    return null;
  };
  T.spent = function (p) { return p.wins.reduce(function (s, w) { return s + w.price; }, 0); };

  /* ---------- live auction state (derived from the log, so Undo is exact) ---------- */

  T.auctionState = function (g) {
    var high = null, passed = {}, bidders = {};
    g.auction.log.forEach(function (e) {
      if (e.type === 'bid') { high = { pid: e.pid, amount: e.amount }; bidders[e.pid] = true; delete passed[e.pid]; }
      if (e.type === 'pass') passed[e.pid] = true;
    });
    return { high: high, passed: passed, bidders: bidders };
  };

  // Why a player can or cannot bid an amount right now. Returns '' when allowed.
  T.bidProblem = function (g, pid, amount) {
    var p = T.player(g, pid);
    if (!p) return 'Pick a player first.';
    if (g.phase !== 'bidding') return 'Bidding is not open.';
    if (!Number.isInteger(amount)) return 'Bids are whole dollars.';
    if (amount < 1) return 'The lowest bid is $1.';
    if (p.balance <= 0) return p.name + ' is out of money.';
    if (amount > p.balance) return p.name + ' only has $' + p.balance + '.';
    var st = T.auctionState(g);
    if (st.high && st.high.pid === pid) return p.name + ' already has the top bid.';
    if (st.high && amount <= st.high.amount) return 'Beat $' + st.high.amount + '. Bid at least $' + (st.high.amount + 1) + '.';
    return '';
  };

  T.placeBid = function (g, pid, amount) {
    var why = T.bidProblem(g, pid, amount);
    if (why) return why;
    g.auction.log.push({ type: 'bid', pid: pid, amount: amount });
    return '';
  };

  T.pass = function (g, pid) {
    var st = T.auctionState(g);
    if (g.phase !== 'bidding') return 'Bidding is not open.';
    if (st.high && st.high.pid === pid) return 'The top bidder cannot pass. Undo their bid instead.';
    if (st.passed[pid]) return '';
    g.auction.log.push({ type: 'pass', pid: pid });
    return '';
  };

  T.undo = function (g) { return g.auction.log.pop() || null; };

  // Who is still able to beat the current high bid.
  T.stillIn = function (g) {
    var st = T.auctionState(g);
    var min = st.high ? st.high.amount + 1 : 1;
    return g.players.filter(function (p) {
      return !st.passed[p.id] && !(st.high && st.high.pid === p.id) && p.balance >= min;
    });
  };

  /* ---------- round flow ---------- */

  T.reveal = function (g) { if (g.phase === 'curtain') g.phase = 'preview'; };
  T.openBidding = function (g) {
    if (g.phase !== 'preview') return;
    g.phase = 'bidding';
    g.auction = freshAuction();
    if (g.bidStyle === 'secret') T.startSecret(g, null);
  };

  // Close the auction. The top bidder pays exactly their bid; nobody else pays anything.
  T.closeAuction = function (g) {
    if (g.phase !== 'bidding') return null;
    var round = T.currentRound(g);
    var st = T.auctionState(g);
    if (!st.high) {
      g.phase = 'unclaimed';
      g.history.push({ round: g.roundIndex, result: 'unclaimed' });
      return { result: 'unclaimed' };
    }
    var winner = T.player(g, st.high.pid);
    var price = st.high.amount;
    if (price > winner.balance) return null; // can never happen through placeBid, guarded anyway
    winner.balance -= price;
    winner.wins.push({ round: g.roundIndex, label: round.label, part: round.part, item: round.item, price: price });
    Object.keys(st.bidders).forEach(function (pid) {
      if (pid !== winner.id) {
        var loser = T.player(g, pid);
        var best = 0;
        g.auction.log.forEach(function (e) { if (e.type === 'bid' && e.pid === pid) best = Math.max(best, e.amount); });
        loser.missed.push({ round: g.roundIndex, name: round.item.name, emoji: round.item.emoji, myBid: best, soldFor: price, to: winner.name });
      }
    });
    g.phase = 'sold';
    g.history.push({ round: g.roundIndex, result: 'sold', pid: winner.id, price: price });
    return { result: 'sold', winner: winner, price: price };
  };

  T.skip = function (g) {
    if (g.phase === 'sold' || g.phase === 'unclaimed' || g.phase === 'skipped' || g.over) return;
    g.phase = 'skipped';
    g.auction = freshAuction();
    g.history.push({ round: g.roundIndex, result: 'skipped' });
  };

  T.isLastRound = function (g) { return g.roundIndex >= g.rounds.length - 1; };

  T.next = function (g) {
    if (!(g.phase === 'sold' || g.phase === 'unclaimed' || g.phase === 'skipped')) return;
    if (T.isLastRound(g) || g.players.every(function (p) { return p.balance === 0; })) { T.endGame(g); return; }
    g.roundIndex += 1;
    g.phase = 'curtain';
    g.auction = freshAuction();
  };

  T.endGame = function (g) {
    g.over = true;
    g.phase = 'over';
    g.auction = freshAuction();
  };

  T.everyoneBroke = function (g) { return g.players.every(function (p) { return p.balance === 0; }); };

  /* ---------- secret (pass-the-device) bidding ---------- */

  T.startSecret = function (g, onlyIds) {
    var ids = (onlyIds || g.players.map(function (p) { return p.id; })).filter(function (id) {
      return T.player(g, id).balance > 0;
    });
    g.auction.log = [];
    g.auction.secret = { order: ids, idx: 0, entries: {}, shown: false, floor: onlyIds ? g.auction.tieWith : 0 };
  };

  T.secretProblem = function (g, pid, amount) {
    var p = T.player(g, pid);
    var s = g.auction.secret;
    if (!Number.isInteger(amount) || amount < 0) return 'Enter a whole-dollar amount.';
    if (amount > p.balance) return p.name + ' only has $' + p.balance + '.';
    if (s && s.floor && amount > 0 && amount < s.floor) return 'This is a tie-breaker: bid at least $' + s.floor + ' or pass.';
    return '';
  };

  T.secretEnter = function (g, amount) {
    var s = g.auction.secret;
    var pid = s.order[s.idx];
    var why = T.secretProblem(g, pid, amount);
    if (why) return why;
    s.entries[pid] = amount;
    s.idx += 1;
    s.shown = false;
    return '';
  };

  T.secretDone = function (g) { var s = g.auction.secret; return !!s && s.idx >= s.order.length; };

  // Turn sealed bids into a result: a single top bid becomes the live high bid; a tie asks the tied players again.
  T.secretResolve = function (g) {
    var s = g.auction.secret;
    var top = 0, tops = [];
    Object.keys(s.entries).forEach(function (pid) {
      var a = s.entries[pid];
      if (a > top) { top = a; tops = [pid]; } else if (a === top && a > 0) tops.push(pid);
    });
    if (top === 0) return { kind: 'none' };
    if (tops.length > 1) { g.auction.tieWith = top; return { kind: 'tie', ids: tops, amount: top }; }
    g.auction.log = [];
    Object.keys(s.entries).forEach(function (pid) {
      if (s.entries[pid] > 0 && pid !== tops[0]) g.auction.log.push({ type: 'bid', pid: pid, amount: s.entries[pid] });
    });
    // bids are pushed lowest-first, the winner last, so derived state keeps them as high bidder
    g.auction.log.sort(function (a, b) { return a.amount - b.amount; });
    g.auction.log.push({ type: 'bid', pid: tops[0], amount: top });
    return { kind: 'winner', pid: tops[0], amount: top };
  };

  /* ---------- results ---------- */

  T.highlights = function (p) {
    if (!p.wins.length) return [];
    var byPrice = p.wins.slice().sort(function (a, b) { return b.price - a.price; });
    var out = [{ tag: 'Prized pick', win: byPrice[0] }];
    var cheap = byPrice[byPrice.length - 1];
    if (cheap !== byPrice[0]) out.push({ tag: 'Best bargain', win: cheap });
    var mid = byPrice[Math.floor(byPrice.length / 2)];
    if (mid !== byPrice[0] && mid !== cheap) out.push({ tag: 'Crowd favorite', win: mid });
    return out;
  };

  T.VOTE_CATS = [
    ['best', 'Best Overall Creation'],
    ['creative', 'Most Creative'],
    ['value', 'Best Value'],
    ['impressive', 'Most Impressive'],
    ['funny', 'Funniest Creation'],
    ['unique', 'Most Unique']
  ];

  return T;
})();
