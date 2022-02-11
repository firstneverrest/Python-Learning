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
