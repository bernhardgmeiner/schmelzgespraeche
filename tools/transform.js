// Plakatwand (Startseite), Fotogalerien (Gesprächsseiten) und CSS-Ergänzung.
// Wird lokal (node) und im Wix-Sandbox gleich ausgeführt: new Function(src)() liefert T.
var M = "https://static.wixstatic.com/media/";
function esc(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}
function poster(e, w) {
  return M + e.poster + "/v1/fill/w_" + w + ",h_" + w + ",q_85,enc_auto/p.jpg";
}
function photoUrls(p) {
  var w = p[1], h = p[2];
  var th = Math.min(440, h);
  var tw = Math.round(th * w / h);
  if (p[0].charAt(0) === "/") // Foto liegt im Repository (docs/fotos/...), Vorschau daneben als -k.jpg
    return { thumb: p[0].replace(/\.jpg$/, "-k.jpg"), big: p[0], tw: tw, th: th, r: (w / h).toFixed(3) };
  var id = "ae5aaf_" + p[0].replace(/\.(\w+)$/, "~mv2.$1");
  return {
    thumb: M + id + "/v1/fill/w_" + tw + ",h_" + th + ",q_80,enc_auto/f.jpg",
    big: M + id + "/v1/fit/w_1800,h_1800,q_85,enc_auto/f.jpg",
    tw: tw,
    th: th,
    r: (w / h).toFixed(3)
  };
}

var CSS = "\n/* Plakatwand auf der Startseite: alle Plakate, 4 Spalten, auf dem Handy 2 */\n" +
  "[hidden]{display:none!important}\n" +
  ".intro{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:20px var(--gut);align-items:end;padding:clamp(36px,6vw,80px) 0 clamp(28px,4vw,48px)}\n" +
  ".intro h1{grid-column:1/8;font-size:clamp(52px,8vw,124px);line-height:.92;letter-spacing:-.035em;font-weight:800;margin:0;text-wrap:balance}\n" +
  ".intro p{grid-column:8/13;font-size:clamp(17px,1.45vw,19px);line-height:1.5;margin:0;text-wrap:pretty}\n" +
  ".nextbar{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 18px;border-top:var(--line);padding:14px 0 16px;text-decoration:none;font-size:17px}\n" +
  ".nextbar .label{color:var(--red)}\n" +
  ".nextbar strong{font-weight:800}\n" +
  ".nextbar .go{margin-left:auto;font-weight:700}\n" +
  ".wall{list-style:none;margin:0 0 clamp(64px,9vw,112px);padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}\n" +
  ".wall a{display:block;position:relative}\n" +
  ".wall img{width:100%;aspect-ratio:1;object-fit:cover;background:var(--tile);transition:opacity .15s}\n" +
  ".wall a:hover img,.wall a:focus-visible img{opacity:.82}\n" +
  ".wall .badge{position:absolute;left:10px;top:10px;margin:0}\n" +
  "/* Fotos auf den Gesprächsseiten: Reihen im Blocksatz, Seitenverhältnis bleibt */\n" +
  ".jump{margin:22px 0 0;font-weight:700}\n" +
  ".jump a{text-decoration:none;border-bottom:2px solid currentColor;padding-bottom:2px}\n" +
  ".gallery{display:flex;flex-wrap:wrap;gap:8px}\n" +
  ".gallery::after{content:\"\";flex-grow:10000}\n" +
  ".gallery a{flex:var(--r) 1 calc(var(--r)*190px);display:block;background:var(--tile)}\n" +
  ".gallery img{width:100%;height:auto;transition:opacity .15s}\n" +
  ".gallery a:hover img,.gallery a:focus-visible img{opacity:.82}\n" +
  ".photos .note{font-size:13px;line-height:1.4;color:var(--muted);margin:14px 0 0}\n" +
  ".lb{border:0;padding:0;margin:0;width:100vw;height:100vh;height:100dvh;max-width:none;max-height:none;background:#1a1530;color:#f7f4fc;overflow:hidden}\n" +
  ".lb::backdrop{background:#1a1530}\n" +
  ".lb figure{position:absolute;inset:60px 72px 52px;margin:0;display:flex;flex-direction:column;align-items:center;justify-content:center;pointer-events:none}\n" +
  ".lb img{max-width:100%;max-height:calc(100% - 34px);width:auto;height:auto;object-fit:contain;pointer-events:auto;cursor:pointer}\n" +
  ".lb figcaption{font-size:14px;color:#cfc8df;margin-top:12px;font-variant-numeric:tabular-nums}\n" +
  ".lb button{position:absolute;width:56px;height:56px;border:0;background:none;color:#f7f4fc;font:inherit;font-size:30px;line-height:1;cursor:pointer}\n" +
  ".lb button:hover{opacity:.65}\n" +
  ".lb button:focus-visible{outline:2px solid #f7f4fc;outline-offset:-6px}\n" +
  ".lb .x{top:6px;right:8px}\n" +
  ".lb .p{left:8px;top:50%;transform:translateY(-50%)}\n" +
  ".lb .n{right:8px;top:50%;transform:translateY(-50%)}\n" +
  "@media (max-width:820px){.intro h1,.intro p{grid-column:1/-1}}\n" +
  "@media (max-width:600px){.wall{grid-template-columns:repeat(2,minmax(0,1fr));gap:6px}.wall .badge{left:6px;top:6px;font-size:11px;padding:4px 7px}.nextbar .go{margin-left:0}.gallery{gap:6px}.gallery a{flex-basis:calc(var(--r)*110px)}.lb figure{inset:56px 8px 64px}.lb .p,.lb .n{top:auto;bottom:4px;transform:none}}\n";

