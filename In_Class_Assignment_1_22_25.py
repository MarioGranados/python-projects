import random
from functools import reduce
#Java and js have reduce functions/methods so i looked up pythons version
#reduce can be used to add all numbers in an array

#function to add current, to next variable then the sum is added to the next variable and so forth
#this function just adds x + y, the rest will be done by the reduce method
def add(x,y):
    return x + y

#main program
def main():
    #I need an empty list
    numbers = []
    #create 10 random ints and add it to our list via append() method
    for i in range(10):
        numbers.append(random.randint(0,10))
    #print the array for the user 
    print('the list of numbers are: ', numbers)
    #reduce method uses the add() function takes the varibles in the array and adds it to the next.
    # For example, it will begin by adding numbers[0] + numbers[1], then ((numbers[0] + numbers[1]) + numbers[2], and so on.
    sum = reduce(add, numbers)
    #print the sum
    print('the sum is: ',sum)
        
main()