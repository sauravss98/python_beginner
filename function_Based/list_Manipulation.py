# 7. Write a function called listManipulation. This function should take in four parameters ( a list,
# command, location and value).
#  1. IF the command is 'remove' and the location is 'end', the function should remove the last value in the list and return the value removed.
#  2. IF the command is 'remove' and the location is 'beginning', the function should remove the first value in the list and return the value removed.
#  3. IF the command is 'add' and the location is 'beginning', the function should add the value (the 4th parameter) to the beginning of the list and return the list.
#  4. IF the command is 'add' and the location is 'end', the function should add the value (the 4th parameter) to the end of the list and return the list.

def listManipulation(lst,command,location,value):
    if command=='remove'and location=='end':
        return lst.pop()
    elif command=='remove' and location=='beginning':
        return lst.pop(0)
    elif command=='add' and location=='beginning':
        lst.insert(0,value)
        return lst
    elif command=='add' and  location=='end':
        lst.append(value)
        return lst
    else:
        print("Wrong command or location")

lst=list(input("Enter the elements: "))
print("Command")
print("1.remove")
print("2.add")
command=str(input("Enter the command to be executed: "))
print("Location")
print("1.end")
print("2.beginning")
location=str(input("Enter the location: "))
if command=='add':
    value=int(input("Enter the value to be added"))
else:
    value=0
print(listManipulation(lst,command,location,value))
