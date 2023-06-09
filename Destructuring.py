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


# Project of Destructuring in python

card_number = list(input("Please enter a card number: ").strip())

# Remove the last digit from the card number
check_digit = card_number.pop()

# Reverse the order of the remaining numbers
card_number.reverse()

processed_digits = []

for index, digit in enumerate(card_number):
    if index % 2 == 0:
        doubled_digit = int(digit) * 2

        # Subtract 9 from any results that are greater than 9       
        if doubled_digit > 9:
            doubled_digit = doubled_digit - 9

        processed_digits.append(doubled_digit)
    else:
        processed_digits.append(int(digit))

total = int(check_digit) + sum(processed_digits)

# Verify that the sum of the digits is divisible by 10
if total % 10 == 0:
    print("Valid!")
else:
    print("Invalid!")
