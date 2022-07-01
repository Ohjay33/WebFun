from flask_app.config.mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash
from flask_app import app

from flask_bcrypt import Bcrypt

class User:
    db = "paintings"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL('paintings').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        result = connectToMySQL('paintings').query_db(query,data)
        return result

    @classmethod
    def get_id(cls,data):
        query  = "SELECT * FROM user WHERE id = %(id)s;"
        result = connectToMySQL('paintings').query_db(query,data)
        if len(result) > 0:
            return cls(result[0])

    @classmethod
    def get_user(cls,data):
        query  = "SELECT * FROM user WHERE username = %(username)s;"
        result = connectToMySQL('paintings').query_db(query,data)
        if len(result) > 0:
            return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('paintings').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM user WHERE id = %(id)s;"
        return connectToMySQL('paintings').query_db(query,data)

    @staticmethod
    def validate_register(data):
        is_valid = True
        if User.get_byemail(data):
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(data['first_name']) < 3:
            flash("First name must be at least 3 characters","register")
            is_valid= False
        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 characters","register")
            is_valid= False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if data['password'] != data['confirm']:
            flash("Passwords don't match","register")
        return is_valid
        


    @classmethod
    def get_byemail(cls,data):
        query  = "SELECT * FROM user WHERE email = %(email)s"
        result = connectToMySQL('paintings').query_db(query,data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return False







    




    # @classmethod
    # def save(cls,data):
    #     query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
    #     return connectToMySQL(cls.db).query_db(query,data)

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM users;"
    #     results = connectToMySQL(cls.db).query_db(query)
    #     users = []
    #     for row in results:
    #         users.append( cls(row))
    #     return users

    # @classmethod
    # def get_by_email(cls,data):
    #     query = "SELECT * FROM users WHERE email = %(email)s;"
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     if len(results) <= 1:
    #         return False
    #     return cls(results[0])

    # @classmethod
    # def get_by_id(cls,data):
    #     query = "SELECT * FROM users WHERE id = %(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     return cls(results[0])