from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!!!!!'

@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<string:me>')
def say(me):
  return "Hi" + me


@app.route('/repeat/<int:x>/<string:y>')
def repeat(x, y):
  return f"{x*y}"








if __name__ == "__main__":
    app.run(debug = True)
