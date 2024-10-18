# Write a program to create a new string made of an input string’s first, middle, and last character.

# # str1 = "Jamedon"
# new_string=str1[0]+str1[2]+str1[-1]
# print(new_string)

# str1 = "Jamedons"
# result = str1[0]+str1[len(str1)//2]+str1[-1]
# print(result) 



# Exercise 1B: Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.

# str1 = "JhonDipPeta"
# middle=len(str1)//2
# new_string=str1[middle-1]+str1[middle]+str1[middle+1]
# print(new_string)

# Exercise 2: Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
# s1 = "Ault"
# s2 = "Kelly"

# # AuKellylt
# s1_mid=len(s1)//2
# s3=s1[:s1_mid]+s2+s1[s1_mid:]
# print(s3)

# Create a new string made of the first, middle, and last characters of each input string

# def mid_list(listo):
#     return len(listo)//2

# s1 = "America"
# s2 = "Japan"

# middle = len(s1) // 2
# s3 = s1[0] + s2[0] + s1[mid_list(s1)] + s2[mid_list(s2)] + s1[len(s1) - 1] + s2[len(s2) - 1]
# print(s3) 


# Exercise 4: Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

# SOLUTION 1
# str1 = "PyNaTive"
# str_low=[]
# str_high=[]
# lower=str1.lower()
# upper=str1.upper()

# for char in str1:
#     if char in lower:
#         str_low.append(char)
#     else:
#         str_high.append(char)

# str_low=''.join(str_low)
# str_high=''.join(str_high)
# result=str_low+str_high
# print(result)

# SOLUTION 2
# str1 = "PyNaTive"
# new_str = "".join(
#     ([i for i in str1 if i.islower()]) + ([i for i in str1 if i.isupper()])
# )
# print(new_str) 

# SOLUTION 3
# def string_sep(string: str):
#     lower_string = ""
#     upper_string = ""
#     for substring in string:
#         if substring.islower():
#             lower_string += substring  # concatenate lowercase letters
#         elif substring.isupper():
#             upper_string += substring  # concatenate uppercase letters
#     return lower_string + upper_string

# result = string_sep("PyNaTive") 
# print(result)

# Exercise 5: Count all letters, digits, and special symbols from a given string
# str1 = "P@#yn26at^&i5ve"

# Digit=0
# Symbol=0
# Char=0
# for i in str1:
#     if i.isalpha():
#         Char += 1
#     elif i.isdigit():
#         Digit += 1
#     elif not i.isalpha() and not i.isdigit():
#         Symbol += 1
# print(Char, Digit, Symbol) 

# SOLUTION 2
# def char_sep(string: str):

#     chars = 0
#     digits = 0
#     symbols = 0
#     for substring in string:
#         if substring.isalpha():
#             symbols += 1
#         elif substring.isdigit():
#             digits += 1
#         else:
#             chars += 1
#     return f"chars: {chars} digits: {digits} symbols : {symbols}"

# result = char_sep("P@#yn26at^&i5ve") 
# print(result)

# Given two strings, s1 and s2. 
# Write a program to create a new string s3 made of the first char of s1, then the last char of s2, 
# Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.



## ASSIGNMENT
# s1 = "Abcdet"
# s2 = "Xyz"

# # get string length
# s1_length = len(s1)
# s2_length = len(s2)

# # get length of a bigger string
# length = s1_length if s1_length > s2_length else s2_length
# result = ""

# # reverse s2
# s2 = s2[::-1]

# # iterate string 
# # s1 ascending and s2 descending
# for i in range(length):
#     if i < s1_length:
#         result = result + s1[i]
#     if i < s2_length:
#         result = result + s2[i]

# print(result)
