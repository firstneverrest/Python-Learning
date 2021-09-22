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
   ```

   Tip: project name need to be snake case like django_project

7. Run project
   ```
   python manage.py runserver
   ```

## Folder Structure

## Reference

- [ปูพื้นฐานการพัฒนา Web Application ภาษา Python ด้วย Django Framework](https://kongruksiamza.medium.com/ปูพื้นฐานการพัฒนา-web-application-กับภาษา-python-ด้วย-django-framework-9d3b7f48718a)
- [Python Django Tutorial: Full-Featured Web App Part 1 - Getting Started](https://www.youtube.com/watch?v=UmljXZIypDc)
