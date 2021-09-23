# Django

Django is a high-level Python web framework. [Visit official website to get more information](https://www.djangoproject.com/).

## Virtualenv

Virtualenv is a tool to create isolated Python environments which solve the different version of Python problem.

1. Install virtualenv package

   1. For windows

      ```
      pip install virtualenvwrapper-win
      ```

   2. For Linux
      ```
      pip install virtualenvwrapper
      ```

2. Create a new virtualenv (open cmd for windows)

   ```
   mkvirtualenv py1
   ```

3. Work on that virtualenv (it will show (py1) at the front)

   ```
   workon py1
   ```

4. Install Django package

   ```
   pip install django
   ```

5. Check Django version

   ```
   python -m django --version
   ```

   To show all subcommand of django, use `django-admin`

6. Create a new Django project

   ```
   django-admin startproject <project_name>
   cd <project_name>
   ```

   Tip: project name need to be snake case like django_project

7. Run project
   ```
   python manage.py runserver
   ```

## Folder Structure

- `manage.py` - script file for running Django command such as run server, collectstatic and model & migration.
- `__init__.py` - initial file for storing Python package. You can add other script file into this file.
- `settings.py` - config project such as path, database, etc.
- `urls.py` - store routing of HTTP request to define Django project's url pattern
- `wsgi.py` - Web Server Gateway Interface (WSGI) describes the way how servers interact with the applications in production environment. The task is to import middleware according to the server.
- `asgi.py` - Asynchronous Server Gateway Interface (ASGI) is similar to WSGI but has more additional functionality.

## MVT (Model-View-Template)

- Model - communicate with database
- View - work as a controller like processing data and command and send to template
- Template - the application UI

## Reference

- [ปูพื้นฐานการพัฒนา Web Application ภาษา Python ด้วย Django Framework](https://kongruksiamza.medium.com/ปูพื้นฐานการพัฒนา-web-application-กับภาษา-python-ด้วย-django-framework-9d3b7f48718a)
- [Python Django Tutorial: Full-Featured Web App Part 1 - Getting Started](https://www.youtube.com/watch?v=UmljXZIypDc)
