from flask import render_template, redirect, session, request, flash
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

    return render_template("paintings.html", paintings=paintings)


@app.route('/paintings/new')
def new_paintings():

    return render_template("new_painting.html")


@app.route("/paintings/create", methods=['POST'])
def create_painting():

    print(request.form)
    if Painting.validate_show(request.form):
        data = {
            'title': request.form['paintings_tite'],
            'price': request.form['paintings_price'],
            'description': request.form['paintings_description'],
            'user_id': request.form['paintings_id']
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

    paintings = paintings.get_paintings_by_id()
    return render_template("sngle_painting.html", paintings=paintings)


@app.route('/paintings/int: paintings_id/edit')
def edit_paintings(paintings_id):
    data = {
        'id': paintings_id
    }
    paintings = paintings.get_show_by_id(data)

    if paintings.user.id != session['user_id']:
        return redirect('/dashboard')

    if paintings.validate_paintings():
        data = {
            'id': paintings_id,
            'title': request.form['paintings_name'],
            'price': request.form['paintings_price'],
            'description': request.form['paintings_description']
        }
        paintings.update_paintings(data)
    
    else:
        return redirect(f'/paintings/{paintings_id}/edit')

    return render_template('edit_paintings.html', paintings = paintings)

# @app.route('paintings/<int:paintings_id>/update')
#     def update_paintings(paintings_id):


@app.route("/paintings/<int:paintings_id>")
def id_painting(paintings_id):

    if Painting.user.id != session['user_id']:

        return redirect('/dashboard')

    return render_template("paintings_delete.html", paintings=Painting)

# @app.route("/paintings/<int: paintings_id>/confirm_delete")
# def confirm_delete_painting(paintings_id):
#     data = {
#         'id': paintings_id,
#     }
#     paintings= paintings.get_paintings_by_id(data)

#     if paintings.user.id != session['user_id']:
#         return redirect('/dashboard')
#     paintings.delete_show(data)

#     return redirect('/dashboard')