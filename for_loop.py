students = [
    {"name": "Rolf", "grade":90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade":80}
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    
    print(f"{name} has got a grade {grade}")
    
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for movie in movies:
    movie = movies[0]
    print(f"{movie[0]}, {movie[2]}, by {movie[1]}")
    
    if movie[0] == "Requiem for a Dream":
        print("Requiem for a Dream is in the movie library!")
        break

# For loop exercise in python
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for employee in employees:
    total = employee[1]*employee[2]
    print(total)
    
total = 0
count = 0
for employee in employees:
    total = total + employee[2]
    count = count + 1
    
average = total/count
print(average)

for employee in employees:
    if employee[2]> average:
        print(employee[0])
        

#For Loop Project Problem

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)