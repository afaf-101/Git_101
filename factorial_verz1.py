'''
Python Code- Factorization (verz 1)-- more explicit code
'''



'''
Formula for factorization:

n*(n-1)*(n-2)*.....

where n= user input

Below is python code for factorials:
'''

# user input value

user = int(input("Please enter an integer.”)) # converts user input to integer

#initialize variables

output = 1 # init output
x = 1 # init counter

if user == 0:  # if user input is equal to 0
    output = 1  # then output should be 1

elif user == 1:  # if user input is equal to 1
    output = 0  # then output should be zero

elif user == 2: # if user input is equal to 2
    output = user * (user - x)  
# then output should be user input times user input minus one

else: # if user input is a number other than 0, 1, or 2, then…

    output = output * user  
#makes up the first part of the equation, n(n-1) calculated only once

    while x!= user: 
#makes up the second part of the equation, (n-x) calculated  according to user's value and counter x

        output = output * (user-x)
        x += 1 

print(output)