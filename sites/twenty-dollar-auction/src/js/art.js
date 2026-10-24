/* Creation renderers. Each one draws a player's creation as SVG from their structured list of wins,
   so the picture always contains every feature they bought, and nothing they did not. */
(function (T) {
  'use strict';
  var esc = T.esc;
  var INK = '#14110F';
  var PAPER = '#FFFFFF';
  var LABEL_FONT = "'Bangers', 'Comic Neue', 'Trebuchet MS', sans-serif";
  var BODY_FONT = "'Comic Neue', 'Trebuchet MS', sans-serif";

  /* ---------- drawing helpers ---------- */

  function emo(x, y, size, e, extra) {
    extra = extra || '';
    return '<text x="' + x + '" y="' + y + '" font-size="' + size + '" text-anchor="middle" dominant-baseline="central" ' + extra + '>' + esc(e) + '</text>';
  }

  function wrap(text, max) {
    var words = String(text).split(/\s+/), lines = [], line = '';
    words.forEach(function (w) {
      if ((line + ' ' + w).trim().length > max && line) { lines.push(line); line = w; } else line = (line + ' ' + w).trim();
    });
    if (line) lines.push(line);
    return lines;
  }

  function label(x, y, text, opts) {
    opts = opts || {};
    var size = opts.size || 11, max = opts.max || 16, fill = opts.fill || INK;
    var lines = wrap(text, max).slice(0, opts.lines || 2);
    var out = '<text x="' + x + '" y="' + y + '" font-size="' + size + '" font-family="' + (opts.display ? LABEL_FONT : BODY_FONT) + '" font-weight="700" text-anchor="middle" fill="' + fill + '"' + (opts.letter ? ' letter-spacing="' + opts.letter + '"' : '') + '>';
    lines.forEach(function (l, i) { out += '<tspan x="' + x + '" dy="' + (i === 0 ? 0 : size * 1.1) + '">' + esc(l) + '</tspan>'; });
    return out + '</text>';
  }

  // A caption box: the yellow narration box of a comic panel.
  function caption(x, y, w, text, opts) {
    opts = opts || {};
    var size = opts.size || 16;
    return '<g><rect x="' + (x - w / 2) + '" y="' + y + '" width="' + w + '" height="' + (size + 12) + '" fill="' + (opts.fill || '#FFE94D') + '" stroke="' + INK + '" stroke-width="2.5"/>' +
      '<text x="' + x + '" y="' + (y + size / 2 + 7) + '" font-size="' + size + '" font-family="' + LABEL_FONT + '" text-anchor="middle" dominant-baseline="central" fill="' + INK + '" letter-spacing="1">' + esc(text) + '</text></g>';
  }

  function sticker(x, y, r, e, opts) {
    opts = opts || {};
    return '<g' + (opts.cls ? ' class="' + opts.cls + '"' : '') + '>' +
      '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="' + (opts.fill || PAPER) + '" stroke="' + INK + '" stroke-width="2.5"/>' +
      emo(x, y + 1, r * 1.15, e) + '</g>';
  }

  function emptySlot(x, y, r) {
    return '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="none" stroke="' + INK + '" stroke-opacity=".28" stroke-width="2" stroke-dasharray="5 5"/>';
  }

  function shade(hex, amt) {
    var c = (hex || '#888888').replace('#', '');
    if (c.length === 3) c = c.split('').map(function (x) { return x + x; }).join('');
    var n = parseInt(c, 16), r = n >> 16, g = n >> 8 & 255, b = n & 255;
    function f(v) { return Math.max(0, Math.min(255, Math.round(amt < 0 ? v * (1 + amt) : v + (255 - v) * amt))); }
    return '#' + [f(r), f(g), f(b)].map(function (v) { return ('0' + v.toString(16)).slice(-2); }).join('');
  }

  function dots(id, color, size, opacity) {
    return '<pattern id="' + id + '" width="' + size + '" height="' + size + '" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">' +
      '<circle cx="' + size / 2 + '" cy="' + size / 2 + '" r="' + size * 0.22 + '" fill="' + color + '" fill-opacity="' + (opacity || 0.35) + '"/></pattern>';
  }

  // Index wins by the round they came from, and group them by part.
  function collect(wins) {
    var byPart = {};
    wins.forEach(function (w) { (byPart[w.part] = byPart[w.part] || []).push(w); });
    return byPart;
  }

  // Positions of the rounds in this game that use a given part, so empty slots show where future wins land.
  function slotIndex(rounds, part, roundIdx) {
    var n = -1;
    for (var i = 0; i <= roundIdx; i++) if (rounds[i] && rounds[i].part === part) n++;
    return n;
  }
  function countPart(rounds, part) { return rounds.filter(function (r) { return r.part === part; }).length; }

  function popCls(w, ctx) { return ctx.newest && ctx.newest === w ? ' class="pop"' : ''; }

  // Wins whose part this renderer did not place still appear, as stickers along the bottom.
  function extrasRow(list, ctx, W, H) {
    if (!list.length) return '';
    var r = 20, gap = 46, start = W / 2 - (list.length - 1) * gap / 2, out = '';
    list.forEach(function (w, i) {
      out += '<g' + popCls(w, ctx) + '>' + sticker(start + i * gap, H - 28, r, w.item.emoji) + '</g>';
    });
    return out;
  }

  /* ---------- 1. building: house, restaurant, candy shop, school, secret HQ ---------- */

  var ROOM_TINTS = ['#FFF3B0', '#CDEBFF', '#FFD6E8', '#D7F5DD', '#FFE1C2', '#E6DBFF', '#D0F4F4', '#FFF0D9', '#E9F7C9', '#FDE2E4', '#DDEBFF', '#FFF7CC'];

  function building(ctx) {
    var W = 480, H = 360, skin = ctx.mode.skin, by = collect(ctx.wins), out = '';
    var under = skin === 'hq';
    var top = under ? 120 : 112, bottom = 334, left = 34, right = 446;
    var walls = { house: '#F6D7A7', restaurant: '#F9E0C7', candy: '#FFD3E6', school: '#F4C89A', hq: '#5B6474' }[skin] || '#F6D7A7';
    var sky = under ? '#9ED8FF' : '#BFE6FF';
    out += '<defs>' + dots('sky-' + ctx.uid, '#FFFFFF', 14, 0.55) + dots('rock-' + ctx.uid, '#000000', 9, 0.18) + '</defs>';
    out += '<rect width="' + W + '" height="' + H + '" fill="' + sky + '"/><rect width="' + W + '" height="' + H + '" fill="url(#sky-' + ctx.uid + ')"/>';
    if (under) {
      out += '<rect y="96" width="' + W + '" height="' + (H - 96) + '" fill="#7A5A3A"/><rect y="96" width="' + W + '" height="' + (H - 96) + '" fill="url(#rock-' + ctx.uid + ')"/>';
      out += '<rect y="86" width="' + W + '" height="14" fill="#4CAF50" stroke="' + INK + '" stroke-width="2.5"/>';
      out += emo(70, 64, 46, '🌳') + emo(410, 66, 40, '🪨') + emo(240, 70, 30, '🚪');
    } else {
      out += '<rect y="' + bottom + '" width="' + W + '" height="' + (H - bottom) + '" fill="#69C36B" stroke="' + INK + '" stroke-width="2.5"/>';
    }
    // roof and facade per skin
    if (skin === 'house') {
      out += '<path d="M' + (left - 18) + ' ' + top + ' L240 30 L' + (right + 18) + ' ' + top + ' Z" fill="#D9472B" stroke="' + INK + '" stroke-width="3" stroke-linejoin="round"/>';
      out += '<rect x="352" y="44" width="30" height="50" fill="#B23A22" stroke="' + INK + '" stroke-width="3"/>';
    } else if (skin === 'restaurant' || skin === 'candy') {
      var stripeA = skin === 'candy' ? '#FF5DA2' : '#E4002B', stripeB = '#FFFFFF';
      out += '<rect x="' + (left - 6) + '" y="' + (top - 52) + '" width="' + (right - left + 12) + '" height="52" fill="' + walls + '" stroke="' + INK + '" stroke-width="3"/>';
      for (var s = 0; s < 12; s++) {
        var sx = left - 10 + s * ((right - left + 20) / 12);
        out += '<path d="M' + sx + ' ' + (top - 10) + ' h' + ((right - left + 20) / 12) + ' v18 q-' + ((right - left + 20) / 24) + ' 14 -' + ((right - left + 20) / 12) + ' 0 z" fill="' + (s % 2 ? stripeB : stripeA) + '" stroke="' + INK + '" stroke-width="2"/>';
      }
      if (skin === 'candy') out += emo(left + 8, top - 70, 44, '🍭') + emo(right - 8, top - 70, 44, '🍭');
    } else if (skin === 'school') {
      out += '<rect x="' + (left - 8) + '" y="' + (top - 14) + '" width="' + (right - left + 16) + '" height="14" fill="#8B3A2E" stroke="' + INK + '" stroke-width="3"/>';
      out += '<rect x="205" y="34" width="70" height="66" fill="' + walls + '" stroke="' + INK + '" stroke-width="3"/><path d="M196 36 L240 6 L284 36 Z" fill="#8B3A2E" stroke="' + INK + '" stroke-width="3"/>';
      out += '<circle cx="240" cy="66" r="20" fill="#FFF" stroke="' + INK + '" stroke-width="3"/><path d="M240 66 V52 M240 66 H252" stroke="' + INK + '" stroke-width="3" stroke-linecap="round"/>';
    }
    out += '<rect x="' + left + '" y="' + top + '" width="' + (right - left) + '" height="' + (bottom - top) + '" fill="' + walls + '" stroke="' + INK + '" stroke-width="3"/>';
    // sign
    var sign = by.sign && by.sign[0];
    var signText = sign ? sign.item.name : (ctx.playerName ? ctx.playerName + '’s ' + ctx.mode.name.replace(/^Dream /, '') : ctx.mode.name);
    var signY = skin === 'house' ? 74 : skin === 'school' ? top - 2 : under ? 12 : top - 46;
    if (skin === 'house' || skin === 'school') signY = skin === 'house' ? 78 : 104;
    out += '<g' + (sign ? popCls(sign, ctx) : '') + '>' + caption(240, signY - 14, Math.min(300, 40 + signText.length * 9), signText, { size: 15, fill: sign ? '#FFE94D' : '#FFFFFF' }) + '</g>';
    // rooms: 4 x 3 grid
    var cols = 4, rows = 3, pad = 8;
    var cw = (right - left - pad * (cols + 1)) / cols, ch = (bottom - top - 14 - pad * (rows + 1)) / rows;
    var roomRounds = countPart(ctx.rounds, 'room');
    var rooms = by.room || [];
    for (var i = 0; i < cols * rows; i++) {
      var cx = left + pad + (i % cols) * (cw + pad), cy = top + 6 + pad + Math.floor(i / cols) * (ch + pad);
      var w = null;
      rooms.forEach(function (rw) { if (slotIndex(ctx.rounds, 'room', rw.round) === i) w = rw; });
      if (w) {
        out += '<g' + popCls(w, ctx) + '><rect x="' + cx + '" y="' + cy + '" width="' + cw + '" height="' + ch + '" fill="' + ROOM_TINTS[i % ROOM_TINTS.length] + '" stroke="' + INK + '" stroke-width="2.5"/>' +
          '<rect x="' + cx + '" y="' + (cy + ch - 9) + '" width="' + cw + '" height="9" fill="' + shade(ROOM_TINTS[i % ROOM_TINTS.length], -0.25) + '"/>' +
          emo(cx + cw / 2, cy + ch * 0.38, ch * 0.46, w.item.emoji) +
          label(cx + cw / 2, cy + ch - 15, w.item.name, { size: 9.5, max: 15, lines: 1 }) + '</g>';
      } else if (i < Math.max(roomRounds, 9)) {
        var lit = i < roomRounds;
        out += '<rect x="' + cx + '" y="' + cy + '" width="' + cw + '" height="' + ch + '" fill="' + (under ? '#3E4552' : '#FFFFFF') + '" fill-opacity="' + (under ? 1 : 0.55) + '" stroke="' + INK + '" stroke-width="2" stroke-opacity=".5"' + (lit ? ' stroke-dasharray="6 5"' : '') + '/>';
        if (!under) out += '<path d="M' + (cx + cw / 2) + ' ' + (cy + 8) + ' V' + (cy + ch - 8) + ' M' + (cx + 10) + ' ' + (cy + ch / 2) + ' H' + (cx + cw - 10) + '" stroke="' + INK + '" stroke-opacity=".18" stroke-width="2"/>';
      } else {
        out += '<rect x="' + cx + '" y="' + cy + '" width="' + cw + '" height="' + ch + '" fill="' + shade(walls, -0.08) + '" stroke="' + INK + '" stroke-width="2" stroke-opacity=".35"/>' + emo(cx + cw / 2, cy + ch / 2, 26, under ? '💡' : '🪟', 'opacity=".55"');
      }
    }
    var placed = { room: 1, sign: 1 };
    out += extrasRow(ctx.wins.filter(function (w) { return !placed[w.part]; }), ctx, W, H);
    return { w: W, h: H, body: out };
  }

  /* ---------- 2. figure: superhero, supervillain, robot, creature ---------- */

  function figure(ctx) {
    var W = 480, H = 360, skin = ctx.mode.skin, by = collect(ctx.wins), out = '', u = ctx.uid;
    function one(part) { return by[part] && by[part][by[part].length - 1]; }
    var suit = one('color'), mask = one('mask'), aura = one('aura'), aura2 = one('aura2'), hand = one('hand');
    var title = one('title'), buddy = one('buddy'), home = one('home'), emblem = one('emblem'), rival = one('rival');
    var head = one('head'), back = one('back'), feet = one('feet'), tail = one('tail');
    var villain = skin === 'villain';
    var skyA = villain ? '#3B1E54' : '#2E9BE6', skyB = villain ? '#7A3E9D' : '#9EDBFF';
    out += '<defs><linearGradient id="sky' + u + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="' + skyA + '"/><stop offset="1" stop-color="' + skyB + '"/></linearGradient>' +
      dots('ht' + u, '#FFFFFF', 12, 0.25) +
      (aura ? '<radialGradient id="aura' + u + '"><stop offset="0" stop-color="' + (aura.item.color || '#FFD60A') + '" stop-opacity=".95"/><stop offset=".6" stop-color="' + (aura.item.color || '#FFD60A') + '" stop-opacity=".35"/><stop offset="1" stop-color="' + (aura.item.color || '#FFD60A') + '" stop-opacity="0"/></radialGradient>' : '') +
      (aura2 ? '<radialGradient id="aurb' + u + '"><stop offset=".55" stop-color="' + (aura2.item.color || '#F15BB5') + '" stop-opacity="0"/><stop offset=".75" stop-color="' + (aura2.item.color || '#F15BB5') + '" stop-opacity=".55"/><stop offset="1" stop-color="' + (aura2.item.color || '#F15BB5') + '" stop-opacity="0"/></radialGradient>' : '') +
      '</defs>';
    out += '<rect width="' + W + '" height="' + H + '" fill="url(#sky' + u + ')"/><rect width="' + W + '" height="' + H + '" fill="url(#ht' + u + ')"/>';
    // action lines radiating from the hero
    for (var k = 0; k < 18; k++) {
      var a = k / 18 * Math.PI * 2;
      out += '<path d="M' + (240 + Math.cos(a) * 120) + ' ' + (190 + Math.sin(a) * 120) + ' L' + (240 + Math.cos(a) * 340) + ' ' + (190 + Math.sin(a) * 340) + '" stroke="#FFFFFF" stroke-opacity=".18" stroke-width="' + (k % 2 ? 6 : 14) + '"/>';
    }
    if (home) out += '<g' + popCls(home, ctx) + '>' + emo(414, 262, 104, home.item.emoji, 'opacity=".9"') + caption(400, 322, 150, home.item.name, { size: 12, fill: '#FFFFFF' }) + '</g>';
    out += '<ellipse cx="240" cy="338" rx="120" ry="14" fill="#000" fill-opacity=".22"/>';
    if (aura) out += '<g' + popCls(aura, ctx) + '><circle cx="240" cy="190" r="165" fill="url(#aura' + u + ')"/>' + emo(118, 120, 34, aura.item.emoji) + emo(362, 110, 30, aura.item.emoji) + emo(128, 250, 26, aura.item.emoji) + '</g>';
    if (aura2) out += '<g' + popCls(aura2, ctx) + '><circle cx="240" cy="190" r="150" fill="url(#aurb' + u + ')"/>' + emo(346, 214, 30, aura2.item.emoji) + emo(150, 66, 26, aura2.item.emoji) + '</g>';

    var body = suit ? suit.item.color : '#C9CED6';
    var bodyDark = shade(body, -0.3);
    var skinTone = '#F2C9A0';
    var stroke = ' stroke="' + INK + '" stroke-width="3" stroke-linejoin="round"';
    var dashed = suit ? '' : ' stroke-dasharray="7 5"';
    var fig = '';

    if (back) fig += '<g' + popCls(back, ctx) + '>' + emo(168, 150, 78, back.item.emoji, 'transform="translate(336 0) scale(-1 1)"') + emo(312, 150, 78, back.item.emoji) + '</g>';
    if (tail) fig += '<g' + popCls(tail, ctx) + '>' + emo(318, 262, 64, tail.item.emoji) + '</g>';

    if (skin === 'robot') {
      fig += '<rect x="208" y="244" width="22" height="70"' + stroke + ' fill="' + bodyDark + '"' + dashed + '/><rect x="250" y="244" width="22" height="70"' + stroke + ' fill="' + bodyDark + '"' + dashed + '/>';
      fig += '<rect x="150" y="150" width="26" height="86" rx="10"' + stroke + ' fill="' + bodyDark + '" transform="rotate(14 163 150)"' + dashed + '/>';
      fig += '<rect x="304" y="150" width="26" height="86" rx="10"' + stroke + ' fill="' + bodyDark + '" transform="rotate(-50 317 150)"' + dashed + '/>';
      fig += '<rect x="180" y="140" width="120" height="110" rx="12"' + stroke + ' fill="' + body + '"' + dashed + '/>';
      [[192, 152], [288, 152], [192, 238], [288, 238]].forEach(function (p) { fig += '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="3.5" fill="' + INK + '"/>'; });
      fig += '<circle cx="240" cy="195" r="24" fill="' + (aura ? aura.item.color : '#E9ECEF') + '"' + stroke + '/>';
      fig += '<rect x="230" y="122" width="20" height="20"' + stroke + ' fill="' + bodyDark + '"/>';
      var hs = mask ? mask.item.shape : null;
      if (hs === 'dome') {
        fig += '<rect x="196" y="78" width="88" height="48" rx="8"' + stroke + ' fill="' + body + '"/><path d="M200 82 A40 40 0 0 1 280 82 Z" fill="#BDE8FF" fill-opacity=".85"' + stroke + '/>' + emo(240, 70, 22, '⚙️');
      } else {
        fig += '<rect x="194" y="58" width="92" height="68" rx="' + (hs === 'screen' ? 6 : 14) + '"' + stroke + ' fill="' + (mask ? mask.item.color : body) + '"' + dashed + '/>';
        if (hs === 'antenna') fig += '<path d="M240 58 V30" stroke="' + INK + '" stroke-width="3"/><circle cx="240" cy="26" r="7" fill="#E4002B"' + stroke + '/>';
      }
      if (hs === 'screen') fig += '<rect x="202" y="66" width="76" height="52" rx="4" fill="#0B132B"/>' + emo(240, 92, 34, emblem ? emblem.item.emoji : '🙂');
      else if (hs !== 'dome') fig += '<rect x="208" y="80" width="64" height="18" rx="9" fill="#0B132B"/><circle cx="226" cy="89" r="5" fill="#5BFFB4"/><circle cx="254" cy="89" r="5" fill="#5BFFB4"/>';
      if (aura) fig += emo(240, 196, 26, aura.item.emoji);
    } else if (skin === 'creature') {
      fig += '<ellipse cx="240" cy="230" rx="78" ry="74"' + stroke + ' fill="' + body + '"' + dashed + '/>';
      fig += '<ellipse cx="240" cy="246" rx="44" ry="44" fill="' + shade(body, 0.45) + '"/>';
      fig += '<circle cx="240" cy="132" r="56"' + stroke + ' fill="' + body + '"' + dashed + '/>';
      fig += '<circle cx="219" cy="126" r="14" fill="#FFF"' + stroke + '/><circle cx="261" cy="126" r="14" fill="#FFF"' + stroke + '/><circle cx="222" cy="128" r="7" fill="' + INK + '"/><circle cx="264" cy="128" r="7" fill="' + INK + '"/>';
      fig += '<path d="M228 154 Q240 166 252 154" fill="none" stroke="' + INK + '" stroke-width="3" stroke-linecap="round"/><circle cx="204" cy="150" r="7" fill="#FF8FAB" fill-opacity=".7"/><circle cx="276" cy="150" r="7" fill="#FF8FAB" fill-opacity=".7"/>';
      if (head) fig += '<g' + popCls(head, ctx) + '>' + emo(240, 72, 52, head.item.emoji) + '</g>';
      if (emblem) fig += '<g' + popCls(emblem, ctx) + '>' + sticker(240, 240, 20, emblem.item.emoji) + '</g>';
    } else {
      // humanoid hero or villain
      var cape = suit && suit.item.shape === 'cape';
      if (cape) fig += '<path d="M196 142 Q160 250 172 318 L308 318 Q320 250 284 142 Z" fill="' + bodyDark + '"' + stroke + '/>';
      fig += '<path d="M214 248 L208 318 L232 318 L238 258 Z" fill="' + body + '"' + stroke + dashed + '/><path d="M266 248 L272 318 L248 318 L242 258 Z" fill="' + body + '"' + stroke + dashed + '/>';
      fig += '<rect x="202" y="300" width="34" height="22" rx="6" fill="' + bodyDark + '"' + stroke + '/><rect x="244" y="300" width="34" height="22" rx="6" fill="' + bodyDark + '"' + stroke + '/>';
      // left arm down on hip, right arm raised
      fig += '<path d="M200 150 Q170 190 186 232" fill="none" stroke="' + INK + '" stroke-width="22" stroke-linecap="round"/><path d="M200 150 Q170 190 186 232" fill="none" stroke="' + body + '" stroke-width="16" stroke-linecap="round"/>';
      fig += '<path d="M282 150 Q318 130 330 92" fill="none" stroke="' + INK + '" stroke-width="22" stroke-linecap="round"/><path d="M282 150 Q318 130 330 92" fill="none" stroke="' + body + '" stroke-width="16" stroke-linecap="round"/>';
      fig += '<circle cx="186" cy="234" r="11" fill="' + skinTone + '"' + stroke + '/><circle cx="331" cy="88" r="11" fill="' + skinTone + '"' + stroke + '/>';
      fig += '<path d="M198 140 Q240 128 282 140 L274 254 Q240 262 206 254 Z" fill="' + body + '"' + stroke + dashed + '/>';
      fig += '<rect x="206" y="236" width="68" height="12" fill="' + (villain ? '#111' : '#FFD60A') + '"' + stroke + '/>';
      fig += '<rect x="230" y="114" width="20" height="22" fill="' + skinTone + '"' + stroke + '/>';
      fig += '<circle cx="240" cy="96" r="32" fill="' + skinTone + '"' + stroke + '/>';
      var ms = mask ? mask.item.shape : null, mc = mask ? mask.item.color : null;
      if (ms === 'hood') fig += '<path d="M204 112 Q200 52 240 54 Q280 52 276 112 Q262 76 240 76 Q218 76 204 112 Z" fill="' + mc + '"' + stroke + '/>';
      if (ms === 'helmet') fig += '<path d="M206 98 Q206 56 240 56 Q274 56 274 98 Z" fill="' + mc + '"' + stroke + '/><rect x="214" y="84" width="52" height="14" rx="7" fill="#7FDBFF"' + stroke + '/>';
      else {
        fig += '<circle cx="229" cy="94" r="3.5" fill="' + INK + '"/><circle cx="251" cy="94" r="3.5" fill="' + INK + '"/>';
        fig += villain ? '<path d="M228 110 Q240 104 252 110" fill="none" stroke="' + INK + '" stroke-width="3" stroke-linecap="round"/><path d="M222 86 L234 90 M258 86 L246 90" stroke="' + INK + '" stroke-width="3" stroke-linecap="round"/>'
          : '<path d="M228 106 Q240 116 252 106" fill="none" stroke="' + INK + '" stroke-width="3" stroke-linecap="round"/>';
      }
      if (ms === 'mask') fig += '<path d="M210 88 Q240 80 270 88 L268 100 Q254 96 240 100 Q226 96 212 100 Z" fill="' + mc + '"' + stroke + '/><circle cx="229" cy="93" r="3" fill="#FFF"/><circle cx="251" cy="93" r="3" fill="#FFF"/>';
      if (ms === 'crown') fig += '<path d="M212 70 L218 46 L230 62 L240 40 L250 62 L262 46 L268 70 Z" fill="' + mc + '"' + stroke + '/>';
      if (ms === 'tophat') fig += '<rect x="214" y="58" width="52" height="8" fill="' + mc + '"' + stroke + '/><rect x="222" y="24" width="36" height="36" fill="' + mc + '"' + stroke + '/><circle cx="251" cy="94" r="8" fill="none" stroke="#E8B10C" stroke-width="3"/>';
      if (!mask) fig += '<path d="M210 84 Q214 60 240 60 Q266 60 270 84 Q256 72 240 74 Q222 72 210 84 Z" fill="#3D2B1F"/>';
      if (emblem) fig += '<g' + popCls(emblem, ctx) + '>' + sticker(240, 186, 22, emblem.item.emoji, { fill: '#FFE94D' }) + '</g>';
      else if (suit) fig += '<path d="M226 170 L240 196 L254 170 Z" fill="#FFE94D"' + stroke + '/>';
    }
    if (feet) fig += '<g' + popCls(feet, ctx) + '>' + emo(206, 324, 40, feet.item.emoji) + emo(274, 324, 40, feet.item.emoji) + '</g>';
    if (hand) fig += '<g' + popCls(hand, ctx) + '>' + emo(skin === 'robot' ? 356 : 340, skin === 'robot' ? 120 : 70, 50, hand.item.emoji) + '</g>';
    var figPop = (suit && ctx.newest === suit) || (mask && ctx.newest === mask);
    out += '<g' + (figPop ? ' class="pop"' : '') + '>' + fig + '</g>';
    if (buddy) out += '<g' + popCls(buddy, ctx) + '>' + emo(92, 300, 64, buddy.item.emoji) + caption(92, 330, 130, buddy.item.name, { size: 11, fill: '#FFFFFF' }) + '</g>';
    if (rival) out += '<g' + popCls(rival, ctx) + '><rect x="12" y="62" width="104" height="96" fill="#FFF" stroke="' + INK + '" stroke-width="3" transform="rotate(-4 64 110)"/>' + emo(64, 104, 46, rival.item.emoji) + label(64, 146, 'VS ' + rival.item.name, { size: 10, max: 16, lines: 2 }) + '</g>';
    var titleText = title ? title.item.name : (ctx.playerName ? ctx.playerName + '’s ' + ctx.mode.name.replace(/^Dream /, '') : ctx.mode.name);
    out += '<g' + (title ? popCls(title, ctx) : '') + '>' + caption(240, 10, Math.min(320, 60 + titleText.length * 10), titleText, { size: 20, fill: title ? '#FFE94D' : '#FFFFFF' }) + '</g>';
    var placed = { color: 1, mask: 1, aura: 1, aura2: 1, hand: 1, title: 1, buddy: 1, home: 1, emblem: 1, rival: 1, head: 1, back: 1, feet: 1, tail: 1 };
    out += extrasRow(ctx.wins.filter(function (w) { return !placed[w.part]; }), ctx, W, H);
    return { w: W, h: H, body: out };
  }

  /* ---------- 3. poster: movie, video game ---------- */

  function shortName(n) { return String(n).replace(/^(A|An|The)\s+/i, ''); }

  function poster(ctx) {
    var W = 360, H = 480, by = collect(ctx.wins), out = '', u = ctx.uid, game = ctx.mode.skin === 'game';
    function one(p) { return by[p] && by[p][by[p].length - 1]; }
    var theme = one('theme'), lead = one('lead'), villain = one('villain'), setting = one('setting');
    var cast = by.cast || [], credits = by.credit || [], tags = by.tagline || [], villains = by.villain || [];
    var bg = theme ? theme.item.color : '#23264A';
    out += '<defs><radialGradient id="pg' + u + '" cx=".5" cy=".42" r=".7"><stop offset="0" stop-color="' + shade(bg, 0.35) + '"/><stop offset="1" stop-color="' + shade(bg, -0.35) + '"/></radialGradient>' + dots('pd' + u, '#FFFFFF', 10, 0.12) + '</defs>';
    out += '<rect width="' + W + '" height="' + H + '" fill="url(#pg' + u + ')"/><rect width="' + W + '" height="' + H + '" fill="url(#pd' + u + ')"/>';
    for (var k = 0; k < 16; k++) {
      var a = k / 16 * Math.PI * 2;
      out += '<path d="M180 210 L' + (180 + Math.cos(a) * 420) + ' ' + (210 + Math.sin(a) * 420) + ' L' + (180 + Math.cos(a + 0.12) * 420) + ' ' + (210 + Math.sin(a + 0.12) * 420) + ' Z" fill="#FFFFFF" fill-opacity=".05"/>';
    }
    if (theme) out += '<g' + popCls(theme, ctx) + '>' + emo(300, 70, 54, theme.item.emoji, 'opacity=".85"') + '</g>';
    if (setting) out += '<g' + popCls(setting, ctx) + '>' + emo(180, 330, 170, setting.item.emoji, 'opacity=".55"') + '</g>';
    villains.forEach(function (v, i) {
      out += '<g' + popCls(v, ctx) + '>' + emo(i ? 70 : 286, i ? 120 : 150, i ? 70 : 96, v.item.emoji, 'opacity=".92"') + '</g>';
    });
    cast.forEach(function (c, i) {
      var x = i % 2 ? 278 : 82, y = 250 + Math.floor(i / 2) * 40;
      out += '<g' + popCls(c, ctx) + '>' + emo(x, y, 64, c.item.emoji) + '</g>';
    });
    if (lead) out += '<g' + popCls(lead, ctx) + '>' + emo(180, 220, 128, lead.item.emoji) + '</g>';
    else out += '<g opacity=".5"><circle cx="180" cy="220" r="62" fill="none" stroke="#FFF" stroke-width="3" stroke-dasharray="8 7"/>' + label(180, 226, game ? 'Hero wanted' : 'Star wanted', { size: 14, fill: '#FFFFFF', display: true }) + '</g>';
    // title
    var title;
    if (game) title = lead ? shortName(lead.item.name) + (theme ? ': ' + theme.item.name : '') : (ctx.playerName ? ctx.playerName + '’s Game' : 'Untitled Game');
    else title = lead && villain ? shortName(lead.item.name) + ' vs. ' + shortName(villain.item.name) : lead ? 'The ' + shortName(lead.item.name) : (ctx.playerName ? ctx.playerName + '’s Movie' : 'Untitled Movie');
    var tl = wrap(title.toUpperCase(), 18).slice(0, 3);
    out += '<g>';
    tl.forEach(function (l, i) {
      out += '<text x="180" y="' + (28 + i * 36) + '" font-size="34" font-family="' + LABEL_FONT + '" text-anchor="middle" dominant-baseline="hanging" fill="#FFE94D" stroke="' + INK + '" stroke-width="6" paint-order="stroke" letter-spacing="1.5">' + esc(l) + '</text>';
    });
    out += '</g>';
    if (theme) out += label(180, 28 + tl.length * 36 + 18, theme.item.name.toUpperCase(), { size: 12, fill: '#FFFFFF', max: 40, lines: 1, letter: 2 });
    // tagline + credits at bottom
    var y = 380;
    tags.forEach(function (t) {
      out += '<g' + popCls(t, ctx) + '>' + caption(180, y, 300, t.item.name, { size: 13 }) + '</g>';
      y += 30;
    });
    var creditText = credits.map(function (c) { return c.item.name; }).join('  •  ');
    if (creditText) {
      var cl = wrap(creditText, 52).slice(0, 2);
      out += '<g' + (credits.length ? popCls(credits[credits.length - 1], ctx) : '') + '>';
      cl.forEach(function (l, i) { out += '<text x="180" y="' + (H - 24 + i * 12 - (cl.length - 1) * 12) + '" font-size="10" font-family="' + BODY_FONT + '" font-weight="700" text-anchor="middle" fill="#FFFFFF" fill-opacity=".85">' + esc(l) + '</text>'; });
      out += '</g>';
    }
    if (game) out += '<g font-family="' + LABEL_FONT + '" font-size="12" fill="#FFFFFF"><text x="14" y="' + (H - 8) + '">PRESS START</text><text x="' + (W - 14) + '" y="' + (H - 8) + '" text-anchor="end">♥ ♥ ♥</text></g>';
    var placed = { theme: 1, lead: 1, villain: 1, setting: 1, cast: 1, credit: 1, tagline: 1 };
    out += extrasRow(ctx.wins.filter(function (w) { return !placed[w.part]; }), ctx, W, H - 40);
    return { w: W, h: H, body: out };
  }

  /* ---------- 4. map: vacation, theme park, festival, boardwalk, fantasy, island ---------- */

  var MAP_SLOTS = {
    blob: [[150, 118], [246, 96], [336, 128], [112, 196], [204, 182], [300, 196], [386, 214], [150, 270], [250, 262], [340, 286]],
    rect: [[96, 120], [192, 112], [288, 112], [384, 120], [96, 210], [192, 200], [288, 200], [384, 210], [144, 290], [336, 290]],
    pier: [[90, 150], [190, 150], [290, 150], [390, 150], [90, 230], [190, 230], [290, 230], [390, 230], [140, 300], [340, 300]]
  };

  function map(ctx) {
    var W = 480, H = 360, skin = ctx.mode.skin, by = collect(ctx.wins), out = '', u = ctx.uid;
    var shape = { park: 'rect', festival: 'rect', boardwalk: 'pier' }[skin] || 'blob';
    var sea = { fantasy: '#4F6BD8', festival: '#8ED081' }[skin] || '#2FA7E0';
    var land = { fantasy: '#7BC67E', park: '#A8DF65', festival: '#F4D06F', island: '#F2D27E', beach: '#F2D27E', boardwalk: '#C99A5B' }[skin] || '#A8DF65';
    out += '<defs>' + dots('w' + u, '#FFFFFF', 16, 0.35) + dots('l' + u, '#000000', 10, 0.08) + '</defs>';
    out += '<rect width="' + W + '" height="' + H + '" fill="' + sea + '"/><rect width="' + W + '" height="' + H + '" fill="url(#w' + u + ')"/>';
    if (skin === 'festival') out += '<rect width="' + W + '" height="70" fill="#FF9F68"/><circle cx="400" cy="70" r="40" fill="#FFE94D"/>';
    if (shape === 'blob') {
      out += '<path d="M70 150 C60 80 170 50 250 62 C340 60 440 90 440 170 C460 250 400 330 300 326 C200 340 90 330 70 260 C50 220 76 190 70 150 Z" fill="' + land + '" stroke="' + INK + '" stroke-width="3"/>';
      out += '<path d="M70 150 C60 80 170 50 250 62 C340 60 440 90 440 170 C460 250 400 330 300 326 C200 340 90 330 70 260 C50 220 76 190 70 150 Z" fill="url(#l' + u + ')"/>';
      out += '<path d="M90 140 C82 96 170 76 250 84 C330 82 418 104 420 172 C434 240 384 304 300 306 C204 318 108 310 92 254 C78 218 96 188 90 140 Z" fill="none" stroke="#FFFFFF" stroke-opacity=".6" stroke-width="3" stroke-dasharray="10 8"/>';
    } else if (shape === 'rect') {
      out += '<rect x="34" y="' + (skin === 'festival' ? 74 : 60) + '" width="412" height="' + (skin === 'festival' ? 270 : 284) + '" rx="26" fill="' + land + '" stroke="' + INK + '" stroke-width="3"/>';
      out += '<path d="M60 160 H420 M60 250 H420 M240 90 V330" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round" stroke-opacity=".75"/>';
    } else {
      out += '<rect x="30" y="104" width="420" height="230" fill="' + land + '" stroke="' + INK + '" stroke-width="3"/>';
      for (var p = 0; p < 21; p++) out += '<path d="M' + (30 + p * 20) + ' 104 V334" stroke="' + INK + '" stroke-opacity=".18" stroke-width="2"/>';
      out += '<path d="M0 104 H480" stroke="' + INK + '" stroke-width="3"/><rect x="0" y="60" width="480" height="44" fill="#F5E6C8"/>';
    }
    var spots = by.spot || [], slots = MAP_SLOTS[shape];
    var total = countPart(ctx.rounds, 'spot');
    for (var i = 0; i < Math.max(total, 0) && i < slots.length; i++) {
      var w = null;
      spots.forEach(function (sw) { if (slotIndex(ctx.rounds, 'spot', sw.round) === i) w = sw; });
      var s = slots[i];
      if (w) {
        out += '<g' + popCls(w, ctx) + '>' + sticker(s[0], s[1], 27, w.item.emoji) +
          '<rect x="' + (s[0] - 46) + '" y="' + (s[1] + 28) + '" width="92" height="17" fill="#FFFFFF" stroke="' + INK + '" stroke-width="2"/>' +
          label(s[0], s[1] + 40, w.item.name, { size: 9.5, max: 18, lines: 1 }) + '</g>';
      } else {
        out += emptySlot(s[0], s[1], 22) + '<text x="' + s[0] + '" y="' + (s[1] + 4) + '" font-size="10" font-family="' + BODY_FONT + '" font-weight="700" text-anchor="middle" fill="' + INK + '" fill-opacity=".35">SOLD?</text>';
      }
    }
    var banner = by.banner && by.banner[by.banner.length - 1];
    var bt = banner ? banner.item.name : (ctx.playerName ? ctx.playerName + '’s ' + ctx.mode.name.replace(/^Dream /, '') : ctx.mode.name);
    out += '<g' + (banner ? popCls(banner, ctx) : '') + '>' + caption(240, 8, Math.min(330, 70 + bt.length * 9), (banner ? banner.item.emoji + ' ' : '') + bt, { size: 17, fill: banner ? '#FFE94D' : '#FFFFFF' }) + '</g>';
    var placed = { spot: 1, banner: 1 };
    out += extrasRow(ctx.wins.filter(function (w) { return !placed[w.part]; }), ctx, W, H);
    return { w: W, h: H, body: out };
  }

  /* ---------- 5. stage: gaming setup, bedroom ---------- */

  var STAGE = {
    gaming: { monitor: [240, 132, 92], pc: [392, 214, 74], console: [104, 232, 58], chair: [240, 284, 70], 'desk-item': [[170, 222, 40], [312, 222, 40]], desk: [240, 250, 0], light: [0, 0, 0], poster: [76, 104, 60] },
    bedroom: { bed: [128, 268, 112], door: [430, 214, 70], screen: [262, 132, 72], nook: [[370, 300, 58], [300, 306, 52]], pet: [212, 314, 50], light: [0, 0, 0], shelf: [372, 112, 54], ceiling: [96, 74, 54] }
  };

  function stage(ctx) {
    var W = 480, H = 360, skin = ctx.mode.skin, by = collect(ctx.wins), out = '', u = ctx.uid, cfg = STAGE[skin] || STAGE.gaming;
    var wall = by.wall && by.wall[0];
    var wallColor = wall ? wall.item.color : '#E9E3D5';
    var light = by.light && by.light[0];
    out += '<defs>' + dots('sd' + u, '#FFFFFF', 14, wall ? 0.16 : 0.45) +
      (light ? '<radialGradient id="glow' + u + '" cx=".5" cy="0" r="1"><stop offset="0" stop-color="' + light.item.color + '" stop-opacity=".75"/><stop offset="1" stop-color="' + light.item.color + '" stop-opacity="0"/></radialGradient>' : '') + '</defs>';
    out += '<g' + (wall ? popCls(wall, ctx) : '') + '><rect width="' + W + '" height="250" fill="' + wallColor + '"/><rect width="' + W + '" height="250" fill="url(#sd' + u + ')"/>';
    if (wall) out += emo(60, 40, 30, wall.item.emoji, 'opacity=".55"') + emo(430, 46, 26, wall.item.emoji, 'opacity=".55"') + emo(250, 30, 22, wall.item.emoji, 'opacity=".45"');
    out += '</g>';
    out += '<path d="M0 250 H480 V360 H0 Z" fill="' + (skin === 'bedroom' ? '#C8A27A' : '#4A4E69') + '" stroke="' + INK + '" stroke-width="3"/>';
    for (var f = 0; f < 8; f++) out += '<path d="M' + (f * 70 - 20) + ' 360 L' + (f * 60 + 20) + ' 250" stroke="' + INK + '" stroke-opacity=".15" stroke-width="2"/>';
    if (light) out += '<g' + popCls(light, ctx) + '><rect width="' + W + '" height="' + H + '" fill="url(#glow' + u + ')"/><rect x="0" y="0" width="' + W + '" height="10" fill="' + light.item.color + '" stroke="' + INK + '" stroke-width="2"/>' + emo(452, 30, 26, light.item.emoji) + '</g>';
    if (skin === 'gaming') {
      var desk = by.desk && by.desk[0];
      out += '<g' + (desk ? popCls(desk, ctx) : '') + '><rect x="96" y="236" width="288" height="22" fill="' + (desk ? '#2B2D42' : 'none') + '" stroke="' + INK + '" stroke-width="3"' + (desk ? '' : ' stroke-dasharray="8 6" stroke-opacity=".5"') + '/>' +
        (desk ? '<rect x="110" y="258" width="14" height="70" fill="#2B2D42" stroke="' + INK + '" stroke-width="3"/><rect x="356" y="258" width="14" height="70" fill="#2B2D42" stroke="' + INK + '" stroke-width="3"/>' + emo(120, 222, 22, desk.item.emoji) : '') + '</g>';
    }
    var placed = { wall: 1, light: 1, desk: 1 };
    Object.keys(cfg).forEach(function (part) {
      if (placed[part]) return;
      placed[part] = 1;
      var spots = Array.isArray(cfg[part][0]) ? cfg[part] : [cfg[part]];
      var list = by[part] || [];
      var expected = Math.min(countPart(ctx.rounds, part), spots.length);
      spots.forEach(function (s, i) {
        var w = list[i];
        if (w) {
          var frame = part === 'monitor' || part === 'screen' || part === 'poster';
          out += '<g' + popCls(w, ctx) + '>';
          if (frame) out += '<rect x="' + (s[0] - s[2] * 0.75) + '" y="' + (s[1] - s[2] * 0.55) + '" width="' + s[2] * 1.5 + '" height="' + s[2] * 1.1 + '" rx="6" fill="#0B132B" stroke="' + INK + '" stroke-width="3"/>';
          out += emo(s[0], s[1], s[2] * (frame ? 0.8 : 1), w.item.emoji);
          out += label(s[0], s[1] + s[2] * 0.62 + 10, w.item.name, { size: 9.5, max: 16, lines: 1, fill: frame || s[1] < 250 ? INK : '#FFFFFF' });
          out += '</g>';
        } else if (i < expected) {
          out += emptySlot(s[0], s[1], Math.max(18, s[2] * 0.4));
        }
      });
    });
    out += extrasRow(ctx.wins.filter(function (w) { return !placed[w.part]; }), ctx, W, H);
    return { w: W, h: H, body: out };
  }

  /* ---------- 6. vehicle: car ---------- */

  function vehicle(ctx) {
    var W = 480, H = 360, by = collect(ctx.wins), out = '', u = ctx.uid;
    function one(p) { return by[p] && by[p][by[p].length - 1]; }
    var bodyW = one('body'), paint = one('paint'), wheels = one('wheels'), glow = one('glow'), decal = one('decal');
    var style = bodyW ? bodyW.item.shape : 'plain';
    var color = paint ? paint.item.color : '#D9DDE3';
    var dark = shade(color, -0.35);
    var stroke = ' stroke="' + INK + '" stroke-width="3" stroke-linejoin="round"';
    var dash = paint ? '' : ' stroke-dasharray="8 6"';
    out += '<defs>' + dots('cd' + u, '#FFFFFF', 12, 0.4) +
      (glow ? '<radialGradient id="ug' + u + '"><stop offset="0" stop-color="' + glow.item.color + '" stop-opacity=".9"/><stop offset="1" stop-color="' + glow.item.color + '" stop-opacity="0"/></radialGradient>' : '') + '</defs>';
    out += '<rect width="' + W + '" height="' + H + '" fill="#FFB347"/><rect width="' + W + '" height="' + H + '" fill="url(#cd' + u + ')"/>';
    // skyline
    [[20, 120], [70, 90], [130, 140], [380, 100], [430, 130]].forEach(function (b, i) {
      out += '<rect x="' + b[0] + '" y="' + b[1] + '" width="' + (i % 2 ? 44 : 56) + '" height="' + (250 - b[1]) + '" fill="#F28C28" stroke="' + INK + '" stroke-opacity=".35" stroke-width="2"/>';
    });
    out += '<rect y="250" width="' + W + '" height="110" fill="#3D405B"/><path d="M0 306 H480" stroke="#FFE94D" stroke-width="6" stroke-dasharray="30 22"/>';
    var lift = style === 'truck' ? -34 : style === 'hover' ? -26 : 0;
    var wy = 262 + lift;
    if (glow) out += '<g' + popCls(glow, ctx) + '><ellipse cx="240" cy="' + (style === 'hover' ? 292 : 290) + '" rx="190" ry="26" fill="url(#ug' + u + ')"/></g>';
    var car = '<g' + (bodyW && ctx.newest === bodyW || paint && ctx.newest === paint ? ' class="pop"' : '') + '>';
    var bodyPath = {
      sport: 'M70 ' + (250 + lift) + ' Q70 210 130 200 L200 168 Q240 156 300 168 L370 196 Q420 206 418 250 L418 ' + (258 + lift) + ' Z',
      truck: 'M70 ' + (226 + lift) + ' L74 ' + (176 + lift) + ' L170 ' + (170 + lift) + ' L200 ' + (122 + lift) + ' L300 ' + (122 + lift) + ' L320 ' + (170 + lift) + ' L414 ' + (176 + lift) + ' L414 ' + (234 + lift) + ' Z',
      classic: 'M66 ' + (250 + lift) + ' Q66 206 120 200 L170 196 Q190 160 240 160 L300 160 Q330 166 346 196 L400 200 Q424 210 420 250 Z',
      hover: 'M80 ' + (246 + lift) + ' Q60 200 140 186 Q200 140 280 140 Q380 150 410 200 Q430 240 400 ' + (250 + lift) + ' Z',
      plain: 'M72 250 Q72 212 120 204 L172 172 Q196 160 240 160 L292 160 Q320 166 338 196 L392 204 Q420 212 418 250 Z'
    }[style] || '';
    car += '<path d="' + bodyPath + '" fill="' + color + '"' + stroke + dash + '/>';
    if (style === 'truck') car += '<rect x="68" y="' + (226 + lift) + '" width="348" height="40" fill="' + dark + '"' + stroke + '/>';
    if (decal) {
      car += '<g' + popCls(decal, ctx) + '>';
      if (/stripe/i.test(decal.item.name)) car += '<path d="M90 ' + (226 + lift) + ' H404" stroke="#FFFFFF" stroke-width="10"/><path d="M90 ' + (240 + lift) + ' H404" stroke="#FFFFFF" stroke-width="10"/>';
      else car += emo(160, 228 + lift, 28, decal.item.emoji) + emo(214, 228 + lift, 28, decal.item.emoji) + emo(268, 228 + lift, 28, decal.item.emoji) + emo(322, 228 + lift, 28, decal.item.emoji);
      car += '</g>';
    }
    // windows
    var winY = { sport: 178, truck: 132, classic: 172, hover: 160, plain: 174 }[style] + (style === 'truck' ? lift : 0);
    car += '<path d="M' + (style === 'truck' ? 212 : 196) + ' ' + (winY + 22) + ' L' + (style === 'truck' ? 216 : 214) + ' ' + winY + ' L' + (style === 'truck' ? 290 : 296) + ' ' + winY + ' L' + (style === 'truck' ? 304 : 320) + ' ' + (winY + 22) + ' Z" fill="#BDE8FF"' + stroke + '/>';
    car += '<circle cx="410" cy="' + (226 + lift) + '" r="7" fill="#FFF6A5"' + stroke + '/>';
    if (style !== 'hover') {
      var rim = wheels ? wheels.item.color : '#C9CED6';
      [130, 350].forEach(function (x) {
        var r = style === 'truck' ? 50 : 34;
        car += '<g' + (wheels ? popCls(wheels, ctx) : '') + '><circle cx="' + x + '" cy="' + (style === 'truck' ? 270 : wy) + '" r="' + r + '" fill="#1B1B1B"' + stroke + '/><circle cx="' + x + '" cy="' + (style === 'truck' ? 270 : wy) + '" r="' + r * 0.5 + '" fill="' + rim + '"' + stroke + '/>' +
          '<path d="M' + (x - r * 0.4) + ' ' + (style === 'truck' ? 270 : wy) + ' H' + (x + r * 0.4) + ' M' + x + ' ' + ((style === 'truck' ? 270 : wy) - r * 0.4) + ' V' + ((style === 'truck' ? 270 : wy) + r * 0.4) + '" stroke="' + INK + '" stroke-width="2.5"/></g>';
      });
    } else {
      car += '<path d="M130 ' + (252 + lift) + ' L120 ' + (282 + lift) + ' M350 ' + (252 + lift) + ' L360 ' + (282 + lift) + '" stroke="#7FDBFF" stroke-width="10" stroke-linecap="round" stroke-opacity=".8"/>';
      if (wheels) car += '<g' + popCls(wheels, ctx) + '><ellipse cx="240" cy="' + (256 + lift) + '" rx="140" ry="8" fill="' + wheels.item.color + '"' + stroke + '/></g>';
    }
    car += '</g>';
    out += car;
    var badges = ctx.wins.filter(function (w) { return w.part === 'badge'; });
    badges.forEach(function (w, i) {
      var x = 64 + i * 72, y = 50 + (i % 2) * 34;
      out += '<g' + popCls(w, ctx) + '>' + sticker(x, y, 26, w.item.emoji) + label(x, y + 40, w.item.name, { size: 9, max: 14, lines: 2 }) + '</g>';
    });
    var name = (ctx.playerName ? ctx.playerName + '’s ' : '') + (bodyW ? bodyW.item.name : 'Dream Car');
    out += caption(240, 318, Math.min(330, 50 + name.length * 9), name, { size: 15, fill: bodyW ? '#FFE94D' : '#FFFFFF' });
    var placed = { body: 1, paint: 1, wheels: 1, glow: 1, decal: 1, badge: 1 };
    out += extrasRow(ctx.wins.filter(function (w) { return !placed[w.part]; }), ctx, W, H);
    return { w: W, h: H, body: out };
  }

  /* ---------- 7. spread: day of food, fast-food tray, dessert table, feast ---------- */

  function spread(ctx) {
    var W = 480, H = 360, skin = ctx.mode.skin, out = '', u = ctx.uid;
    var bg = { day: '#E4002B', tray: '#C1121F', dessert: '#FF8FC7', feast: '#8C5E2A' }[skin] || '#E4002B';
    var meals = ctx.wins.filter(function (w) { return w.part === 'meal'; });
    out += '<defs><pattern id="ck' + u + '" width="40" height="40" patternUnits="userSpaceOnUse"><rect width="40" height="40" fill="' + bg + '"/><rect width="20" height="20" fill="#FFFFFF" fill-opacity="' + (skin === 'feast' ? 0.06 : 0.85) + '"/><rect x="20" y="20" width="20" height="20" fill="#FFFFFF" fill-opacity="' + (skin === 'feast' ? 0.06 : 0.85) + '"/></pattern></defs>';
    out += '<rect width="' + W + '" height="' + H + '" fill="url(#ck' + u + ')"/>';
    if (skin === 'tray') out += '<rect x="24" y="44" width="432" height="300" rx="22" fill="#E63946" stroke="' + INK + '" stroke-width="3"/><rect x="40" y="58" width="400" height="272" rx="14" fill="#FFF3E0" stroke="' + INK + '" stroke-width="2"/>';
    if (skin === 'feast') out += '<rect x="14" y="40" width="452" height="310" rx="16" fill="#A0703C" stroke="' + INK + '" stroke-width="3"/>' + emo(30, 54, 26, '🕯️') + emo(450, 54, 26, '🕯️');
    var total = countPart(ctx.rounds, 'meal');
    var cols = 5, rows = Math.max(2, Math.ceil(total / cols));
    var cw = 88, ch = 140, x0 = 240 - (cols * cw) / 2 + cw / 2, y0 = 112;
    for (var i = 0; i < total; i++) {
      var x = x0 + (i % cols) * cw, y = y0 + Math.floor(i / cols) * ch;
      var w = null;
      meals.forEach(function (m) { if (slotIndex(ctx.rounds, 'meal', m.round) === i) w = m; });
      var r = ctx.rounds.filter(function (rr) { return rr.part === 'meal'; })[i];
      var tag = r ? r.label : '';
      if (w) {
        out += '<g' + popCls(w, ctx) + '>';
        if (skin === 'dessert') out += '<path d="M' + (x - 34) + ' ' + (y + 30) + ' H' + (x + 34) + ' L' + (x + 8) + ' ' + (y + 40) + ' V' + (y + 52) + ' H' + (x - 8) + ' V' + (y + 40) + ' Z" fill="#FFF" stroke="' + INK + '" stroke-width="2.5"/>';
        else out += '<circle cx="' + x + '" cy="' + y + '" r="38" fill="#FFFFFF" stroke="' + INK + '" stroke-width="2.5"/><circle cx="' + x + '" cy="' + y + '" r="28" fill="none" stroke="' + INK + '" stroke-opacity=".2" stroke-width="2"/>';
        out += emo(x, y, 44, w.item.emoji);
        out += '<rect x="' + (x - 42) + '" y="' + (y + 44) + '" width="84" height="30" fill="#FFE94D" stroke="' + INK + '" stroke-width="2"/>';
        out += label(x, y + 56, w.item.name, { size: 9.5, max: 15, lines: 2 });
        out += '</g>';
      } else {
        out += '<circle cx="' + x + '" cy="' + y + '" r="34" fill="#FFFFFF" fill-opacity=".55" stroke="' + INK + '" stroke-opacity=".4" stroke-width="2" stroke-dasharray="6 5"/>';
      }
      out += label(x, y - 50, tag.length > 13 ? tag.split(' ').slice(-1)[0].toUpperCase() : tag.toUpperCase(), { size: 9, max: 14, lines: 1, fill: skin === 'feast' || skin === 'tray' ? (skin === 'tray' ? INK : '#FFFFFF') : INK, letter: 1, display: true });
    }
    var titleText = ctx.playerName ? ctx.playerName + '’s ' + ctx.mode.name.replace(/^Dream /, '') : ctx.mode.name;
    out += caption(240, 8, Math.min(340, 60 + titleText.length * 9), titleText, { size: 16, fill: '#FFFFFF' });
    var placed = { meal: 1 };
    out += extrasRow(ctx.wins.filter(function (w) { return !placed[w.part]; }), ctx, W, H);
    return { w: W, h: H, body: out };
  }

  /* ---------- 8. pizza ---------- */

  function pizza(ctx) {
    var W = 480, H = 360, by = collect(ctx.wins), out = '', u = ctx.uid;
    function one(p) { return by[p] && by[p][by[p].length - 1]; }
    var crust = one('crust'), sauce = one('sauce'), cheese = one('cheese');
    var tops = by.topping || [], sides = by.side || [];
    var rand = T.rng(T.hash(ctx.seed || 'pizza'));
    out += '<defs>' + dots('pz' + u, '#000000', 12, 0.08) + '</defs>';
    out += '<rect width="' + W + '" height="' + H + '" fill="#2A9D8F"/><rect width="' + W + '" height="' + H + '" fill="url(#pz' + u + ')"/>';
    out += '<circle cx="240" cy="186" r="160" fill="#B07D48" stroke="' + INK + '" stroke-width="3"/>';
    for (var g = 0; g < 8; g++) out += '<path d="M' + (100 + g * 36) + ' ' + (60 + (g % 2) * 6) + ' V320" stroke="' + INK + '" stroke-opacity=".12" stroke-width="2"/>';
    out += '<g' + (crust ? popCls(crust, ctx) : '') + '><circle cx="240" cy="186" r="136" fill="' + (crust ? crust.item.color : '#F3E2C3') + '" stroke="' + INK + '" stroke-width="3"' + (crust ? '' : ' stroke-dasharray="8 6"') + '/></g>';
    if (sauce) out += '<g' + popCls(sauce, ctx) + '><circle cx="240" cy="186" r="116" fill="' + sauce.item.color + '" stroke="' + INK + '" stroke-width="2"/></g>';
    if (cheese) {
      var cg = '<g' + popCls(cheese, ctx) + '>';
      for (var c = 0; c < 26; c++) {
        var a = rand() * Math.PI * 2, d = Math.sqrt(rand()) * 98;
        cg += '<circle cx="' + (240 + Math.cos(a) * d) + '" cy="' + (186 + Math.sin(a) * d) + '" r="' + (14 + rand() * 12) + '" fill="' + cheese.item.color + '" fill-opacity=".92"/>';
      }
      out += cg + '</g>';
    }
    tops.forEach(function (t, ti) {
      var tg = '<g' + popCls(t, ctx) + '>';
      for (var k = 0; k < 6; k++) {
        var a = (k / 6) * Math.PI * 2 + ti * 0.5 + rand() * 0.4, d = 30 + ((k + ti) % 3) * 30 + rand() * 10;
        tg += emo(240 + Math.cos(a) * d, 186 + Math.sin(a) * d, 24, t.item.emoji);
      }
      out += tg + '</g>';
    });
    for (var s = 0; s < 6; s++) out += '<path d="M240 186 L' + (240 + Math.cos(s * Math.PI / 3) * 136) + ' ' + (186 + Math.sin(s * Math.PI / 3) * 136) + '" stroke="' + INK + '" stroke-opacity=".25" stroke-width="2"/>';
    var sideSpots = [[56, 70], [424, 70], [56, 300], [424, 300]];
    sides.forEach(function (w, i) {
      var p = sideSpots[i % 4];
      out += '<g' + popCls(w, ctx) + '>' + sticker(p[0], p[1], 32, w.item.emoji) + label(p[0], p[1] + 48, w.item.name, { size: 10, max: 14, lines: 2, fill: '#FFFFFF' }) + '</g>';
    });
    var placed = { crust: 1, sauce: 1, cheese: 1, topping: 1, side: 1 };
    out += extrasRow(ctx.wins.filter(function (w) { return !placed[w.part]; }), ctx, W, H);
    if (tops.length) out += '<g>' + caption(240, 330, Math.min(380, 40 + tops.map(function (t) { return t.item.name; }).join(', ').length * 6.5), tops.map(function (t) { return t.item.name; }).join(', '), { size: 11 }) + '</g>';
    return { w: W, h: H, body: out };
  }

  /* ---------- 9. sundae: ice cream ---------- */

  function sundae(ctx) {
    var W = 480, H = 360, by = collect(ctx.wins), out = '', u = ctx.uid;
    function one(p) { return by[p] && by[p][by[p].length - 1]; }
    var base = one('base'), sauce = one('sauce'), cream = one('cream'), crown = one('crown');
    var scoops = by.scoop || [], tops = by.topping || [];
    var shape = base ? base.item.shape : 'cone';
    var rand = T.rng(T.hash(ctx.seed || 'sundae'));
    out += '<defs>' + dots('ic' + u, '#FFFFFF', 14, 0.5) + '</defs>';
    out += '<rect width="' + W + '" height="' + H + '" fill="#7FD1F7"/><rect width="' + W + '" height="' + H + '" fill="url(#ic' + u + ')"/>';
    out += '<rect y="300" width="' + W + '" height="60" fill="#FF8FC7" stroke="' + INK + '" stroke-width="3"/>';
    var stroke = ' stroke="' + INK + '" stroke-width="3" stroke-linejoin="round"';
    var baseTop;
    var bg = '<g' + (base ? popCls(base, ctx) : '') + '>';
    if (shape === 'bowl' || shape === 'boat') {
      baseTop = 236;
      if (shape === 'boat') bg += '<path d="M120 236 H360 Q350 290 300 296 H180 Q130 290 120 236 Z" fill="#E0F4FF"' + stroke + '/>' + emo(170, 230, 50, '🍌') + emo(310, 230, 50, '🍌');
      else bg += '<path d="M150 236 H330 Q326 296 240 300 Q154 296 150 236 Z" fill="#E0F4FF"' + stroke + '/><rect x="222" y="296" width="36" height="8" fill="#E0F4FF"' + stroke + '/>';
    } else {
      baseTop = 214;
      var cc = shape === 'cone-choc' ? '#6B3E26' : '#E3A857';
      bg += '<path d="M190 214 L240 312 L290 214 Z" fill="#E3A857"' + stroke + (base ? '' : ' stroke-dasharray="8 6"') + '/>';
      for (var l = 0; l < 5; l++) bg += '<path d="M' + (198 + l * 20) + ' 214 L' + (226 + l * 8) + ' 290" stroke="' + INK + '" stroke-opacity=".3" stroke-width="2"/>';
      if (shape === 'cone-choc') bg += '<path d="M188 212 H292 L284 232 Q240 240 196 232 Z" fill="' + cc + '"' + stroke + '/>';
    }
    out += bg + '</g>';
    var y = baseTop;
    scoops.forEach(function (sc, i) {
      var r = 46 - i * 3, x = 240 + (i % 2 ? 6 : -6);
      y -= i === 0 ? 20 : r * 1.35;
      out += '<g' + popCls(sc, ctx) + '><circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="' + sc.item.color + '"' + stroke + '/>' +
        '<path d="M' + (x - r) + ' ' + (y + 10) + ' q10 18 20 0 q10 18 20 0 q10 18 20 0 q10 18 20 0 q' + (r * 2 - 80) + ' 10 ' + (r * 2 - 80) + ' 0" fill="' + sc.item.color + '"' + stroke + '/>' +
        '<circle cx="' + (x - r * 0.4) + '" cy="' + (y - r * 0.4) + '" r="' + r * 0.18 + '" fill="#FFFFFF" fill-opacity=".55"/></g>';
    });
    var topY = scoops.length ? y - 40 : baseTop - 20;
    if (sauce && scoops.length) out += '<g' + popCls(sauce, ctx) + '><path d="M' + 196 + ' ' + (y - 16) + ' Q220 ' + (y - 50) + ' 240 ' + (y - 38) + ' Q262 ' + (y - 52) + ' 284 ' + (y - 16) + ' L280 ' + (y + 20) + ' Q274 ' + (y + 8) + ' 270 ' + (y - 4) + ' L262 ' + (y + 30) + ' Q254 ' + (y + 6) + ' 248 ' + (y - 8) + ' L232 ' + (y + 24) + ' Q224 ' + (y + 2) + ' 216 ' + (y - 6) + ' L204 ' + (y + 14) + ' Z" fill="' + sauce.item.color + '"' + stroke + '/></g>';
    else if (sauce) out += '<g' + popCls(sauce, ctx) + '>' + emo(240, baseTop - 10, 36, sauce.item.emoji) + '</g>';
    if (cream) {
      out += '<g' + popCls(cream, ctx) + '>';
      [0, 1, 2].forEach(function (k) { out += '<ellipse cx="240" cy="' + (topY + 10 - k * 16) + '" rx="' + (38 - k * 11) + '" ry="12" fill="' + (/choc/i.test(cream.item.name) ? '#8B5A3C' : '#FFFFFF') + '"' + stroke + '/>'; });
      out += '</g>';
      topY -= 40;
    }
    tops.forEach(function (t) {
      var tg = '<g' + popCls(t, ctx) + '>';
      for (var k = 0; k < 5; k++) tg += emo(200 + rand() * 80, (scoops.length ? y : baseTop - 10) - 30 + rand() * 50, 18, t.item.emoji);
      out += tg + '</g>';
    });
    if (crown) out += '<g' + popCls(crown, ctx) + '>' + emo(240, topY - 6, 46, crown.item.emoji) + '</g>';
    // ingredient ticket on the right
    var lines = ctx.wins.map(function (w) { return w.item.name; });
    if (lines.length) {
      out += '<rect x="356" y="24" width="112" height="' + (22 + lines.length * 14) + '" fill="#FFFFFF" stroke="' + INK + '" stroke-width="2.5" transform="rotate(3 412 40)"/>';
      out += '<g transform="rotate(3 412 40)">' + label(412, 40, 'ORDER', { size: 12, display: true, letter: 2 });
      lines.forEach(function (l, i) { out += '<text x="364" y="' + (56 + i * 14) + '" font-size="9.5" font-family="' + BODY_FONT + '" font-weight="700" fill="' + INK + '">' + esc((l.length > 19 ? l.slice(0, 18) + '…' : l)) + '</text>'; });
      out += '</g>';
    }
    var placed = { base: 1, scoop: 1, sauce: 1, topping: 1, cream: 1, crown: 1 };
    out += extrasRow(ctx.wins.filter(function (w) { return !placed[w.part]; }), ctx, W, H);
    return { w: W, h: H, body: out };
  }

  /* ---------- 10. team: sports, zombie, adventure, superpower ---------- */

  function team(ctx) {
    var W = 480, H = 360, skin = ctx.mode.skin, by = collect(ctx.wins), out = '', u = ctx.uid;
    function one(p) { return by[p] && by[p][by[p].length - 1]; }
    var title = one('title'), banner = one('banner'), home = one('home');
    var members = by.member || [], gear = by.gear || [];
    var bg = { sports: '#0B6E4F', zombie: '#4F772D', adventure: '#BC6C25', powers: '#1D3557' }[skin] || '#1D3557';
    out += '<defs>' + dots('tm' + u, '#FFFFFF', 12, 0.14) + '</defs>';
    out += '<rect width="' + W + '" height="' + H + '" fill="' + bg + '"/><rect width="' + W + '" height="' + H + '" fill="url(#tm' + u + ')"/>';
    if (skin === 'sports') out += '<circle cx="240" cy="200" r="60" fill="none" stroke="#FFFFFF" stroke-opacity=".3" stroke-width="4"/><path d="M240 40 V360" stroke="#FFFFFF" stroke-opacity=".3" stroke-width="4"/>';
    if (home) out += '<g' + popCls(home, ctx) + '>' + emo(410, 300, 110, home.item.emoji, 'opacity=".55"') + '</g>';
    var tText = title ? title.item.name : banner ? banner.item.name : (ctx.playerName ? ctx.playerName + '’s Team' : 'The Team');
    out += '<g' + (title ? popCls(title, ctx) : banner ? popCls(banner, ctx) : '') + '>' + caption(240, 8, Math.min(340, 70 + tText.length * 9), (title || banner ? (title || banner).item.emoji + ' ' : '') + tText, { size: 18, fill: title || banner ? '#FFE94D' : '#FFFFFF' }) + '</g>';
    if (title && banner) out += label(240, 54, banner.item.name.toUpperCase(), { size: 11, fill: '#FFFFFF', letter: 2, max: 40, lines: 1 });
    var total = countPart(ctx.rounds, 'member');
    var perRow = Math.min(5, Math.max(4, Math.ceil(total / 2)));
    var cw = 80, chh = 104, gap = 10;
    var memberRounds = ctx.rounds.filter(function (r) { return r.part === 'member'; });
    for (var i = 0; i < total; i++) {
      var row = Math.floor(i / perRow), inRow = Math.min(perRow, total - row * perRow);
      var x = 240 - (inRow * cw + (inRow - 1) * gap) / 2 + (i % perRow) * (cw + gap), y = 68 + row * (chh + 12);
      var w = null;
      members.forEach(function (m) { if (slotIndex(ctx.rounds, 'member', m.round) === i) w = m; });
      var role = memberRounds[i] ? memberRounds[i].label : '';
      if (w) {
        out += '<g' + popCls(w, ctx) + '><rect x="' + x + '" y="' + y + '" width="' + cw + '" height="' + chh + '" rx="6" fill="#FFFFFF" stroke="' + INK + '" stroke-width="2.5"/>' +
          '<rect x="' + x + '" y="' + y + '" width="' + cw + '" height="18" rx="6" fill="' + (ctx.color || '#E4002B') + '" stroke="' + INK + '" stroke-width="2.5"/>' +
          label(x + cw / 2, y + 13, role.toUpperCase(), { size: 8.5, fill: '#FFFFFF', max: 18, lines: 1, letter: 0.5 }) +
          emo(x + cw / 2, y + 50, 36, w.item.emoji) +
          label(x + cw / 2, y + 82, w.item.name, { size: 9, max: 15, lines: 2 }) + '</g>';
      } else {
        out += '<rect x="' + x + '" y="' + y + '" width="' + cw + '" height="' + chh + '" rx="6" fill="#FFFFFF" fill-opacity=".12" stroke="#FFFFFF" stroke-opacity=".5" stroke-width="2" stroke-dasharray="6 5"/>' +
          label(x + cw / 2, y + chh / 2 + 4, role.toUpperCase(), { size: 9, fill: '#FFFFFF', max: 12, lines: 2 });
      }
    }
    gear.forEach(function (w, i) {
      var x = 50 + i * 64;
      out += '<g' + popCls(w, ctx) + '>' + sticker(x, 316, 24, w.item.emoji, { fill: '#FFE94D' }) + '</g>';
    });
    var placed = { title: 1, banner: 1, home: 1, member: 1, gear: 1 };
    out += extrasRow(ctx.wins.filter(function (w) { return !placed[w.part]; }), ctx, W, H);
    return { w: W, h: H, body: out };
  }

  /* ---------- 11. collage: custom modes ---------- */

  function collage(ctx) {
    var W = 480, H = 360, out = '', u = ctx.uid;
    var total = ctx.rounds.length;
    out += '<defs>' + dots('cl' + u, '#FFFFFF', 14, 0.4) + '</defs>';
    out += '<rect width="' + W + '" height="' + H + '" fill="' + (ctx.mode.color || '#00A6E8') + '"/><rect width="' + W + '" height="' + H + '" fill="url(#cl' + u + ')"/>';
    var cols = 5, cw = 88, ch = 120, x0 = 240 - (cols * cw) / 2 + cw / 2;
    for (var i = 0; i < total; i++) {
      var x = x0 + (i % cols) * cw, y = 110 + Math.floor(i / cols) * ch;
      var w = ctx.wins.filter(function (ww) { return ww.round === i; })[0];
      if (w) out += '<g' + popCls(w, ctx) + '>' + sticker(x, y, 34, w.item.emoji) + '<rect x="' + (x - 42) + '" y="' + (y + 40) + '" width="84" height="28" fill="#FFE94D" stroke="' + INK + '" stroke-width="2"/>' + label(x, y + 51, w.item.name, { size: 9.5, max: 15, lines: 2 }) + '</g>';
      else out += emptySlot(x, y, 30);
    }
    var t = ctx.playerName ? ctx.playerName + '’s ' + ctx.mode.name.replace(/^Dream /, '') : ctx.mode.name;
    out += caption(240, 10, Math.min(340, 60 + t.length * 9), t, { size: 17, fill: '#FFFFFF' });
    return { w: W, h: H, body: out };
  }

  var RENDERERS = { building: building, figure: figure, poster: poster, map: map, stage: stage, vehicle: vehicle, spread: spread, pizza: pizza, sundae: sundae, team: team, collage: collage };
  T.KINDS = Object.keys(RENDERERS);

  // Render a player's creation as a standalone SVG string.
  // opts: { wins, rounds, playerName, color, newest (win object to animate), seed }
  T.renderCreation = function (mode, opts) {
    var fn = RENDERERS[mode.kind] || collage;
    var ctx = {
      mode: mode, wins: opts.wins || [], rounds: opts.rounds || mode.rounds, playerName: opts.playerName || '',
      color: opts.color, newest: opts.newest || null, seed: opts.seed || mode.id, uid: 'u' + T.uid()
    };
    var r = fn(ctx);
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + r.w + ' ' + r.h + '" width="' + r.w + '" height="' + r.h + '" role="img" aria-label="' + esc((opts.playerName ? opts.playerName + '’s ' : '') + mode.name) + '" style="font-family:' + BODY_FONT.replace(/"/g, "'") + '">' + r.body + '</svg>';
  };

  T.creationAspect = function (mode) { return mode.kind === 'poster' ? 360 / 480 : 480 / 360; };

  // Convert an SVG string to a PNG blob (used for saving final images).
  T.svgToPng = function (svg, scale, title) {
    return new Promise(function (resolve, reject) {
      var m = /viewBox="0 0 (\d+) (\d+)"/.exec(svg);
      var w = +m[1], h = +m[2];
      var img = new Image();
      img.onload = function () {
        var pad = 24, head = title ? 56 : 0;
        var c = document.createElement('canvas');
        c.width = (w + pad * 2) * scale; c.height = (h + pad * 2 + head) * scale;
        var x = c.getContext('2d');
        x.scale(scale, scale);
        x.fillStyle = '#FFE94D'; x.fillRect(0, 0, w + pad * 2, h + pad * 2 + head);
        x.fillStyle = INK; x.fillRect(pad - 4, pad + head - 4, w + 8, h + 8);
        x.drawImage(img, pad, pad + head, w, h);
        if (title) {
          x.fillStyle = INK; x.font = '34px Bangers, "Comic Neue", sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle';
          x.fillText(title, (w + pad * 2) / 2, pad + 22);
        }
        c.toBlob(function (b) { b ? resolve(b) : reject(new Error('Could not create the image.')); }, 'image/png');
      };
      img.onerror = function () { reject(new Error('Could not draw the creation.')); };
      img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
    });
  };
})(window.TDA);
