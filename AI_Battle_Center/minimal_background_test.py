import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        'backgroundImage': 'url("nebula_background.jpg")',
        'backgroundSize': 'cover',
        'backgroundAttachment': 'fixed',
        'backgroundPosition': 'center',
        'height': '100vh',
        'width': '100vw',
    },
    children=[
        html.H1("Background Test", style={'color': 'white', 'textAlign': 'center', 'paddingTop': '40vh'})
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)