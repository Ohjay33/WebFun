from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World i made it!'  # Return the string 'Hello World!' as a response

    
@app.route('/success')
def success():
  return "success baby!" 

@app.route('/hello/<banana>/<int:num>') 
def hello(banana,num):
    return render_template("hello.html",banana=banana, num=num)

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
    {'name' : 'Michael', 'age' : 35},
    {'name' : 'John', 'age' : 30 },
    {'name' : 'Mark', 'age' : 25},
    {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)
    # i am passing in to (lists.html) some "random numbers" and a list of students from student info; 

@app.route('/user') 
def users ():
    users_list = [
   {'first_name' : 'Michael', 'last_name' : 'Choi', 'full_name':'Michael Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name': 'John Susupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name': 'Mark Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel', 'full_name': 'KB Tone1'},
]

    return render_template("user.html", users = users_list)


    








if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



