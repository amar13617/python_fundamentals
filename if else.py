#friend = "Rolf"
#user_name = input("Enter your name:")

#if user_name == friend:
#    print("Hello, friend")
#else:
#    print("Hello, stranger")
    

#name = input("Enter name")
#print(bool(name))
#if name:
#    print("I know")
 
 
friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter yout name")
if user_name in friends:
    print("Hello, Friends")
elif user_name in family:
    print("Hello , Family")
else:
    print("I don't know")
    
    
# ternary operator
x = 10
value = x if x < 10 else "Invalid value"