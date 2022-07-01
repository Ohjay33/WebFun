
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.show import Show
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/')

    shows = Show.get_all_shows()

    return render_template("shows.html", shows = shows)

@app.route('/shows/new')
def new_show():

    return render_template("new_show.html")

@app.route("/shows/create", methods=['POST'])
def create_show():
# I must validte first
    print(request.form)
    if Show.validate_show(request.form):
        data = {
            'name': request.form ['show_name'], 
            'date': request.form ['show_date'],
            'description': request.form ['show_description'],
            'user_id': session['user_id']
        }
        Show.create_show(data) 
    else:
        return redirect('/shows/new')


    return redirect('/home')
