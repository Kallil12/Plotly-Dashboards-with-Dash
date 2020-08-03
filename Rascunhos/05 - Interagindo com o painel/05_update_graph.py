import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()
df = pd.read_csv('../mpg.csv')

# se quiser fazer os valores de lançamento dos carros parecerem
# mais reais, faça o seguinte:
#df['year']=random.randint(-4,5,len(df))*0.1+df['model_year']
# adding noise or jitter que chama

app.layout = html.Div([
             dcc.Graph(id='mpg-scatter',
                       figure={'data':[go.Scatter(x=df['model_year']+1900,
                                                  y=df['mpg'],
                                                  text=df['name'],
                                                  hoverinfo= 'text+y+x',
                                                  mode='markers')],
                               'layout':go.Layout(title='Dados de consumo',
                                                  xaxis={'title':'Model Year'},
                                                  yaxis={'title':'MPG'},
                                                  hovermode='closest')})
])


if __name__ == '__main__':
    app.run_server()
