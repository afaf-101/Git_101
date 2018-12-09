'''
Python Code- Factorization (verz 2)--> much more concise code
'''


'''
Formula for factorization:

n*(n-1)*(n-2)*.....

where n= user input

Below is python code for factorials:
'''

user = int(input("Please enter an integer.")) # need to convert user input to integer

#initialize variable:
output = 1 #output init

if user== 0:
    output = 1
    print(output)

elif user == 1:
    output = 0
    print(output)

else:
  while user>1:
    output=output*user
    user=user-1 # user value as counter for the while loop
  print(output)