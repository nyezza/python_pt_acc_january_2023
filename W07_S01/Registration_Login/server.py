from flask_app import app

# !  DO NOT FORGET TO IMPORT ALL CONTROLLERS
from flask_app.controllers import users
if __name__ == '__main__':
    app.run(debug=True)