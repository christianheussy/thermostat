from database import db_session
from flask import Flask, render_template
from controller import Controller
from utils.appstate import AppState


app = Flask(__name__)

appstate = AppState()
controller = Controller(db_session, appstate)

controller.start_controller()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
