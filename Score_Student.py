#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Get Name And Family From User
name = input("Please Enter Your Name And Familly: ")

# Save Scores math,physics,economy Courses
math = float(input("Your Score in Math : "))
physics = float(input("Your Score in Physics : "))
economy  = float(input("Your Score in Economy  : "))

# Calculate Average Scores = sum scores / count course
average = (math + physics + economy) / 3

# Conditions :
if average >= 17 :
    print("Great")
elif average >= 12 and average < 17 :
        print("Normal")
elif average < 12 :
    print("Fail")
else :
    print("Please Enter Number, Dont Enter String")

