# -*- coding: utf-8 -*-
"""Copy of fiboo recursion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16v4DjZf26Kw50BNYwnH5m5mZNr4fmPR2
"""

# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
if __name__ == "__main__":
    n = 9
    print(fibonacci(n))
 
 # This code is contributed by Manan Tyagi.