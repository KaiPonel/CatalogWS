# Katalog WebApp
- Dieses Projekt umfasst eine komplette Web-App zum katalogisieren von Gegenständen. 
- Ziel war es, dass ein authentifizierten Client Gegenständen erstellen, bearbeiten, löschen und nach ihnen Suchen/Sortieren kann.
- Die Website ist durch ein Authentifizierungsprozess geschützt, was beudetet dass alle Seiten bis auf die Startseite nur mit einem Login eingesehen werden können.

## Verwendete Techniken
- Python 
- [Django](https://www.djangoproject.com/) (Python Web-Framework)
- HTML, CSS, JS, Bootstrap4
- SQLite (In Django eingebettet)

## Beschreibung
Das Projekt ist in einzelne Apps unterteilt. Diese Apps sind auf einzelne Aufgaben beschränkt, was eine Abkapselung erlaubt. Dadurch bleibt das Programm einfach zu Warten. Das Projekt gliedert sich in 3 Apps:
- items (Alle Operationen bezogen auf Gegenstände)
- login (Alle Operationen bezogen auf Benutzer)
- pages (Alle Operationen welche keine Datenbank benötigen)

## Disclaimer
- Dieses Projekt Entstand für einen einzigen, sehr speziellen Anwendungsfall. Soll der Anwendungsfall angepasst werden, müssen die Attribute in der App "items" angepasst werden. 
- Sensitive Daten wie bspw. die Inhalte der Datenbank oder der Django Secret-Key wurden entfernt. Alle im Code veränderten Stellen wurden dementsprechend makiert. 
