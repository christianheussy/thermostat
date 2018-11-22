from database import db_session
from flask import Flask, render_template
from controller import Controller
from utils.appstate import AppState

from flask_wtf import Form
from wtforms import SubmitField


app = Flask(__name__)
app.secret_key = '99a98vjkndJNkjn'

appstate = AppState()
controller = Controller(db_session, appstate)

controller.start_controller()


class ControlForm(Form):
    auto_btn = SubmitField()
    on_btn = SubmitField()
    off_btn = SubmitField()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ControlForm()
    temp = controller.temp
    relay = appstate.heat_on

    if form.validate_on_submit():
        if form.auto_btn.data:
            appstate.set_auto()
        elif form.on_btn.data:
            appstate.set_manual_on()
        elif form.off_btn.data:
            appstate.set_manual_off()


    return render_template('index.html',temp=temp,relay=relay,form=form)


if __name__ == '__main__':
    app.run()
