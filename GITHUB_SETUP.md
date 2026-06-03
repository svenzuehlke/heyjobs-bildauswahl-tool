# 📦 GitHub Repository Setup Guide

## 🚀 Quick Deploy zu GitHub Pages

### Schritt 1: Repository erstellen

```bash
# Lokales Repository initialisieren
git init heyjobs-bildauswahl-tool
cd heyjobs-bildauswahl-tool

# Dateien aus diesem Projekt kopieren:
# - index.html (das Tool)
# - README.md
# - LICENSE
# - .gitignore
# - copy_images.py
# - HeyJobs_Bildauswahl_Tool_Dokumentation.md (in docs/ Ordner)

# Ordnerstruktur:
heyjobs-bildauswahl-tool/
├── index.html                              # Haupttool
├── README.md                               # GitHub Landing Page
├── LICENSE                                 # MIT License
├── .gitignore                             # Git Ignore
├── copy_images.py                         # Beispiel-Script
└── docs/
    └── DOKUMENTATION.md                    # Ausführliche Doku
```

### Schritt 2: Git Commits

```bash
# Erste Commits
git add .
git commit -m "Initial commit: HeyJobs Bildauswahl Tool v1.0"

# GitHub Remote hinzufügen
git remote add origin https://github.com/DEIN-USERNAME/heyjobs-bildauswahl-tool.git
git branch -M main
git push -u origin main
```

### Schritt 3: GitHub Pages aktivieren

1. Gehe zu deinem GitHub Repository
2. **Settings** → **Pages**
3. **Source**: Deploy from a branch
4. **Branch**: `main` → `/` (root)
5. **Save**

⏱️ **Nach ~2 Minuten** ist dein Tool live unter:
```
https://DEIN-USERNAME.github.io/heyjobs-bildauswahl-tool/
```

---

## ✅ Wie alles funktioniert

### 🌐 Online Tool (GitHub Pages)
- **index.html** wird öffentlich gehostet
- Tool läuft **komplett im Browser** (JavaScript)
- Keine Backend-Server nötig

### 💾 Bilder bleiben lokal
```
Dein Computer:                    GitHub Pages:
┌─────────────────┐              ┌─────────────────┐
│ /junger_deutsche│              │                 │
│ /junge_deutsche │              │   index.html    │
│ /ältere_deutsche│  ----X---►   │   (Tool only)   │
│ /nicht_deutsch  │              │                 │
└─────────────────┘              └─────────────────┘
      Lokal!                          Online!
```

**Bilder werden NICHT hochgeladen!**
- Tool nutzt `webkitdirectory` → Browser öffnet lokalen Ordner
- `URL.createObjectURL(file)` → Temporäre Blob-URLs im Browser
- Keine Netzwerk-Requests für Bilder

### 📦 CSV-Export (lokal)
```
Browser (Client-Side):
1. Auswahl treffen
2. "CSV Export" klicken
3. JavaScript generiert CSV
4. Download als Datei → landet in deinem Downloads-Ordner

GitHub Pages Server:
→ Weiß nichts von deinen CSVs
→ Speichert nichts
```

### 💾 LocalStorage (Cache)

**Wie es funktioniert:**
```javascript
// Speichern (automatisch nach jeder Auswahl)
localStorage.setItem('jobImageSelections', JSON.stringify(selections));

// Laden (beim nächsten Öffnen)
const saved = localStorage.getItem('jobImageSelections');
selections = JSON.parse(saved);

// Löschen (mit "Cache löschen" Button)
localStorage.removeItem('jobImageSelections');
```

**Browser-Storage:**
```
Browser: Chrome/Firefox/Safari
Domain: https://DEIN-USERNAME.github.io/heyjobs-bildauswahl-tool/

LocalStorage:
├── jobImageSelections    → { "123": { "cat1": "image.png", ... }, ... }
└── jobBadImages          → { "123": { "cat1": ["bad.png"], ... }, ... }
```

**Wichtig:**
- ✅ **Pro Browser/Domain** → Chrome & Firefox = separate Caches
- ✅ **Bleibt beim Neuladen** → Fortschritt geht nicht verloren
- ⚠️ **Browser-Daten löschen** → Cache ist weg
- ⚠️ **Anderer Computer** → Kein Zugriff auf Cache

---

## 🎯 User Workflow (mit Online-Tool)

### Szenario 1: Erster Durchlauf

```bash
1. User öffnet: https://DEIN-USERNAME.github.io/heyjobs-bildauswahl-tool/
2. Browser lädt index.html von GitHub Pages
3. Tool läuft lokal im Browser
4. User klickt "Ordner auswählen"
5. Browser öffnet lokale Ordner-Auswahl
6. User wählt 4 lokale Ordner aus
7. Tool scannt Dateien (lokal, kein Upload!)
8. User wählt Bilder aus
9. LocalStorage speichert Fortschritt (automatisch)
10. User exportiert CSV (Download zu Downloads-Ordner)
11. User lädt copy_images.py herunter
12. User führt Script aus → Bilder werden lokal kopiert
```

### Szenario 2: Fortsetzen nach Pause

```bash
1. User öffnet Tool (selbe URL)
2. Tool lädt → LocalStorage wiederherstellen
3. ✅ Alle Auswahlen sind noch da!
4. User macht weiter wo er aufgehört hat
```

### Szenario 3: Neuer Computer

