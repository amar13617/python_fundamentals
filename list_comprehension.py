numbers = [0,1,2,3,4]
double_number = []
for number in numbers:
    double_number.append(number*2)
    
print(double_number)

#list comprehension

double_number = [number *2 for number in numbers]
print(double_number) 
double_number = [number *2 for number in range(4)]
print(double_number) 

double_number = [2 for number in range(5)]
print(double_number)

friend_ages = [22,31,35,37]
age_string = [f"My friend is {age} years old." for age in friend_ages]
print(age_string)

names = ["Rolf", "Anne", "Jen", "Bob"]
lower_case = [name.lower() for name in names if name.startswith("J")]

friend = input("Enter your friend name")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friend_lower = [name.lower()for name in friends]
if friend.lower() in friend_lower:
    print(f"this is my friend {friend}")

#list comprehension allow more than two for clause
roll_combinations = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7)]
print(roll_combinations)

names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = [(name.title(), age) for name, age in zip(names, ages)]
print(people)

#person = [(name.title(), age) for name in names  for age in ages]
#print(person)

names = ["mary", "Richard", "Noah", "KATE"]
names = {name.title() for name in names}
print(names)

student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {
    student_id: name.title()
    for student_id, name in zip(student_ids, names)
}
print(students)

#Exercise of list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [number*2 for number in numbers]
print(squares)

#2
movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

movie = {key: value.title() for key, value in movie.items()}

names = ["Matthew", "John", "Helen", "Stephen", "Alexandra", "Rolf"]
short_final_n = [name for name in names if len(name) < 6 if name[-1] == "n"]

# ['John', 'Helen']