import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('motivartions.csv')

app.Layout = html.Div(children=[
    html.H1(
        children='今日のモチベーションの変化',
        style={
            'textAlign': 'center',
            'color': 'black'
        }
    ),
    dcc.Graph(
        id='exsample-graph',
        figure={
            'data': [
                go.Scatter(
                    x=df['times'],
                    y=df['motivartions'],
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size': 10,
                        'color': 'blue'
                    },
                    name='今日のモチベーション'
                )
            ],
            'layout': go.Layout(
                xaxis={'title': '時刻'},
                yaxis={'title': 'モチベーション'},

            )
        }
    ),
    html.H2(
        children='今日の日付',
        style={
            'textAlign': 'black',
            'color': 'black'
        }
    )
])

if __name__ == 'main':
    app.run_server(debug=True)
