from flask import Flask, render_template
# import the class from friend.py
from friend import Friend

app = Flask(__name__)

# @app.route("/")
# def index():
#     # call the get all classmethod to get all friends
#     friends = Friend.get_all()
#     print(friends)
# return render_template("index.html")

# @app.route("/hello/<string>:banna>/<int:num>")
# def hello(bannana,num):
#     return render_template("hello.html", phrase= "Hello", times= 5)


@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends=friends)


# relevant code snippet from server.py
from friend import Friend
@app.route('/create_friend', methods=["POST"])
def create_friend():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
}
# We pass the data dictionary into the save method from the Friend class.
Friend.save(data)
# Don't forget to redirect after saving to the database.
return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
