# This changes location//
from flask import app
from flask_app.controllers import controller_routes, controller_table_name
app = Flask(__name__)
# our index route will handle rendering our form

# @app.route('/')
# def index():
#     return render_template("index1.html")


if __name__ == "__main__":
    app.run(debug=True)