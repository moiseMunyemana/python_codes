#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("welcome to python pizza delivery! ")
user_input = input ("would you like to order a pizza today ?: (y/n)").lower()
pizza_large = 30
pizza_medium = 20
pizza_small = 15
toppings = 3
extra_cheese = 2
total = 0
if user_input =="y" :
    print("okay")
    request = input ("what size do you like to order?  choose between L/M/S:").lower()

    if request == "l" :
        total = pizza_large
        print (f"your total bill today is {total}")

        request1 = input ("would you like to add topping ? (y/n)").lower()
        if request1 == "y":
            total = pizza_large + toppings
            print(f"your total bill today is {total}")

        if request1 =="n":
            total = pizza_large
            print(f"your total bill today is {total}")

        request2 = input("would you like to add extra cheese? (y/n)").lower()
        if request2 == "y" and request1 =="y":
            total = pizza_large + toppings + extra_cheese
            print(f"your total bill today is {total}")
        elif request2 =="n" and request1 =="n":
            total = pizza_large
            print(f"your total bill today is {total}")
        elif request2 =="y" and request1 =="n":
            total = pizza_large + extra_cheese
            print(f"your total bill today is {total}")
        elif request2 =="n" and request1 =="y":
            total = pizza_large + toppings

            print(f"your total bill today is {total}")


    elif request =="m":
        total = pizza_medium
        print (f"your total bill today is {total}")

        request1 = input ("would you like to add topping ? (y/n)").lower()
        if request1 == "y":
            total = pizza_medium + toppings
            print(f"your total bill today is {total}")

        if request1 =="n":
            total = pizza_medium
            print(f"your total bill today is {total}")

        request2 = input("would you like to add extra cheese? (y/n)").lower()
        if request2 == "y" and request1 =="y":
            total = pizza_medium + toppings + extra_cheese
            print(f"your total bill today is {total}")
        elif request2 =="n" and request1 =="n":
            total = pizza_medium
            print(f"your total bill today is {total}")
        elif request2 =="y" and request1 =="n":
            total = pizza_medium + extra_cheese
            print(f"your total bill today is {total}")
        elif request2 =="n" and request1 =="y":
            total = pizza_medium + toppings

            print(f"your total bill today is {total}")

    elif request == "s" :
        total = pizza_small
        print (f"your total bill today is {total}")

        request1 = input ("would you like to add topping ? (y/n)").lower()
        if request1 == "y":
            total = pizza_small + toppings
            print(f"your total bill today is {total}")

        if  request1 =="n":
            total = pizza_small
            print(f"your total bill today is {total}")

        request2 = input("would you like to add extra cheese? (y/n)").lower()
        if request2 == "y" and request1 =="y":
            total = pizza_small + toppings + extra_cheese
            print(f"your total bill today is {total}")
        elif request2 =="n" and request1 =="n":
            total = pizza_small
            print(f"your total bill today is {total}")
        elif request2 =="y" and request1 =="n":
            total = pizza_small + extra_cheese
            print(f"your total bill today is {total}")
        elif request2 =="n" and request1 =="y":
            total = pizza_small + toppings
            print(f"your total bill today is {total}")
else:
    print("invalid choice")
print("Done! 'HAVE A GOOD ONE'")


