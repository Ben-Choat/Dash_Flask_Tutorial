'''
BChoat 2024/09/11

This is a basic app with no interactivity

Some functions/attributes of note:

- a basic dash app with interactivity consists of 
--- app definition
--- layout (wraps html and css in more pythonic syntax, but html and css 
    can be used)
--- callback (this is where the interactivity magic happens)
--- a function tied to a callback
--- command to run

- an app can include many callbacks associated with different user actions
- each funciton tied to a callback can return many values

- there are dash-core-components (dcc) which are based on html and css
    https://dash.plotly.com/dash-core-components
- there are also dash-bootstrap-components (dbc; a separate library)
    https://dash-bootstrap-components.opensource.faculty.ai/
- there are also dash html components. These are more aligned with
    standard html and tend to be used along side dcc and dbc.
    https://dash.plotly.com/dash-html-components

-I've been using dbc as much as possible. dbc does not include options
    for all dcc's though.


- the dash website has a lot of very helpful guidance and is a great
    reference, and a great place to learn
    https://dash.plotly.com/

'''

# load libraries
from dash import Dash, dcc, html
from C_PlotlyPlots import create_go_plot
import numpy as np
import pandas as pd


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

# app definition
app = Dash()

# app layout
app.layout = html.Div(children=[
    # html.H1('This is an html header'),
    dcc.Graph(figure = create_go_plot(
                    df=df_work, 
                    col1='Day', 
                    col2='Rain_cm', 
                    cat_col='Irrigated'
                    ), # style={"width": "50%"}
            )
    ], #style={"display": "flex",
        #   "flex-direction": "column",
        #   "align-items": "center",
        #   "min-height": "100vh",
        #   "width": "100vw"} # style can be used to override previous set styles
)

# debug=True allows app to update while being ran (helps w/troublehsooting)
# it also includes a troubleshooting help button (you will see when you run)
app.run_server(debug=True) # other options available here too