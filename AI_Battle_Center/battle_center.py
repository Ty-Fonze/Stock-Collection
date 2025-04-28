import dash
from dash import html

app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        'position': 'relative',
        'height': '100vh',
        'width': '100vw',
        'background': '#333333',  # Dark grey background
        'color': 'white',
        'overflow': 'hidden',
    },
    children=[
        # Central Adeptus Mechanicus icon with breathing red effect
        html.Div(
            id='mechanicus-container',
            style={
                'position': 'absolute',
                'top': '50%',
                'left': '50%',
                'width': '180px',  # Size of the container
                'height': '180px',  # Size of the container
                'transform': 'translate(-50%, -50%)',
                'borderRadius': '50%',  # Maintain circular shape
                'backgroundColor': '#333333',  # Match the gray page background
                'animation': 'breathing 4s infinite',  # Slower breathing effect
                'overflow': 'hidden',  # Ensure no extra spacing
                'display': 'flex',  # Use flexbox for centering
                'alignItems': 'center',  # Center logo vertically
                'justifyContent': 'center',  # Center logo horizontally
            },
            children=[
                # Adeptus Mechanicus logo
                html.Img(
                    src="/assets/adeptus_mechanicus_logo.png",  # Path to the logo
                    style={
                        'width': '90%',  # Slightly smaller than container
                        'height': '90%',  # Maintain aspect ratio
                        'objectFit': 'contain',  # Ensure logo fits without distortion
                    },
                )
            ],
        ),
    ],
)

# Add CSS styles for breathing effect and interaction color
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            /* Breathing effect animation */
            @keyframes breathing {
                0% {
                    box-shadow: 0 0 10px 5px rgba(255, 0, 0, 0.8);
                }
                50% {
                    box-shadow: 0 0 20px 10px rgba(255, 0, 0, 0);
                }
                100% {
                    box-shadow: 0 0 10px 5px rgba(255, 0, 0, 0.8);
                }
            }

            /* Interaction color override to red */
            :focus, :hover, :active {
                outline-color: red;  /* Change interaction outline to red */
            }
        </style>
    </head>
    <body>
        <div id="react-entry-point">
            <div id="dash-loading"></div>
            {%app_entry%} <!-- Required for Dash content -->
        </div>
        <footer>
            {%config%} <!-- Required for Dash configuration -->
            {%scripts%} <!-- Required for Dash scripts -->
            {%renderer%} <!-- Required for DashRenderer -->
        </footer>
    </body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)