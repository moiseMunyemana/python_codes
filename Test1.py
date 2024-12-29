#!/usr/bin/env python
# coding: utf-8

# In[2]:


print(" welcome to computer test!")

agree = True

while agree:
    if  input ("Do you want take this test? ").lower() !="yes":
        break;
    else:
        print("Let's start !")
    score  = 0
    miss = 0
    total = 0

    answer1 = input("what AI stands for ? : ")
    if answer1.lower().strip() == "artificial intelligence":
        print ("correct")
        score +=1
        total +=1
    else:
        print("incorect")
        miss +=1
        total +=1
    answer2 = input("what 3D stands for ? : ")
    if answer2.lower().strip() == "three dimension":
        print("correct")
        score +=1
        total +=1
    else:
        print("incorrect")
        miss +=1
        total +=1
    answer3 = input("what bjt stands for? :")
    if answer3.lower().strip()=="bipolar junction transistor " :
        print("correct")
        score +=1
        total +=1
    else:
        print ("incorrect")
        miss +=1
        total +=1
    print(f"your test score is {score} \n you have missed {miss} \n and your overall percentage is " + str(round((score/total)*100)) +"%" )
print("Thanks for coming")





