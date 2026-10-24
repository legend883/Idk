/* Screens and controls. One render function per screen; clicks route through data-act attributes. */
(function (T) {
  'use strict';
  var esc = T.esc;
  var app;

  var KEYS = { game: 'tda.game.v1', settings: 'tda.settings.v1', gallery: 'tda.gallery.v1', custom: 'tda.custom.v1' };
  var SETTINGS = Object.assign({ sound: true, ai: true }, T.store.get(KEYS.settings, {}));
  var GALLERY = T.store.get(KEYS.gallery, []);
  var CUSTOM = T.store.get(KEYS.custom, []);
  T.addModes(CUSTOM);
  T.Sound.on = SETTINGS.sound;

  var G = null;
  var UI = {
    screen: 'home', filter: 'all', setup: null, drawer: null, tab: 'players', overlay: null,
    toast: null, msg: '', pop: null, reveal: false, showMode: false, confirm: null,
    nextNames: null, galleryIdx: null, editor: null, editorErr: ''
  };

  /* ---------- icons (authored, one stroke weight) ---------- */
  var IC = {
    gavel: '<path d="M14 4l6 6M11 7l6 6M12.5 5.5l-5 5M18.5 11.5l-5 5M10 12l-7 7"/>',
    soundOn: '<path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M16 8.5a5 5 0 0 1 0 7M18.5 6a8.5 8.5 0 0 1 0 12"/>',
    soundOff: '<path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M17 9l5 6M22 9l-5 6"/>',
    menu: '<path d="M4 7h16M4 12h16M4 17h16"/>',
    eye: '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    minus: '<path d="M5 12h14"/>',
    x: '<path d="M6 6l12 12M18 6L6 18"/>',
    trash: '<path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/>',
    save: '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>',
    redo: '<path d="M20 12a8 8 0 1 1-2.3-5.6M20 4v5h-5"/>',
    arrow: '<path d="M5 12h14M13 6l6 6-6 6"/>',
    undo: '<path d="M9 7L4 12l5 5M4 12h11a5 5 0 0 1 0 10h-2"/>',
    skip: '<path d="M5 6l8 6-8 6zM15 6v12"/>',
    brush: '<path d="M14 4l6 6-8 8H6v-6z"/><path d="M4 20c1-3 3-4 5-4"/>',
    back: '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    flag: '<path d="M5 21V4M5 4h12l-2 4 2 4H5"/>'
  };
  function icon(n) { return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + IC[n] + '</svg>'; }

  function burst(fill, points, inner) {
    points = points || 16; inner = inner || 0.72;
    var pts = [];
    for (var i = 0; i < points * 2; i++) {
      var r = i % 2 ? 50 * inner : 50, a = (i / (points * 2)) * Math.PI * 2 - Math.PI / 2;
      pts.push((50 + Math.cos(a) * r).toFixed(1) + ',' + (50 + Math.sin(a) * r).toFixed(1));
    }
    return '<svg class="burst" viewBox="-4 -4 108 108" aria-hidden="true"><polygon points="' + pts.join(' ') + '" fill="' + fill + '" stroke="#14110F" stroke-width="3" stroke-linejoin="round"/></svg>';
  }

  /* ---------- persistence ---------- */
  function save() { if (G) T.store.set(KEYS.game, G); }
  function saveSettings() { T.store.set(KEYS.settings, SETTINGS); }

  function loadGame() {
    var g = T.store.get(KEYS.game, null);
    if (!g || g.v !== 1 || !T.modeById[g.modeId] || !Array.isArray(g.players)) return null;
    g.players.forEach(function (p) { if (p.ai && p.ai.status === 'loading') p.ai.status = p.ai.url ? 'ok' : 'idle'; });
    return g;
  }

  /* ---------- helpers ---------- */
  function money(n, cls) {
    return '<span class="money-tag ' + (cls || '') + '"><span class="cur">$</span>' + n + '</span>';
  }
  function moneyClass(p) { return p.balance === 0 ? 'zero' : p.balance <= 3 ? 'low' : ''; }
  function moneyNote(p) {
    if (p.balance === 0) return '<span class="money-note low">Out of money. Can’t bid anymore.</span>';
    if (p.balance <= 3) return '<span class="money-note low">Running low!</span>';
    return '<span class="money-note">left of $20</span>';
  }
  function creationSvg(g, p, opts) {
    opts = opts || {};
    var mode = g.modeObj || T.modeById[g.modeId];
    return T.renderCreation(mode, {
      wins: p.wins, rounds: g.rounds, playerName: p.name, color: p.color,
      newest: opts.pop && UI.pop && UI.pop.pid === p.id ? UI.pop.win : null, seed: g.id + p.id
    });
  }
  function coverArt(m, idx) {
    var c = m.cover || ['⭐'];
    return '<div class="cover-art" style="--c:' + esc(m.color) + '">' +
      '<span class="e e1">' + esc(c[0] || '⭐') + '</span>' + (c[1] ? '<span class="e e2">' + esc(c[1]) + '</span>' : '') + (c[2] ? '<span class="e e3">' + esc(c[2]) + '</span>' : '') +
      (idx != null ? '<span class="issue">No. ' + (idx + 1) + '</span>' : '') + '<span class="price">$20</span></div>';
  }
  function toast(msg) {
    UI.toast = msg;
    render();
    clearTimeout(toast.t);
    toast.t = setTimeout(function () { UI.toast = null; render(); }, 2600);
  }
  function aiChip(p) {
    if (!SETTINGS.ai || !p.wins.length) return '';
    var s = p.ai.status;
    if (s === 'loading') return '<span class="ai-chip loading"><span class="spin"></span> Painting…</span>';
    if (s === 'error') return '<span class="ai-chip error">Painting failed</span>';
    if (s === 'ok') return '<span class="ai-chip ok">Painted</span>';
    return '';
  }

  /* ---------- HOME ---------- */
  function homeScreen() {
    var h = '<div class="wrap">';
    h += '<section class="splash">' +
      '<div class="panel splash-title"><div class="splash-burst" aria-hidden="true">' + burst('#FFE94D', 14, 0.66) + '<span>$20<small>each</small></span></div>' +
      '<h1>The $20<br>Auction</h1><div class="sub">Build Your Dream</div>' +
      '<p class="lede">A bidding party game for 2 to 8 players on one phone, tablet or TV. Win items, spend wisely, and watch your creation come to life.</p>' +
      '<div class="row"><a class="btn btn-yellow btn-big" href="#modes">Pick a game ' + icon('arrow') + '</a></div></div>' +
      '<div class="howto">' +
      '<div class="panel"><span class="big">1</span><span class="caption-box step">Everyone gets $20</span><p>Play money. Nobody can borrow or go below $0.</p></div>' +
      '<div class="panel"><span class="big">2</span><span class="caption-box step">The host reveals an item</span><p>One surprise at a time. No peeking ahead.</p></div>' +
      '<div class="panel"><span class="big">3</span><span class="caption-box step">Bid or pass</span><p>Highest bid wins and pays it. Everyone else keeps their money.</p></div>' +
      '<div class="panel"><span class="big">4</span><span class="caption-box step">Build and vote</span><p>Your creation grows with every win. The family votes on the best.</p></div>' +
      '</div></section>';
    if (G && !G.over) {
      var m = T.modeById[G.modeId];
      h += '<div class="panel resume"><div class="grow"><b>Game in progress</b><div>' + esc(m.name) + ' · item ' + (G.roundIndex + 1) + ' of ' + G.rounds.length + ' · ' + G.players.map(function (p) { return esc(p.name); }).join(', ') + '</div></div>' +
        '<button class="btn btn-yellow" data-act="resume">Back to the auction ' + icon('arrow') + '</button></div>';
    }
    if (UI.nextNames) {
      h += '<div class="panel resume"><div class="grow"><b>Next game</b><div>Pick a mode for ' + UI.nextNames.map(esc).join(', ') + '.</div></div><button class="btn btn-ghost btn-small" style="--f:var(--desk-text)" data-act="clear-next">Start fresh instead</button></div>';
    }
    var cats = ['dream', 'food', 'action'];
    if (T.modes.some(function (m) { return m.cat === 'custom'; })) cats.push('custom');
    h += '<div class="shelf-head" id="modes"><h2>Choose your game</h2><div class="chips" role="group" aria-label="Filter modes">' +
      '<button class="chip" data-act="filter" data-v="all" aria-pressed="' + (UI.filter === 'all') + '">All ' + T.modes.length + '</button>' +
      cats.map(function (c) { return '<button class="chip" data-act="filter" data-v="' + c + '" aria-pressed="' + (UI.filter === c) + '">' + esc(T.CATS[c]) + '</button>'; }).join('') + '</div></div>';
    var n = 0;
    cats.forEach(function (c) {
      if (UI.filter !== 'all' && UI.filter !== c) return;
      var list = T.modes.filter(function (m) { return m.cat === c; });
      h += '<h3 class="caption-box" style="margin:18px 0 10px">' + esc(T.CATS[c]) + '</h3><div class="covers">';
      list.forEach(function (m) {
        var idx = T.modes.indexOf(m);
        var cv = '<button class="cover" data-act="pick-mode" data-id="' + esc(m.id) + '">' + coverArt(m, m.cat === 'custom' ? null : idx) +
          '<div class="cover-body"><h3>' + esc(m.name) + '</h3><p>' + esc(m.blurb) + '</p></div></button>';
        h += m.custom ? '<div class="cover-slot">' + cv + '<button class="btn btn-small edit" data-act="edit-custom" data-id="' + esc(m.id) + '">Edit</button></div>' : cv;
        n++;
      });
      if (c === 'custom' || (UI.filter === 'all' && c === 'action' && cats.indexOf('custom') < 0)) {
        h += '<button class="cover add" data-act="new-custom">' + icon('plus') + 'Make your own mode</button>';
      }
      h += '</div>';
    });
    if (GALLERY.length) {
      h += '<div class="shelf-head"><h2>Hall of creations</h2></div><div class="gallery">';
      GALLERY.slice().reverse().forEach(function (s, ri) {
        var i = GALLERY.length - 1 - ri;
        h += '<button class="panel" data-act="view-gallery" data-i="' + i + '"><b class="caption-box">' + esc(s.game.modeObj.name) + '</b><span>' + new Date(s.at).toLocaleDateString() + ' · ' + s.game.players.map(function (p) { return esc(p.name); }).join(', ') + '</span><div class="thumbs">' +
          s.game.players.slice(0, 4).map(function (p) { return creationSvg(s.game, p); }).join('') + '</div></button>';
      });
      h += '</div>';
    }
    h += '<p class="footer-note">Tip: the host can tap “Hide host desk” during the game to show only the stage on a TV. Games save in this browser automatically, so a refresh will not lose anyone’s money.</p>';
    return h + '</div>';
  }

  /* ---------- SETUP ---------- */
  function setupScreen() {
    var s = UI.setup, m = T.modeById[s.modeId];
    var h = '<div class="wrap"><div class="topbar"><button class="btn btn-small" data-act="go-home">' + icon('back') + ' All games</button><span class="spacer"></span><span class="logo">$20 Auction</span></div>';
    h += '<div class="setup">';
    h += '<section class="panel span2"><div class="mode-pick">' + coverArt(m) + '<div><h3>' + esc(m.name) + '</h3><p>' + esc(m.blurb) + '</p><p class="hint" style="margin-top:6px;color:var(--muted)">' + m.rounds.length + ' different auction rounds, with random items each game.</p></div></div></section>';
    h += '<section class="panel"><h2>Who’s playing?</h2><div class="players-list">';
    s.names.forEach(function (n, i) {
      h += '<div class="player-input"><span class="swatch" style="background:' + T.PLAYER_COLORS[i] + '">' + (i + 1) + '</span>' +
        '<input id="pname-' + i + '" data-input="pname" data-i="' + i + '" value="' + esc(n) + '" placeholder="Player ' + (i + 1) + ' name" maxlength="16" autocomplete="off" aria-label="Player ' + (i + 1) + ' name">' +
        '<button class="btn btn-small icon-btn" data-act="remove-player" data-i="' + i + '" ' + (s.names.length <= 2 ? 'disabled' : '') + ' aria-label="Remove player ' + (i + 1) + '">' + icon('minus') + '</button></div>';
    });
    h += '</div><div class="row" style="margin-top:12px"><button class="btn btn-small" data-act="add-player" ' + (s.names.length >= 8 ? 'disabled' : '') + '>' + icon('plus') + ' Add player</button><span class="hint" style="color:var(--muted)">' + s.names.length + ' of 8 players. Each gets $20.</span></div></section>';
    h += '<section class="panel"><h2>Game options</h2><div style="display:flex;flex-direction:column;gap:14px">';
    var max = m.rounds.length, quick = Math.min(6, max);
    h += '<div class="field"><span class="lbl">How long?</span><div class="seg">' +
      '<button data-act="set-opt" data-k="rounds" data-v="' + quick + '" aria-pressed="' + (s.rounds === quick) + '"><b>Quick</b><span>' + quick + ' items, about 10 minutes</span></button>' +
      '<button data-act="set-opt" data-k="rounds" data-v="' + max + '" aria-pressed="' + (s.rounds === max) + '"><b>Full game</b><span>' + max + ' items, about 20 minutes</span></button></div></div>';
    h += '<div class="field"><span class="lbl">How do people bid?</span><div class="seg">' +
      '<button data-act="set-opt" data-k="bidStyle" data-v="live" aria-pressed="' + (s.bidStyle === 'live') + '"><b>Out loud</b><span>Shout bids, the host taps them in</span></button>' +
      '<button data-act="set-opt" data-k="bidStyle" data-v="secret" aria-pressed="' + (s.bidStyle === 'secret') + '"><b>Secret bids</b><span>Pass the device, bid privately</span></button></div></div>';
    h += '<div class="field"><span class="lbl">Extras</span><div class="seg">' +
      '<button data-act="toggle-setting" data-k="ai" aria-pressed="' + SETTINGS.ai + '"><b>AI paintings ' + (SETTINGS.ai ? 'on' : 'off') + '</b><span>' + (AI_BLOCKED ? 'Not available on this page' : 'Free painter (Pollinations.ai) paints each creation') + '</span></button>' +
      '<button data-act="toggle-setting" data-k="sound" aria-pressed="' + SETTINGS.sound + '"><b>Sound ' + (SETTINGS.sound ? 'on' : 'off') + '</b><span>Bids, gavel and fanfare</span></button></div></div>';
    h += '</div></section>';
    if (G && !G.over) h += '<section class="panel span2" style="background:#FFF4D6"><p>Heads up: a game of ' + esc(T.mode(G).name) + ' is still in progress. Starting this one replaces it.</p></section>';
    h += '<section class="panel span2"><div class="row"><button class="btn btn-red btn-big" data-act="start-game">' + icon('gavel') + ' Start the auction</button><span class="form-error" role="alert">' + esc(UI.msg) + '</span></div></section>';
    return h + '</div></div>';
  }

  /* ---------- GAME ---------- */
  function gameScreen() {
    var g = G, m = T.mode(g), round = T.currentRound(g), st = T.auctionState(g);
    var h = '<div class="wrap">';
    h += '<div class="topbar"><button class="logo" data-act="go-home" aria-label="Home">$20 Auction</button><span class="round-tag">' + esc(m.name) + ' · item ' + (g.roundIndex + 1) + ' of ' + g.rounds.length + '</span><span class="spacer"></span>' +
      '<button class="btn btn-small icon-btn" data-act="toggle-sound" aria-label="' + (SETTINGS.sound ? 'Mute sound' : 'Turn sound on') + '">' + icon(SETTINGS.sound ? 'soundOn' : 'soundOff') + '</button>' +
      '<button class="btn btn-small" data-act="toggle-show">' + icon('eye') + (UI.showMode ? ' Show host desk' : ' Hide host desk') + '</button>' +
      '<button class="btn btn-small btn-ink" data-act="open-host">' + icon('menu') + ' Host menu</button></div>';
    h += '<div class="game' + (UI.showMode ? ' show-mode' : '') + '"><div class="left">';
    // stage
    h += '<section class="panel stage" aria-live="polite"><div class="stage-inner' + (UI.reveal ? ' reveal-anim' : '') + '">';
    h += '<div class="round-label"><span class="caption-box">Item ' + (g.roundIndex + 1) + '</span><span class="of">of ' + g.rounds.length + '</span></div>';
    if (g.phase === 'curtain') {
      h += '<div class="curtain"><div class="q">???</div><p>The host is about to reveal the next item. Get your bidding hands ready!</p></div>';
    } else {
      h += '<div class="item-show"><div class="item-art">' + burst(m.color === '#14110F' ? '#FFE94D' : '#FFE94D') + '<span class="e">' + esc(round.item.emoji) + '</span></div>' +
        '<div class="item-text"><span class="caption-box" style="font-size:1rem">' + esc(round.label) + '</span><h2 style="margin-top:10px">' + esc(round.item.name) + '</h2><p class="desc">' + esc(round.item.desc) + '</p></div></div>';
      if (g.phase === 'preview') h += '<p class="status-line">Read it out loud! Bidding opens when the host says go.</p>';
      if (g.phase === 'bidding') {
        if (g.bidStyle === 'secret') {
          var s = g.auction.secret;
          h += '<div class="balloon-row"><div class="balloon top"><span class="who">SECRET BIDS</span>' + (s ? Object.keys(s.entries).length : 0) + ' of ' + (s ? s.order.length : 0) + ' locked in</div></div>';
        } else {
          var bids = g.auction.log.filter(function (e) { return e.type === 'bid'; }).slice(-4).reverse();
          h += '<div class="balloon-row">';
          if (!bids.length) h += '<div class="balloon top"><span class="who">OPENING BID</span>Who’ll start at $1?</div>';
          bids.forEach(function (b, i) {
            var p = T.player(g, b.pid);
            h += '<div class="balloon ' + (i === 0 ? 'top' : 'old') + '"' + (i === 0 ? ' style="border-color:' + p.color + '"' : '') + '><span class="who">' + esc(p.name.toUpperCase()) + '</span>$' + b.amount + (i === 0 ? '!' : '') + '</div>';
          });
          h += '</div>';
        }
      }
      var last = g.history[g.history.length - 1];
      if (g.phase === 'sold' && last) {
        var w = T.player(g, last.pid);
        h += '<div class="result-banner"><b>SOLD!</b><span>' + esc(w.name) + ' won ' + esc(round.item.name) + ' for $' + last.price + '.</span></div>';
      }
      if (g.phase === 'unclaimed') h += '<div class="result-banner"><b>No sale!</b><span>Nobody bid. ' + esc(round.item.name) + ' goes unclaimed.</span></div>';
      if (g.phase === 'skipped') h += '<div class="result-banner"><b>Skipped</b><span>The host skipped this item. No money changed hands.</span></div>';
    }
    h += '</div></section>';
    h += deskPanel();
    h += '</div>';
    // players
    h += '<section class="players-grid" aria-label="Players">';
    g.players.forEach(function (p) {
      var top = g.phase === 'bidding' && st.high && st.high.pid === p.id;
      h += '<button class="pcard' + (top ? ' is-top' : '') + '" style="--pc:' + p.color + '" data-act="open-player" data-pid="' + p.id + '" aria-label="' + esc(p.name) + ', $' + p.balance + ' left. Open dashboard">' +
        '<div class="pcard-head"><span class="nm">' + esc(p.name) + '</span><span class="count">' + p.wins.length + (p.wins.length === 1 ? ' item' : ' items') + '</span></div>' +
        '<div class="art">' + creationSvg(g, p, { pop: true }) + '</div>' +
        '<div class="pcard-foot">' + money(p.balance, moneyClass(p)) + moneyNote(p) + aiChip(p) + '</div></button>';
    });
    h += '</section></div>';
    return h + '</div>';
  }

  function deskPanel() {
    var g = G, st = T.auctionState(g);
    var h = '<section class="desk" aria-label="Host desk"><div class="desk-head"><h3>Host desk</h3><span class="note">Only the host taps here.</span></div>';
    if (g.phase === 'curtain') {
      h += '<div class="desk-actions"><button class="btn btn-yellow btn-big" data-act="reveal">Reveal item ' + (g.roundIndex + 1) + '</button><button class="btn btn-ghost" data-act="skip">' + icon('skip') + ' Skip item</button></div>';
    } else if (g.phase === 'preview') {
      h += '<div class="desk-actions"><button class="btn btn-cash btn-big" data-act="open-bidding">' + icon('gavel') + (g.bidStyle === 'secret' ? ' Start secret bids' : ' Start bidding') + '</button><button class="btn btn-ghost" data-act="skip">' + icon('skip') + ' Skip item</button></div>';
    } else if (g.phase === 'bidding' && g.bidStyle === 'secret') {
      h += secretDesk();
    } else if (g.phase === 'bidding') {
      var min = st.high ? st.high.amount + 1 : 1;
      h += '<div class="bid-rows">';
      g.players.forEach(function (p) {
        var isTop = st.high && st.high.pid === p.id, passed = st.passed[p.id], broke = p.balance < min && !isTop;
        var flag = isTop ? 'Top bid $' + st.high.amount : passed ? 'Passed' : p.balance === 0 ? 'Out of money' : broke ? 'Can’t beat $' + st.high.amount : '';
        h += '<div class="bid-row' + (isTop ? ' is-top' : '') + (passed || broke ? ' is-out' : '') + '"><div class="bid-who"><span class="dot" style="background:' + p.color + '"></span><span class="nm">' + esc(p.name) + '</span>' + (flag ? '<span class="flag">' + esc(flag) + '</span>' : '') + '<span class="bal">$' + p.balance + '</span></div>';
        if (!isTop && !passed && !broke) {
          var amounts = [min, min + 1, min + 4, p.balance].filter(function (a, i, arr) { return a <= p.balance && arr.indexOf(a) === i; });
          h += '<div class="bid-btns">' + amounts.map(function (a) {
            return '<button class="btn btn-small btn-cash" data-act="bid" data-pid="' + p.id + '" data-amt="' + a + '">' + (a === p.balance && a > min ? 'All in $' : '$') + a + '</button>';
          }).join('') +
            '<span class="custom"><label class="sr-only" for="cb-' + p.id + '">Exact bid for ' + esc(p.name) + '</label><input id="cb-' + p.id + '" type="number" inputmode="numeric" min="' + min + '" max="' + p.balance + '" step="1" placeholder="$"><button class="btn btn-small" data-act="bid-custom" data-pid="' + p.id + '">Bid</button></span>' +
            '<button class="btn btn-small btn-ghost" data-act="pass" data-pid="' + p.id + '">Pass</button></div>';
        } else h += '<div></div>';
        h += '</div>';
      });
      h += '</div>';
      var left = T.stillIn(g);
      var hint = st.high && !left.length ? 'Everyone else is out. Bang the gavel!' : '';
      h += '<p class="desk-msg" role="alert">' + esc(UI.msg || hint) + '</p>';
      h += '<div class="desk-actions">';
      if (st.high) h += '<button class="btn btn-red btn-big" data-act="sell">' + icon('gavel') + ' SOLD to ' + esc(T.player(g, st.high.pid).name) + ' for $' + st.high.amount + '</button>';
      else h += '<button class="btn btn-big" data-act="sell">No bids: leave it unclaimed</button>';
      h += '<button class="btn btn-ghost" data-act="undo" ' + (g.auction.log.length ? '' : 'disabled') + '>' + icon('undo') + ' Undo last</button>' +
        '<button class="btn btn-ghost" data-act="skip">' + icon('skip') + ' Skip item</button></div>';
    } else if (g.phase === 'sold' || g.phase === 'unclaimed' || g.phase === 'skipped') {
      var lastRound = T.isLastRound(g) || T.everyoneBroke(g);
      h += '<div class="desk-actions"><button class="btn btn-yellow btn-big" data-act="next">' + (lastRound ? 'See the final results ' : 'Next item ') + icon('arrow') + '</button></div>';
      if (T.everyoneBroke(g) && !T.isLastRound(g)) h += '<p class="note" style="color:var(--desk-muted)">Everyone is out of money, so the auction is over.</p>';
    }
    return h + '</section>';
  }

  function secretDesk() {
    var g = G, s = g.auction.secret, h = '';
    if (!s) return '';
    if (!T.secretDone(g)) {
      var p = T.player(g, s.order[s.idx]);
      h += '<p>Secret bids: ' + Object.keys(s.entries).length + ' of ' + s.order.length + ' locked in.' + (s.floor ? ' Tie-breaker: bid at least $' + s.floor + ' or pass.' : '') + '</p>';
      h += '<div class="desk-actions"><button class="btn btn-yellow btn-big" data-act="secret-open">Hand the device to ' + esc(p.name) + ' ' + icon('arrow') + '</button><button class="btn btn-ghost" data-act="skip">' + icon('skip') + ' Skip item</button></div>';
    } else {
      h += '<p>All secret bids are in.</p><div class="desk-actions"><button class="btn btn-red btn-big" data-act="secret-reveal">' + icon('gavel') + ' Reveal the bids</button><button class="btn btn-ghost" data-act="skip">' + icon('skip') + ' Skip item</button></div>';
    }
    return h;
  }

  /* ---------- overlays ---------- */
  function soldOverlay(o) {
    var g = G, p = T.player(g, o.pid), round = g.rounds[o.round];
    var last = T.isLastRound(g) || T.everyoneBroke(g);
    return '<div class="overlay" role="dialog" aria-modal="true" aria-label="Sold"><div class="sold-box">' +
      '<div class="sold-burst">' + burst('#E4002B', 14, 0.62).replace('class="burst"', '') + '<span>SOLD!</span></div>' +
      '<div class="panel sold-card"><h2>' + esc(p.name) + ' wins ' + esc(round.item.emoji) + ' ' + esc(round.item.name) + '!</h2>' +
      '<div class="sold-money">Paid $' + o.price + ' · ' + money('<span data-ticker data-from="' + o.before + '" data-to="' + p.balance + '">' + o.before + '</span>', moneyClass(p)) + ' left</div>' +
      '<div class="art">' + creationSvg(g, p, { pop: true }) + '</div>' +
      (SETTINGS.ai ? '<p class="empty-note">The AI painter is updating ' + esc(p.name) + '’s painting in the background.</p>' : '') +
      '<div class="row" style="justify-content:center"><button class="btn btn-yellow btn-big" data-act="next-from-overlay">' + (last ? 'See final results ' : 'Next item ') + icon('arrow') + '</button><button class="btn" data-act="close-overlay">Look around</button></div></div>' +
      '</div></div>';
  }
  function unclaimedOverlay() {
    var round = T.currentRound(G);
    return '<div class="overlay" role="dialog" aria-modal="true" aria-label="No sale"><div class="sold-box"><div class="sold-burst">' + burst('#8D99AE', 12, 0.7).replace('class="burst"', '') + '<span style="font-size:clamp(3rem,10vw,5rem)">NO SALE</span></div>' +
      '<div class="panel sold-card"><h2>' + esc(round.item.name) + ' goes unclaimed.</h2><p>Nobody bid, so everyone keeps their money.</p>' +
      '<div class="row" style="justify-content:center"><button class="btn btn-yellow btn-big" data-act="next-from-overlay">' + (T.isLastRound(G) ? 'See final results ' : 'Next item ') + icon('arrow') + '</button><button class="btn" data-act="close-overlay">Close</button></div></div></div></div>';
  }
  function secretOverlay() {
    var g = G, s = g.auction.secret, o = UI.overlay;
    if (o.step === 'cover') {
      var p = T.player(g, s.order[s.idx]);
      return '<div class="overlay" role="dialog" aria-modal="true"><div class="panel secret"><h2>Pass to ' + esc(p.name) + '</h2><p>Everyone else, look away!</p><button class="btn btn-red btn-big" data-act="secret-show">I’m ' + esc(p.name) + ', show my bid pad</button><button class="btn btn-small" data-act="close-overlay">Back to host desk</button></div></div>';
    }
    if (o.step === 'pad') {
      var pp = T.player(g, s.order[s.idx]), round = T.currentRound(g);
      var keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'C', 0, '⌫'];
      return '<div class="overlay" role="dialog" aria-modal="true"><div class="panel secret"><h2>' + esc(pp.name) + '’s secret bid</h2>' +
        '<p>For ' + esc(round.item.emoji) + ' <b>' + esc(round.item.name) + '</b>. You have ' + money(pp.balance, moneyClass(pp)) + '</p>' +
        '<div class="secret-amount" aria-live="polite">$' + (o.amt || 0) + '</div>' +
        '<div class="keypad">' + keys.map(function (k) { return '<button data-act="secret-key" data-k="' + k + '" aria-label="' + (k === 'C' ? 'Clear' : k === '⌫' ? 'Delete' : k) + '">' + k + '</button>'; }).join('') + '</div>' +
        '<p class="form-error" role="alert">' + esc(UI.msg) + '</p>' +
        '<div class="row" style="justify-content:center"><button class="btn btn-cash btn-big" data-act="secret-lock" ' + (o.amt > 0 ? '' : 'disabled') + '>Lock in $' + (o.amt || 0) + '</button><button class="btn btn-big" data-act="secret-pass">Pass</button></div></div></div>';
    }
    if (o.step === 'locked') {
      var next = T.secretDone(g) ? null : T.player(g, s.order[s.idx]);
      return '<div class="overlay" role="dialog" aria-modal="true"><div class="panel secret"><h2>Locked in!</h2><p>Your bid is secret.</p>' +
        (next ? '<button class="btn btn-red btn-big" data-act="secret-cover">Pass to ' + esc(next.name) + ' ' + icon('arrow') + '</button>' : '<button class="btn btn-yellow btn-big" data-act="close-overlay">Give the device back to the host</button>') + '</div></div>';
    }
    if (o.step === 'reveal') {
      var entries = Object.keys(o.entries).map(function (id) { return { p: T.player(g, id), a: o.entries[id] }; }).sort(function (a, b) { return b.a - a.a; });
      var res = o.result;
      var h = '<div class="overlay" role="dialog" aria-modal="true"><div class="panel secret"><h2>The secret bids</h2><div class="reveal-list">';
      entries.forEach(function (e) { h += '<div class="' + (res.kind === 'winner' && e.p.id === res.pid ? 'win' : '') + '"><span>' + esc(e.p.name) + '</span><span>' + (e.a ? '$' + e.a : 'Pass') + '</span></div>'; });
      h += '</div>';
      if (res.kind === 'winner') h += '<button class="btn btn-red btn-big" data-act="sell">' + icon('gavel') + ' SOLD to ' + esc(T.player(g, res.pid).name) + ' for $' + res.amount + '</button>';
      else if (res.kind === 'tie') h += '<p>It’s a tie at $' + res.amount + ' between ' + res.ids.map(function (id) { return esc(T.player(g, id).name); }).join(' and ') + '!</p><button class="btn btn-yellow btn-big" data-act="secret-tie">Tie-breaker: they bid again</button>';
      else h += '<p>Everybody passed.</p><button class="btn btn-big" data-act="sell">Leave it unclaimed</button>';
      return h + '</div></div>';
    }
    return '';
  }

  /* ---------- drawers ---------- */
  function aiBox(g, p, readOnly) {
    var a = p.ai || {};
    var compact = !a.url && a.status !== 'loading';
    var h = '<div class="ai-box">' + (compact ? '' : '<div class="ai-frame">');
    if (a.url) h += '<img src="' + esc(a.url) + '" alt="AI painting of ' + esc(p.name) + '’s creation" referrerpolicy="no-referrer">';
    if (a.status === 'loading') h += a.url ? '<span class="ai-loading"><span class="spin"></span> Painting the newest win…</span>' : '<p><span class="spin"></span> The AI painter is working. This takes 10 to 40 seconds.</p>';
    h += (compact ? '' : '</div>') + '<div class="ai-bar"' + (compact ? ' style="border-top:0"' : '') + '><span class="grow">';
    if (compact && a.status !== 'error') h += (AI_BLOCKED ? AI_BLOCKED_MSG : !SETTINGS.ai && !readOnly ? 'AI paintings are off. Turn them on in Host menu \u2192 Settings.' : p.wins.length ? 'No AI painting yet. ' : 'Win an item and the AI painter will paint this creation.');
    if (a.status === 'error') h += '<b style="color:var(--red)" title="' + esc(a.error || '') + '">Painting failed.</b> ' + (readOnly || UI.screen === 'results' ? 'Try again in a moment.' : 'The AI painter didn\u2019t answer. ' + (a.url ? 'Showing the last painting that worked. ' : '') + 'The drawing above is always up to date.');
    else if (a.status === 'ok' && a.sig !== T.AI.signature(p)) h += 'New wins since this painting.';
    else if (a.status === 'ok') h += 'AI painting of all ' + p.wins.length + ' features, by ' + T.AI.provider + '.';
    else if (a.status === 'loading') h += 'Painting with every feature ' + esc(p.name) + ' owns.';
    else if (!compact) h += 'AI painter: ' + T.AI.provider + ' (free).';
    h += '</span>';
    if (!readOnly && SETTINGS.ai && p.wins.length && a.status !== 'loading') {
      var label = a.status === 'error' ? 'Try again' : a.url ? (a.sig !== T.AI.signature(p) ? 'Update painting' : 'Repaint') : 'Paint it now';
      h += '<button class="btn btn-small" data-act="ai-paint" data-pid="' + p.id + '">' + icon(a.status === 'error' ? 'redo' : 'brush') + ' ' + label + '</button>';
    }
    if (a.url) h += '<a class="btn btn-small" href="' + esc(a.url) + '" target="_blank" rel="noopener noreferrer">Open full size</a>';
    return h + '</div></div>';
  }

  function itemList(wins) {
    if (!wins.length) return '<p class="empty-note">No items yet.</p>';
    return '<ul class="item-list">' + wins.map(function (w) {
      return '<li><span class="e">' + esc(w.item.emoji) + '</span><span class="n">' + esc(w.item.name) + '<small>' + esc(w.label) + '</small></span><span class="p">$' + w.price + '</span></li>';
    }).join('') + '</ul>';
  }

  function playerDrawer(pid) {
    var g = G, p = T.player(g, pid);
    if (!p) return '';
    var spent = T.spent(p);
    var h = '<div class="drawer-scrim" data-act="close-drawer"></div><aside class="drawer" role="dialog" aria-modal="true" aria-label="' + esc(p.name) + ' dashboard">';
    h += '<div class="drawer-head"><span class="swatch" style="background:' + p.color + '"></span><h2>' + esc(p.name) + '</h2><button class="btn btn-small icon-btn" data-act="close-drawer" aria-label="Close">' + icon('x') + '</button></div>';
    h += '<div class="stat-grid"><div class="stat hero ' + (p.balance <= 3 ? 'low' : '') + '"><div class="k">Money left</div><div class="v">$' + p.balance + '</div>' + (p.balance === 0 ? '<div>Out of money. Can’t bid anymore.</div>' : p.balance <= 3 ? '<div>Running low. Choose wisely!</div>' : '') + '</div>' +
      '<div class="stat"><div class="k">Started with</div><div class="v">$' + T.START_MONEY + '</div></div><div class="stat"><div class="k">Spent</div><div class="v">$' + spent + '</div></div>' +
      '<div class="stat"><div class="k">Items won</div><div class="v">' + p.wins.length + '</div></div><div class="stat"><div class="k">Items missed</div><div class="v">' + p.missed.length + '</div></div></div>';
    h += '<h3 class="caption-box">The creation</h3><div class="panel" style="line-height:0;overflow:hidden">' + creationSvg(g, p) + '</div>';
    h += '<h3 class="caption-box">AI painting</h3>' + aiBox(g, p);
    h += '<h3 class="caption-box">Collected</h3>' + itemList(p.wins);
    h += '<h3 class="caption-box">Got away</h3>';
    h += p.missed.length ? '<ul class="item-list missed">' + p.missed.map(function (m) { return '<li><span class="e">' + esc(m.emoji) + '</span><span class="n">' + esc(m.name) + '<small>Bid $' + m.myBid + ', ' + esc(m.to) + ' won it for $' + m.soldFor + '</small></span><span class="p">—</span></li>'; }).join('') + '</ul>' : '<p class="empty-note">Nothing lost yet.</p>';
    return h + '</aside>';
  }

  function hostDrawer() {
    var g = G, t = UI.tab;
    var h = '<div class="drawer-scrim" data-act="close-drawer"></div><aside class="drawer" role="dialog" aria-modal="true" aria-label="Host menu">';
    h += '<div class="drawer-head"><h2>Host menu</h2><button class="btn btn-small icon-btn" data-act="close-drawer" aria-label="Close">' + icon('x') + '</button></div>';
    h += '<div class="tabs" role="tablist">' + [['players', 'Money & items'], ['game', 'Game'], ['settings', 'Settings'], ['rules', 'Rules']].map(function (x) {
      return '<button class="chip" role="tab" data-act="tab" data-v="' + x[0] + '" aria-pressed="' + (t === x[0]) + '" aria-selected="' + (t === x[0]) + '">' + x[1] + '</button>';
    }).join('') + '</div>';
    if (t === 'players') {
      h += '<div class="table-wrap"><table class="bal"><thead><tr><th>Player</th><th>Left</th><th>Spent</th><th>Items</th></tr></thead><tbody>' +
        g.players.map(function (p) { return '<tr><td><button class="chip" data-act="open-player" data-pid="' + p.id + '" style="border-color:' + p.color + '">' + esc(p.name) + '</button></td><td class="num">$' + p.balance + '</td><td class="num">$' + T.spent(p) + '</td><td class="num">' + p.wins.length + '</td></tr>'; }).join('') +
        '</tbody></table></div>';
      g.players.forEach(function (p) { h += '<h3 class="caption-box" style="border-color:' + p.color + '">' + esc(p.name) + '’s collection</h3>' + itemList(p.wins); });
    } else if (t === 'game') {
      var r = T.currentRound(g);
      h += '<p>' + esc(T.mode(g).name) + ' · item ' + (g.roundIndex + 1) + ' of ' + g.rounds.length + ' · ' + (g.bidStyle === 'secret' ? 'secret bids' : 'out-loud bids') + '</p>';
      h += '<div class="row">';
      if (!(g.phase === 'sold' || g.phase === 'unclaimed' || g.phase === 'skipped')) h += '<button class="btn" data-act="skip">' + icon('skip') + ' Skip this item</button>';
      h += '<button class="btn btn-red" data-act="ask-end">' + icon('flag') + ' End game now</button></div>';
      if (UI.confirm === 'end') h += '<div class="confirm"><b>End the game now?</b><p>Everyone keeps what they won' + (g.phase === 'bidding' ? ', and the current auction is cancelled with no money taken' : '') + '. You’ll go to the final results and voting.</p><div class="row"><button class="btn btn-red" data-act="end-game">Yes, end the game</button><button class="btn" data-act="cancel-confirm">Keep playing</button></div></div>';
      h += '<div class="row"><button class="btn" data-act="ask-new">' + icon('redo') + ' Restart with a new mode</button></div>';
      if (UI.confirm === 'new') h += '<div class="confirm"><b>Leave this game?</b><p>This game ends without results. The same players will pick a new mode.</p><div class="row"><button class="btn btn-red" data-act="restart-new">Yes, pick a new mode</button><button class="btn" data-act="cancel-confirm">Keep playing</button></div></div>';
      h += '<p class="empty-note">Upcoming items stay hidden until revealed, even from the host. ' + (r ? 'This is item ' + (g.roundIndex + 1) + '.' : '') + '</p>';
    } else if (t === 'settings') {
      h += '<div class="seg"><button data-act="toggle-setting" data-k="sound" aria-pressed="' + SETTINGS.sound + '"><b>Sound ' + (SETTINGS.sound ? 'on' : 'off') + '</b><span>Bids, gavel, fanfare</span></button>' +
        '<button data-act="toggle-setting" data-k="ai" aria-pressed="' + SETTINGS.ai + '"><b>AI paintings ' + (SETTINGS.ai ? 'on' : 'off') + '</b><span>' + (AI_BLOCKED ? 'Not available on this page' : 'Paint each creation after a win') + '</span></button></div>';
      h += '<p class="empty-note">AI paintings come from ' + T.AI.provider + ', a free image service with no account. If it is slow or blocked on your network, the drawn creations still work and update instantly. You can retry any painting from a player’s dashboard.</p>';
      h += '<p class="empty-note">Custom modes are made from the home screen: “Make your own mode”.</p>';
    } else {
      h += '<ol style="margin:0;padding-left:20px;display:flex;flex-direction:column;gap:6px"><li>Everyone starts with $20.</li><li>Bids are whole dollars. You can’t bid more than you have.</li><li>The highest bid wins when the host bangs the gavel, and only the winner pays.</li><li>If you pass or lose, you keep your money.</li><li>If nobody bids, the item goes unclaimed.</li><li>At $0 you can’t bid anymore, but you still get to vote.</li><li>At the end the family votes. Spending the most does not make you the winner.</li></ol>';
    }
    return h + '</aside>';
  }

  function editorDrawer() {
    var e = UI.editor;
    var kinds = [['collage', 'Sticker board'], ['spread', 'Table of plates'], ['map', 'Island map'], ['building', 'Building with rooms'], ['team', 'Team of cards']];
    var colors = ['#00AEEF', '#E4002B', '#00A651', '#FF8200', '#7B2CBF', '#EC008C', '#14110F'];
    var h = '<div class="drawer-scrim" data-act="close-drawer"></div><aside class="drawer editor" role="dialog" aria-modal="true" aria-label="Make your own mode">';
    h += '<div class="drawer-head"><h2>' + (e.id ? 'Edit mode' : 'Make your own mode') + '</h2><button class="btn btn-small icon-btn" data-act="close-drawer" aria-label="Close">' + icon('x') + '</button></div>';
    h += '<div class="field"><label for="ed-name">Name</label><input id="ed-name" data-input="ed" data-k="name" value="' + esc(e.name) + '" placeholder="Dream Treehouse" maxlength="32"></div>';
    h += '<div class="field"><label for="ed-blurb">One-line description</label><input id="ed-blurb" data-input="ed" data-k="blurb" value="' + esc(e.blurb) + '" placeholder="Rope bridges, secret doors and a snack bucket on a pulley." maxlength="90"></div>';
    h += '<div class="field"><label for="ed-cover">Cover pictures (up to 3 emoji)</label><input id="ed-cover" data-input="ed" data-k="cover" value="' + esc(e.cover) + '" placeholder="🌳 🪜 🍪"></div>';
    h += '<div class="field"><span class="lbl">How the creation is drawn</span><div class="seg">' + kinds.map(function (k) { return '<button data-act="ed-kind" data-v="' + k[0] + '" aria-pressed="' + (e.kind === k[0]) + '"><b>' + k[1] + '</b></button>'; }).join('') + '</div></div>';
    h += '<div class="field"><span class="lbl">Cover color</span><div class="row">' + colors.map(function (c) { return '<button class="swatch" style="background:' + c + ';outline:' + (e.color === c ? '4px solid var(--ink)' : 'none') + ';outline-offset:2px" data-act="ed-color" data-v="' + c + '" aria-label="Color ' + c + '" aria-pressed="' + (e.color === c) + '"></button>'; }).join('') + '</div></div>';
    h += '<div class="field"><label for="ed-rounds">Rounds: one per line</label><textarea id="ed-rounds" data-input="ed" data-k="rounds" spellcheck="false" placeholder="Bed: 🛏️ Hammock bed (Sway to sleep), 🪺 Nest bed">' + esc(e.rounds) + '</textarea>' +
      '<span class="hint">Write the round name, a colon, then items separated by commas. Start an item with an emoji for its picture, and add a short description in brackets. At least 3 rounds; one random item per round is auctioned each game.</span></div>';
    h += '<p class="form-error" role="alert">' + esc(UI.editorErr) + '</p>';
    h += '<div class="row"><button class="btn btn-cash" data-act="ed-save">Save mode</button>' + (e.id ? '<button class="btn btn-ghost" data-act="ed-delete">' + icon('trash') + ' Delete</button>' : '') + '</div>';
    return h + '</aside>';
  }

  /* ---------- RESULTS ---------- */
  function resultsScreen() {
    var g = UI.galleryIdx != null ? GALLERY[UI.galleryIdx].game : G;
    var ro = UI.galleryIdx != null;
    var mode = g.modeObj || T.modeById[g.modeId];
    var h = '<div class="wrap"><div class="topbar"><button class="btn btn-small" data-act="go-home">' + icon('back') + ' Home</button><span class="spacer"></span><span class="logo">$20 Auction</span></div>';
    h += '<section class="panel results-head"><h1>' + (ro ? 'From the hall of creations' : 'The final issue!') + '</h1><p>' + esc(mode.name) + '. Compare every creation side by side, then vote together. Spending the most doesn’t make you the winner. The family decides.</p></section>';
    var awards = tallyVotes(g);
    h += '<div class="results-grid">';
    g.players.forEach(function (p) {
      var spent = T.spent(p);
      h += '<article class="panel rcard"><div class="pcard-head" style="--pc:' + p.color + ';background:' + p.color + '"><span class="nm">' + esc(p.name) + '</span><span class="count">' + p.wins.length + ' items</span></div>' +
        '<div class="art">' + creationSvg(g, p) + '</div><div class="body">' +
        '<div class="money-line">Spent <b>$' + spent + '</b> · Left ' + money(p.balance, moneyClass(p)) + '</div>';
      if (awards.byPlayer[p.id] && awards.byPlayer[p.id].length) h += '<ul class="awards">' + awards.byPlayer[p.id].map(function (a) { return '<li>🏆 ' + esc(a) + '</li>'; }).join('') + '</ul>';
      var hl = T.highlights(p);
      if (hl.length) h += '<div class="highlights">' + hl.map(function (x) { return '<div><b>' + esc(x.tag) + ':</b> ' + esc(x.win.item.emoji + ' ' + x.win.item.name) + ' ($' + x.win.price + ')</div>'; }).join('') + '</div>';
      h += itemList(p.wins);
      if (p.ai && (p.ai.url || !ro)) h += aiBox(g, p, ro);
      h += '<div class="row"><button class="btn btn-small" data-act="save-png" data-pid="' + p.id + '">' + icon('save') + ' Save image</button></div>';
      h += '</div></article>';
    });
    h += '</div>';
    h += '<section class="vote"><div class="shelf-head"><h2>Family vote</h2><span>Tap who wins each award. Tap again to change.</span></div><div class="vote-grid">';
    T.VOTE_CATS.forEach(function (c) {
      var cur = (g.votes || {})[c[0]];
      h += '<div class="panel vote-cat"><h3>' + esc(c[1]) + '</h3><div class="opts">' + g.players.map(function (p) {
        return '<button data-act="vote" data-c="' + c[0] + '" data-pid="' + p.id + '" aria-pressed="' + (cur === p.id) + '"><span class="dot" style="background:' + p.color + '"></span>' + esc(p.name) + '</button>';
      }).join('') + '</div></div>';
    });
    h += '</div>';
    if (awards.champ) h += '<div class="panel champ"><b>' + esc(awards.champ) + '</b><span>' + esc(awards.champLine) + '</span></div>';
    h += '</section>';
    h += '<div class="row" style="margin-top:28px"><button class="btn btn-red btn-big" data-act="play-again">' + icon('redo') + ' Play again, same players</button><button class="btn btn-big" data-act="go-home">New game</button></div>';
    return h + '</div>';
  }

  function tallyVotes(g) {
    var byPlayer = {}, counts = {};
    T.VOTE_CATS.forEach(function (c) {
      var pid = (g.votes || {})[c[0]];
      if (!pid) return;
      (byPlayer[pid] = byPlayer[pid] || []).push(c[1]);
      counts[pid] = (counts[pid] || 0) + 1;
    });
    var best = 0, champs = [];
    Object.keys(counts).forEach(function (pid) { if (counts[pid] > best) { best = counts[pid]; champs = [pid]; } else if (counts[pid] === best) champs.push(pid); });
    var votedAll = T.VOTE_CATS.every(function (c) { return (g.votes || {})[c[0]]; });
    var out = { byPlayer: byPlayer, champ: null };
    if (votedAll && champs.length) {
      var names = champs.map(function (id) { var p = g.players.filter(function (x) { return x.id === id; })[0]; return p ? p.name : ''; });
      out.champ = champs.length === 1 ? names[0] + ' is the family champion!' : 'It’s a tie: ' + names.join(' & ') + '!';
      out.champLine = 'Most awards from the family vote (' + best + ' of ' + T.VOTE_CATS.length + ').';
    }
    return out;
  }

  /* ---------- render ---------- */
  function render() {
    var active = document.activeElement, keep = {};
    if (active && active.id) keep.focus = active.id;
    app.querySelectorAll('input[id],textarea[id]').forEach(function (el) { keep[el.id] = el.value; });
    var h;
    if (UI.screen === 'setup') h = setupScreen();
    else if (UI.screen === 'game' && G) h = gameScreen();
    else if (UI.screen === 'results') h = resultsScreen();
    else h = homeScreen();
    if (UI.drawer === 'host' && G) h += hostDrawer();
    if (UI.drawer && UI.drawer.indexOf('player:') === 0 && G) h += playerDrawer(UI.drawer.slice(7));
    if (UI.drawer === 'editor' && UI.editor) h += editorDrawer();
    if (UI.overlay && G) {
      if (UI.overlay.type === 'sold') h += soldOverlay(UI.overlay);
      if (UI.overlay.type === 'unclaimed') h += unclaimedOverlay();
      if (UI.overlay.type === 'secret') h += secretOverlay();
    }
    if (UI.toast) h += '<div class="toast" role="status">' + esc(UI.toast) + '</div>';
    app.innerHTML = h;
    Object.keys(keep).forEach(function (id) {
      if (id === 'focus') return;
      var el = document.getElementById(id);
      if (el && el.value !== keep[id] && el.dataset.input == null) el.value = keep[id];
    });
    if (keep.focus) { var f = document.getElementById(keep.focus); if (f && f.focus) f.focus({ preventScroll: true }); }
    runTickers();
    UI.reveal = false;
  }

  function runTickers() {
    app.querySelectorAll('[data-ticker]').forEach(function (el) {
      var from = +el.dataset.from, to = +el.dataset.to;
      if (from === to) return;
      delete el.dataset.ticker;
      var t0 = performance.now(), dur = 900;
      (function step(t) {
        var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3), v = Math.round(from + (to - from) * e);
        if (el.textContent !== String(v)) { el.textContent = v; T.Sound.play('tick'); }
        if (k < 1) requestAnimationFrame(step);
      })(t0);
    });
  }

  /* ---------- confetti ---------- */
  function confetti(colors) {
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var c = document.createElement('canvas');
    c.className = 'confetti';
    document.body.appendChild(c);
    var dpr = Math.min(2, window.devicePixelRatio || 1);
    c.width = innerWidth * dpr; c.height = innerHeight * dpr;
    var x = c.getContext('2d'); x.scale(dpr, dpr);
    var parts = [];
    for (var i = 0; i < 140; i++) parts.push({ x: innerWidth / 2 + (Math.random() - 0.5) * 200, y: innerHeight * 0.35, vx: (Math.random() - 0.5) * 14, vy: -Math.random() * 14 - 4, r: Math.random() * Math.PI, vr: (Math.random() - 0.5) * 0.4, w: 8 + Math.random() * 8, h: 5 + Math.random() * 6, c: colors[i % colors.length] });
    var t0 = performance.now();
    (function frame(t) {
      x.clearRect(0, 0, innerWidth, innerHeight);
      parts.forEach(function (p) {
        p.vy += 0.38; p.vx *= 0.99; p.x += p.vx; p.y += p.vy; p.r += p.vr;
        x.save(); x.translate(p.x, p.y); x.rotate(p.r); x.fillStyle = p.c; x.strokeStyle = '#14110F'; x.lineWidth = 1.5;
        x.fillRect(-p.w / 2, -p.h / 2, p.w, p.h); x.strokeRect(-p.w / 2, -p.h / 2, p.w, p.h); x.restore();
      });
      if (t - t0 < 2600) requestAnimationFrame(frame); else c.remove();
    })(t0);
  }

  /* ---------- AI painting flow ---------- */
  function paint(pid) {
    var g = G, p = T.player(g, pid);
    if (!p || !p.wins.length || !SETTINGS.ai) return;
    var sig = T.AI.signature(p);
    p.ai.status = 'loading'; p.ai.pending = sig; p.ai.error = null;
    save(); render();
    var gameId = g.id;
    T.AI.paint(T.mode(g), p, g.id).then(function (url) {
      if (!G || G.id !== gameId || p.ai.pending !== sig) return;
      p.ai.status = 'ok'; p.ai.url = url; p.ai.sig = sig; p.ai.pending = null;
    }, function (err) {
      if (!G || G.id !== gameId || p.ai.pending !== sig) return;
      p.ai.status = 'error'; p.ai.error = err.message; p.ai.pending = null;
    }).then(function () { save(); if (G && G.over) syncGalleryVotes(); render(); });
  }

  /* ---------- saving images ---------- */
  function saveBlob(name, blob) {
    var cl = window.claude;
    var tryHost = cl && cl.use ? cl.use('downloads').catch(function () { return null; }) : Promise.resolve(null);
    return tryHost.then(function (dl) {
      if (dl) return dl.save({ filename: name, data: blob }).then(function (r) { return r && r.status === 'saved' ? 'Saved ' + name : 'Save cancelled.'; });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob); a.download = name;
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000);
      return 'Saved ' + name;
    });
  }

  /* ---------- game over bookkeeping ---------- */
  function finishGame() {
    T.endGame(G);
    if (!G.savedToGallery) {
      G.savedToGallery = true;
      var snap = JSON.parse(JSON.stringify(G));
      snap.modeObj = T.mode(G);
      GALLERY.push({ at: Date.now(), game: snap });
      while (GALLERY.length > 12) GALLERY.shift();
      T.store.set(KEYS.gallery, GALLERY);
    }
    UI.screen = 'results'; UI.overlay = null; UI.drawer = null; UI.galleryIdx = null; UI.confirm = null;
    save();
    T.Sound.play('fanfare');
    confetti(T.PLAYER_COLORS);
    render();
    window.scrollTo(0, 0);
  }
  function syncGalleryVotes() {
    for (var i = GALLERY.length - 1; i >= 0; i--) if (GALLERY[i].game.id === G.id) { GALLERY[i].game.votes = JSON.parse(JSON.stringify(G.votes)); GALLERY[i].game.players = JSON.parse(JSON.stringify(G.players)); }
    T.store.set(KEYS.gallery, GALLERY);
  }

  /* ---------- custom mode editor ---------- */
  var PART_FOR = { collage: 'spot', spread: 'meal', map: 'spot', building: 'room', team: 'member' };
  var EMOJI_START = /^(\p{Extended_Pictographic}(️|‍\p{Extended_Pictographic}|\p{Emoji_Modifier})*)\s*/u;
  function parseEditor(e) {
    var name = e.name.trim();
    if (!name) return { err: 'Give your mode a name.' };
    var lines = e.rounds.split('\n').map(function (l) { return l.trim(); }).filter(Boolean);
    var rounds = [], err = '';
    lines.forEach(function (l, i) {
      var c = l.indexOf(':');
      if (c < 1) { err = err || 'Line ' + (i + 1) + ' needs a round name and a colon, like “Bed: Hammock, Bunk bed”.'; return; }
      var items = l.slice(c + 1).split(',').map(function (s) { return s.trim(); }).filter(Boolean).map(function (s) {
        var em = '⭐', m = EMOJI_START.exec(s);
        if (m) { em = m[1]; s = s.slice(m[0].length); }
        var desc = '', d = /\(([^)]*)\)\s*$/.exec(s);
        if (d) { desc = d[1].trim(); s = s.slice(0, d.index).trim(); }
        return [s || 'Mystery item', desc || 'A custom pick', em].join('|');
      });
      if (!items.length) { err = err || 'Line ' + (i + 1) + ' has no items after the colon.'; return; }
      rounds.push([l.slice(0, c).trim(), PART_FOR[e.kind], items]);
    });
    if (err) return { err: err };
    if (rounds.length < 3) return { err: 'Add at least 3 rounds (one per line).' };
    var cover = [];
    var rest = e.cover.trim(), m;
    while (rest && (m = EMOJI_START.exec(rest)) && cover.length < 3) { cover.push(m[1]); rest = rest.slice(m[0].length); }
    if (!cover.length) cover = rounds.slice(0, 3).map(function (r) { return r[2][0].split('|')[2]; });
    return {
      mode: {
        id: e.id || 'custom-' + T.uid(), name: /^dream /i.test(name) ? name : 'Dream ' + name, cat: 'custom', custom: true,
        kind: e.kind, skin: e.kind === 'map' ? 'island' : e.kind === 'building' ? 'house' : e.kind === 'spread' ? 'day' : e.kind === 'team' ? 'powers' : 'collage',
        blurb: e.blurb.trim() || 'A family-made mode.', ai: 'a dream ' + name.replace(/^dream /i, ''), color: e.color, cover: cover, rounds: rounds
      }
    };
  }
  function modeToEditor(raw) {
    return {
      id: raw.id, name: raw.name.replace(/^Dream /, ''), blurb: raw.blurb, cover: (raw.cover || []).join(' '), kind: raw.kind, color: raw.color,
      rounds: raw.rounds.map(function (r) {
        return r[0] + ': ' + r[2].map(function (s) { var p = s.split('|'); return (p[2] ? p[2] + ' ' : '') + p[0] + (p[1] && p[1] !== 'A custom pick' ? ' (' + p[1] + ')' : ''); }).join(', ');
      }).join('\n')
    };
  }

  /* ---------- actions ---------- */
  function startSetup(modeId) {
    var names = UI.nextNames || (UI.setup && UI.setup.names) || ['', ''];
    var m = T.modeById[modeId];
    UI.setup = { modeId: modeId, names: names.slice(0, 8), rounds: Math.min(10, m.rounds.length), bidStyle: (UI.setup && UI.setup.bidStyle) || 'live' };
    if (UI.setup.names.length < 2) UI.setup.names.push('');
    UI.screen = 'setup'; UI.msg = ''; UI.nextNames = null;
    render(); window.scrollTo(0, 0);
  }

  var A = {
    'filter': function (el) { UI.filter = el.dataset.v; render(); },
    'pick-mode': function (el) { startSetup(el.dataset.id); },
    'resume': function () { UI.screen = 'game'; render(); window.scrollTo(0, 0); },
    'clear-next': function () { UI.nextNames = null; render(); },
    'go-home': function () { UI.screen = 'home'; UI.drawer = null; UI.overlay = null; UI.galleryIdx = null; render(); window.scrollTo(0, 0); },
    'view-gallery': function (el) { UI.galleryIdx = +el.dataset.i; UI.screen = 'results'; render(); window.scrollTo(0, 0); },
    'add-player': function () { if (UI.setup.names.length < 8) { UI.setup.names.push(''); render(); var el = document.getElementById('pname-' + (UI.setup.names.length - 1)); if (el) el.focus(); } },
    'remove-player': function (el) { if (UI.setup.names.length > 2) { UI.setup.names.splice(+el.dataset.i, 1); render(); } },
    'set-opt': function (el) { var v = el.dataset.v; UI.setup[el.dataset.k] = el.dataset.k === 'rounds' ? +v : v; render(); },
    'toggle-setting': function (el) {
      var k = el.dataset.k;
      if (k === 'ai' && AI_BLOCKED) { toast(AI_BLOCKED_MSG); return; }
      SETTINGS[k] = !SETTINGS[k]; saveSettings();
      if (k === 'sound') { T.Sound.on = SETTINGS.sound; if (SETTINGS.sound) T.Sound.play('bid', 1); }
      render();
    },
    'toggle-sound': function () { SETTINGS.sound = !SETTINGS.sound; T.Sound.on = SETTINGS.sound; saveSettings(); if (SETTINGS.sound) T.Sound.play('bid', 1); render(); },
    'start-game': function () {
      var s = UI.setup;
      var names = s.names.map(function (n, i) { return n.trim() || 'Player ' + (i + 1); });
      var lower = names.map(function (n) { return n.toLowerCase(); });
      var dup = lower.filter(function (n, i) { return lower.indexOf(n) !== i; })[0];
      if (dup) { UI.msg = 'Two players are both called “' + names[lower.indexOf(dup)] + '”. Give everyone a different name.'; render(); return; }
      G = T.newGame(s.modeId, names, { rounds: s.rounds, bidStyle: s.bidStyle });
      UI.screen = 'game'; UI.msg = ''; UI.showMode = false;
      save(); T.Sound.play('reveal'); render(); window.scrollTo(0, 0);
    },
    'reveal': function () { T.reveal(G); UI.reveal = true; T.Sound.play('reveal'); save(); render(); },
    'open-bidding': function () {
      T.openBidding(G); UI.msg = ''; T.Sound.play('gavel'); save();
      if (G.bidStyle === 'secret' && G.auction.secret && !G.auction.secret.order.length) { toast('Nobody has money left to bid.'); }
      render();
    },
    'bid': function (el) { doBid(el.dataset.pid, +el.dataset.amt); },
    'bid-custom': function (el) {
      var input = document.getElementById('cb-' + el.dataset.pid);
      var raw = input ? input.value.trim() : '';
      if (!/^\d+$/.test(raw)) { UI.msg = 'Type a whole-dollar amount, like 7.'; T.Sound.play('error'); render(); return; }
      doBid(el.dataset.pid, parseInt(raw, 10));
    },
    'pass': function (el) {
      var why = T.pass(G, el.dataset.pid);
      UI.msg = why; if (!why) T.Sound.play('pass'); else T.Sound.play('error');
      save(); render();
    },
    'undo': function () { var e = T.undo(G); UI.msg = e ? 'Undid ' + T.player(G, e.pid).name + '’s ' + (e.type === 'bid' ? '$' + e.amount + ' bid' : 'pass') + '.' : ''; save(); render(); },
    'sell': function () {
      var before = {};
      G.players.forEach(function (p) { before[p.id] = p.balance; });
      var res = T.closeAuction(G);
      if (!res) return;
      UI.msg = '';
      if (res.result === 'sold') {
        var w = res.winner;
        UI.pop = { pid: w.id, win: w.wins[w.wins.length - 1] };
        UI.overlay = { type: 'sold', pid: w.id, price: res.price, before: before[w.id], round: G.roundIndex };
        T.Sound.play('gavel'); T.Sound.play('sold');
        save(); render();
        confetti([w.color, '#FFE94D', '#00AEEF', '#EC008C']);
        setTimeout(function () { UI.pop = null; }, 1400);
        if (SETTINGS.ai) paint(w.id);
      } else {
        UI.overlay = { type: 'unclaimed' };
        T.Sound.play('sad'); save(); render();
      }
    },
    'skip': function () { T.skip(G); UI.overlay = null; UI.msg = ''; UI.confirm = null; T.Sound.play('pass'); save(); render(); },
    'next': function () { goNext(); },
    'next-from-overlay': function () { UI.overlay = null; goNext(); },
    'close-overlay': function () { UI.overlay = null; UI.msg = ''; render(); },
    'toggle-show': function () { UI.showMode = !UI.showMode; render(); },
    'open-host': function () { UI.drawer = 'host'; UI.confirm = null; render(); },
    'open-player': function (el) { UI.drawer = 'player:' + el.dataset.pid; render(); },
    'close-drawer': function () { UI.drawer = null; UI.confirm = null; UI.editorErr = ''; render(); },
    'tab': function (el) { UI.tab = el.dataset.v; UI.confirm = null; render(); },
    'ask-end': function () { UI.confirm = 'end'; render(); },
    'ask-new': function () { UI.confirm = 'new'; render(); },
    'cancel-confirm': function () { UI.confirm = null; render(); },
    'end-game': function () { finishGame(); },
    'restart-new': function () {
      UI.nextNames = G.players.map(function (p) { return p.name; });
      T.store.del(KEYS.game); G = null;
      UI.drawer = null; UI.confirm = null; UI.screen = 'home'; render(); window.scrollTo(0, 0);
    },
    'ai-paint': function (el) { paint(el.dataset.pid); },
    'secret-open': function () { UI.overlay = { type: 'secret', step: 'cover' }; UI.msg = ''; render(); },
    'secret-cover': function () { UI.overlay = { type: 'secret', step: 'cover' }; render(); },
    'secret-show': function () { UI.overlay = { type: 'secret', step: 'pad', amt: 0 }; UI.msg = ''; render(); },
    'secret-key': function (el) {
      var o = UI.overlay, k = el.dataset.k;
      if (k === 'C') o.amt = 0; else if (k === '⌫') o.amt = Math.floor((o.amt || 0) / 10); else o.amt = Math.min(999, (o.amt || 0) * 10 + (+k));
      UI.msg = ''; T.Sound.play('tick'); render();
    },
    'secret-lock': function () { secretEnter(UI.overlay.amt || 0); },
    'secret-pass': function () { secretEnter(0); },
    'secret-reveal': function () {
      var entries = JSON.parse(JSON.stringify(G.auction.secret.entries));
      var res = T.secretResolve(G);
      UI.overlay = { type: 'secret', step: 'reveal', entries: entries, result: res };
      T.Sound.play('reveal'); save(); render();
    },
    'secret-tie': function () {
      var ids = UI.overlay.result.ids;
      T.startSecret(G, ids);
      UI.overlay = { type: 'secret', step: 'cover' }; save(); render();
    },
    'vote': function (el) {
      var g = UI.galleryIdx != null ? GALLERY[UI.galleryIdx].game : G;
      g.votes = g.votes || {};
      var c = el.dataset.c;
      var allBefore = T.VOTE_CATS.every(function (x) { return g.votes[x[0]]; });
      g.votes[c] = g.votes[c] === el.dataset.pid ? null : el.dataset.pid;
      T.Sound.play('bid', 3);
      if (UI.galleryIdx != null) T.store.set(KEYS.gallery, GALLERY); else { save(); syncGalleryVotes(); }
      var t = tallyVotes(g);
      render();
      if (t.champ && !allBefore) { T.Sound.play('fanfare'); confetti(T.PLAYER_COLORS); }
    },
    'save-png': function (el) {
      var g = UI.galleryIdx != null ? GALLERY[UI.galleryIdx].game : G;
      var p = g.players.filter(function (x) { return x.id === el.dataset.pid; })[0];
      var mode = g.modeObj || T.modeById[g.modeId];
      T.svgToPng(creationSvg(g, p), 2, p.name + '’s ' + mode.name.replace(/^Dream /, 'Dream ')).then(function (blob) {
        return saveBlob((p.name + '-' + mode.name).replace(/[^\w-]+/g, '-').toLowerCase() + '.png', blob);
      }).then(toast, function (err) { toast('Could not save the image: ' + err.message); });
    },
    'play-again': function () {
      var g = UI.galleryIdx != null ? GALLERY[UI.galleryIdx].game : G;
      UI.nextNames = g.players.map(function (p) { return p.name; });
      if (UI.galleryIdx == null) { T.store.del(KEYS.game); G = null; }
      UI.galleryIdx = null; UI.screen = 'home'; render();
      var el = document.getElementById('modes'); if (el) el.scrollIntoView(); else window.scrollTo(0, 0);
    },
    'new-custom': function () {
      UI.editor = { id: null, name: '', blurb: '', cover: '', kind: 'collage', color: '#00AEEF', rounds: 'Bed: 🛏️ Hammock bed (Sway to sleep), 🪺 Giant nest bed\nWay up: 🪜 Rope ladder, 🛗 Tiny elevator, 🧗 Climbing wall\nSnacks: 🍪 Cookie jar on a pulley, 🍿 Popcorn machine\nLookout: 🔭 Telescope, 🏴‍☠️ Pirate crow’s nest\nSecret: 🚪 Trap door, 🗝️ Hidden key vault' };
      UI.editorErr = ''; UI.drawer = 'editor'; render();
    },
    'ed-kind': function (el) { UI.editor.kind = el.dataset.v; render(); },
    'ed-color': function (el) { UI.editor.color = el.dataset.v; render(); },
    'ed-save': function () {
      var r = parseEditor(UI.editor);
      if (r.err) { UI.editorErr = r.err; render(); return; }
      CUSTOM = CUSTOM.filter(function (m) { return m.id !== r.mode.id; });
      CUSTOM.push(r.mode);
      T.store.set(KEYS.custom, CUSTOM);
      T.addModes([r.mode]);
      UI.drawer = null; UI.editor = null; UI.filter = 'custom';
      toast('Saved “' + r.mode.name + '”. Find it under Your Own Modes.');
    },
    'ed-delete': function () {
      var id = UI.editor.id;
      CUSTOM = CUSTOM.filter(function (m) { return m.id !== id; });
      T.store.set(KEYS.custom, CUSTOM);
      if (!(G && G.modeId === id)) T.removeMode(id);
      UI.drawer = null; UI.editor = null; UI.filter = 'all';
      toast('Mode deleted.');
    },
    'edit-custom': function (el) {
      var raw = CUSTOM.filter(function (m) { return m.id === el.dataset.id; })[0];
      if (!raw) return;
      UI.editor = modeToEditor(raw); UI.editorErr = ''; UI.drawer = 'editor'; render();
    }
  };

  function doBid(pid, amount) {
    var why = T.placeBid(G, pid, amount);
    UI.msg = why;
    if (why) T.Sound.play('error');
    else {
      T.Sound.play('bid', amount);
      app.querySelectorAll('.bid-btns input').forEach(function (el) { el.value = ''; });
    }
    save(); render();
  }
  function secretEnter(amount) {
    var why = T.secretEnter(G, amount);
    if (why) { UI.msg = why; T.Sound.play('error'); render(); return; }
    UI.msg = ''; T.Sound.play(amount ? 'bid' : 'pass', amount);
    UI.overlay = { type: 'secret', step: 'locked' };
    save(); render();
  }
  function goNext() {
    if (T.isLastRound(G) || T.everyoneBroke(G)) { finishGame(); return; }
    T.next(G); UI.msg = ''; save(); render();
    var st = document.querySelector('.stage'); if (st && st.getBoundingClientRect().top < 0) st.scrollIntoView({ behavior: 'smooth' });
  }

  /* ---------- boot ---------- */
  var AI_BLOCKED = false;
  var AI_BLOCKED_MSG = 'AI paintings can\u2019t load inside this Claude page. Open the game\u2019s index.html file in a normal browser to use them.';
  T.boot = function (root, restored) {
    app = root;
    // Pages hosted inside the Claude viewer may only load images from their own files, so the AI painter cannot work there.
    AI_BLOCKED = !!(window.claude && window.claude.use);
    if (AI_BLOCKED) SETTINGS.ai = false;
    G = restored && restored.G ? restored.G : loadGame();
    if (restored && restored.UI) Object.assign(UI, restored.UI, { overlay: null, drawer: null });
    else if (G) UI.screen = G.over ? 'results' : 'game';
    app.addEventListener('click', function (e) {
      var el = e.target.closest('[data-act]');
      if (!el || el.disabled) return;
      var fn = A[el.dataset.act];
      if (fn) { e.preventDefault(); fn(el); }
    });
    app.addEventListener('input', function (e) {
      var el = e.target;
      if (el.dataset.input === 'pname') UI.setup.names[+el.dataset.i] = el.value;
      if (el.dataset.input === 'ed') UI.editor[el.dataset.k] = el.value;
    });
    app.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && e.target.id && e.target.id.indexOf('cb-') === 0) { e.preventDefault(); doBid(e.target.id.slice(3), parseInt(e.target.value, 10)); }
      if (e.key === 'Escape' && (UI.drawer || (UI.overlay && UI.overlay.type !== 'secret'))) { UI.drawer = null; UI.overlay = null; render(); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && (UI.drawer || (UI.overlay && UI.overlay.type !== 'secret')) && !app.contains(e.target)) { UI.drawer = null; UI.overlay = null; render(); }
    });
    render();
  };
  T.snapshot = function () { return { G: G, UI: { screen: UI.screen, filter: UI.filter, setup: UI.setup, nextNames: UI.nextNames, galleryIdx: UI.galleryIdx } }; };
})(window.TDA);
