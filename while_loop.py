is_learning = True
while is_learning:
    print("learning")
    is_learning = False
    
is_learning = True
while is_learning:
    print("learning")
    is_learning = input("are they still learning")
    
is_learning = True
while is_learning:
    print("You are learning")
    user_input = input("They are learning")
    is_learning == user_input == "Yes"
    
user_input = input("Do you wish to run the program? (yes/no)")

while user_input == "yes":
    print("We are running")
    user_input = input("Do you wish to run the program?(yes/no)")

print("We stopped running")
    
user_input = int(input("Enter number"))
while user_input < 10:
    print("Your number was less than 10.")
    user_input = int(input("select another"))
    
print("Your number was at least 10.")

q = input("enter q")
p = input("enter p")
user_input = input("enter p or q")
while user_input != q:
    if user_input == p:
        print("Hello")
    user_input = input("enter p or q")

target_number = 40
guess = int(input("enter number"))
while guess != target_number:
    print("wrong")
    if guess > target_number:
        print("High")
    else:
        print("low")
    guess = int(input("enter number"))
print("you select a successfully")

sample_string = "Python"
for string in sample_string:
    if string == "o":
        continue
    print(string)
 
       
    

