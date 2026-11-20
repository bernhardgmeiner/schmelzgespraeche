# -*- coding: utf-8 -*-
import os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from site_data import EVENTS, SCHULJAHRE, TEAM_AKTUELL, EHEMALIGE, LOGO

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")
os.makedirs(OUT + "/gespraeche", exist_ok=True)
E = {e["nr"]: e for e in EVENTS}
esc = html.escape

FAVICON = LOGO + "/v1/crop/x_95,y_250,w_870,h_870/fill/w_64,h_64,al_c,q_95/favicon.png"
MARK = LOGO + "/v1/crop/x_95,y_340,w_870,h_690/fill/w_96,h_76,al_c,q_95/logo.png"

def img(e, w):
    return f'{e["poster"]}/v1/fill/w_{w},h_{w},q_85,enc_auto/p.jpg'

def disp_name(e):
    return e["name"] + (f' („{e["alias"]}“)' if e.get("alias") else "")

def short_date(e):
    y, m, d = e["date"].split("-")
    return f"{int(d)}.{int(m)}.{y}"

def head(title, desc, path, og=None):
    og = og or img(E[16], 1200)
    return f'''<!doctype html>
<html lang="de-AT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{og}">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_AT">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt</a>
<header class="site"><div class="wrap">
<a class="brand" href="/"><img src="{MARK}" alt="" width="48" height="38">Schmelzgespräche</a>
<nav class="main" aria-label="Hauptnavigation">
<a href="/gespraeche.html"{' aria-current="page"' if path=="gespraeche" else ''}>Gespräche</a>
<a href="/ueber-uns.html"{' aria-current="page"' if path=="ueber" else ''}>Über uns</a>
<a href="/kontakt.html"{' aria-current="page"' if path=="kontakt" else ''}>Kontakt</a>
</nav>
</div></header>
<main id="inhalt">
'''

FOOT = '''</main>
<footer class="site"><div class="wrap cols">
<p class="f1"><strong>Schmelzgespräche</strong><br>Die Talkreihe des GRG 15 Auf der Schmelz, seit 2019</p>
<p class="f2">Auf der Schmelz 4, 1150 Wien<br><a href="mailto:schmelzgespraeche@schmelz.at">schmelzgespraeche@schmelz.at</a></p>
<p class="f3"><a href="https://www.instagram.com/schmelzgespraeche/">Instagram</a><br><a href="/kontakt.html">Kontakt</a> · <a href="/impressum.html">Impressum</a></p>
</div></footer>
<script>(function(){var t=document.querySelector("[data-until]");if(!t)return;if(Date.now()>Date.parse(t.getAttribute("data-until"))){document.querySelectorAll("[data-before]").forEach(function(e){e.hidden=true});document.querySelectorAll("[data-after]").forEach(function(e){e.hidden=false})}})();</script>
</body>
</html>
'''

def tile(e):
    return f'''<a class="tile" href="/gespraeche/{e["slug"]}.html">
<img src="{img(e,480)}" srcset="{img(e,480)} 480w, {img(e,800)} 800w" sizes="(max-width: 820px) 50vw, 25vw" alt="Plakat: {esc(e["name"])}, {short_date(e)}" width="480" height="480" loading="lazy">
<p class="no"><span>Nr. {e["nr"]:02d}</span> · {short_date(e)}</p>
<h3>{esc(e["name"])}</h3>
<p>{esc(e["short"])}</p>
</a>'''

def meta(e):
    rows = [("Datum", e["datum"])]
    if e.get("zeit"): rows.append(("Zeit", e["zeit"]))
    if e.get("ort"): rows.append(("Ort", e["ort"]))
    rows.append(("Publikum", e["publikum"]))
    if e.get("gaeste"): rows.append(("Gäste", e["gaeste"]))
    if e.get("team"): rows.append(("Moderation" if e["nr"] >= 6 else "Team", e["team"]))
    return '<dl class="meta">' + "".join(f"<dt>{k}</dt><dd>{esc(v)}</dd>" for k, v in rows) + "</dl>"

# ---------- Startseite ----------
nxt = E[16]
recent = [E[15], E[14], E[13]]
index = head("Schmelzgespräche – die Talkreihe des GRG 15 Wien",
             "Seit 2019 holen Schüler:innen des GRG 15 Auf der Schmelz Gäste aus Politik, Journalismus und Kultur ins Atrium und stellen ihre Fragen.", "home")
index += f'''<div class="wrap">
<section class="hero">
<h1>Schule fragt nach.</h1>
<p class="lead">Seit 2019 holen Schüler:innen des GRG 15 Auf der Schmelz ihre Gäste ins Atrium. Menschen aus Politik, Journalismus und Kultur, mit denen Jugendliche sonst kaum ins Gespräch kommen. Die Fragen entstehen im Unterricht, moderiert wird von Schüler:innen.</p>
</section>
<section class="row" data-until="{nxt["date"]}T12:00:00+01:00">
<h2 class="label"><span data-before>Nächstes Gespräch</span><span data-after hidden>Zuletzt</span></h2>
<div class="body feature">
<a class="poster" href="/gespraeche/{nxt["slug"]}.html"><img src="{img(nxt,720)}" srcset="{img(nxt,720)} 720w, {img(nxt,1080)} 1080w" sizes="(max-width: 820px) 100vw, 40vw" alt="Plakat: Franz-Stefan Gady, 24.11.2026" width="720" height="720"></a>
<div class="info">
<p class="folio" aria-hidden="true">{nxt["nr"]:02d}</p>
<h3 class="big">{esc(nxt["name"])}</h3>
<p class="sub">„Wie erklärt man Krieg? Die Welt 2026 verstehen“</p>
{meta(nxt)}
<a class="more" href="/gespraeche/{nxt["slug"]}.html">Mehr zum Gespräch</a>
</div>
</div>
</section>
<section class="row">
<h2 class="label">Zuletzt</h2>
<div class="body">
<div class="grid recent">
{"".join(tile(e) for e in recent)}
</div>
<a class="more" href="/gespraeche.html">Alle {len(EVENTS)} Gespräche seit 2019</a>
</div>
</section>
<section class="row">
<h2 class="label">So entsteht ein Schmelzgespräch</h2>
<div class="body">
<ol class="steps">
<li><span class="n">01</span><h3>Klassen melden sich an</h3><p>Klassenvorstände melden ihre Klasse an. Eine Lehrperson aus dem Klassenteam übernimmt die Vorbereitung.</p></li>
<li><span class="n">02</span><h3>Fragen entstehen im Unterricht</h3><p>Die Klassen recherchieren zum Gast und formulieren Fragen. Vor Wahlen stimmt die ganze Oberstufe darüber ab, welche gestellt werden.</p></li>
<li><span class="n">03</span><h3>Schüler:innen moderieren</h3><p>Das Schmelzgespräche-Team empfängt den Gast, führt durch das Gespräch und gibt Fragen aus dem Publikum weiter.</p></li>
<li><span class="n">04</span><h3>Im Atrium</h3><p>Meist in der 3. und 4. Stunde, vor bis zu 300 Schüler:innen.</p></li>
</ol>
</div>
</section>
</div>
'''
index += FOOT
open(OUT + "/index.html", "w", encoding="utf-8").write(index)

# ---------- Archiv ----------
arch = head("Alle Gespräche – Schmelzgespräche", "Alle Schmelzgespräche am GRG 15 seit Oktober 2019: Gäste, Termine, Themen.", "gespraeche")
arch += f'''<div class="wrap">
<section class="hero small">
<h1>Alle Gespräche</h1>
<p class="lead">{len(EVENTS)} Gespräche seit Oktober 2019, vom ersten Besuch von Armin Wolf bis heute.</p>
</section>
'''
for sj, nrs in SCHULJAHRE:
    arch += f'''<section class="row">
<h2 class="label">Schuljahr {sj}</h2>
<div class="body"><div class="grid">
{"".join(tile(E[n]) for n in nrs)}
</div></div>
</section>
'''
arch += "</div>\n" + FOOT
open(OUT + "/gespraeche.html", "w", encoding="utf-8").write(arch)

