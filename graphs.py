# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:34:33 2021

@author: ASUS
"""
#plotting basic
#import pyplot from matplotlib
import matplotlib.pyplot as plt
x_day =[1,2,3,4,5]
y_price1 =[9,9.5,10.1,10,12]
y_price2 =[11,12,10.5,11.5,12.5]
#define chart element
plt.title("stock movement")
plt.xlabel("week days")
plt.ylabel("prices in USD")
plt.plot(x_day,y_price1,label='stock1')
plt.plot(x_day,y_price2,label='stock2')
plt.legend(loc=2, fontsize =8)
plt.show()

