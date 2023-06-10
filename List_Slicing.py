slice_instance = slice(0, 2)
x = [1, 2, 3, 4, 5]
print(x[slice_instance])

#Negative step index
t = (1, 2, 3, 4, 5)
print(t[4:2:-1])  # (5, 4)

#warning about negative index
t = (1, 2, 3, 4, 5)
print(t[1:4:-1])  # ()  <- Empty tuple


t = (1, 2, 3, 4, 5)
print(t[-1:-5:-1])  # (5, 4, 3, 2)

numbers = [1, 3, 3]
numbers[1:2] = [2]

print(numbers)  # [1, 2, 3]

#Assigning for multiple value
numbers = [1, 3, 5]
numbers[1:3] = [2, 3]

print(numbers)  # [1, 2, 3]

numbers = [1, 3, 5]
numbers[1:3] = [2, 3, 4, 5]

print(numbers) # [1, 2, 3, 4, 5]

#Zero length slice
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]

print(numbers)  # [1, 2, 3, 4, 5]


numbers = [1, 3, 3, 5, 5]
numbers[1:4:2] = [2, 4]

print(numbers)  # [1, 2, 3, 4, 5]

#numbers = [1, 3, 3, 5, 5]
#numbers[1:3:2] = [2, 4]

#print(numbers)  # ValueError

d = numbers.__getitem__(slice(1, 3))

print(d)  # [2, 3]

numbers = [1, 2, 3, 4, 5]

print(numbers[2])  # 3
print(numbers.__getitem__(2))  # 3

friends = ["Rolf", "John", "Mary"]
friends_reversed = friends[::-1]
print(friends_reversed)  # ['Mary', 'John', 'Rolf']

greet = "Hello, World!"
print(greet[::-4])  # "!dlroW ,olleH"
