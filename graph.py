#creating a bell-curve graph with mobile data
print("Hello!\nThis is a bell-curve graph which shows the average rating for amazon mobile brands.")

#importing the right libraries
import csv 
import pandas as pd
import plotly.figure_factory as ff

#reading the csv file
df=pd.read_csv("mobileData.csv")

#creating a distribution plot graph (bell-curve)
fig=ff.create_distplot([df["Average Rating"].tolist()], ["Average Rating"])

#calling the function
fig.show()