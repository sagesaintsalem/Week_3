# from flask_intro import render_template # ADDED
# from flask_intro import app
# from models.todo_list import tasks

# @app.route('/tasks')
# def index():
#     return render_template('index.html', title='Home', tasks=tasks)

from app import app

@app.route('/')
def index():
    return "Hello World!"

@app.route('/<name>')
def greet(name):
    return f'Hello {name}!'