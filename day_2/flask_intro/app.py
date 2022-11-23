# from flask_intro import Flask

# app = Flask(__name__)

# from flask_intro.controllers import controller

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask

app = Flask(__name__)

from controllers import controller

if __name__ == '__main__':
    app.run(debug=True)