#exception handling allow us to handle errors gracefullly without intruputinh the execution of program 
#what are exceptions?
'''ans: exceptions are those event which intrupts the noramal execution of our program 
like: zero division error
      file not found erroe
      value error
      type error
'''



#eg
'''
print(a=b)
output: "b" is not defined
if we directly write this we will get name error which looks harsh and flashy but insted if can handle it gracefully'''
try:
    a=b
except:
    print("hey, i think you have forgot to assing the value")#simple
#now we know it is a name error so we can inclued name error class to it and see the magic
try:
    a=b
except NameError as exception:
    print(exception)
#it printed the same thing but in a syntax manner



#eg
'''
suppose i have written
div=5/0 this will give me a zero division error
now lets handle it gracefully'''
try:
    div=5/0
except ZeroDivisionError as ex:
    print(ex)
    print("the values are not supposed to be divided by zero")



'''all this errors belongs from classes like
NameError exception class
ZeroDivisionError etc'''
#eg
try:
    num=int(input("enter the number of your choice: "))
    result= 20/num
except ValueError:
    print("there is a value error, please give a valid int/number")
except ZeroDivisionError:
    print("the num cannot be divided by 0, please enter a higher number")
else:
    print(f"your answer is: {result}")


'''
there is one more block like try, except, else called finally, in this block even if we face corrcet ans or erroe this block will surely executed
like you have ZeroDivision error, elecution complete, this block doesnt realy on correct or incorrect answer'''
#eg
try:
    num=int(input("enter the number of your choice: "))
    result= 20/num
except ValueError:
    print("there is a value error, please give a valid int/number")
except ZeroDivisionError:
    print("the num cannot be divided by 0, please enter a higher number")
else:
    print(f"your answer is: {result}")
finally:
    print("execution finished")



#this things can be mostly use wherever we deal with user interactions
