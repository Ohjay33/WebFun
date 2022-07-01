# from dataclasses import dataclass
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User


class Painting():

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def create_paintings(cls, data):
        query = "INSERT INTO paintings (title, price, description, user_id) VALUES (%(title)s, %(price)s, %(description)s, %(user_id)s)"
        result = connectToMySQL("paintings").query_db(query, data)
        return result

    @classmethod
    def get_all_paintings(cls):
            query = "SELECT * FROM paintings JOIN user ON paintings.user_id = user.id;"

            result = connectToMySQL("paintings").query_db(query)
            print(result)
            paintings = []

            for item in result:
                new_paintings = Painting(item)
                user_data = {
                    'id': item['user.id'],
                    'first_name': item['first_name'],
                    'last_name': item['last_name'],
                    'email' : item['email'],
                    'password': item['password'],
                    'created_at': item['user.created_at'],
                    'updated_at': item['user.updated_at'],
                }
                new_user = User(user_data)
                new_paintings.user = new_user
                paintings.append(new_paintings)
            return paintings

    @classmethod
    def get_paintings_by_id(cls,data):
        query = "SELECT * FROM paintings JOIN user on paintings.user_id = user.id WHERE paintings.id= %(id)s;"

        results = connectToMySQL("paintings").query_db(query, data)

        new_paintings = Painting(results[0])

        user_data = {
                    'id': results[0]['user.id'],
                    'first_name': results[0]['first_name'],
                    'last_name': results[0]['last_name'],
                    'email': results[0]['email'],
                    'password': results[0]['password'],
                    'created_at': results[0]['user.created_at'],
                    'updated_at': results[0]['user.updated_at'],
        }
        new_user = User(user_data)
        new_paintings.user = new_user

        return new_paintings

    @staticmethod
    def validate_paintings(data):
        is_valid = True

        if len(data['painting_title']) < 1 or len(data['painting_title']) > 100:
            is_valid = False
            flash("PAinting title should be 1 to 100 characters")

        if len(data['painting_description']) < 1 or len(data['painting_description']) > 500:
            is_valid = False
            flash('Painting decsription should be 1 to 500 characters long')

        if len(data['painting_price']) < 1 or len(data['painting_price']) > 100:
            is_valid = False
            flash('price must be greater then 1 but under 100')

        return is_valid

    @classmethod
    def update_paintings(cls, data):
        query = " UPDATE paintings SET title= %(title)s, price = %(price)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL("paintings").query_db(query, data)

    @classmethod
    def delete_paintings(cls, data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"

        return connectToMySQL("paintings").query_db(query, data)