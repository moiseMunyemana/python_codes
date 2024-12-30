#!/usr/bin/env python
# coding: utf-8

# In[1]:


#json javaScript object notation  for reading the javascript OOP document.for dictionaries.
import json 
data ='''{
"name" : "Moise",
"phone" :{
"type" : "intl",
"number" : "+1 902 318 6021"
},
"email" :{"hide":"yes"},
"name":"kelly"

}'''

info = json.loads(data)
print(info)
print ( info["name"])
print (" His phone number is :" , info["phone"]["number"])
print("Is email hided:" , info['email']["hide"])


# In[ ]:




