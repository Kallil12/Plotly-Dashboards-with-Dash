import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([

  html.Label('Dropdown'),
  dcc.Dropdown(options=[{'label':'Mossoró',
                         'value':'Calor'},
                        {'label':'Pau dos Ferros',
                         'value':'Muito calor'}],
                value='Calor moderado'),

  html.Label('Slider'),
  dcc.Slider(min=-10,max=20,step=0.5,value=0,
             marks={i:i for i in range(-10,20)}),

  html.Label('Some Radio Items'),
  dcc.RadioItems(options=[{'label':'Mossoró',
                           'value':'Calor'},
                          {'label':'Pau dos Ferros',
                           'value':'Muito calor'}],
                    value='Mossoró')

])

if __name__ == '__main__':
    app.run_server()
