#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("BMI CALCULATE , Height : Centimeter , Weight : Kg")

# Get Height and Weight From User
ghad = float(input("Please Enter your Height : "))
vazn = float(input("Please Enter your Weight : "))

# convert Height Centimeter TO Meter
ghad_to_meter = ghad / 100

# BMI Calculate Formula
bmi = vazn / (ghad_to_meter ** 2)
print ("Your BMI is : ",bmi)
if bmi <= 18.5 :
    print("Thin")
elif bmi > 18.5 and bmi < 24.5 :
    print("Good")
elif bmi > 25 and bmi < 29.9 :
    print("Fat")
elif bmi > 30 :
    print("Very Fat")

