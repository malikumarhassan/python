import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mtl
sns.set(color_codes = True)

car = pd.read_csv('D:/RIT/car.csv')
#print(car.head())
# print(car.head(3))
#print(car.dtypes)
# print(car.columns.values)
# Analytic summary
#print(car.describe(include='all'))
#print(car.hist(figsize=(0,30)))
#survey.plot(column='Year')

#https://www.youtube.com/watch?v=vacXuZAmOWY
#_= mtl.plot(car['Number of Doors'],car['Vehicle Style'], label='Vehicle')
#_= mtl.legend()
#_ =mtl.title('Vehicle Doors')
#_= mtl.show()

# histogram8
#_ =mtl.hist(car['Transmission Type'], bins=8)
#_ = mtl.xlabel('Transmission')
#_ = mtl .ylabel('Value')
#_ = mtl.title('Transmissions Type')
#_ = mtl .show()


#box plot seaborn
#_ = sns.boxplot(x='Vehicle Size', y='Engine HP', data =car)
#_ = mtl.show()

#pair plot
#_ = sns.pairplot(car)
#_ = mtl.show()


#Drop colums form dataframe

#car = car.drop(['Engine HP',	'Engine Cylinders',	'Transmission Type'	,'Driven_Wheels'], axis =1)
#print(car.head())


# Data shape rows and col
#print(car.shape)


# Data Summary
#print(car.describe())

#Rename columns name
#car =car.rename(columns={"Engine HP" : "HP",	"Engine Cylinders" : "Cyliders",	"Transmission Type" : "Trans Type"	,"Driven_Wheels" : "Wheels"})
#car.head(5)
#print(car)

# rows contianing duplicate data
#duplicate_rows_car = car[car.duplicated()]
#print("duplicated row :" , duplicate_rows_car)

#remove duplicates
#car = car.drop_duplicates()
#print(car)

#remove null values
#print(car.isnull().sum())

#find the outliers
#_ = sns.boxplot(x=car['Popularity'])
#mtl.show()

#plot hitogram show different value of cars models
#_ = car.Make.value_counts().nlargest(400).plot(kind='bar',figsize=(10,5))
#_ = mtl.xlabel('Make')
#_ = mtl .ylabel('coutn')
#_ = mtl.title('Car Make')
#mtl.show()

# find the relation between the variable heat map
#mtl.figure(figsize=(20,10))
#car = car.corr()
#sns.heatmap(car,cmap='BrBG', annot = True)
#mtl.show()

