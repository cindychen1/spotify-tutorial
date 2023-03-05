# Imports
import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output  


# Creating the app
app = Dash(__name__)

# Read file 
df = pd.read_csv('Spotify Data.csv')
df['duration']=df['duration_ms']/1000
df_year = df.groupby('year').mean(numeric_only=True).reset_index()
song_features = ['acousticness','speechiness','danceability','energy',
                 'instrumentalness','liveness','valence','duration']


# App layout
app.layout = html.Div([
    html.H1(children="Spotify Data"),
    html.P(children=(["Observe trends in Spotify songs over time",
                     " and the distribution of traits in popular songs.",html.Br(),
                     'Data: Kaggle, "Top Hits Spotify from 2000-2019"']),),
    dcc.Dropdown(id ='dropdown',
        options = [
            {"label": song_feature, "value": song_feature}
            for song_feature in song_features
            ],
        value = 'danceability'),
    dcc.Graph(id ='graph'),
    dcc.Dropdown(id ='dropdown2',
        options = [
            {"label": song_feature, "value": song_feature}
            for song_feature in song_features
            ],
        value = 'danceability'),
    dcc.Graph(id ='box'),
    dcc.Dropdown(id ='dropdown3',
        options = [
            {"label": song_feature, "value": song_feature}
            for song_feature in song_features
            ],
        value = 'danceability'),
    dcc.Graph(id ='line'),
    dcc.Dropdown(id ='dropdown4',
        options = [
            {"label": song_feature, "value": song_feature}
            for song_feature in song_features
            ],
        value = 'danceability'),
    dcc.Graph(id ='scatter'),   
    ])


# Callback for Histograms
@app.callback(Output(component_id='graph', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = px.histogram(df,x=dropdown_value)
    fig.update_layout(title = 'Distribution of Song Features',
                      xaxis_title = 'Song Feature',
                      yaxis_title = 'Frequency'
                      )
    return fig

# Callback for Boxplots
@app.callback(Output(component_id='box', component_property= 'figure'),
              [Input(component_id='dropdown2', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = px.box(df,x='year',y=dropdown_value)
    fig.update_layout(title = 'Distribution of Song Features over Time',
                      xaxis_title = 'Year',
                      yaxis_title = dropdown_value
                      )
    return fig

# Callback for Lineplots
@app.callback(Output(component_id='line', component_property= 'figure'),
              [Input(component_id='dropdown3', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = px.line(df_year,x='year',y=dropdown_value)
    fig.update_layout(title = 'Song Features over Time',
                      xaxis_title = 'Year',
                      yaxis_title = dropdown_value
                      )
    return fig

# Callback for Scatterplots
@app.callback(Output(component_id='scatter', component_property= 'figure'),
              [Input(component_id='dropdown4', component_property= 'value')])
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = px.scatter(df,x=dropdown_value,y='popularity')
    fig.update_layout(title = 'Song Features vs Popularity',
                      xaxis_title = dropdown_value,
                      yaxis_title = 'Popularity'
                      )
    return fig


# Run app
if __name__ == '__main__': 
    app.run_server(debug=True)
