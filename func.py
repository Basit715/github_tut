#decorator in python
# Afunction can be stored in data structures like list and hash tables

def factorial(x):
     fact = 1
     for i in range(1, x+1):
          fact*=i
          
     return fact

print(factorial(5)) 
          