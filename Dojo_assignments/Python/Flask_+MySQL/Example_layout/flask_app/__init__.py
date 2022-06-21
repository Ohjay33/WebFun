from flask import flask
app = flask(__name__)
app.secret_key = '123456'
DATABASE = 'schema name'