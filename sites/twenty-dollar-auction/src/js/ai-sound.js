/* AI paintings (Pollinations.ai, free, no account) and synthesized sound effects. */
(function (T) {
  'use strict';

  /* ---------- AI painting ----------
     Integration point: T.AI.provider builds an image URL from a text prompt.
     To switch services, replace buildUrl with one that returns a URL (or a data: URL from your own API). */
  var AI = T.AI = {
    provider: 'Pollinations.ai',
    providerUrl: 'https://pollinations.ai',
    timeoutMs: 90000,
    style: 'vibrant comic book illustration, bold black ink outlines, halftone dots, bright flat colors, family friendly, no text',
    buildUrl: function (prompt, seed) {
      return 'https://image.pollinations.ai/prompt/' + encodeURIComponent(prompt) +
        '?width=768&height=576&nologo=true&seed=' + seed + '&model=flux';
    }
  };

  // The prompt always lists every feature the player owns, so a new painting never forgets earlier wins.
  AI.prompt = function (mode, player) {
    var feats = player.wins.map(function (w) { return w.item.name + ' (' + w.label.toLowerCase() + ')'; });
    var subject = mode.ai;
    return subject + ', featuring: ' + (feats.length ? feats.join(', ') : 'nothing yet') + '. ' + AI.style;
  };

  AI.signature = function (player) { return player.wins.map(function (w) { return w.round + ':' + w.item.name; }).join('|'); };

  // Load the painting in the browser. Resolves with the URL only once the image really loaded.
  AI.paint = function (mode, player, gameId) {
    var seed = T.hash(gameId + player.id) % 1000000;
    var url = AI.buildUrl(AI.prompt(mode, player), seed);
    return new Promise(function (resolve, reject) {
      var img = new Image();
      var done = false;
      var timer = setTimeout(function () { if (!done) { done = true; img.src = ''; reject(new Error('The AI painter took too long.')); } }, AI.timeoutMs);
      img.onload = function () {
        if (done) return; done = true; clearTimeout(timer);
        if (img.naturalWidth < 16) reject(new Error('The AI painter sent back an empty image.')); else resolve(url);
      };
      img.onerror = function () {
        if (done) return; done = true; clearTimeout(timer);
        reject(new Error('Could not reach ' + AI.provider + '. Your network or this page may block it.'));
      };
      img.referrerPolicy = 'no-referrer';
      img.src = url;
    });
  };

  /* ---------- Sound ---------- */
  var ctx = null;
  var S = T.Sound = { on: true };
  function ac() {
    if (!ctx) { try { ctx = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return null; } }
    if (ctx.state === 'suspended') ctx.resume();
    return ctx;
  }
  function tone(freq, start, dur, type, vol, slideTo) {
    var c = ac(); if (!c) return;
    var o = c.createOscillator(), g = c.createGain();
    o.type = type || 'square';
    o.frequency.setValueAtTime(freq, c.currentTime + start);
    if (slideTo) o.frequency.exponentialRampToValueAtTime(slideTo, c.currentTime + start + dur);
    g.gain.setValueAtTime(0.0001, c.currentTime + start);
    g.gain.exponentialRampToValueAtTime(vol || 0.12, c.currentTime + start + 0.015);
    g.gain.exponentialRampToValueAtTime(0.0001, c.currentTime + start + dur);
    o.connect(g); g.connect(c.destination);
    o.start(c.currentTime + start); o.stop(c.currentTime + start + dur + 0.05);
  }
  function noise(start, dur, vol, freq) {
    var c = ac(); if (!c) return;
    var len = Math.floor(c.sampleRate * dur), buf = c.createBuffer(1, len, c.sampleRate), d = buf.getChannelData(0);
    for (var i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, 3);
    var src = c.createBufferSource(), f = c.createBiquadFilter(), g = c.createGain();
    f.type = 'lowpass'; f.frequency.value = freq || 900;
    g.gain.value = vol || 0.5;
    src.buffer = buf; src.connect(f); f.connect(g); g.connect(c.destination);
    src.start(c.currentTime + start);
  }
  S.play = function (name, n) {
    if (!S.on) return;
    switch (name) {
      case 'bid': tone(440 + Math.min(n || 1, 20) * 28, 0, 0.12, 'square', 0.08); tone(660 + Math.min(n || 1, 20) * 28, 0.07, 0.12, 'square', 0.07); break;
      case 'pass': tone(220, 0, 0.18, 'triangle', 0.12, 140); break;
      case 'reveal': tone(300, 0, 0.35, 'sawtooth', 0.05, 900); noise(0, 0.3, 0.12, 3000); break;
      case 'gavel': noise(0, 0.12, 0.9, 700); tone(130, 0, 0.12, 'sine', 0.35, 60); noise(0.18, 0.12, 0.9, 700); tone(130, 0.18, 0.12, 'sine', 0.35, 60); break;
      case 'sold': [523, 659, 784, 1047].forEach(function (f, i) { tone(f, 0.25 + i * 0.09, 0.22, 'square', 0.08); }); tone(1047, 0.62, 0.5, 'triangle', 0.1); break;
      case 'sad': tone(392, 0, 0.3, 'sawtooth', 0.06, 370); tone(370, 0.3, 0.3, 'sawtooth', 0.06, 349); tone(349, 0.6, 0.7, 'sawtooth', 0.06, 262); break;
      case 'tick': tone(1200, 0, 0.04, 'square', 0.04); break;
      case 'error': tone(160, 0, 0.16, 'square', 0.08); break;
      case 'fanfare': [392, 523, 659, 784, 659, 784, 1047].forEach(function (f, i) { tone(f, i * 0.12, 0.2, 'square', 0.07); }); break;
    }
  };
})(window.TDA);
