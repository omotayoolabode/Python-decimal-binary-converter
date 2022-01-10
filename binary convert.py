# collect input from user
import math
first_input = int(input("Please enter the first number :")) 
second_input = int(input("Please enter the second number :"))
# add two numbers
add = first_input + second_input
print ("The addition of the two numbers gives %s" %add)
# convert to binary
for num in range(10):
    prompt = input("would you like to convert to binary?(Yes/no)")
    if prompt.lower() == "yes":
        binary = bin(add)
        print ("The binary representation is :" +binary)
        break
    elif prompt.lower() == "no":
        print("Thanks")
        break
    else:
        print("Invalid input")