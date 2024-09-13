'''
BChoat 2024/09/11

Create two basic plotly plots. One using plotly express (think Seaborn), and the other 
    using graph objects (think matplotlib)

Some functions/attributes of note:
- Can use plotly.express or plotly.graph_objects
- express is easier and faster but more prescriptive
- when using graph_objects, each trace must be drawn individually, so 
    loops are typically used if wanting to color by category, for example
- The pop-up text and layout can be modified with a mix of python
    and html. Note the <br> tag in the code doing this. THat is html
    for 'next line'. Simliar to '\n' in many languages
- 
'''

# import libraries
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


def create_px_plot(df: pd.DataFrame, col1: str, col2: str, cat_col: str=None) -> go.Figure:
    '''
    Creates a simple scatter plot using plotly express.

    For a graph gallery, see: https://plotly.com/python/plotly-express/

    Inputs
    -----------------------
    df (pandas DataFrame): A dataframe with at least numerical columns
    col1 (string): Column name in df holding numerical values
    col2 (string): Second column name in df holding numerical values
    cat_col (string; optional): 3rd column name that holds categories by which points will
        be colored
    
    Returns
    ----------------------
    plot (Plotly plot object): this lot will automatically be displayed
        but also returned so user can call it again.
    '''
    
    if cat_col:
        # create scatter plot and color points by cat_col
        fig = px.scatter(df, x=col1, y=col2, color=cat_col)
    else:
        # create scatter plot and make points a constant color
        fig = px.scatter(df, x=col1, y=col2)

        fig.update_traces(marker=dict(color='cyan'))

    # Update layout if needed
    fig.update_layout(
        title='Scatter Plot Example',
        xaxis_title='Day Of Season',
        yaxis_title='Rain (cm)',
        legend_title='I am Legend'
    )

    # fig.show()

    return fig


def create_go_plot(df: pd.DataFrame, col1: str, col2: str, cat_col: str) -> go.Figure:
    '''
    Creates a simple scatter plot using plotly express.

    For a graph gallery, see: https://plotly.com/python/plotly-express/

    Inputs
    -----------------------
    df (pandas DataFrame): A dataframe with at least numerical columns
    col1 (string): Column name in df holding numerical values
    col2 (string): Second column name in df holding numerical values
    cat_col (string; optional): 3rd column name that holds categories by which points will
        be colored
    
    Returns
    ----------------------
    plot (Plotly plot object): this lot will automatically be displayed
        but also returned so user can call it again.
    '''

    fig = go.Figure()

    if cat_col:
        # If `cat_col` is provided, use it to color points
        categories = df[cat_col].unique()
        for category in categories:
            subset = df[df[cat_col] == category]
            fig.add_trace(go.Scatter(
                x=subset[col1],
                y=subset[col2],
                mode='markers',
                name=category,
                hovertext=df.apply(
                    lambda row: (f'Day: {row[col1]}<br>'
                                 f'Rain (cm): {row[col2]}<br>'
                                 f'Irrigated: {row[cat_col]}'), 
                    axis=1),
                hovertemplate='%{hovertext}<extra></extra>'  # Custom pop-up format
            ))
    else:
        # Create a scatter plot without coloring
        fig.add_trace(go.Scatter(
            x=df[col1],
            y=df[col2],
            mode='markers',
            marker=dict(color='orange')
        ))

    # update attributes of traces. In this case updating pop up layout/text
    fig.update_traces(
        hovertext=df.apply(
                lambda row: (f'Day: {row[col1]}<br>'
                                f'Rain (cm): {row[col2]}<br>'
                                f'Irrigated: {row[cat_col]}'), 
                axis=1),
        hovertemplate='%{hovertext}<extra></extra>'  # Custom pop-up format
    )

    # Update layout if needed
    fig.update_layout(
        title='Scatter Plot Example',
        xaxis_title='Day Of Season' if col1=='Day' else col1,
        yaxis_title='Rain (cm)' if col2=='Rain_cm' else col2,
        legend_title='I am Legend'
    )

    # fig.show()

    return fig


if __name__ == '__main__':

    # how many data points to work with?
    n_in = 100
    # random numbers representing irrigated or not
    rndm_numbers = np.random.binomial(1, 0.25, n_in)

    # dataframe to work with
    df_work = pd.DataFrame({
        'Day': [i+1 for i in range(n_in)],
        'Rain_cm': np.round(np.random.exponential(scale=1, size=n_in), 4),
        'Irrigated': ['yes' if i == 1 else 'no' for i in rndm_numbers]
    })

    # make plot with plotly express
    fig_px = create_px_plot(
        df=df_work, 
        col1='Day', 
        col2='Rain_cm', 
        cat_col='Irrigated'
        )
    
    # display plot
    fig_px.show()

    # make plot with graph-objects
    fig_go = create_go_plot(
        df=df_work, 
        col1='Day', 
        col2='Rain_cm', 
        cat_col='Irrigated'
        )

    # display plot
    fig_go.show()



    # after returning a plotly graph_object Figure object, you can still update it
    fig_go.add_annotation(
        x=50,
        y=2.5,
        text="THIS IS A DEMONSTRATION<br>AND IS <span style='color: red'>HTML</span>"
    )

    fig_go.show()