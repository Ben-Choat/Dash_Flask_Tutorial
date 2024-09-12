'''
BChoat 2024/09/12

Create a plotly plot to be rendered in plotly.html.

Some Notes:
Describe how to pass plot to html 

'''


# load libraries
from C_PlotlyPlots import create_go_plot
import numpy as np
import pandas as pd
from flask import render_template, request



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


# def route
# @bp.route('/plot', methods=['GET', 'POST'])
def plotRender():

    columns = df_work.columns
    x_column = request.form.get('x_column', columns[0])
    print(x_column)

    # # create plot
    plot = create_go_plot(df_work, x_column)

    # convert to html
    plot_html = plot.to_html(full_html=False)

    # render template with plot html and x_column for use in the form
    return render_template('plot.html',
                           plot_html=plot_html,
                            x_column=x_column,
                            columns=columns)