from flask import Flask
app = Flask(__name__)



@app.route('/hello/<name>') 
def hello(name):
    print(name)
    return "Hello, " + name


@app.route('/hello/<int:number>/<string:name>')
def repeat(number, name):
  return f"{number*name}"



if __name__ == "__main__":
    app.run(debug=True)
