# from dataclasses import dataclass
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User


class Car():

    def __init__(self, data):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.price = data['price']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def create_cars(cls, data):
        query = "INSERT INTO cars (make, price, model, year, description, user_id) VALUES (%(make)s, %(price)s, %(model)s, %(year)s, %(description)s, %(user_id)s)"
        result = connectToMySQL("cars").query_db(query, data)
        return result

    @classmethod
    def get_all_cars(cls):
            query = "SELECT * FROM cars JOIN user ON cars.user_id = user.id;"

            result = connectToMySQL("cars").query_db(query)
            print(result)
            cars = []

            for item in result:
                new_cars = Car(item)
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
                new_cars.user = new_user
                cars.append(new_cars)
            return cars

    @classmethod
    def get_cars_by_id(cls,data):
        query = "SELECT * FROM cars JOIN user on cars.user_id = user.id WHERE cars.id= %(id)s;"

        results = connectToMySQL("cars").query_db(query, data)

        new_cars = Car(results[0])

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
        new_cars.user = new_user
        # Car.append(new_cars)


        return new_cars

    @staticmethod
    def validate_cars(data):
        is_valid = True

        if len(data['car_make']) < 1 or len(data["car_make"]) > 100:
            is_valid = False
            flash("Car make should be 1 to 100 characters")

        if len(data['car_model']) < 1 or len(data['car_model']) > 100:
            is_valid = False
            flash("Car model should be 1 to 100 characters")

        if len(data['car_year']) < 1 or len(data['car_year']) > 100:
            is_valid = False
            flash("Car year should be 1 to 100 characters")


        if len(data['car_description']) < 1 or len(data['car_description']) > 500:
            is_valid = False
            flash('Car decsription should be 1 to 500 characters long')

        if len(data['car_price']) < 1 or len(data['car_price']) > 100:
            is_valid = False
            flash('price must be greater then 1 but under 100')

        return is_valid

    @classmethod
    def update_cars(cls, data):
        query = " UPDATE cars SET make= %(make)s, price = %(price)s, model = %(model)s, year = %(year)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL("cars").query_db(query, data)

    @classmethod
    def delete_cars(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s;"

        return connectToMySQL("cars").query_db(query, data)