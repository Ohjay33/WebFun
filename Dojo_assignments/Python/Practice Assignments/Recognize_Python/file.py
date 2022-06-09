num1 = 42 # Variable initialization, integer value
num2 = 2.3 # Variable initizalization, float value
boolean = True # Boolean data type, checks if true/false
string = 'Hello World' # String data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Initializes the list "pizza_toppings"
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Initializes the dictionary "person" and creates keys
fruit = ('blueberry', 'strawberry', 'banana') # Initializes the tuple "fruit"
print(type(fruit)) #prints out the data type of "fruit"
print(pizza_toppings[1]) #prints out sausage from the list of "pizza toppings"
pizza_toppings.append('Mushrooms')
print(person['name']) # Prints "John" from the key "name" in the dictionary "person"
person['name'] = 'George' # George is the key "name" in the dictionary "person"
person['eye_color'] = 'blue' #blue is the eye color in the dictionary "person"
print(fruit[2]) #prints bannana dictionary "fruit"

if num1 > 45:             
    print("It's greater")               
else:
    print("It's lower")
    """ if variable value '42' is greater then 45 print string 'It's Greater'
    else prnt string 'It's lower' """

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

    """if the length of string datatype 'Hello World!' is less than 5  print datatype 'Its a short word!' 
    else if the length of string 'Hello World!' is greater then 15, print string datatype 'It's a long word!' 
    else print string 'Just right!' '"""

for x in range(5):
    print(x) # print the values 1-5
for x in range(2,5):
    print(x) # print the values 2-5
for x in range(2,10,3): 
    print(x) # print the values 2-3, and 3-10

x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #remove last item in the string "Olives"
pizza_toppings.pop(1) #remove item 'Sausage' from list "pizza_toppings"

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)