# ---------- Gesprächsseiten ----------
for e in EVENTS:
    prev_e, next_e = E.get(e["nr"] - 1), E.get(e["nr"] + 1)
    desc = f'Schmelzgespräch Nr. {e["nr"]} am GRG 15: {disp_name(e)}, {e["datum"]}. {e["short"]}.'
    p = head(f'{disp_name(e)} – Schmelzgespräch Nr. {e["nr"]}', desc, "gespraeche", og=img(e, 1200))
    badge = ""
    until = ""
    if e.get("upcoming"):
        until = f' data-until="{e["date"]}T12:00:00+01:00"'
        badge = '<p class="badge" data-before>Demnächst</p>'
    p += f'''<div class="wrap">
<p class="crumb label"><a href="/gespraeche.html">Gespräche</a> / Nr. {e["nr"]:02d}</p>
<article class="event"{until}>
<div class="ev-head">
<div class="info">
<p class="folio" aria-hidden="true">{e["nr"]:02d}</p>
{badge}
<h1>{esc(disp_name(e))}</h1>
<p class="sub">{esc(e["short"])}</p>
{meta(e)}
</div>
<figure class="poster"><img src="{img(e,900)}" alt="Plakat: {esc(e["name"])}, {short_date(e)}" width="900" height="900">{f'<figcaption>{esc(e["credit"])}</figcaption>' if e.get("credit") else ''}</figure>
</div>
<section class="row">
<h2 class="label">{"Vorschau" if e.get("upcoming") else "Rückblick"}</h2>
<div class="body text">
{"".join(f"<p>{esc(t)}</p>" for t in e["text"])}
</div>
</section>
</article>
<nav class="pager" aria-label="Weitere Gespräche">
{f'<a class="prev" href="/gespraeche/{prev_e["slug"]}.html"><span class="label">← Nr. {prev_e["nr"]:02d}</span>{esc(prev_e["name"])}</a>' if prev_e else '<span></span>'}
{f'<a class="next" href="/gespraeche/{next_e["slug"]}.html"><span class="label">Nr. {next_e["nr"]:02d} →</span>{esc(next_e["name"])}</a>' if next_e else '<span></span>'}
</nav>
</div>
'''
    p += FOOT
    open(f'{OUT}/gespraeche/{e["slug"]}.html', "w", encoding="utf-8").write(p)

