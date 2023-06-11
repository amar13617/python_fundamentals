friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]
friends_lower = set([f.lower() for f in friends])
#print(friends_lower)
guest_lower = set([g.lower() for g in guests])
#print(guest_lower.intersection(friends_lower))

present_friends = [
    name.title() for name in guests if name.lower() in [f.lower() for f in friends]
]
print(present_friends)



    
def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(cube, numbers))

print(cubed_numbers)

def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)
print(cubed_numbers)

for number in cubed_numbers:
    print(number)
    
def is_even(number):
    return number%2 == 0

number = [22,34,66,33,21]
numbers = filter(is_even, number)

for numb in numbers:
    print(numb)
    
#Exercise
def line_stripper(line):
    return line.strip()

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",  
    "    Couldn't put Humpty together again."
]

print(*map(line_stripper, humpty_dumpty), sep="\n")

#2
names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
name_list = [name.title() for name in names if len(name)<8]
print(name_list)

#3
def is_positive(number):
    return number>= 0

numbers = filter(is_positive, range(-5,11))
print(numbers)

for numb in numbers:
    print(numb)
