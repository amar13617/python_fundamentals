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
print(value)

#Comparison
print(5 < 10)     # True
print(5 > 10)     # False
print(10 > 10)    # False
print("A" < "a")  # True

# The ASCII code for A is 65, while a is 97


a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # 139806639351360
print(id(b))  # 139806638418944

print(a == b)  # True
print(a is b)  # False


a = [1, 2, 3]
b = a

print(id(a))  # 139685763327296
print(id(b))  # 139685763327296

print(a == b)  # True
print(a is b)  # True
