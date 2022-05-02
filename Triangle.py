#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Enter Three Edge and this can say triangle possible Or Not Possible")
# Input Triangle Edges
z1 = int(input("Enter Edge 1 : "))
z2 = int(input("Enter Edge 2 : "))
z3 = int(input("Enter Edge 3 : "))
# If edge 1 + edge 2 > edge 3 : triangle else not triangle
if z1 + z2 > z3 :
    print("This Possible")
else :
    print ("Not Possible")

