#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np
import pandas as pd

df = pd.read_csv('../iris.csv')

# Define the traces

# HINT:
# This grabs the petal_length column for a particular flower
iris_setosa = df[df['class']=='Iris-setosa']['petal_length']
iris_versicolor = df[df['class']=='Iris-versicolor']['petal_length']
iris_virginica = df[df['class']=='Iris-virginica']['petal_length']

# Define a data variable
hist_data = [iris_setosa,iris_versicolor,iris_virginica]
group_labels = ['Setosa','Versicolor','Virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data,group_labels,bin_size=[.2,.2,.2])
pyo.plot(fig, filename='iris_multgroup.html')
