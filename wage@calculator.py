#!/usr/bin/env python
# coding: utf-8

# In[13]:



hours = int ( input (" employee's hours"))     
wage = int(input (" employyes's wage"))
if hours > 40:
    print ("overtime")
    pay_otp = (hours-40.0)* (wage*1.5) 
    pay_overtime =pay_otp + 40.0*wage
    print ("The final pay with overtime is " , pay_overtime)
else:
    print ("regular")
    pay= (hours*wage)
    print (f"The regular pay is {pay : 2f}" )
print ("All done ")

