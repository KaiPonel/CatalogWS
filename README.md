# DJANGO-Based Web-App for item management
- This project encompasses a complete web app for cataloging items.
- A client can create, edit, delete, and search/sort items.
- The website is protected by an authentication process, meaning all pages except the homepage can only be accessed with a login.

## Used Techniques
- Python
- [Django](https://www.djangoproject.com/) (Python web framework)
- HTML, CSS, JS, Bootstrap4
- SQLite (Embedded in Django)
- Apache (For local server hosting)

## Description
The project is divided into individual apps. These apps are limited to specific tasks, allowing encapsulation. This keeps the program easy to maintain. The project is divided into three apps:
- `items`
- `login`  
- `pages` (All operations that do not require a database)

For more information on building a web application using Django, see the official [Django Documentation](https://docs.djangoproject.com/en/3.2/intro/overview/)

## Disclaimer
- This project is designed for a single, very specific use case. No further work on the project from the original contributer is planned. 
- For different usecases, the attributes in `items` need to be modified.
- Sensitive data such as the contents of the database or the Django Secret-Key have been removed. All places in the code that have been changed are marked accordingly.

## Demo
- Since the website is currently only hosted locally, a live demo is not possible at this time.
