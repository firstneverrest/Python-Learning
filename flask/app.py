from django.shortcuts import render
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/about')
def about(): 
    return render_template('about.html')

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

if __name__ == '__main__':
    app.run()