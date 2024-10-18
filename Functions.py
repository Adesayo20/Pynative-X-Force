# Exercise 1: Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and print their value.

# def details(name, age):
#     print(f"{name} and {age}")


# details("Ade",20)


# Exercise 2: Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.

# Note: Create a function in such a way that we can pass any number of arguments to this function,
# and the function should process them and display each argument’s value.

# def func1(*args):
#     print(*args)

# func1(2, 3,8, 9, "sugar", False)

# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and 
# calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

# def calculation(a, b):
#     return a+b,a-b

# res = calculation(40, 10)
# print(res)

# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary


# def show_employee(name, salary=9000):
#     print(f"Name: {name} salary: {salary}")

# # show_employee("Ben", 12000)
# # show_employee("Jessa")

# # Expected output:

# # Name: Ben salary: 12000
# # Name: Jessa salary: 9000

# show_employee("Ben", 12000)
# show_employee("Jessa")


# Exercise 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

# def outer_func(a:int, b:int):
#     def inner_func():
#         return a + b
#     return a + b + 5
    
# result = outer_func(5, 10)
# print(result) 

# Exercise 6: Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

# A recursive function is a function that calls itself again and again.

# Expected Output:

# 55

# def sum_numbers(n):
#     if n == 0:  # base case
#         return 0
#     else:
#         return n + sum_numbers(n - 1)
    
# print(sum_numbers(10))

# def addition(num):
#     if num:
#         # call same function by reducing number by 1
#         return num + addition(num - 1)
#     else:
#         return 0

# res = addition(10)
# print(res)

# Explaining the logic using a for loop
# total=0
# for i in range(10, -1, -1):
#         total+=i
   
# print(total)

# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). 
# Assign a new name show_tudent(name, age) to it and call it using the new name.

# def display_student(name, age):
#     print(name, age)

# # display_student("Emma", 26)
# show_student=display_student

# show_student("Aaminah", 25)

# Generate a Python list of all the even numbers between 4 to 30
# our_list=[num for num in range(4, 30) if num%2 == 0]
# our_list2=[num for num in range(4, 30, 2)]
# print(our_list)
# print(our_list2)

# Exercise 9: Find the largest item from a given list

# x = [4, 6, 8, 24, 12, 2]
# print(max(x))
# list.sort(x)
# print(x[-1])

