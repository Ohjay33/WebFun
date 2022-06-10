from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template("index.html", phrase="I Love you", times=10)


@app.route('/dojo')
def dojo():
  return render_template("index.html", hello= "my name is oscar moore, i love coding dojo!", phrase="yesssiirrr!!", times=30)

@app.route('/say/<string:name>')
def say(name):
  return(name)


@app.route('/repeat/<int:number>/<string:name>')
def repeat(number, name):
  return f"{number*name}"




if __name__ == "__main__":
    app.run(debug = True)
