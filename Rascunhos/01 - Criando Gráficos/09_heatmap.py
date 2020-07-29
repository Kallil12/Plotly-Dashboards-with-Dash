import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../2010SantaBarbaraCA.csv')

# X e Y são os eixos, Z é a escala de cores, mas não aceita uma coluna pandas
# então é necessário transformar numa lista, isso é feito usando o
# .values.tolist()
data = [go.Heatmap(x=df['DAY'],
                   y=df['LST_TIME'],
                   z=df['T_HR_AVG'].values.tolist(),
                   colorscale = 'Jet')]

layout = go.Layout(title='SB CA Temps')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap_test.html')
