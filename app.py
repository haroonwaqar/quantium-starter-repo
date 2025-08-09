import dash
import pandas as pd
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("processed_sales_data.csv")
df['date'] = pd.to_datetime(df['date'])

# Group by date to get total daily sales
daily_sales = df.groupby('date')['sales'].sum().reset_index()

fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Daily Sales of Pink Morsels',
    labels={'sales': 'Total Sales ($)', 'date': 'Date'}
)

# Add vertical line for price change
fig.add_shape(
    type="line",
    x0="2021-01-15",
    x1="2021-01-15",
    y0=0,
    y1=1,
    line=dict(color="red", dash="dash"),
    xref='x',
    yref='paper'
)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales Visualiser',
        style={'textAlign': 'center'}
    ),
    html.Div(children='''
        Visualising Pink Morsel sales before and after the 15 Jan 2021 price change.
    ''', style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)