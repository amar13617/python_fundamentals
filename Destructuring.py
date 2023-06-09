currencies = 0.8, 1.2
usd, eur = currencies #extracting the individual values from some iterable. This process is also called destructuring


friends = [("Rolf", 25), ("Anne",37), ("Charlie",31), ("Bob", 22)]
for name, age in friends:
    print(name,age)
    
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

for index in range(len(movies)):
    print(f"{index + 1}. {movies[index][0]} ({movies[index][2]}), by {movies[index][1]}")
    

names = ["Harry", "Rachel", "Brian"]

for counter, name in enumerate(names, start = 1):
    print(f"{counter}. {name}")


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

for counter, movie in enumerate(movies, start=1):
    print(f"{counter}. {movie[0]} ({movie[2]}), by {movie[1]}")


#Exercise of destructuring.
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for character in main_characters:
    print(f"{character[0]} is a {character[2].lower()} voiced by {character[1]}.")
    
#2.

student = ("John Smith", 11743, ("Computer Science", "Mathematics"))

name, id_number, (major, minor) = student

#3

letters = ["a", "b", "c"]
numbers = [1, 2]

print(list(zip(letters, numbers)))

