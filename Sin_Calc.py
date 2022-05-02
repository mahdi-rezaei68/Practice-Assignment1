#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Define Function For FACTORIAL
def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i
    return fact

# Before Start Program Assignment Variable
n = 0
sum_sigma_sin_degree = 0
sum_sigma_sin_radian = 0

# Get x = Degree For Calculate Sin From User
x = float(input("Enter Degree For Calculate Sin : "))

# Get y = Radian For Calculate Sin From User
y = float(input("\nEnter Radian For Calculate Sin : "))

# Convert Degree to Radian
radian = x * 3.141592653589793 / 180

# Convert Radian to Degree
degree = y * 180/3.141592653589793

# Continue Tylor Equation To 9 Digits
while n <= 9 :
    # Tylor Equation For Calculate Sin By Convert Degree To Radian : User Input Degree and convert to radian
    sigma_sin_degree = (((-1) ** n) * ((radian) ** (2 * n + 1))) / (factorial((2 * n) + 1))
    sum_sigma_sin_degree = sum_sigma_sin_degree + sigma_sin_degree
    
    # Tylor Equation For Calculate Sin By Radian : input radian by user
    sigma_sin_radian = (((-1) ** n) * ((y) ** (2 * n + 1))) / (factorial((2 * n) + 1))
    sum_sigma_sin_radian = sum_sigma_sin_radian + sigma_sin_radian
    # for while end
    n = n + 1

print(f"\n{x} Degree : is {radian} Radian") 
print(f"\nSin {x} Degree : is {sum_sigma_sin_degree}")
print(f"\nSin {y} Radian : is {sum_sigma_sin_radian}")

