#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

letters = ["A", "B", "C", "D", "E", "F"," G", "H", "I", "J", "K", "L"," M",
           " N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"," Y", "Z" , "a", "b",
           "c", "d", "e", "f", "g", "h", "i", "j"," k", "l", "m"," n"," o", "p", "q", "r", 
           "s", "t", "u", "v", "w", "x", "y", "z"]

digits = ["0","1" , "2","3" , "4", "5", "6", "7", "8", "9"]
special = [ "!", "#", "$", "%", "&",  "*", "+",]
print("welcome to password generator")
number_letter = int(input("Enter the number of letters you want for your password ?\n"))
number_digits = int(input(f"Enter the number of digits you want for your password ?\n"))
number_special = int(input(f"Enter the number of special you want for your password ?\n"))
password = " "
password_list = [] #high _level

for char in range (1 , number_letter + 1):
    random_char = random.choice(letters)
    password += random_char
    #print(password)
for char in range (1 , number_special + 1):
    random_char = str(random.choice(special))
    password += random_char
    
for char in range (1 , number_digits + 1):
    random_char = random.choice(digits)
    password += random_char
print(f"Least proteted password{password}")

for char in range (1 , number_letter + 1):
    random_char = random.choice(letters)
    password_list.append(random_char)
    #print(password)
for char in range (1 , number_special + 1):
    random_char = str(random.choice(special))
    password_list.append(random_char)
    
for char in range (1 , number_digits + 1):
    random_char = random.choice(digits)
    password_list.append(random_char)
    
print(password_list)
random.shuffle(password_list)
print(password_list)
high_level = " "

for char in password_list:
    high_level += char
print(f"your password is now well protected: {high_level}")


# In[ ]:




