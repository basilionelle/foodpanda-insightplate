# -*- coding: utf-8 -*-
"""
FoodPanda Restaurant Analysis
Data101 Final Project

Data Preparation Steps:
1. Merge two CSV files: 'restos (1).csv' and 'restos_2025.csv'
2. Clean and process the merged data
3. Create interactive dashboard for analysis
"""

# Part 1: Install required packages for Google Colab
try:
    import google.colab
    IN_COLAB = True
    print("Running in Google Colab...")
    !pip install dash==2.9.3 dash-bootstrap-components==1.4.1 plotly==5.13.1 jupyter-dash==0.4.2
    from google.colab import files
    import nest_asyncio
    nest_asyncio.apply()
except:
    IN_COLAB = False
    print("Not running in Google Colab")

# Part 2: Import required libraries
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash

# Part 3: Data Merging
def merge_csv_files():
    """Merge the two restaurant CSV files into a single dataset."""
    try:
        # For Colab: Upload the source files if they don't exist
        if IN_COLAB:
            print("Please upload 'restos (1).csv'...")
            files.upload()
            print("\nPlease upload 'restos_2025.csv'...")
            files.upload()
        
        # Read both CSV files
        df1 = pd.read_csv('restos (1).csv')
        df2 = pd.read_csv('restos_2025.csv')
        
        # Concatenate the dataframes
        combined_df = pd.concat([df1, df2], ignore_index=True)
        
        # Clean the data
        combined_df = combined_df.dropna(subset=['FoodType'])
        combined_df = combined_df.drop_duplicates()
        combined_df['City'] = combined_df['City'].str.title()
        
        # Save the combined dataframe
        combined_df.to_csv('FoodpandaCombo.csv', index=False)
        print("CSV files merged successfully!")
        return combined_df
        
    except Exception as e:
        print(f"Error merging files: {str(e)}")
        print("\nPlease ensure:")
        print("1. Both CSV files are uploaded correctly")
        print("2. Files are named exactly 'restos (1).csv' and 'restos_2025.csv'")
        print("3. Files contain the expected columns")
        return None

# Part 4: Dashboard Setup
# Load and process the data
def load_data():
    # Read the combined CSV file
    df = pd.read_csv('FoodpandaCombo.csv')
    
    # Clean the data
    df['City'] = df['City'].str.title()
    df = df.dropna(subset=['FoodType'])
    df = df.drop_duplicates()
    
    return df

# Add geospatial information
city_coords = {
    'Manila': (14.599512, 120.984222),
    'Cebu City': (10.316720, 123.890710),
    'Dagupan Pangasinan': (16.043000, 120.334000),
    'Davao City Davao Del Sur': (7.207573, 125.395874),
    'Koronadal South Cotabato': (6.497396, 124.847160),
    'Lapu-Lapu City Cebu': (10.266182, 123.997292),
    'Makati City': (14.556586, 121.023415),
    'Malolos Bulacan': (14.852739, 120.816040),
    'Mandaluyong City': (14.616700, 121.033300),
    'Marikina': (14.637300, 121.091700),
    'Muntinlupa City': (14.408133, 121.041466),
    'Ormoc Leyte': (11.006390, 124.607500),
    'Pasay City': (14.537752, 121.001381),
    'Pasig City': (14.560500, 121.076500),
    'Quezon City': (14.676208, 121.043861),
    'San Juan': (14.604200, 121.029900),
    'Taguig City': (14.517600, 121.050900),
    'Valencia Bukidnon': (7.900000, 125.083333)
}

# Create visualization functions
# Graph styling
plot_layout = {
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'font': {
        'family': 'SF Pro Display, -apple-system, BlinkMacSystemFont, sans-serif',
        'color': 'white'
    },
    'margin': dict(t=30, l=10, r=10, b=10)
}

def create_scatter_map(df):
    # Add latitude and longitude to the dataframe
    df['Latitude'] = df['City'].map(lambda x: city_coords.get(x, (None, None))[0])
    df['Longitude'] = df['City'].map(lambda x: city_coords.get(x, (None, None))[1])
    
    # Create city-level aggregations
    city_df = df.groupby('City').agg({
        'AverageRating': 'mean',
        'Reviewers': 'sum'
    }).reset_index()
    
    city_df['Latitude'] = city_df['City'].map(lambda x: city_coords.get(x, (None, None))[0])
    city_df['Longitude'] = city_df['City'].map(lambda x: city_coords.get(x, (None, None))[1])
    
    # Create scatter map
    fig = px.scatter_mapbox(
        city_df,
        lat='Latitude',
        lon='Longitude',
        size='Reviewers',
        color='AverageRating',
        hover_name='City',
        zoom=5,
        mapbox_style='carto-positron',
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        mapbox=dict(center=dict(lat=12.8797, lon=121.7740)),
        **plot_layout
    )
    
    return fig

def create_food_type_distribution(df, city=None):
    # Filter by city if specified
    if city:
        df = df[df['City'] == city]
    
    # Get food type distribution
    food_type_counts = df['FoodType'].value_counts().head(10)
    
    # Create bar chart
    fig = px.bar(
        x=food_type_counts.values,
        y=food_type_counts.index,
        orientation='h',
        labels={'x': 'Number of Restaurants', 'y': 'Food Type'},
        color=food_type_counts.values,
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        **plot_layout,
        showlegend=False,
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255,255,255,0.1)',
            title_font=dict(color='white')
        ),
        yaxis=dict(
            showgrid=False,
            title_font=dict(color='white')
        )
    )
    
    return fig

