# Schmelzgespräche – Website

Website der Schmelzgespräche, der Talkreihe des GRG 15 Auf der Schmelz in Wien: https://schmelzgespraeche.at

Die Seite besteht nur aus statischen HTML-Dateien und wird über GitHub Pages aus dem Ordner `docs/` ausgeliefert.

## Aufbau

| Ordner | Inhalt |
|---|---|
| `docs/` | die fertige Website (Startseite mit Plakatwand, Archiv, 16 Gesprächsseiten mit Fotos, Über uns, Kontakt, Impressum, 404-Seite, Weiterleitungen von Adressen der alten Wix-Seite) |
| `docs/fonts/` | Schibsted Grotesk, selbst gehostet (SIL Open Font License, siehe `OFL.txt`) |
| `tools/site_data.py` | alle Inhalte: Gespräche, Texte, Team |
| `tools/sitedata.json` | Plakate und Fotos je Gespräch (Datei-IDs in der Wix-Mediathek, Seitenverhältnis, Fotonachweis) |
| `tools/build_site.py` | erzeugt die HTML-Seiten in `docs/` |
| `tools/transform.js` | baut Plakatwand, Fotogalerien samt Großansicht und die zugehörigen CSS-Regeln ein |

## Neu bauen

```
python3 tools/build_site.py
node tools/apply.js
```

`docs/styles.css` ist die Hauptdatei für das Aussehen; `apply.js` hängt die Regeln für Plakatwand und Galerien jedes Mal frisch an.

## Wichtig

Plakate und Fotos liegen in der Wix-Mediathek der Wix-Seite „Schmelzgespräche neu“ und werden von static.wixstatic.com geladen. Diese Wix-Seite darf deshalb nicht gelöscht werden, auch wenn die Website selbst nicht mehr dort läuft.
