from flask import Flask

app = Flask(__name__)

@app.route('/')
def index(): 
    return '<h1>Hello World!</h1>'

@app.route('/about')
def about(): 
    return '<h1>About me</h1>'

@app.route('/user/<username>')
def user(username):
    return '<b>User: {} </b>'.format(username)

if __name__ == '__main__':
    app.run()