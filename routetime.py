import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("/Users/svalentino/Desktop/Data Projects/TravelTime/travel.csv")

#input the names of the routes here
Route1 = str(input("What is the name of the first route?"))
Route2 = str(input("What is the name of the second route?"))
#get the mean for each route of travel
Route1Mean= round(df.loc[df['Route'] == Route1, 'Time'].mean(),2)
Route2Mean = round(df.loc[df['Route'] == Route2, 'Time'].mean(),2)
#get the standard deviation for each route of travel
Route1SD = round(df.loc[df['Route'] == Route1, 'Time'].std(),2)
Route2SD = round(df.loc[df['Route'] == Route2, 'Time'].std(),2)
#get the times and means in array form
Times = np.array([Route1Mean,Route2Mean])
Routes = np.array([Route1,Route2])
#make a bar chart and style it with red for route 1 and blue for route 2 
bar = plt.bar(Routes,Times,color= ["red","blue"])
plt.title("Average Time Based on Route")
plt.bar_label(bar,fmt='%.2f')
plt.xlabel("Route")
plt.ylabel("Time (Seconds)")
#get the date
now = datetime.now().strftime("%m/%d/%Y")
#get the number of observations. Accounts for headers
obs = len(df)
#count observations by route
obsof1 = len(df.loc[df['Route'] == Route1])
obsof2 = len(df.loc[df['Route'] == Route2])
#get the new data in data frame and save to a csv file
d = {'First Route Average': Route1Mean, 'First Route SD': Route1SD,'Second Route Average': Route2Mean,'Second Route SD': Route2SD,'Last Run Date': now,'# of Observations': obs,'First Route Observations': obsof1,'Second Route Observations': obsof2}
data = pd.DataFrame(data=d,index=[0])

data.to_csv('ResultLog.csv',header=True,index=None)
plt.show()
