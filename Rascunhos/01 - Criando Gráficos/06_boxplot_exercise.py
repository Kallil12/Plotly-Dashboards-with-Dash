import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('../abalone.csv')

sample_1 = np.random.choice(df['rings'],60,replace=False)
sample_2 = np.random.choice(df['rings'],55,replace=False)

data = [
    go.Box(y=sample_1,name='Sample 1'),
    go.Box(y=sample_2,name='Sample 2')
]

layout = go.Layout(title='2 Random Samples')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='sample_1_vs_sample_2.html')

# Esse exemplo serve para mostrar que
# duas amostras podem divergir, mesmo
# dentro da mesma população
