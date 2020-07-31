import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../wheels.csv')

app = dash.Dash()

app.layout = html.Div([
             dcc.RadioItems(id='wheels',
                            options=[{'label':i,'value':i}for i in df['wheels'].unique()],
                            value=1),
             html.Div(id='wheels-output'),
             html.Hr(),
             dcc.RadioItems(id='colors',
                            options=[{'label':i,'value':i}for i in df['color'].unique()],
                            value='blue'),
             html.Div(id='colors-output')
], style={'fontFamily':'helvetica','fontsize':18})


@app.callback(Output('wheels-output','children'),
             [Input('wheels','value')])
def callback_a(wheels_value):
    return "you chose {}".format(wheels_value)

@app.callback(Output('colors-output','children'),
             [Input('colors','value')])
def callback_b(colors_value):
    return "you chose {}".format(colors_value)


if __name__ == "__main__":
    app.run_server()
