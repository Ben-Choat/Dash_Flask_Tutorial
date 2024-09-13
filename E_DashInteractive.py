'''
BChoat 2024/09/11

Simple dash app allowing user to select which columns to plot.

Some functions/attributes of note:

- a basic dash app with interactivity consists of 
--- app definition
--- layout (wraps html and css in more pythonic syntax, but html and css 
    can be used)
--- callback (this is where the interactivity magic happens)
--- a function tied to a callback

- an app can include many callbacks associated with different user actions
- each funciton tied to a callback can return many values

- there are dash-core-components (dcc) which are based on html and css
    https://dash.plotly.com/dash-core-components
- there are also dash-bootstrap-components (dbc; a separate library)
    https://dash-bootstrap-components.opensource.faculty.ai/
- there are also dash html components. These are more aligned with
    standard html and tend to be used along side dcc and dbc.
    https://dash.plotly.com/dash-html-components

Some helpful resources

-I've been using dbc as much as possible. dbc does not include options
    for all dcc's though.

- Lots of good interactive plotting help available here:
    https://dash.plotly.com/interactive-graphing

- the dash website has a lot of very helpful guidance and is a great
    reference, and a great place to learn
    https://dash.plotly.com/

'''

# load libraries
from dash import Dash, dcc, html
from C_PlotlyPlots import create_go_plot
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output


# create dataframe to work with
# how many data points to work with?
n_in = 100
# random numbers representing irrigated or not
rndm_numbers = np.random.binomial(1, 0.25, n_in)

# dataframe to work with
df_work = pd.DataFrame({
    'Day': [i+1 for i in range(n_in)],
    'Rain_cm': np.round(np.random.exponential(scale=1, size=n_in), 4),
    'Radiation': np.round(np.random.normal(loc=20, scale=5, size=n_in)),
    'Irrigated': ['yes' if i == 1 else 'no' for i in rndm_numbers]
})

app = Dash()

# app layout
app.layout = html.Div(children=[
    html.H1('~~~~Basic Dash Example~~~~'),
    html.Div(children = [
        html.P('Select Variable for X-Axis'),
        dcc.Dropdown(
            options=df_work.columns[0:3],
            value='Rain_cm',
            id='x_axis', 
        ),
        html.P('Select Variable for Y-Axis'),
        dcc.Dropdown(
            options=df_work.columns[0:3],
            value='Day',
            id='y_axis', 
        )], 
        style={"width": "20%"}
    )
        ,
    dcc.Graph(
        id='irrigation_plot', 
        style={"width": "50%"}
        ) # graph
    ], style={"display": "flex",
          "flex-direction": "column",
          "align-items": "center",
          "min-height": "100vh",
          "width": "100vw"} # style can be used to override previous set styles
)

# Callbacks for handling tab changes and file uploads
@app.callback(
    Output('irrigation_plot', 'figure'),
    [Input('x_axis', 'value'),
     Input('y_axis', 'value')]
)
def junk_name(x_ax, y_ax):
    # print(f'x_ax: {x_ax}, y_ax: {y_ax}')
    # print(f'df: {df_work}')
    figure = create_go_plot(
                    df=df_work, 
                    col1=x_ax,
                    col2=y_ax, 
                    cat_col='Irrigated'
                    )
    return figure


# debug=True allows app to update while being ran (helps w/troublehsooting)
# it also includes a troubleshooting help button (you will see when you run)
app.run_server(debug=True) # other options available here too


