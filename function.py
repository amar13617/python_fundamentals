def greet():
    name = input("Enter your name:")
    print(f"hello, {name}")
    
greet()

#for number in range(1, 11):
#    print(number * 2)

#def get_even_numbers():
#    for number in range(1, 11):
 #       print(number * 2)

#get_even_numbers()

#def get_even_numbers(amount):
#    for number in range(1, amount + 1):
#        print(number * 2)
#get_even_numbers(4)
#multiple parameter
#def x_print(requested_output, quantity):
#    for _ in range(requested_output):
 #       print(quantity)

#x_print(7, "Hello")

#keyword Argument
def x_print(requested_output, quantity):
    for _ in range(quantity):
        print(requested_output)

x_print(requested_output="Hello", quantity=2)
