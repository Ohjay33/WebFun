# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
DATABASE = 'sports_db'

class friends:
    def __init__( self , data ):
    # Every column in DB has to have an attribute ie['first_name]
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # C


    # R

# Now we use class methods to query our database
@classmethod
def get_all(cls):
        query = "SELECT * FROM friends;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
    # Create an empty list to append our instances of friends
        if results:
            all_playes =[]
        all_friends = []
    # Iterate over the db results and create instances of friends with cls.
        for dict in results:
            all_friends.append( cls(dict) )
        return all_friends
        return []



    # U


    # D

# Now we use class methods to query our database
@classmethod
def get_all(cls):
        query = "SELECT * FROM friends;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
    # Create an empty list to append our instances of friends
        friends = []
    # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends

