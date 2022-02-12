# Flask

Flask is a micro web framework written in Python. It does not require particular tools or libraries like other framework. Therefore, just a few line of code can create website. Flask is suitable for small project to medium size project.

## Installation

```
pip install Flask

python app.py
```

## Create web server

```py
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()
```

## Dynamic Routing

```py
@app.route('/user/<username>')
def user(username):
    return '<b>User: {} </b>'.format(username)

```

## Debug mode

In default mode, debug mode is off to prevent other users see server code. Therefore, if some mistake occur, the user would see 500 internal error. However, you can turn it on when you are developing flask server. Debug mode helps logging error message to make you more understand about the error instead of 500 internal error message.

```py
# app.py
if __name__ == '__main__':
    app.run(debug=True)
```

## Template

Template is a user interface of your application including HTML. Jinja2 template is a template for Flask framework that enable inserting Python code in HTML.

## Send data to template

```py
# app.py
@app.route('/blog/<username>')
def blog(username):
    blogs = [
        {
            "title": "Cryptocurrency in the future",
            "author": "Chitsanupong",
        },
        {
            "title": "How to build a blockchain",
            "author": "Chitsanupong",
        }
    ]
    return render_template('blog.html', username=username, blogs=blogs)

```

```html
# blog.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="../static/global.css" />
    <link rel="stylesheet" href="../static/blog.css" />
    <title>Flask</title>
  </head>
  <body>
    <div class="container">
      <h1>Blog</h1>
      <p class="blog-description">These are blogs from {{username}}</p>
      <ul class="items-container">
        {% for blog in blogs %}
        <li>
          {{blog.title}} : {{blog.author}}
        </li>
        {% endfor %}
    </div>
  </body>
</html>

```
