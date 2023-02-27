import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Bootstrap
external_stylesheets = [{'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css',
     'rel': 'stylesheet', 'integrity': 'sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi',
     'crossorigin': 'anonymous'}]

# Initialize app
app = Dash(__name__,
           use_pages=True,
           external_stylesheets=external_stylesheets
           )

server = app.server

# Page layout
app.layout = dbc.Container(

    dash.page_container

)

if __name__ == '__main__':
    app.run_server(debug=True)