var LIGHTBOX = '<dialog class="lb" aria-label="Fotos">\n' +
  '<figure><img src="data:," alt=""><figcaption></figcaption></figure>\n' +
  '<button class="x" type="button" aria-label="Schließen">✕</button>\n' +
  '<button class="p" type="button" aria-label="Vorheriges Foto">←</button>\n' +
  '<button class="n" type="button" aria-label="Nächstes Foto">→</button>\n' +
  '</dialog>\n' +
  '<script>(function(){var d=document.querySelector(".lb");if(!d||!d.showModal)return;var a=[].slice.call(document.querySelectorAll(".gallery a")),i=0,m=d.querySelector("img"),c=d.querySelector("figcaption"),sx=null;' +
  'function s(k){i=(k+a.length)%a.length;var x=a[i];m.src=x.href;m.alt=x.querySelector("img").alt;c.textContent=(i+1)+" / "+a.length+(x.getAttribute("data-c")?" · Foto: "+x.getAttribute("data-c"):"")}' +
  'a.forEach(function(x,k){x.addEventListener("click",function(e){if(e.metaKey||e.ctrlKey)return;e.preventDefault();s(k);d.showModal()})});' +
  'd.querySelector(".x").onclick=function(){d.close()};d.querySelector(".p").onclick=function(){s(i-1)};d.querySelector(".n").onclick=function(){s(i+1)};m.onclick=function(){s(i+1)};' +
  'd.addEventListener("click",function(e){if(e.target===d)d.close()});' +
  'd.addEventListener("keydown",function(e){if(e.key==="ArrowLeft")s(i-1);if(e.key==="ArrowRight")s(i+1)});' +
  'd.addEventListener("touchstart",function(e){sx=e.touches[0].clientX},{passive:true});' +
  'd.addEventListener("touchend",function(e){if(sx===null)return;var dx=e.changedTouches[0].clientX-sx;sx=null;if(Math.abs(dx)>50)s(dx<0?i+1:i-1)});' +
  'd.addEventListener("close",function(){m.src="data:,"})})();</script>\n';

function gallery(e, credit) {
  var n = e.ph.length;
  var items = e.ph.map(function (p, k) {
    var u = photoUrls(p);
    var c = p[3] ? ' data-c="BMK/Cajetan Perwein"' : (credit ? ' data-c="' + esc(credit) + '"' : "");
    return '<a href="' + u.big + '" style="--r:' + u.r + '"' + c + '><img src="' + u.thumb + '" width="' + u.tw + '" height="' + u.th +
      '" alt="' + esc(e.name) + ', Foto ' + (k + 1) + ' von ' + n + '" loading="lazy" decoding="async"></a>';
  });
  var note = "";
  if (e.slug === "leonore-gewessler") note = '\n<p class="note">Ein Teil der Fotos: BMK/Cajetan Perwein.</p>';
  else if (credit) note = '\n<p class="note">Fotos: ' + esc(credit) + '.</p>';
  return '<section class="row photos" id="fotos">\n<h2 class="label">Fotos</h2>\n<div class="body">\n<div class="gallery">\n' +
    items.join("\n") + '\n</div>' + note + '\n</div>\n</section>\n';
}