```bash
1. User öffnet Tool auf anderem Computer
2. LocalStorage ist leer (neuer Browser)
3. User muss von vorne beginnen
   
   ODER:
   
4. User importiert vorherige CSV (Feature-Idee für v2.0)
```

---

## 🔐 Sicherheit & Privacy

### Was wird auf GitHub gespeichert?
```
GitHub Repository:
✅ index.html (Code)
✅ README.md (Doku)
✅ LICENSE
✅ copy_images.py (Beispiel)

❌ KEINE Bilder
❌ KEINE CSVs
❌ KEINE User-Daten
```

### Was wird online übertragen?
```
Erste Ladung:
→ index.html (~50 KB) von GitHub Pages
→ Google Fonts: IBM Plex Sans

Danach:
→ NICHTS mehr!
→ Alles passiert lokal im Browser
```

---

## 🛠️ Cache-Management

### Automatischer Cache
```javascript
// Nach JEDER Auswahl:
function selectImage(...) {
    // ... Auswahl-Logik
    saveSelections(); // ← Automatisch!
}

function toggleBadImage(...) {
    // ... Flaggen-Logik
    saveSelections(); // ← Automatisch!
}
```

### Manueller Cache-Reset

**Im Tool:**
```
Navigation → "Reset" → "Cache löschen" Button
→ Bestätigung: "⚠️ Alle Fortschritte löschen?"
→ localStorage.clear()
```

**Im Browser:**
```
Chrome: F12 → Application → Local Storage → Delete
Firefox: F12 → Storage → Local Storage → Delete
Safari: Develop → Show Web Inspector → Storage → Delete
```

**Browser-Daten löschen:**
```
Chrome: Settings → Privacy → Clear browsing data
Firefox: Settings → Privacy → Clear Data
Safari: History → Clear History
```

---

## 📊 Datenfluss-Diagramm

```
┌─────────────────────────────────────────────────────────────┐
│                       Dein Computer                         │
│                                                             │
│  ┌──────────────┐    ┌──────────────┐   ┌──────────────┐ │
│  │  Bildordner  │    │   Browser    │   │  Downloads   │ │
│  │              │    │              │   │              │ │
│  │ /junger_...  │◄───│  Tool läuft  │───►│ .csv         │ │
│  │ /junge_...   │    │  lokal       │   │ .py          │ │
│  │ /ältere_...  │    │              │   │              │ │
│  │ /nicht_...   │    │ LocalStorage │   └──────────────┘ │
│  └──────────────┘    │ (Cache)      │                     │
│                      └──────────────┘                     │
│                           ▲                                │
└───────────────────────────┼────────────────────────────────┘
                            │ Einmalig beim Laden
                            │ index.html (~50 KB)
                            │
                    ┌───────┴────────┐
                    │  GitHub Pages  │
                    │                │
                    │   index.html   │
                    │   (Static)     │
                    └────────────────┘
```

---

## 🎨 Optional: Custom Domain

Wenn du eine eigene Domain hast:

```bash
# In Repository Settings → Pages → Custom domain:
bildauswahl.heyjobs.de

# CNAME Record bei DNS-Provider:
bildauswahl.heyjobs.de → DEIN-USERNAME.github.io

# Fertig! Tool erreichbar unter:
https://bildauswahl.heyjobs.de
```

---

## 🐛 Troubleshooting

### Problem: "Bilder werden hochgeladen?"
**Antwort:** 
Nein! Der Browser fragt nur nach **lokaler** Ordner-Permission. Die Dateien bleiben auf deinem Computer.

### Problem: Cache funktioniert nicht
**Lösung:**
- Browser-Daten-Einstellungen prüfen
- LocalStorage aktiviert?
- Private/Incognito Mode deaktivieren

### Problem: Tool lädt nicht
**Lösung:**
```bash
# GitHub Pages Status prüfen:
https://github.com/DEIN-USERNAME/heyjobs-bildauswahl-tool/deployments

# Warten (~2 Min nach Push)
# Cache leeren (Strg+Shift+R)
```

---

## 📝 .gitignore Erklärung

```bash
# Diese Dateien NICHT committen:
*.csv          # Exports sind lokal
*.xml          # Exports sind lokal
*.png          # Bilder sind lokal
*.jpg          # Bilder sind lokal
final/         # Kopierte Bilder sind lokal
bad_images/    # Kopierte Bilder sind lokal

# Diese Dateien COMMITTEN:
index.html     # ✅ Das Tool selbst
README.md      # ✅ Dokumentation
copy_images.py # ✅ Beispiel-Script
```

---

## 🚀 Deployment-Checklist

- [ ] Repository erstellt
- [ ] Alle Dateien commited
- [ ] GitHub Pages aktiviert
- [ ] URL getestet
- [ ] README aktualisiert (USERNAME ersetzen)
- [ ] Tool funktioniert online
- [ ] Cache-Funktionalität getestet
- [ ] Export getestet (CSV Download)
- [ ] Python-Script getestet (lokal)
- [ ] Optional: Custom Domain konfiguriert

---

## 🎯 Fertig!

Dein Tool ist jetzt:
- ✅ **Online verfügbar** (GitHub Pages)
- ✅ **Komplett lokal** (Bilder bleiben bei dir)
- ✅ **Cache funktioniert** (LocalStorage)
- ✅ **Export funktioniert** (CSV Download)
- ✅ **Open Source** (GitHub Repository)

**Live unter:**
```
https://DEIN-USERNAME.github.io/heyjobs-bildauswahl-tool/
```

---

*Happy Coding! 🚀*
