import string

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


## ASSIGNMENT
# Given two strings, s1 and s2. 
# Write a program to create a new string s3 made of the first char of s1, then the last char of s2, 
# Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.



#Figure out which string is longer
# Figure out a way to get the remainder of the longer string
#reverse s2
#Find a way to join si and s2 (Easier to zip)
# SOLUTION 1
# s1 = "Abcex"
# s2 = "Xyz"
# s2=s2[::-1]


# if s1_length == s2_length:
#     pass
# elif s2_length > s1_length:
#     rem=s2[length:]
# else:
#     rem= s1[length:]

# s3=list(zip(s1, s2))
# s3=''.join([char for item in s3 for char in item])
# s3=s3+rem
# print(s3)

# SOLUTION 2
# s1 = "Abcgy"
# s2 = "Xyz"
# s2 = s2[::-1]

# l1 = len(s1)
# l2 = len(s2)


# new_length = l1 if l1 > l2 else l2
# s3 = ""

# for i in range(new_length):
#     if i < l1:
#         s3 = s3 + s1[i]
#     if i < l2:
#       s3 = s3 + s2[i]

# print(s3)

# Write a program to check if two strings are balanced. 
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

# s2 = "Ynu"
# s1 = "PYnative"

# def check_balance(s1, s2):
#     x = 0
#     for i in s2:
#         if i in s1:
#             x += 1
#     if x == len(s1):
#         return True
#     else:
#         return False 

# print(check_balance(s1, s2))

# def check_balance(s1, s1):

#     for char in 


# check_balance(s1, s2)

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.

# SOLUTION 2
# str1 = "Welcome to USA. usa awesome, isn't it?"
# print(str1.lower().count("USA".lower())) 
# # result=""
# # print(result)

# # SOLUTION 2
# str1 = "Welcome to USA. usa awesome, isn't it?"
# print(str1.casefold().count("usa".casefold()))

# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

# total=0
# count=0
# str1 = "PYnative29@#8496"
# for char in str1:
#     if char.isnumeric():
#         count+=1
#         total+=int(char)
# print(total)
# print(f"{(total/count):.2f}")

# Exercise 10: Write a program to count occurrences of all characters within a string

# str1 = "Apple"
# count={}
# for i in str1:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)

# aplle_dict={char:str1.count(char) for char in str1}
# print(aplle_dict)

# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

# Reverse a given string

# SOLUTION 1
# str1 = "PYnative"
# str1=str1[::-1]
# print(str1)

# # SOLUTION2
# str1 = "PYnative"
# reversed_str = "".join((reversed(str1)))  # or use reversed(str1)
# print(reversed_str)

# Exercise 12: Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.

# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# var="Emma"

# str2=str1.rfind("Emma")
# print(str2)

# Exercise 13: Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.

# str1 = "Emma-is-a-data-scientist"
# str1=str1.split("-")
# print(str1)
# for item in str1:
#     print(item)

# Exercise 14: Remove empty strings from a list of strings

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# SOLUTION1
# result=[item for item in str_list if item != "" and item != None]
# print(result)

# SOLUTION2
# result=list(filter(None, str_list))
# print(result)

# SOLUTION3
# res = [item for item in str_list if item]
# print(res) 

# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

# Exercise 15: Remove special symbols / punctuation from a string

# str1 = "/*Jon is @developer & musician"


# for i in str1:
#     if i.isalnum():
#         print(i, end="")
#     elif i.isspace():
#         print(i, end="") 

# Exercise 16: Removal all characters from a string except integers

# str1 = 'I am 25 years and 10 months old'

# for i in str1:
#     if i.isdigit():
#         print (i, end="")

# str1 = "Emma25 is Data scientist50 and AI Expert"

# split_str=str1.split()
# print(split_str)

# for item in split_str:
#     if any(char.isdigit() for char in item):
#         print(item)

# Replace each special symbol with # in the following string

# str1 = '/*Jon is @developer & musician!!'
# str2=""
# SOLUTION 1
# for i in string.punctuation:
#     str1=str1.replace(i, "#")
# print(str1)
 
 #SOLUTION 2
# for i in str1:
#     if i.isalnum():
#         print(i, end="")
#     elif i.isspace():
#         print(i, end="")
#     else:
#         print("#", end="")

# SOLUTION 3
# str2 = ''.join([char if char not in string.punctuation else "#"for char in str1])
# print(str2)
# LIST COMPREHENSION SYNTAX
# comp=[item for item in my_iterable for my_condition]
