# Persönlicher Budget Tracker

Ein konsolenbasiertes Python-Programm zur Verwaltung persönlicher Finanzen. Benutzer können passwortgeschützt Einnahmen und Ausgaben verwalten, monatliche Statistiken einsehen und den Budgetplan speichern. Das Projekt wurde im Rahmen eines Assessments nach didaktischen Vorgaben umgesetzt. 

## Eingaben, Validierung und Buchungen

Dieser Teil des Projekts deckt die komplette Eingabelogik für Einnahmen und Ausgaben ab und stellt sicher, dass nur gültige Daten gespeichert werden. Der Fokus liegt auf robusten Benutzereingaben für Datum, Betrag und Kategorie sowie auf dem Erstellen und Speichern einzelner Buchungen in der passenden Monatsdatei.

Beim Hinzufügen einer Einnahme oder Ausgabe werden Datum, Kategorie und Betrag interaktiv abgefragt. Das Datum wird im Format **TT.MM.JJJJ** erwartet. Bei leerer Eingabe wird automatisch das aktuelle Datum verwendet. Der Betrag wird als Zahl geprüft, unterstützt sowohl Komma als auch Punkt als Dezimaltrennzeichen und erlaubt maximal zwei Nachkommastellen. Kategorien werden gegen eine Liste erlaubter Kategorien geprüft (`allowed_categories`), sodass keine ungültigen oder frei erfundenen Kategorien gespeichert werden können.

Die erlaubten Kategorien werden über `load_categories()` aus der Datei **kategorien.csv** geladen. Falls diese Datei nicht existiert, wird sie automatisch mit Standardkategorien über `create_default_categories()` erstellt. Dadurch bleibt das System flexibel, da Kategorien im Nachhinein direkt in der CSV-Datei erweitert oder angepasst werden können und beim nächsten Programmstart automatisch übernommen werden.

Beim Speichern einer Buchung werden aus dem eingegebenen Datum der Monat und das Jahr extrahiert. Anschliessend wird die passende Monatsdatei, zum Beispiel `budget_2025_12.csv`, geladen, der neue Eintrag als Dictionary hinzugefügt und die Datei wieder gespeichert. Einnahmen werden als positive Beträge gespeichert. Ausgaben werden im Datensatz als negative Werte abgelegt, damit spätere Auswertungen wie Saldo, Summen und Kategorien einfach berechnet werden können.
  



# Budget-Daten-Analyse-Skript

## Kurzbeschreibung

Dieses Python-Skript (`data_reports1.py`) dient zur Verwaltung und Analyse von Budgetdaten, die im CSV-Format gespeichert sind. Es ermöglicht das Laden, Speichern und Auswerten von Finanztransaktionen (Einnahmen und Ausgaben).

**Funktionen**

Das Skript bietet folgende Hauptfunktionen:

## Dateifunktionen

**`get_budget_filename(month, year)`**: Erzeugt einen standardisierten Dateinamen (z. B. `budget_2024_05.csv`).
**`load_data(filename)`**: Liest eine CSV-Datei ein. Die Datei muss die Spalten `Datum`, `Typ`, `Kategorie` und `Betrag` enthalten. Der `Betrag` wird automatisch in eine Fliesskommazahl umgewandelt.
**`save_data(filename, data)`**: Speichert eine Liste von Transaktionen in eine CSV-Datei.

## Auswertungsfunktionen

**`show_summary(data)`**: Berechnet die Summe aller Einnahmen (positive Beträge) und Ausgaben (negative Beträge) sowie den aktuellen Saldo und gibt diese auf der Konsole aus.
**`show_largest_category(data)`**: Ermittelt die Kategorie mit den höchsten Gesamtausgaben und zeigt diese an.
**`show_month_entries(data, month, year)`**: Filtert die Transaktionen nach einem bestimmten Monat und Jahr und gibt diese tabellarisch aus.

## Hilfsfunktionen

**`parse_month_year(datum_str)`**: Extrahiert Monat und Jahr aus einem Datumsstring im Format `TT.MM.JJJJ`.

## Datenstruktur

Die CSV-Dateien und internen Datenstrukturen verwenden folgendes Format:

**Datum**: String (Format: `TT.MM.JJJJ`, z.B. "01.05.2024")
**Typ**: String (z.B. "Einnahme", "Ausgabe")
**Kategorie**: String (z.B. "Essen", "Gehalt", "Transport")
**Betrag**: Float (Positiv für Einnahmen, Negativ für Ausgaben)

## Installation & Voraussetzungen

*   Python 3.x
*   Keine externen Bibliotheken erforderlich (nutzt nur Standard-Bibliotheken `csv`, `collections`, `datetime`).

## Verwendung

Das Skript kann direkt ausgeführt werden, um die integrierte Testfunktion zu starten, oder als Modul importiert werden.

## Direktes Ausführen (Demo)

Führe das Skript in der Konsole aus:


python data_reports1.py


Dies führt die Funktion `test_functions()` aus, welche Beispieldaten erstellt, speichert, wieder lädt und die Berichte anzeigt.

## Als Modul importieren


import data_reports1

## Dateinamen bestimmen
filename = data_reports1.get_budget_filename(5, 2024)

## Daten laden
data = data_reports1.load_data(filename)

## Berichte anzeigen
data_reports1.show_summary(data)
data_reports1.show_largest_category(data)

## Projektstruktur

personlicher-budget-tracker/

│


├── main.py                  # Programmstart, Menü, Steuerlogik

├── login.py                 # Passwort-Handling, Login, Hashing

├── budgetfunctions.py       # Eingaben (Einnahmen, Ausgaben)

├── data_reports.py          # Auswertungen und Monatsanzeigen

├── validationfunctions.py   # Prüfung von Datum, Betrag, Kategorie

│

├── kategorien.csv           # Liste gültiger Kategorien

├── passwort.csv             # Passwort (verschlüsselt)

├── budget_2025_12.csv       # Beispielhafte Monatsdatei

└── README.md                # Diese Datei