# ---------- Über uns ----------
ab = head("Über uns – Schmelzgespräche", "Wer hinter den Schmelzgesprächen am GRG 15 steht: die Idee, das Team, die Leitung.", "ueber")
ab += f'''<div class="wrap">
<section class="hero small">
<h1>Über uns</h1>
<p class="lead">Die Schmelzgespräche sind eine Talkreihe, die Schüler:innen am GRG 15 Auf der Schmelz selbst veranstalten. Seit Oktober 2019 kommen Menschen an die Schule, die etwas zu erzählen haben.</p>
</section>
<section class="row">
<h2 class="label">Die Idee</h2>
<div class="body text">
<p>Jugendliche treffen Menschen aus Politik, Journalismus, Kultur und Wissenschaft, mit denen sie im Alltag kaum in Kontakt kommen. Sie lernen aus deren Biografien, hören andere Blickwinkel und fragen bei echten Expert:innen nach.</p>
<p>Die Fragen kommen aus dem Unterricht. Die Klassen bereiten sich auf jeden Gast vor, das Team wählt aus und moderiert. Vor Wahlen laden wir Vertreter:innen aller im jeweiligen Parlament oder Gemeinderat vertretenen Parteien zur Elefantenrunde ein.</p>
</div>
</section>
<section class="row">
<h2 class="label">Team</h2>
<div class="body">
<ul class="names">{"".join(f"<li>{esc(n)}</li>" for n in TEAM_AKTUELL)}</ul>
<p class="muted">Das Team organisiert, recherchiert, bereitet Fragen vor und moderiert.</p>
</div>
</section>
<section class="row">
<h2 class="label">Leitung</h2>
<div class="body text">
<p><strong>Bernhard Gmeiner</strong> unterrichtet am GRG 15 Englisch sowie Geographie und wirtschaftliche Bildung. Er hat die Schmelzgespräche 2019 gegründet und leitet sie seither. <a href="https://bernhardgmeiner.com">bernhardgmeiner.com</a></p>
</div>
</section>
<section class="row">
<h2 class="label">Ehemalige</h2>
<div class="body">
<dl class="meta alumni">{"".join(f"<dt>{esc(y)}</dt><dd>{esc(n)}</dd>" for y, n in EHEMALIGE)}</dl>
</div>
</section>
<section class="row">
<h2 class="label">Danke</h2>
<div class="body text">
<p>An die Klassenvorstände und Lehrer:innen, die jedes Gespräch im Unterricht vorbereiten. An Rahmi Özaltin für Administration und Technik, an das Technik-Team der Schüler:innen, an unsere Schulwart:innen und das Reinigungsteam. Und an alle Gäste, die zu uns gekommen sind.</p>
</div>
</section>
<section class="row">
<h2 class="label">Presse</h2>
<div class="body text">
<p>FALTER.morgen, 13. Mai 2024: „Der Vorreiter“, ein Porträt über die Schmelzgespräche anlässlich der Elefantenrunde zur EU-Wahl. <a href="https://www.falter.at/morgen/20240513/oesterreichs-superreiche-steuerflucht-finanzamt-firmengeflecht-hnwi">Zum Artikel</a></p>
</div>
</section>
</div>
'''
ab += FOOT
open(OUT + "/ueber-uns.html", "w", encoding="utf-8").write(ab)

# ---------- Kontakt ----------
ko = head("Kontakt – Schmelzgespräche", "So erreichen Sie die Schmelzgespräche am GRG 15 Auf der Schmelz in Wien.", "kontakt")
ko += '''<div class="wrap">
<section class="hero small">
<h1>Kontakt</h1>
<p class="lead">Für Gäste, Presse und die Schulgemeinschaft.</p>
</section>
<section class="row">
<h2 class="label">E-Mail</h2>
<div class="body"><p class="big-link"><a href="mailto:schmelzgespraeche@schmelz.at">schmelzgespraeche@schmelz.at</a></p></div>
</section>
<section class="row">
<h2 class="label">Telefon</h2>
<div class="body"><p class="big-link"><a href="tel:+431982035121">+43 1 982 03 51-21</a></p></div>
</section>
<section class="row">
<h2 class="label">Adresse</h2>
<div class="body text"><p>GRG 15 Auf der Schmelz<br>Auf der Schmelz 4<br>1150 Wien</p><p><a href="https://www.schmelz.at">schmelz.at</a></p></div>
</section>
<section class="row">
<h2 class="label">Instagram</h2>
<div class="body"><p class="big-link"><a href="https://www.instagram.com/schmelzgespraeche/">@schmelzgespraeche</a></p></div>
</section>
</div>
'''
ko += FOOT
open(OUT + "/kontakt.html", "w", encoding="utf-8").write(ko)

