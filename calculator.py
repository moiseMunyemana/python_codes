#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
     return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

# Display menu for the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")

# Check if choice is one of the four options
if choice in ('1', '2', '3', '4'):
    # Take input for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the operation based on the user's choice
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
else:
    print("Invalid input")


# In[ ]:




