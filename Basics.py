
# Given two integer numbers, write a Python code to return their product only 
# if the product is equal to or lower than 1000. Otherwise, return their sum.

# num1 = 20
# num2 = 30
# if num1*num2 <= 1000:
#     print(num1*num2)
# else:
#     print(num1+num2)

# def calc_number(n1,n2):
#     if n1*n2 <= 1000:
#         return n1*n2
#     else:
#         return n1+n2


# result = calc_number(40,30)
# print(result)
# calc_number(20,30)


# Write a Python code to iterate the first 10 numbers, 
# and in each iteration, print the sum of the current and previous number.
# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number  0  Sum:  0
# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
# Current Number 5 Previous Number  4  Sum:  9
# Current Number 6 Previous Number  5  Sum:  11
# Current Number 7 Previous Number  6  Sum:  13
# Current Number 8 Previous Number  7  Sum:  15
# Current Number 9 Previous Number  8  Sum:  17

# for i in range(10):
#     sum=i+x
#     print(f"Current number {i} Previous Number {x} Sum {sum} ")
# x= 0
# for i in range(10):
#     if i <=0 and x == 0:
#         print(f"Sum of {i} and {x} is {0}")
#     else:
#         print(f"Sum of {i} and {x} is {x + i}")
#         x+=1
# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0

# # loop from 1 to 10
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     # modify previous number
#     # set it to the current number
#     previous_num = i 

# for i in range(10):
#     if i == 0:


#         c = i
#         x = 0
#     else:
#         x = i -1
#         c = i


#     print(f"{i}{x} {x + i}")

#     i = 10
#     x = 9      


# print(f"{i}{x} {x + i}") 
# x=0
# for i in range(10):
#     if i <=0 and x == 0:
#         print(f"Sum of {i} and {x} is {0}")
#     else:
#         print(f"Sum of {i} and {x} is {x + i}")
#         x+=1

# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0   
    
# x= 0
# for i in range(1, 11):
#     print(f"Sum of {x} and {i} is {x + i}")
#     previous_num = i 
#     x+=1 

# Write a Python code to accept a string from the user and display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
# string=input("please type anything: ")
# length= len(string)
# for i in range (0, length, 2):
#     print(string[i])

# Write a Python code to remove characters from a string from 0 to n and return a new string.
# For Example:
# remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
# remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
# Note: n must be less than the length of the string.

# string="Pynative"
# new_string=string[2:8]
# print(new_string)

# Write a code to return True if the list’s first and last numbers are the same. 
# If the numbers are different, return False.

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]


# def check_list(a):
#     if a[0]==a[-1]:
#         print ("True")
#     else:
#         print("False")
    
# check_list(numbers_x)
