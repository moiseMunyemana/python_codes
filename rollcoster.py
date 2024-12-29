#!/usr/bin/env python
# coding: utf-8

# In[1]:


#roll coaster 

user_input = int(input ("what is height : "))
price = 0
if user_input >= 120:
    print("you re allowed to ride a rollcoster")
    
    user_age = int(input ("what is your age "))
    if user_age < 12:
        price +=5
        
    elif user_age <= 18:
        price += 7
        
    else:
        price +=12
    wants_picture = input ("do you wants a picture: (y/n)").lower()
    if wants_picture =="y":
        price +=3
            
    print(f"you total bill is ${price}")

else:
    print ("you need to grow higher before you start ridding rollcoaster")


# In[ ]:




