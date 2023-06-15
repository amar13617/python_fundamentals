def divide(x,y):
    if y == 0:
        return "you tried it again"
    else:
        return x/y

print(divide(10,0))

def greet(name):
    greeting = f"Hello, {name}!"
    print(greeting)

greet("Phil")

#print(globals())
names = ["Mike", "Fiona", "Patrick"]
x = 53657

def add(a, b):
    print(a, b)

print(globals())

def greet(name):
    greeting = f"Hello, {name}!"
    return (greeting)

print(greet('Phil'))

# Exercise
#1.
def exponentiate(base, exponent):
    return base ** exponent

print(exponentiate(2,3))

#2.
def process_string(name):
    return name.strip().lower()

print(process_string("AMAR"))

#3.
def dictify(actor):
    name, nationality, age = actor

    return {
        "name": name,
        "nationality": nationality,
        "age": age
    }

#4

def check_prime(number):
    
    for j in range(2,number):
        if number % j == 0:
            return False
    else:
        return True

print(check_prime(11))

