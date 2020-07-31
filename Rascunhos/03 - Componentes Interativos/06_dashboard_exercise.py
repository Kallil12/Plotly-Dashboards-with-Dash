#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:

app.layout = html.Div([
             dcc.RangeSlider(id='teste-range-slider',
                             min=-10,
                             max=10,
                             marks={i:str(i) for i in range(-10,10)},
                             step=1,
                             value=[-5,5]),
             html.Div(id='range-slider'),
             ], style={'fontFamily':'helvetica','fontsize':18})

# Create a Dash callback:
@app.callback(
    Output('range-slider', 'children'),
    [Input('teste-range-slider', 'value')])
def update_output(value):
    produto_valores = value[0]*value[1]
    return 'O produto entre os valores é: "{}"'.format(produto_valores)



# Add the server clause:
if __name__ == "__main__":
    app.run_server()
