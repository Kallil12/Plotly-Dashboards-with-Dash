import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../2018WinterOlympics.csv')
#print(df.head(10))

# dentro de cada chamada de .Layout existe um parâmetro chamado de "barmode",
# esse barmode diz como vai ser o tipo de gráfico de barras mostrado

trace1 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Gold Medals',
                marker={'color':'#FFD700'})

trace2 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Silver Medals',
                marker={'color':'#9EA0A1'})

trace3 = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronze Medals',
                marker={'color':'#CD7F32'})

#data = [go.Bar(x=df['NOC'], y=df['Total'])]
data = [trace1,trace2,trace3]
layout = go.Layout(title='Medals',barmode='stack')
fig = go.Figure(data=data,layout=layout)


pyo.plot(fig,filename='04_bar_chart.html')
