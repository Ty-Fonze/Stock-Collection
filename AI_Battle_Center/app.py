import dash
from dash import html
from dash.dependencies import Input, Output
import DynamicWidgets  # Import the new component

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Super AI Trading Assistant"

# App layout
app.layout = html.Div(
    children=[
        DynamicWidgets.DynamicWidgets()  # Use the new DynamicWidgets component
    ]
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)