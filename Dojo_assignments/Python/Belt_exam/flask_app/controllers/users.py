from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/home')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/login',methods=['POST'])
def login():
    data= {
        "email": request.form['email'],
        "password": request.form['password']
    }
    user = User.get_byemail(data)
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    session['user_email'] = user.email
    session['username'] = user.username
    return redirect('/home')


    

# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data ={
#         'id': session['user_id']
#     }
#     user = User.get_one(data)
#     return render_template("shows.html",user=user)