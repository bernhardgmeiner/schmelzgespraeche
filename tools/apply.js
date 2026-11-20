// node tools/apply.js [docs]: baut Plakatwand, Fotogalerien und CSS-Ergänzung in die von build_site.py erzeugten Seiten ein
const fs = require("fs"), path = require("path");
const dir = process.argv[2] || path.join(__dirname, "..", "docs");
const T = new Function(fs.readFileSync(path.join(__dirname, "transform.js"), "utf8"))();
const data = JSON.parse(fs.readFileSync(path.join(__dirname, "sitedata.json"), "utf8"));
const rw = (f, fn) => { const p = path.join(dir, f); fs.writeFileSync(p, fn(fs.readFileSync(p, "utf8"))); return [f, fs.statSync(p).size]; };
const out = [];
out.push(rw("styles.css", T.transformCss));
out.push(rw("index.html", h => T.transformIndex(h, data.events)));
for (const e of data.events) out.push(rw("gespraeche/" + e.slug + ".html", h => T.transformEvent(h, e, data.credits)));
console.log(JSON.stringify(Object.fromEntries(out)));
