# Katalog WebApp
- Dieses Projekt umfasst eine komplette Web-App zum Katalogisieren von Gegenständen.
- Ein Client kann Gegenständen erstellen, bearbeiten, löschen und nach ihnen Suchen/Sortieren.
- Die Website ist durch ein Authentifizierungsprozess geschützt, was bedeutet dass alle Seiten bis auf die Startseite nur mit einem Login eingesehen werden können.

## Verwendete Techniken
- Python
- [Django](https://www.djangoproject.com/) (Python Web-Framework)
- HTML, CSS, JS, Bootstrap4
- SQLite (In Django eingebettet)
- Apache (Für lokales Serverhosting)

## Beschreibung
Das Projekt ist in einzelne Apps unterteilt. Diese Apps sind auf einzelne Aufgaben beschränkt, was eine Abkapselung erlaubt. Dadurch bleibt das Programm einfach zu Warten. Das Projekt gliedert sich in drei Apps:
- items (Alle Operationen bezogen auf Gegenstände)
- login (Alle Operationen bezogen auf Benutzer)
- pages (Alle Operationen welche keine Datenbank benötigen)

Für mehr Informationen zum Aufbau einer Web-Application mithilfe von Django, siehe [hier](https://docs.djangoproject.com/en/3.2/intro/overview/)

## Disclaimer
- Dieses Projekt ist für einen einzigen, sehr speziellen Anwendungsfall konzipiert worden. 
- Soll der Anwendungsfall angepasst werden, müssen die Attribute in der App "items" angepasst werden.
- Sensitive Daten wie bspw. die Inhalte der Datenbank oder der Django Secret-Key wurden entfernt. Alle im Code veränderten Stellen wurden dementsprechend markiert.

## Demo
- Da die Website zurzeit nur lokal gehostet wird, ist eine Live-Demo zu diesem Zeitpunkt leider nicht möglich.
