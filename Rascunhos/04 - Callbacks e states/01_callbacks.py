import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

app.layout = html.Div([
             dcc.Input(id='number-in',value=1, style={'fontsize':24}),
             html.Button(id='submit-button',
                         n_clicks=0,
                         children='Submit here',
                         style={'fontsize':24}),
             html.H1(id='number-out')
])

@app.callback(Output('number-out','children'),
             [Input('submit-button','n_clicks')],
             [State('number-in','value')])
def output(n_clicks,number):
    return "{} foi digitado e o botão foi clicado {} vezes".format(number,n_clicks)

if __name__ == "__main__":
    app.run_server()
