# Persönlicher Budget Tracker

Ein konsolenbasiertes Python-Programm zur Verwaltung persönlicher Finanzen. Benutzer können passwortgeschützt Einnahmen und Ausgaben verwalten, monatliche Statistiken einsehen und den Budgetplan speichern. Das Projekt wurde im Rahmen eines Assessments nach didaktischen Vorgaben umgesetzt. 

---

### Projektbeschreibung

Der **Persönliche Budget-Tracker** ermöglicht es Benutzern ihre monatlichen Einnahmen und Ausgaben übersichtlich zu erfassen, auszuwerten und in CSV-Dateien zu speichern.

Das Programm läuft vollständig in **Terminal** und verwendet eine menügesteuerte Benutzerführung.
Die Daten werden **monatsweise** gespeichert (z.B. 'budget_2025_12.csv'), wodurch eine klare Trennung der Budgets gewährleistet ist.

---

### Motivation

Finanzmanagement ist ein zentrales Alltagsthema, insbesondere für **Studierende und Berufseinsteiger**.
Viele möchten ihre Ausgaben im Blick behalten, ohne komplexe Software oder externe Tools zu nutzen. 

Dieses Projekt bietet:
- einen **einfache, lokale Lösung**
- einen **praxisnahen Anwendungsfall** für Python-Grundlagen
- einen klaren Fokus auf **Logik, Struktur und Verständlichkeit**

---

## Programmstart und Hauptmenü

Nach dem Start des Programms wird der Benutzer begrüsst und zur Anmeldung aufgefordert. Dazu muss das festgelegte Passwort eingegeben werden. Erst nach einer erfolgreichen Anmeldung wird der Zugriff auf die Anwendung freigegeben. Bei einer falschen Eingabe wird der Benutzer erneut zur Passworteingabe aufgefordert.

Nach dem Login lädt das Programm automatisch die benötigten Daten, darunter die erlaubten Kategorien sowie die Budgetdaten des aktuellen Monats. Falls benötigte Dateien noch nicht existieren, werden diese automatisch erstellt, sodass das Programm sofort einsatzbereit ist.

Anschliessend wird das Hauptmenü angezeigt. Folgende Funktionen werden angezeigt:  


**1.** Einnahme hinzufügen

**2.** Ausgabe hinzufügen

**3.** Verfügbares Budget anzeigen

**4.** Grösste Ausgabenkategorie anzeigen

**5.** Monatliche Einträge anzeigen

**6.** Budgetplan speichern

**7.** Passwort ändern

**8.** Programm beenden 

Über dieses Menü wählt der Benutzer die gewünschte Funktion aus, indem er die entsprechende Nummer eingibt.. Es besteht die Möglichkeit, eine Einnahme hinzuzufügen oder eine Ausgabe zu erfassen. Alle Eingaben werden geprüft und fehlerhafte Eingaben werden abgefangen. Zusätzlich kann das aktuell verfügbare Budget angezeigt werden, ebenso wie die Kategorie mit den höchsten Ausgaben. Der Benutzer kann sich ausserdem alle Einträge eines bestimmten Monats anzeigen lassen. Weiter bietet das Hauptmenü die Möglichkeit, den aktuellen Budgetplan zu speichern oder das Passwort zu ändern. Zum Abschluss kann das Programm über das Menü bewusst beendet werden. Nach jeder ausgeführten Aktion kehrt die Anwendung automatisch wieder zum Hauptmenü zurück, bis der Benutzer das Programm verlässt.

---

## Hauptfunktion

- **Passwortgeschützter Login**
  - Passwort wird sicher als SHA-256-Hash gespeichert
  - Maximal 3 Login-Versuche
  - Passwortänderung über Menü möglich
 
- **Einnahmen und Ausgaben erfassen**
  - Einnahmen positiv, Ausgaben negativ gespeichert
  - Kategorien werden validiert

- **Monatliche Budgetübersicht**
  - Anzeige aller Einträge für einen bestimmten Monat
  - Automatisches Laden der passenden Monatsdatei
 
- **Grösste Ausgabenkategorie**
  - Analyse der Ausgaben pro Kategorie
  - Anzeige der höchsten Gesamtausgaben
 
- **CSV-Speicherung**
  - Automatische Erstellung von Monatsdateien ('budget_JAHR_MONAT.csv')
  - CSV-Format kompatibel mit Excel

---

### Installation & Voraussetzungen

*   Python 3.x
*   Keine externen Bibliotheken erforderlich

---

### Verwendete Python-Konzepte

- **Datentypen:** `str`, `int`, `float`, `list`, `dict`
- **Kontrollstrukturen:** `if / elif / else`, `for`, `while`
- **Funktionen:** Separate Funktionen pro Hauptaufgabe (`add_income()`, `add_expenses()`, `show_summary()`, `save_data()` usw.)
- **Dateiverarbeitung:** `open()`, `read()`, `write()`, `csv`-Modul
- **Exception Handling:** `try / except` für Eingabe- und Datei-Validierung
- **String-Operationen:** Formatiere Tabellen- und Betragsausgabe
- **Modularisierung:** Aufteilung in mehrere `.py`-Dateien