# ---------- Impressum ----------
im = head("Impressum – Schmelzgespräche", "Impressum und Datenschutzhinweise der Schmelzgespräche-Website.", "impressum")
im += '''<div class="wrap">
<section class="hero small">
<h1>Impressum</h1>
</section>
<section class="row">
<h2 class="label">Medieninhaber und verantwortlich für den Inhalt</h2>
<div class="body text"><p>Bernhard Gmeiner<br>GRG 15 Auf der Schmelz<br>Auf der Schmelz 4, 1150 Wien<br>Tel. <a href="tel:+431982035121">+43 1 982 03 51-21</a><br><a href="mailto:bernhard.gmeiner@schmelz.at">bernhard.gmeiner@schmelz.at</a></p></div>
</section>
<section class="row">
<h2 class="label">Bildrechte</h2>
<div class="body text"><p>Plakate: Schmelzgespräche-Team. Die Rechte an den Porträtfotos auf den Plakaten liegen bei den jeweiligen Fotograf:innen; soweit bekannt, sind sie auf der Seite des Gesprächs genannt.</p></div>
</section>
<section class="row">
<h2 class="label">Datenschutz</h2>
<div class="body text"><p>Diese Website wird über GitHub Pages (GitHub Inc.) ausgeliefert. GitHub speichert beim Aufruf aus Sicherheitsgründen die IP-Adresse der Besucher:innen. Plakate und Fotos kommen aus der Mediathek von Wix (static.wixstatic.com), dabei erhält auch Wix die IP-Adresse. Die Website setzt keine Cookies und nutzt keine Statistik- oder Werbedienste. Wenn Sie uns per E-Mail schreiben, verwenden wir Ihre Angaben nur, um Ihre Anfrage zu beantworten.</p></div>
</section>
</div>
'''
im += FOOT
open(OUT + "/impressum.html", "w", encoding="utf-8").write(im)
# ---------- 404 ----------
nf = head("Seite nicht gefunden – Schmelzgespräche", "Diese Seite gibt es auf schmelzgespraeche.at nicht.", "404")
nf += '''<div class="wrap">
<section class="hero small">
<h1>Diese Seite gibt es nicht.</h1>
<p class="lead">Die Adresse stimmt nicht, oder die Seite ist beim Umzug der Website verloren gegangen.</p>
</section>
<section class="row">
<h2 class="label">Weiter</h2>
<div class="body"><p class="big-link"><a href="/">Zur Startseite</a></p><p class="big-link"><a href="/gespraeche.html">Alle Gespräche seit 2019</a></p></div>
</section>
</div>
'''
nf += FOOT
open(OUT + "/404.html", "w", encoding="utf-8").write(nf)

# ---------- Weiterleitungen von Adressen der alten Wix-Seite ----------
REDIRECTS = {
    "bio": "/ueber-uns.html",
    "website-für-skiresort": "/gespraeche/armin-wolf-2019.html",
    "kopie-von-01-wolf": "/gespraeche/josef-dollinger.html",
    "kopie-von-02-dollinger": "/gespraeche/manuel-rubey.html",
    "kopie-von-03-rubey": "/gespraeche/alma-zadic.html",
    "kopie-von-04-zadic": "/gespraeche/andreas-sator.html",
    "kopie-von-05-sator": "/gespraeche/barbara-blaha.html",
    "kopie-von-06-blaha": "/gespraeche/toxische-pommes.html",
    "kopie-von-07-toxische-pommes": "/gespraeche/armin-wolf-2023.html",
    "kopie-von-08-wolf": "/gespraeche/leonore-gewessler.html",
    "kopie-von-09-gewessler": "/gespraeche/elefantenrunde-eu-wahl-2024.html",
    "veit": "/gespraeche/hannelore-veit.html",
    "kopie-von-11-veit": "/gespraeche/elefantenrunde-wien-wahl-2025.html",
    "krell": "/gespraeche/checker-tobi.html",
    "kopie-von-13-krell": "/gespraeche/christoph-wiederkehr.html",
    "kopie-von-14-wiederkehr": "/gespraeche/natascha-fuerst.html",
}
for old, target in REDIRECTS.items():
    open(f"{OUT}/{old}.html", "w", encoding="utf-8").write(f'''<!doctype html>
<html lang="de-AT">
<head>
<meta charset="utf-8">
<title>Weiterleitung – Schmelzgespräche</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="https://schmelzgespraeche.at{target}">
<meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
<p>Diese Seite ist umgezogen: <a href="{target}">weiter</a></p>
</body>
</html>
''')

# ---------- GitHub Pages ----------
open(OUT + "/CNAME", "w").write("schmelzgespraeche.at\n")
open(OUT + "/.nojekyll", "w").write("")
print("built", len(os.listdir(OUT + "/gespraeche")), "event pages")
