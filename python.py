import numpy as np
from __future__ import division
list= input ("Input some numbers seprated by a comma:")
def avg(list):
    return sum(list) / len(list)
print avg(list)
from collections import Counter
list2= input ("Input some numbers seprated by a comma: ")
number_of_occurrances = input ("Inpute the number of occurrences to calculate the average")
def avg(list2):
    return sum(list2[len(list2)-number_of_occurrances:])/number_of_occurrances
print avg(list2)
import random
x=1
y=100
number=random.randint(x,y)
print number
number=random.randint(x,y)
def lottery(number):
    if number > 50 and number < 100:
        return "Win"
    elif number >= 1 and number <=50:
        return "Loss"
    elif number ==y:
        return "Drow"
print lottery(number)
import pandas_datareader.data as web
stocks=["IBM", "AAPL", "MSFT"]
for stock in stocks:
    if stock=="IBM":
        stock1 = web.DataReader("IBM","google")
        print stock1.head(7)
    elif stock=="AAPL":
        stock2 = web.DataReader("AAPL","google")
        print stock2.head(7)
    else:
        stock3 =web.DataReader("MSFT","google")
        print stock3.head(7)
  import matplotlib.pyplot as plt
  for stock in stocks:
    if stock=="IBM":
        plt.plot(data1.head(7))
        plt.show()
    elif stock=="AAPL":
        plt.plot(data2.head(7))
        plt.show()
    else:
        plt.plot(data3.head(7))
        plt.show()       