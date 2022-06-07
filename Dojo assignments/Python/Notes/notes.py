# import random
# print(random.randint(1,10)) # provides a random number between 2 and 5
#            # Syntax
# #List[]
# #tuple()
# #dictionary{}

#  <                       #List of  Methods
#  list.extend(list2)      # adds all values from a second sequence to the end of the original sequence.
# list.pop(index)    #remove a value at given position. if no parameter is passed, defaults to final value in the list.
# list.index(value)     # returns the index position in a list for the given parameter.


"""# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)
be_cheerful()    # output: good morning (repeated on 2 lines)
be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)"""





def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2


