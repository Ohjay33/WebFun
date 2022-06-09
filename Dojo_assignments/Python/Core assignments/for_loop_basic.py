# #  #print numbers from 0-150
# for x in range(151):  
#     print(x)


#      # Print all the multiples of 5 from 5 to 1,000
# for i in range(1, 1000):
#     if(i % 5 == 0):
#         print(i)


# #Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
# def counting_dojo():
#     for i in range (1,101):
#         if i % 5 == 0:
#             print ('Coding')
#         if i % 10 == 0:
#             print ('Dojo')
#         else:
#             print(i)
# counting_dojo()


# # Add odd integers from 0 to 500,000, and print the final sum.
# min = 0
# max = 500000
# Oddtotal = 0

# for number in range(min, max+1):
#     if(number % 2 != 0):
#         print("{0}".format(number))
#         Oddtotal = Oddtotal + number
# print("The Sum of Odd Numbers from {0} to {1} = {2}".format(min, max, Oddtotal))


# # Print positive numbers starting at 2018, counting down by fours.
# def count_down_four():
#     number = 2018
#     while number > 0:
#         print (number)
#         number = number - 4
        
# count_down_four()

# #optional
# def countdown(low, high, mult):
#     for i in range (low, high):
#         if i % mult == 0:
#             print (i)
            
# countdown(5, 100, 2)



