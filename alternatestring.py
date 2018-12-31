
#Method that returns alternate characters of a string

def alternate(user):
    idx = 0
    output = ""
    len_string = len(user)

    while idx < len_string:
      if idx % 2 == 0:  # to alternate another way: "if idx % 2 != 0"
        output = output + user[idx]
      idx = idx+1
    return output

user = input("Please enter a string")

print(alternate(user))