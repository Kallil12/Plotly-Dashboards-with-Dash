import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('../mpg.csv')
#print(df)
#print(df.columns)

data = [go.Scatter(x=df['horsepower'],
                   y=df['acceleration'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=2*df['cylinders'],
                                showscale=True))]

layout = go.Layout(title='Horsepower vs Acceleration', hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename='05_bubble_plots_exercise.html')
