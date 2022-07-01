from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.paintings import Painting
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    paintings = Painting.get_all_paintings()

    return render_template("paintings.html", paintings = paintings)

@app.route('/paintings/new')
def new_paintings():

    return render_template("new_painting.html")

@app.route("/painting/create", methods= ['POST'])

def create_painting():

    print(request.form)
    if Painting.validate_paintings(request.form):
        data = {
            'title' : request.form['painting_title'],
            'price': request.form['painting_price'],
            'description': request.form['painting_description'],
            'user_id': request.form['user_id']
        }
        Painting.create_paintings(data)
    else:
        return redirect('/paintings/new')
    return redirect('/dashboard')

@app.route('/paintings/<int:paintings_id>')
def single_painting(paintings_id):
    data = {
        'id': paintings_id
    }

    paintings = Painting.get_paintings_by_id(data)
    return render_template("single_paintings.html", paintings = paintings)

@app.route('/paintings/<int:paintings_id>/edit')
def edit_paintings(paintings_id):
    data = {
        'id': paintings_id
    }
    paintings = Painting.get_paintings_by_id(data)
    if paintings.user.id != session['user_id']:
        return redirect('/dashboard')
    return render_template('edit_paintings.html', painting = paintings)

@app.route('/painting/<int:paintings_id>/update', methods = ['POST'])
def update_paintings(paintings_id):
    if Painting.validate_paintings(request.form):
        data = {
            'id': paintings_id,
            'title': request.form['painting_title'],
            'price': request.form['painting_price'],
            'description': request.form['painting_description']
        }
        Painting.update_paintings(data)
        return redirect("/dashboard")
    return redirect(f"/paintings/{paintings_id}/edit")



@app.route("/paintings/<int:paintings_id>/confirm_delete")
def confirm_delete_painting(paintings_id):
    data = {
        'id': paintings_id,
    }
    paintings= Painting.get_paintings_by_id(data)

    if paintings.user.id != session['user_id']:
        return redirect('/dashboard')
    Painting.delete_paintings(data)

    return redirect('/dashboard')