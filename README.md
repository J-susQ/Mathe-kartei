# Analysis-Kartei

Karteikarten für Definitionen, Axiome, Lemmata und Sätze aus Analysis, als Offline-Web-App (PWA) für das iPhone.

- **Level 1:** Inhalte der eigenen handschriftlichen Mindmap (Karten mit „Lesung prüfen“ sind unsicher gelesen oder ergänzt).
- **Level 2:** Analysis 1, **Level 3:** Analysis 2. Kanon: Forster (Analysis 1/2) und Königsberger (Analysis 1/2).

## Installation auf dem iPhone
Seite in Safari öffnen → Teilen → „Zum Home-Bildschirm“. Nach dem ersten Öffnen läuft die App offline.
Der Lernfortschritt liegt im Speicher dieser App auf dem Gerät.

## Aufbau
- `index.html`: die komplette App (KaTeX und alle Karten eingebettet)
- `sw.js`, `manifest.webmanifest`, `icon-*.png`: Offline-Fähigkeit und Homescreen-Symbol
- `quelle/`: Kartendaten (`l1.py`, `l2.py`, `l3.py`) und Build-Skripte. `build.py` erwartet das entpackte npm-Paket `katex@0.16.11` unter `../dl/package`.

Nach Änderungen an Karten: `python3 build_cards.py && python3 build.py`, dann `out/pwa/*` ins Hauptverzeichnis kopieren und in `sw.js` die Cache-Version erhöhen.
