#!/usr/bin/env python
# coding: utf-8

# In[25]:


class character():
    def __init__(self, health ,damage , speed):
        self.health= health
        self.damage= damage
        self.speed = speed
    def double(self):
        self.speed *= 4
        self.health +=3
       
        
    def square (self):
        self.damage **=2
     
        
worrior = character(40 , 60 , 10)
ninja = character(5 , 70 , 80)
print ("warrior damage is:" , worrior.damage)
print("ninja speed is :",  ninja.speed)
ninja.double()
worrior.double()
print("new ninja's speed is :" ,ninja.speed)
print("new worrior'ps health: " , worrior.health)
ninja.square()
print("The square damage for ninja is :",ninja.damage)


