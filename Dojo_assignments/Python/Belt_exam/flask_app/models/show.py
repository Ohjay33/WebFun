from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User 
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

class Show():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.date = data['date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None


    @classmethod
    def create_show(cls, data):
        query = "INSERT INTO shows (name, date, description, user_id) VALUES (%(name)s, %(date)s, %(description)s, %(user_id)s);"
        result = connectToMySQL("Belt_exam").query_db(query, data)
        return result 

    @classmethod
    def get_all_shows(cls):
        query = "SELECT * FROM shows JOIN users ON shows.user_id =users.id;"

        result = connectToMySQL("Belt_exam").query_db(query)
        shows = []

        for item in result:
            new_show = Show(item)
            user_data = {
                'id': item['users.id'],
                'username': item['username'],
                'email': item['email'],
                'password': item['password'],
                'created_at': item['users.created_at'],
                'updated_at': item['users.updated_at']

            }
            new_user = User(user_data)
            new_show.user = new_user

            shows.append(new_show)

        return shows


    @staticmethod
    def validate_show(data):
        is_valid = True

        if len(data['show_name']) < 1 or len(data['show_name']) > 100:
            is_valid = False 
            flash("Show name must be 1 to 100 characters") 

        
        if data['show_date'] == "":
            is_valid = False
            flash("Show must have date")

        if len(data['show_description']) < 1 or len(data['show_description']) > 500:
            is_valid = False 
            flash("Show description must be 1 to 500 characters")

        return is_valid

