from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def page():
    return render_template("checkerboard.html")

@app.route('/4')
def page():
    return render_template("checkerboard2.html")

@app.route('/<rows>/<columns>')
def changeSquares(rows, columns):
    return render_template("checkerboard3.html", rows=int(rows), columns=int(columns))







if __name__ == "__main__":
    app.run(debug=True)
