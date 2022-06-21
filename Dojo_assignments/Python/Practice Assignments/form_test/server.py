from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("form.html")
if __name__ == "__main__":
    app.run(debug=True)


            
@app.route('/users', methods=['POST'])  # Must provide a value for methods "POST"
def create_user():
    print("Got Post Info")
    print(request.form)
    return redirect('/')

# Never render a template on a POST request.
# Instead we will redirect to our index route.