---

### Projektstruktur

personlicher-budget-tracker/

│


├── main.py                  # Programmstart & Menülogik

├── login.py                 # Passwort-Handling, Login, Hashing

├── budgetfunctions.py       # Eingaben (Einnahmen, Ausgaben)

├── data_reports.py          # Auswertungen & Speicherung

├── validationfunctions.py   # Eingabenvalidierung

├── kategorien.csv           # Liste gültiger Kategorien

├── budget_YYYY_MM.csv       # Beispielhafte Monatsdatei

└── Passwort.csv             # Gespeicherter Passwort-Hash

---

### Teamarbeit
- Person 1: Login-System, Programmstart, Menüführung
- Person 2: Einnahmen/Ausgaben, CSV-Speicherung
- Person 3: Auswertungen, Kategorien, Monatsübersichten

Die Aufgaben wurden klar getrennt und in separaten Modulen umgesetzt.

--

## Eingaben, Validierung und Buchungen

### Eingaben
Einnahmen und Ausgaben werden interaktiv über die Konsole erfasst. Dabei werden Datum, Kategorie und Betrag abgefragt. Wird kein Datum eingegeben, verwendet das System automatisch das aktuelle Datum. Die Kategorie wird aus einer vorgegebenen Liste ausgewählt, um eine einheitliche Erfassung zu gewährleisten.

### Validierung
Alle Eingaben werden vor der Verarbeitung geprüft. Datumsangaben müssen dem Format **TT.MM.JJJJ** entsprechen. Beträge müssen numerisch sein und dürfen maximal zwei Nachkommastellen enthalten. Kategorien werden gegen die erlaubte Kategorienliste geprüft. Ungültige Eingaben werden abgefangen und erneut abgefragt.

### Buchungen
Nach erfolgreicher Eingabe und Validierung werden Einnahmen und Ausgaben als einzelne Buchungen gespeichert. Anhand des Datums wird der passende Monat ermittelt und die entsprechende Monatsdatei geladen. Einnahmen werden als positive Beträge gespeichert, Ausgaben als negative. Diese Struktur ermöglicht einfache und konsistente Auswertungen.


## Budget-Daten-Analyse-Skript

### Kurzbeschreibung

Dieses Python-Skript (`data_reports1.py`) dient zur Verwaltung und Analyse von Budgetdaten, die im CSV-Format gespeichert sind. Es ermöglicht das Laden, Speichern und Auswerten von Finanztransaktionen (Einnahmen und Ausgaben).

### Funktionen

Das Skript bietet folgende Hauptfunktionen:

### Dateifunktionen

**`get_budget_filename(month, year)`**: Erzeugt einen standardisierten Dateinamen (z. B. `budget_2024_05.csv`).
**`load_data(filename)`**: Liest eine CSV-Datei ein. Die Datei muss die Spalten `Datum`, `Typ`, `Kategorie` und `Betrag` enthalten. Der `Betrag` wird automatisch in eine Fliesskommazahl umgewandelt.
**`save_data(filename, data)`**: Speichert eine Liste von Transaktionen in eine CSV-Datei.

### Auswertungsfunktionen

**`show_summary(data)`**: Berechnet die Summe aller Einnahmen (positive Beträge) und Ausgaben (negative Beträge) sowie den aktuellen Saldo und gibt diese auf der Konsole aus.
**`show_largest_category(data)`**: Ermittelt die Kategorie mit den höchsten Gesamtausgaben und zeigt diese an.
**`show_month_entries(data, month, year)`**: Filtert die Transaktionen nach einem bestimmten Monat und Jahr und gibt diese tabellarisch aus.

### Hilfsfunktionen

**`parse_month_year(datum_str)`**: Extrahiert Monat und Jahr aus einem Datumsstring im Format `TT.MM.JJJJ`.

### Datenstruktur

Die CSV-Dateien und internen Datenstrukturen verwenden folgendes Format:

**Datum**: String (Format: `TT.MM.JJJJ`, z.B. "01.05.2024")
**Typ**: String (z.B. "Einnahme", "Ausgabe")
**Kategorie**: String (z.B. "Essen", "Gehalt", "Transport")
**Betrag**: Float (Positiv für Einnahmen, Negativ für Ausgaben)


### Verwendung

Das Skript kann direkt ausgeführt werden, um die integrierte Testfunktion zu starten, oder als Modul importiert werden.

### Direktes Ausführen (Demo)

Führe das Skript in der Konsole aus:


python data_reports1.py


Dies führt die Funktion `test_functions()` aus, welche Beispieldaten erstellt, speichert, wieder lädt und die Berichte anzeigt.

### Als Modul importieren


import data_reports1

### Dateinamen bestimmen
filename = data_reports1.get_budget_filename(5, 2024)

### Daten laden
data = data_reports1.load_data(filename)

### Berichte anzeigen
data_reports1.show_summary(data)
data_reports1.show_largest_category(data)
