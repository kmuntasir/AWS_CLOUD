import random as r

def read(prompt):
    return input(prompt)

def generate(first,last,howmany):
    return r.sample(range(first,last),howmany) 

#Generate random Student IDs of 3-digit size as keys
def create_dict():
    names = {} #empty dictionary
    first = int(read("First = "))
    last = int(read("Last = "))
    howmany = int(read("How many = "))
    keys = generate(first,last,howmany) #list of student IDs
    for key in keys:
        names[key] = read("Name = ")
    return names 
    
    
# this function will sort the dictionary by ID
def sort(dicts):
    for key in sorted(dicts.keys()):
        print("%s :: %s"%(key,dicts[key]))
        

# delete funtion will remove an item in the
# dictionary by ID
def delete():
    new_dict = create_dict()
    print(new_dict)
    print("Please enter ID to remove the user : ")
    ID = int(read("ID = "))
    # Using dictionary comprehension
    for key in [key for key in new_dict if key == ID]: 
        del new_dict[key]
    return print("Updated list:",new_dict)

# Update_dict function will update dictinary 
#by inserting an item using built in update method
def update_dict():
    new_dict = create_dict()
    print(new_dict)
    print("Please enter the ID to insert : ")
    ID = int(read("ID = "))
    print("Please enter the Name to insert : ")
    Name = str(read("Name = "))
    new_dict.update({ID:Name})
    return print (new_dict)


    
    
#Task 1: Define a function that deletes an element from the dictionary 
#Task 2: Define a function that updates an element in a dictionary
#Task 3: use the above two functions in the dictionaryOps main()