def create_rating_distribution(df, city=None):
    # Filter by city if specified
    if city:
        df = df[df['City'] == city]
    
    # Create histogram
    fig = px.histogram(
        df,
        x='AverageRating',
        nbins=20,
        labels={'AverageRating': 'Average Rating', 'count': 'Number of Restaurants'},
        color_discrete_sequence=['rgba(255,255,255,0.6)']
    )
    
    fig.update_layout(
        **plot_layout,
        bargap=0.1,
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255,255,255,0.1)',
            title_font=dict(color='white')
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255,255,255,0.1)',
            title_font=dict(color='white')
        )
    )
    
    return fig

# Initialize the Dash app
if IN_COLAB:
    app = JupyterDash(__name__, external_stylesheets=[dbc.themes.FLATLY])
else:
    app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# Define the layout
app.layout = dbc.Container([
    html.Div([
        html.H1('FoodPanda Restaurant Analysis', style=title_style),
        html.P('Interactive Dashboard for Restaurant Data Analysis', 
               style={'color': 'white', 'opacity': '0.7', 'margin-bottom': '2rem'}),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Restaurant Distribution Map', style=title_style),
                        dcc.Graph(id='scatter-map')
                    ])
                ], style=card_style)
            ], width=12)
        ]),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Food Type Distribution', style=title_style),
                        dcc.Graph(id='food-type-chart')
                    ])
                ], style=card_style)
            ], width=6),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Rating Distribution', style=title_style),
                        dcc.Graph(id='rating-chart')
                    ])
                ], style=card_style)
            ], width=6)
        ], className='mt-4'),
    ], style=app_style),
    
    dcc.Store(id='selected-city')
], fluid=True)

# Callbacks
@app.callback(
    Output('selected-city', 'data'),
    Input('scatter-map', 'clickData')
)
def update_selected_city(clickData):
    if clickData:
        return clickData['points'][0]['hovertext']
    return None

@app.callback(
    [Output('food-type-chart', 'figure'),
     Output('rating-chart', 'figure')],
    Input('selected-city', 'data')
)
def update_charts(selected_city):
    df = load_data()
    return (
        create_food_type_distribution(df, selected_city),
        create_rating_distribution(df, selected_city)
    )

@app.callback(
    Output('scatter-map', 'figure'),
    Input('scatter-map', 'id')
)
def update_map(_):
    df = load_data()
    return create_scatter_map(df)

# Custom CSS for the dashboard
app_style = {
    'background': 'linear-gradient(165deg, #0057B7, #0098E5)',
    'min-height': '100vh',
    'padding': '1.5rem',
    'font-family': 'SF Pro Display, -apple-system, BlinkMacSystemFont, sans-serif'
}

card_style = {
    'background': 'rgba(255, 255, 255, 0.06)',
    'backdrop-filter': 'blur(8px)',
    'border': '1px solid rgba(255, 255, 255, 0.08)',
    'border-radius': '20px',
    'transition': 'transform 0.2s cubic-bezier(0.4, 0, 0.2, 1)',
    'margin-bottom': '1rem'
}

title_style = {
    'color': 'white',
    'opacity': '0.9',
    'letter-spacing': '-0.2px',
    'font-weight': '400'
}

# Run the app
if __name__ == '__main__':
    try:
        if IN_COLAB:
            # For Google Colab, use JupyterDash
            app = JupyterDash(__name__, 
                            external_stylesheets=[dbc.themes.FLATLY, 'https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;500&display=swap'])
            
            print("\nChoose an option:")
            print("1. Merge CSV files (if you have 'restos (1).csv' and 'restos_2025.csv')")
            print("2. Upload existing FoodpandaCombo.csv")
            
            choice = input("Enter your choice (1 or 2): ")
            
            if choice == "1":
                # Merge the CSV files
                df = merge_csv_files()
                if df is None:
                    raise Exception("Failed to merge CSV files")
                print("\nData merged successfully! Using the merged dataset for the dashboard.")
            else:
                # File upload for Colab
                print("\nPlease upload your FoodpandaCombo.csv file")
                uploaded = files.upload()
                filename = next(iter(uploaded))
                df = pd.read_csv(filename)
            
            # Run the server
            app.run_server(mode='external', port=8050, debug=True)
            
        else:
            # For local development
            app = Dash(__name__, 
                      external_stylesheets=[dbc.themes.FLATLY, 'https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;500&display=swap'])
            df = pd.read_csv('FoodpandaCombo.csv')
            app.run_server(debug=True)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you have the required CSV files in your working directory")
        print("2. Check that all required packages are installed")
        print("3. Ensure you have a stable internet connection for the dashboard")
        print("4. If running in Colab, make sure to:")
        print("   - Run this notebook with a GPU runtime")
        print("   - Allow pop-ups for the dashboard to open in a new tab")
        print("   - Keep the notebook running while using the dashboard")

"""
Notes for running in Google Colab:
1. Choose option 1 if you have both original CSV files ('restos (1).csv' and 'restos_2025.csv')
2. Choose option 2 if you already have the merged 'FoodpandaCombo.csv' file
3. The dashboard will open in a new browser tab
4. Click on cities in the map to filter the data
5. Use the charts to analyze restaurant distribution and ratings
"""
