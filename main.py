from utils import square, is_even, celsius_to_fahrenheit
from utils import square, is_even, celsius_to_fahrenheit, greet


number = float(input("Enter a number: "))

print(f"Square: {square(number)}")
print(f"Even or odd: {'Even' if is_even(number) else 'Odd'}")
print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(number)}")

name = input("Enter your name: ")
print(greet(name))