#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd

# Create a DataFrame from  "flights" data
df = pd.read_csv('../flights.csv')

# Define a data variable

data = [go.Heatmap(x=df['year'],
                   y=df['month'],
                   z=df['passengers'].values.tolist(),
                   colorscale = 'Jet',
                   zmin=150,zmax=600)]

# Define the layout
layout = go.Layout(title='Passengers flying per Year and Month')

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap_exercise.html')
