# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:53:35 2021

@author: ASUS
"""

# Import the pyplot
import matplotlib.pyplot as plt

# Open and read the file
f = open('agedata2.csv','r')
agefile = f.readlines()
# integer list
city_list = []
for records in agefile:
    #split the record
    age,city =records.split(sep=',')
    city_list.append(city)
#we need count of cities so we import a class 
from collections import Counter
city_count =Counter(city_list)
#return object of type dictionary
#we cannot this to our piechart function
city_names =list(city_count.keys())
#this function will extract all the data from the dictionary to list
city_values =list(city_count.values())
#plot pie chart
plt.pie(city_values,labels=city_names,autopct='%.2f%%')
#autopct will simply print total percentage of respective cities on the pie chart
plt.show()