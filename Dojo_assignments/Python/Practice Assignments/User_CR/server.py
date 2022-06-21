from flask import Flask, render_template, request, redirect

from user import User

app=Flask(__name__)

# @app.route('/')
# def index():
#     # return redirect('/users')
#     return render_template("read.html")

@app.route('/')
def users():
    return render_template("read.html",users=User.get_all())

@app.route('/create',methods = ("Get", "Post"))
def create():
    # return redirect('/')
    return render_template("create.html")


if __name__=="__main__":
    app.run(debug=True)