function transformEvent(html, e, credits) {
  if (!e.ph.length || html.indexOf('id="fotos"') > -1) return html;
  var n = e.ph.length;
  html = html.replace("</dl>\n", '</dl>\n<p class="jump"><a href="#fotos">' + n + ' Fotos</a></p>\n');
  html = html.replace("</article>", gallery(e, credits[e.slug]) + "</article>");
  html = html.replace("</body>", LIGHTBOX + "</body>");
  return html;
}

function wallMain(events) {
  var list = events.slice().sort(function (a, b) { return b.nr - a.nr; });
  var next = events.filter(function (e) { return e.up; })[0];
  var bar = "";
  if (next) {
    bar = '<a class="nextbar" href="/gespraeche/' + next.slug + '.html" data-until="' + next.date + 'T12:00:00+01:00" data-before>' +
      '<span class="label">Nächstes Gespräch</span><strong>' + esc(next.name) + '</strong><span>' + esc(next.datum) +
      (next.zeit ? ", " + esc(next.zeit) : "") + (next.ort ? ", " + esc(next.ort) : "") + '</span><span class="go">Mehr →</span></a>\n';
  }
  var tiles = list.map(function (e) {
    return '<li><a href="/gespraeche/' + e.slug + '.html"><img src="' + poster(e, 400) + '" srcset="' + poster(e, 400) + ' 400w, ' + poster(e, 800) +
      ' 800w" sizes="(max-width: 600px) 50vw, 25vw" alt="' + esc(e.name) + ', Schmelzgespräch Nr. ' + e.nr + ', ' + e.d + '" width="400" height="400">' + (e.up ? '<span class="badge" data-before>Demnächst</span>' : "") + '</a></li>';
  });
  return '\n<div class="wrap">\n<section class="intro">\n<h1>Schule fragt nach.</h1>\n' +
    '<p>Seit 2019 holen Schüler:innen des GRG 15 Auf der Schmelz ihre Gäste ins Atrium. Menschen aus Politik, Journalismus und Kultur, mit denen Jugendliche sonst kaum ins Gespräch kommen. Die Fragen entstehen im Unterricht, moderiert wird von Schüler:innen.</p>\n</section>\n' +
    bar +
    '<h2 class="skip">Alle Gespräche seit 2019</h2>\n<ul class="wall">\n' + tiles.join("\n") + '\n</ul>\n' +
    '<section class="row">\n<h2 class="label">So entsteht ein Schmelzgespräch</h2>\n<div class="body">\n<ol class="steps">\n' +
    '<li><span class="n">01</span><h3>Klassen melden sich an</h3><p>Klassenvorstände melden ihre Klasse an. Eine Lehrperson aus dem Klassenteam übernimmt die Vorbereitung.</p></li>\n' +
    '<li><span class="n">02</span><h3>Fragen entstehen im Unterricht</h3><p>Die Klassen recherchieren zum Gast und formulieren Fragen. Vor Wahlen stimmt die ganze Oberstufe darüber ab, welche gestellt werden.</p></li>\n' +
    '<li><span class="n">03</span><h3>Schüler:innen moderieren</h3><p>Das Schmelzgespräche-Team empfängt den Gast, führt durch das Gespräch und gibt Fragen aus dem Publikum weiter.</p></li>\n' +
    '<li><span class="n">04</span><h3>Im Atrium</h3><p>Meist in der 3. und 4. Stunde, vor bis zu 300 Schüler:innen.</p></li>\n' +
    '</ol>\n</div>\n</section>\n</div>\n';
}

function transformIndex(html, events) {
  var a = html.indexOf('<main id="inhalt">');
  var b = html.indexOf("</main>");
  if (a < 0 || b < 0) throw new Error("index: main nicht gefunden");
  return html.slice(0, a + '<main id="inhalt">'.length) + wallMain(events) + html.slice(b);
}

function transformCss(css) {
  if (css.indexOf("/* Plakatwand") > -1) css = css.slice(0, css.indexOf("\n/* Plakatwand"));
  return css + CSS;
}

return { transformEvent: transformEvent, transformIndex: transformIndex, transformCss: transformCss };
