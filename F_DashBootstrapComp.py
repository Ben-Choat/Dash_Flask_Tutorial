'''
BChoat 2024/09/12

Incorporating bootstrap (dash-bootstrap-components)

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

- there are also dash html components. These are more aligned with
    standard html and tend to be used along side dcc and dbc.
    https://dash.plotly.com/dash-html-components

- there are also dash-bootstrap-components (dbc; a separate library)
    https://dash-bootstrap-components.opensource.faculty.ai/

One feature of bootstrap (that we are not fully utilizing as of now)
    is the ability to make the layout friendly/fluid for a variety
    of screen sizes, such as for mobile

SOME DBC Layout tips
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
For best results, make sure you adhere to the following two rules when constructing your layouts:

1. Only use Row and Col inside a Container. A single Container wrapping your entire app's content is
    fine. Set fluid=True if you don't want the margins that Container adds by default. Since the 
    content of this page is wrapped with a Container, the snippets below don't explicitly include them.
2. The immediate children of any Row component should always be Col components. Your content should 
    go inside the Col components.
'''



# load libraries
from dash import Dash, dcc, html
from C_PlotlyPlots import create_go_plot
import numpy as np
import pandas as pd
import dash_bootstrap_components as dbc
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

# for info about bootstrap themes in Dash see: 
   # https://dash-bootstrap-components.opensource.faculty.ai/docs/#:~:text=Linking%20a%20stylesheet
# print(dbc.themes.COSMO)
# app definition
# app = Dash()
# app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app = Dash(external_stylesheets=[dbc.themes.CYBORG])
# app = Dash(external_stylesheets=[dbc.themes.GRID])

# app layout
# dbc.Container initiates bootstraps grid system (screen split to 12 columns, and can define rows)
app.layout = dbc.Container(children=[ 
# app.layout = html.Div(children=[
    dbc.Row(children=[
        dbc.Col(children = [
            # html.Div(children=[
                html.H1('~~~~Basic Dash Example~~~~'),
        ], width={"size": 10, "offset": 1}
        )
        ]),
    dbc.Row(children = [
        dbc.Col(children=[
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
                )
                    ,
                dcc.Graph(
                    id='irrigation_plot', 
                    # style={"width": "50%"}
                    )
                ], 
                # style={"display": "flex",
                #     "flex-direction": "column",
                #     "align-items": "center",
                #     "min-height": "100vh",
                #     "width": "100vw"
                #     } # style can be used to override previous set styles
        #     )
        # ], 
        width = {"size": 4, "offset": 4}# width options: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/#:~:text=Specify%20order%20and%20offset
        ) # column 
    ]) # row
]) # container (or Div)

# Callbacks for handling tab changes and file uploads
@app.callback(
    Output('irrigation_plot', 'figure'),
    [Input('x_axis', 'value'),
     Input('y_axis', 'value')]
)
def make_plot(x_ax, y_ax):
    # print(f'x_ax: {x_ax}, y_ax: {y_ax})
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


