from flask_app import app
from flask import render_template,redirect, session, request

from flask_app.models import model_player

# app = Flask(__name__)


@app.route('/player/new')
def player_new():
    return render_template("index.html", phrase="I Love you", times=10)


@app.route('/player/create', methods=['POST'])
def player_create():
    return redirect('/')

@app.route('/player/<int:id>')
def player_show(id):
    return render_template('player_show.html')


@app.route('/player/<int:id>/edit')
def player_edit(id):
    return render_template('player_edit.html')


@app.route('/player/<int:id>/update', methods=['POST'])
def player_update(id):
    return redirect('/')


@app.route('/player/<int:id>/delete')
def player_delete(id):
    return redirect('/')




if __name__ == "__main__":
    app.run(debug = True)
