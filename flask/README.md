# Flask

Flask is a micro web framework written in Python. It does not require particular tools or libraries like other framework. Therefore, just a few line of code can create website. Flask is suitable for small project to medium size project.

## Installation

```
pip install Flask
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
