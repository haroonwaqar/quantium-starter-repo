import dash
import pandas as pd
from dash import dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("processed_sales_data.csv")
# df['date'] = pd.to_datetime(df['date'])

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),

    dcc.RadioItems(
        id='region-filter',
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"}
        ],
        value='all',
        labelStyle={'display': 'inline-block', 'margin': '10px'}
    ),

    dcc.Graph(id='sales-line-chart')
], style={"fontFamily": "Arial", "padding": "20px"})


# Callback to update chart
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f"Sales Over Time ({selected_region.capitalize()})",
        labels={'date': 'Date', 'sales': 'Sales Amount'}
    )
    fig.update_layout(template='plotly_dark')  # optional theme
    return fig

if __name__ == '__main__':
    app.run(debug=True)