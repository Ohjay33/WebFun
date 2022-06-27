from flask_app.models import burger
from flask_app.config.mysqlconnection import connectToMySQL
# burger.py


class Burger:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# burger.py...
# gets all the burgers and returns them in a list of burger objects

@classmethod
def get_all(cls):
	query = "SELECT * FROM burgers"
	burgers_from_db = connectToMySQL('burgers').query_db(query)
	burgers = []
	for b in burgers_from_db:
		burgers.append(cls(b))
	return burgers


# We will need to import burger.py to access the class


class Topping:
    def __init__(self, db_data):

        self.id = db_data['id']
        self.topping_name = db_data['topping_name']
# we need have a list in ="keyword from-rainbow">case we want to show which burgers are related to the topping.
        self.on_burgers = []
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']


@classmethod
def save(cls, data):
    query = "INSERT INTO toppings ( topping_name, created_at , updated_at ) VALUES (%(topping_name)s,NOW(),NOW());"
    return connectToMySQL('burgers').query_db(query, data)
# This method will retrieve the specific topping along with all the burgers associated with it.

@classmethod
def get_topping_with_burgers(cls, data):
        query = "SELECT * FROM toppings LEFT JOIN add_ons ON add_ons.topping_id = toppings.id LEFT JOIN burgers ON add_ons.burger_id = burgers.id WHERE toppings.id = %(id)s;"
        results = connectToMySQL('burgers').query_db(query, data)
        # results will be a list of topping objects with the burger attached to each row.
        topping = cls( results[0] )
        for row_from_db in results:
        # Now we parse the topping data to make instances of toppings ="keyword from-rainbow">and add them into our list.
           burger_data = {
               "id" : row_from_db["burgers.id"],
               "name" : row_from_db["name"],
"bun" : row_from_db["bun"],
"calories" : row_from_db["calories"],
               "created_at" : row_from_db["toppings.created_at"],
               "updated_at" : row_from_db["toppings.updated_at"]
           }
           topping.on_burgers.append( burger.Burger( burger_data ) )
        return topping





# We need to import the topping class from our models
from flask_app.models import topping
class Burger:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated']
# We now create a list so that later we can add in all the topping objects that relate to a burger.
        self.toppings = []
# This method will retrieve the burger with all the toppings that are associated with the burger.
    @classmethod
    def get_burger_with_toppings( cls , data ):
        query = "SELECT * FROM burgers LEFT JOIN add_ons ON add_ons.burger_id = burgers.id LEFT JOIN toppings ON add_ons.topping_id = toppings.id WHERE burgers.id = %(id)s;"
    results = connectToMySQL('burgers').query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
    burger = cls( results[0] )
        for row_from_db in results:
# Now we parse the topping data to make instances of toppings and add them into our list.
            topping_data = {
                "id" : row_from_db["toppings.id"],
                "topping_name" : row_from_db["topping_name"],
                "created_at" : row_from_db["toppings.created_at"],
                "updated_at" : row_from_db["toppings.updated_at"]
            }
            burger.toppings.append( topping.Topping( topping_data ) )
        return burger
