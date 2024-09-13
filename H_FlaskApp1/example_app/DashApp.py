'''
BChoat 2024/09/12

Same as F_DashBootsrapComp.py, except modified
to be rendered within an iframe in flask.
'''


# load libraries
from dash import Dash, dcc, html
from .PlotlyPlotFuncts import create_go_plot
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
# app = Dash(external_stylesheets=[dbc.themes.CYBORG])
# app = Dash(external_stylesheets=[dbc.themes.GRID])
def create_dash_app(server): 
    # Create Dash app instance with Bootstrap theme
    app = Dash(__name__, 
                    server=server, 
                    url_base_pathname='/dashApp/', 
                    external_stylesheets=[dbc.themes.CYBORG,
                                        #  'assets/bootstrap.css',
                                        #  'assets/supplement.css'
                                         ], # )
                                         suppress_callback_exceptions=True)


    # app layout
    # dbc.Container initiates bootstraps grid system (screen split to 12 columns, and can define rows)
    app.layout = dbc.Container(children=[ 
    # app.layout = html.Div(children=[
        dbc.Row(children=[
            dbc.Col(children = [
                # html.Div(children=[
                    html.H1('~~~~Basic Dash Example~~~~'),
        #     ], width={"size": 10, "offset": 1}
        #     )
        #     ]),
        # dbc.Row(children = [
        #     dbc.Col(children=[
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
                        # style={"width": "20%"}
                    )
                        ,
                    dcc.Graph(
                        id='irrigation_plot', 
                        # style={"width": "50%"}
                        )
                    ],  
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
    # app.run_server(debug=True) # other options available here too

    return app


