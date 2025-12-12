**Persönlicher Budget Tracker**


## Eingaben, Validierung und Buchungen

Dieser Teil des Projekts deckt die komplette Eingabelogik für Einnahmen und Ausgaben ab und stellt sicher, dass nur gültige Daten gespeichert werden. Der Fokus liegt auf robusten Benutzereingaben für Datum, Betrag und Kategorie sowie auf dem Erstellen und Speichern einzelner Buchungen in der passenden Monatsdatei.

Beim Hinzufügen einer Einnahme oder Ausgabe werden Datum, Kategorie und Betrag interaktiv abgefragt. Das Datum wird im Format **TT.MM.JJJJ** erwartet. Bei leerer Eingabe wird automatisch das aktuelle Datum verwendet. Der Betrag wird als Zahl geprüft, unterstützt sowohl Komma als auch Punkt als Dezimaltrennzeichen und erlaubt maximal zwei Nachkommastellen. Kategorien werden gegen eine Liste erlaubter Kategorien geprüft (`allowed_categories`), sodass keine ungültigen oder frei erfundenen Kategorien gespeichert werden können.

Die erlaubten Kategorien werden über `load_categories()` aus der Datei **kategorien.csv** geladen. Falls diese Datei nicht existiert, wird sie automatisch mit Standardkategorien über `create_default_categories()` erstellt. Dadurch bleibt das System flexibel, da Kategorien im Nachhinein direkt in der CSV-Datei erweitert oder angepasst werden können und beim nächsten Programmstart automatisch übernommen werden.

Beim Speichern einer Buchung werden aus dem eingegebenen Datum der Monat und das Jahr extrahiert. Anschliessend wird die passende Monatsdatei, zum Beispiel `budget_2025_12.csv`, geladen, der neue Eintrag als Dictionary hinzugefügt und die Datei wieder gespeichert. Einnahmen werden als positive Beträge gespeichert. Ausgaben werden im Datensatz als negative Werte abgelegt, damit spätere Auswertungen wie Saldo, Summen und Kategorien einfach berechnet werden können.
  
