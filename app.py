import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from db_load import db_load_pasardki 
import pandas as pd

df = db_load_pasardki()
df['Date'] = pd.to_datetime(df['Date'])
df['Price'] = df['Price'].replace('NaN', float('nan'))
df['Price'] = df['Price'].fillna(0)

df = df.sort_values('Date')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('DKI Jakarta Market Price Commodities'),
    dcc.Dropdown(
        id='market-dropdown',
        options=[{'label': market, 'value': market} for market in df['MarketName'].unique()],
        multi=True,
        value=[],
        style={"width": "50%", "margin-bottom": "10px"}
    ),
    dcc.Dropdown(
        id='commodity-dropdown',
        options=[{'label': commodity, 'value': commodity} for commodity in df['Commodity'].unique()],
        value=df['Commodity'].unique()[0],
        style={"width": "50%", "margin-bottom": "10px"}
    ),
    html.Div(
        dcc.DatePickerRange(
            id='date-range',
            min_date_allowed=df['Date'].min(),
            max_date_allowed=df['Date'].max(),
            initial_visible_month=df['Date'].min(),
            start_date=df['Date'].min(),
            end_date=df['Date'].max()
        ),
        style={"width": "100%", "margin-bottom": "10px"}
    ),
    dcc.Graph(id='line-chart')
])


@app.callback(
    Output('line-chart', 'figure'),
    [Input('market-dropdown', 'value'),
     Input('commodity-dropdown', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_line_chart(selected_markets, selected_commodity, start_date, end_date):
    filtered_df = df[
        (df['MarketName'].isin(selected_markets)) &
        (df['Commodity'] == selected_commodity) &
        (df['Date'] >= start_date) &
        (df['Date'] <= end_date)
    ]
    fig = px.line(filtered_df, x='Date', y='Price', color='MarketName', category_orders={'Date': filtered_df['Date']})
    
    # Set y-axis range
    max_value = filtered_df['Price'].max()
    y_axis_range = [0, max_value * 1.1]  # Set y-axis range from min_value to max_value + 10%

    fig.update_yaxes(range=y_axis_range)
    
    return fig


if __name__ == '__main__':
    app.run_server(host='38.47.180.145', port=8050)
