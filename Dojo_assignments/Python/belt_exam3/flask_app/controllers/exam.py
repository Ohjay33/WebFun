from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.cars import Car
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    cars = Car.get_all_cars()

    return render_template("cars.html", cars = cars)

@app.route('/cars/new')
def new_cars():

    return render_template("new_car.html")

@app.route("/car/create", methods= ['POST'])

def create_car():

    print(request.form)
    if Car.validate_cars(request.form):
        data = {
            'price': request.form['car_price'],
            'make': request.form['car_make'],
            'model': request.form['car_model'],
            'year': request.form['car_year'],
            'description': request.form['car_description'],
            'user_id': request.form['user_id']
        }
        Car.create_cars(data)
    else:
        return redirect('/cars/new')
    return redirect('/dashboard')

@app.route('/cars/<int:cars_id>')
def single_car(cars_id):
    data = {
        'id': cars_id
    }

    cars = Car.get_cars_by_id(data)
    return render_template("single_cars.html", cars = cars)

@app.route('/cars/<int:cars_id>/edit')
def edit_cars(cars_id):
    data = {
        'id': cars_id
    }
    cars = Car.get_cars_by_id(data)
    if cars.user.id != session['user_id']:
        return redirect('/dashboard')
    return render_template('edit_cars.html', car = cars)

@app.route('/car/<int:cars_id>/update', methods = ['POST'])
def update_cars(cars_id):
    if Car.validate_cars(request.form):
        data = {
            'id': cars_id,
            'price': request.form['car_price'],
            'model': request.form['car_model'],
            'make': request.form['car_make'],
            'year': request.form['car_year'],
            'description': request.form['car_description']
        }
        Car.update_cars(data)
        return redirect("/dashboard")
    return redirect(f"/cars/{cars_id}/edit")



@app.route("/cars/<int:cars_id>/confirm_delete")
def confirm_delete_car(cars_id):
    data = {
        'id': cars_id,
    }
    cars= Car.get_cars_by_id(data)

    if cars.user.id != session['user_id']:
        return redirect('/dashboard')
    Car.delete_cars(data)

    return redirect('/dashboard')