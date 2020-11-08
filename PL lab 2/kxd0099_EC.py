# Name : Karun Dawadi 
# Student ID : 1001660099
# Date turned in : November 8, 2020

import os as operating_system

# implementaing a stack
stack = []

#For output
output = []
text_file_location = operating_system.getcwd()+"/input_RPN_EC.txt"
test_file = open(text_file_location,'r')
try:
    # All the contents of the file are transfeered to a list file_contents
    file_contents = test_file.readlines()
finally:
    test_file.close()

# For individual line 
for i in file_contents:
    i = i.rstrip("\n") #Removing the \n
    i = i.split(" ") # Splitting with white line
    # Pushing to stack 
    for j in i:
        if j.isnumeric() :
            output.append(float(j))
        elif j == ' ' :
            continue
        elif j == '\n' :
            continue
        # Comparing if the value are the operators
        elif (j == '+' or j == '+' or j == '-' or j == '*' or j == '/') :
            if len(stack) == 0 :
                stack.append(j)
            else :
                output.append(stack.pop())
            
        else :
            continue

print(output)