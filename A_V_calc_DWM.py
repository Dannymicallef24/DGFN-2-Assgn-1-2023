# TPRG 2131 Fall 2023 Assignment 1 Main file
# October 15, 2023
# Daniel M <daniel.micallef@durhamcollege> 100893638
# This program is strictly my own work. Any material 
# beyond course learning materials that is taken from 
# the Web or other sources is properly cited, giving
# credit to the original author(s)
# I used Python Libraries (https://docs.python.org/3/search.html?q=module) to learn about modules.
# I asked chat gpt "How to make and use a menu in python?" on October 10th.
# I asked chat gpt "How to use modules and functions together in python?" on October 12th.
# I asked chat gpt "How to have the answers from equations rounded to one decimal place?" on October 10th.

import math

# Function to calculate the area of a rectangle
def calculate_area_of_rectangle(length, width):
    return length * width

# Function to calculate the volume of a sphere
def calculate_volume_of_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

# Function to calculate the area of a triangle
def calculate_area_of_triangle(base, height):
    return (1/2) * base * height

# Function to calculate the volume of a cylinder
def calculate_volume_of_cylinder(radius, height):
    return math.pi * (radius ** 2) * height

# Function to calculate the area of a circle
def calculate_area_of_circle(radius):
    return math.pi * (radius ** 2)

# Function to display the main menu
def display_main_menu():
    print("A/V Calculator")
    print("(Level 0)")
    print("Enter Q/q to quit - select either to gracefully close the application and cancel the calculated view option, if set.")
    print("Enter V/v to change the calculated view or D/d for the default view.")
    print("(Level 1)")
    print("1. Calculate Area of Rectangle")
    print("2. Calculate Volume of Sphere")
    print("3. Calculate Area of Triangle")
    print("4. Calculate Volume of Cylinder")
    print("5. Calculate Area of Circle")

# Function to handle the main menu and user input
def main_menu():
    display_with_equations = False
    
    while True:
        display_main_menu()
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'q':
            print("Exiting the calculator.")
            break
        elif choice == 'v':
            # Display calculation details with equations
            display_with_equations = True
        elif choice == 'd':
            # Display calculation details without equations (default view)
            display_with_equations = False
        elif choice in ('1', '2', '3', '4', '5'):
            calculate_and_display_result(choice, display_with_equations)
        else:
            print("Invalid choice. Please try again.")

# Function to calculate and display the result of a chosen calculation
def calculate_and_display_result(choice, display_with_equations):
    if choice == '1':
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = calculate_area_of_rectangle(length, width)
        area = round(area, 1)  # Round the area to one decimal place
        print_result("Area of Rectangle", area, length, width, "A = l x w", display_with_equations)
    elif choice == '2':
        radius = float(input("Enter the radius: "))
        volume = calculate_volume_of_sphere(radius)
        volume = round(volume, 1)  # Round the volume to one decimal place
        print_result("Volume of Sphere", volume, radius, "V = (4/3)πr^3", display_with_equations)
    elif choice == '3':
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = calculate_area_of_triangle(base, height)
        area = round(area, 1)  # Round the area to one decimal place
        print_result("Area of Triangle", area, base, height, "A = (1/2)bh", display_with_equations)
    elif choice == '4':
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        volume = calculate_volume_of_cylinder(radius, height)
        volume = round(volume, 1)  # Round the volume to one decimal place
        print_result("Volume of Cylinder", volume, radius, height, "V = πr^2h", display_with_equations)
    elif choice == '5':
        radius = float(input("Enter the radius: "))
        area = calculate_area_of_circle(radius)
        area = round(area, 1)  # Round the area to one decimal place
        print_result("Area of Circle", area, radius, "A = πr^2", display_with_equations)

# Function to print the result with or without equations
def print_result(description, result, *args, equation="", display_with_equations=False):
    if display_with_equations:
        print(f"{description} ({equation}) = {result} {format_args(args)}")
    else:
        print(f"{description} = {result}")

# Function to format arguments for displaying with equations
def format_args(args):
    return "(" + " x ".join(map(str, args)) + ")"

if __name__ == "__main__":
    main_menu()
