#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Math Python 
import math
# Select User For Calculate
op = input("Please Enter For Operation : + , - , * , / . radical , sin . cot , cos , tan , factorial: ")

# Conditions User Select How to Calc ,
if op == "+" or op == "-" or op == "*" or op =="/" :
    first_num = float(input("Plese Enter First Number : "))
    second_num = float(input("Plese Enter Second Number : "))
    
# Conditions User Select How to Calc ,
elif op == "radical" or op == "sin" or op == "cot" or op == "cos" or op == "tan" or op == "factorial":
    number = float(input("Plese Enter Number : "))

else :
    print("Please Select From List ")

#START Calculate Conditions :
if op == "+":
    result = first_num + second_num
    
elif op == "-":
    result = first_num - second_num
    
elif op == "*":
    result = first_num * second_num
    
elif op == "/" and second_num != 0:
    result = first_num / second_num
    
elif op == "/" and second_num == 0:
    result = "can not Devide Zero"
    
elif op == "sin":
    result = math.sin(number)
    
elif op == "radical":
    result = math.sqrt(number)
    
elif op == "cot":
    result = 1 / (math.tan(number))
    
elif op == "cos":
    result = math.cos(number)
    
elif op == "tan":
    result = math.tan(number)
    
elif op == "factorial":
    result = math.factorial(int(number))
#END Calculate Conditions

else :
    print("Not Found")
# Show Result
print(result)


# In[ ]:




