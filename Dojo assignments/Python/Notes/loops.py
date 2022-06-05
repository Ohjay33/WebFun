#Basic - Print all integers from 0 to 150. Hint:use a for loop and range
for i in range(0,151,1):
    print(i)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000   
for i in range(5,1000,1):
    print(i*5)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def counting_dojo():
    for i in range (1,101,1):
        if i % 5 == 0:
            print ('Coding')
        if i % 10 == 0:
            print ('Dojo')
counting_dojo()

# Add odd integers from 0 to 500,000, and print the final sum.
minimum = 0
maximum = 500000
Oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
        
count_down_four()   

#Flexible Counter (optional) - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flex_countdown(low, high, mult):
    for i in range (low, high):
        if i % mult == 0:
            print (i)
            
flex_countdown(2, 9, 3)

