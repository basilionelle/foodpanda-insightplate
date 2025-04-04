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

# Custom styling for dropdowns
dropdown_style = {
    'backgroundColor': 'rgba(255, 255, 255, 0.1)',
    'border': '1px solid rgba(255, 255, 255, 0.2)',
    'borderRadius': '10px',
    'color': 'white'
}

# Custom styling for dropdown options
dropdown_options_style = {
    'backgroundColor': '#0057B7',
    'color': 'white',
    'hover': {
        'backgroundColor': '#0098E5',
        'color': 'white'
    }
}

# Update plot layout with filter-friendly styling
plot_layout.update({
    'transition_duration': 500,
    'hovermode': 'closest',
    'dragmode': False,
    'modebar': {
        'bgcolor': 'rgba(0,0,0,0)',
        'color': 'white',
        'activecolor': '#0098E5'
    }
})

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

def create_filter_options(df):
    """Create options for filter dropdowns"""
    cities = sorted(df['City'].unique())
    food_types = sorted(df['FoodType'].unique())
    rating_ranges = ['All', '4.5+', '4.0-4.4', '3.5-3.9', 'Below 3.5']
    
    return {
        'cities': [{'label': city, 'value': city} for city in cities],
        'food_types': [{'label': food_type, 'value': food_type} for food_type in food_types],
        'rating_ranges': [{'label': rating, 'value': rating} for rating in rating_ranges]
    }

def filter_dataframe(df, city=None, food_type=None, rating_range=None):
    """Filter dataframe based on selected criteria"""
    filtered_df = df.copy()
    
    if city and city != 'All':
        filtered_df = filtered_df[filtered_df['City'] == city]
    
    if food_type and food_type != 'All':
        filtered_df = filtered_df[filtered_df['FoodType'] == food_type]
    
    if rating_range and rating_range != 'All':
        if rating_range == '4.5+':
            filtered_df = filtered_df[filtered_df['AverageRating'] >= 4.5]
        elif rating_range == '4.0-4.4':
            filtered_df = filtered_df[(filtered_df['AverageRating'] >= 4.0) & (filtered_df['AverageRating'] < 4.5)]
        elif rating_range == '3.5-3.9':
            filtered_df = filtered_df[(filtered_df['AverageRating'] >= 3.5) & (filtered_df['AverageRating'] < 4.0)]
        else:  # Below 3.5
            filtered_df = filtered_df[filtered_df['AverageRating'] < 3.5]
    
    return filtered_df

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
        
        # Filter Section
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Filters', style=title_style),
                        dbc.Row([
                            dbc.Col([
                                html.Label('City', style={'color': 'white', 'margin-bottom': '0.5rem'}),
                                dcc.Dropdown(
                                    id='city-filter',
                                    options=[{'label': 'All Cities', 'value': 'All'}],
                                    value='All',
                                    style=dropdown_style
                                )
                            ], width=4),
                            dbc.Col([
                                html.Label('Food Type', style={'color': 'white', 'margin-bottom': '0.5rem'}),
                                dcc.Dropdown(
                                    id='food-type-filter',
                                    options=[{'label': 'All Types', 'value': 'All'}],
                                    value='All',
                                    style=dropdown_style
                                )
                            ], width=4),
                            dbc.Col([
                                html.Label('Rating', style={'color': 'white', 'margin-bottom': '0.5rem'}),
                                dcc.Dropdown(
                                    id='rating-filter',
                                    options=[{'label': 'All Ratings', 'value': 'All'}],
                                    value='All',
                                    style=dropdown_style
                                )
                            ], width=4),
                        ], className='g-2')
                    ])
                ], style=card_style)
            ], width=12)
        ], className='mb-4'),
        
        # Map Section
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
        
        # Charts Section
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
        
        # Stats Row
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Quick Stats', style=title_style),
                        html.Div(id='stats-container', style={'color': 'white'})
                    ])
                ], style=card_style)
            ], width=12)
        ], className='mt-4'),
        
    ], style=app_style),
    
    dcc.Store(id='selected-city'),
    dcc.Store(id='filtered-data')
], fluid=True)

# Callbacks for filter updates
@app.callback(
    [Output('city-filter', 'options'),
     Output('food-type-filter', 'options'),
     Output('rating-filter', 'options')],
    [Input('filtered-data', 'data')]
)
def update_filters(data):
    df = pd.read_json(data) if data else load_data()
    filter_opts = create_filter_options(df)
    return [
        [{'label': 'All Cities', 'value': 'All'}] + filter_opts['cities'],
        [{'label': 'All Types', 'value': 'All'}] + filter_opts['food_types'],
        [{'label': 'All Ratings', 'value': 'All'}] + filter_opts['rating_ranges']
    ]

@app.callback(
    [Output('scatter-map', 'figure'),
     Output('food-type-chart', 'figure'),
     Output('rating-chart', 'figure'),
     Output('stats-container', 'children'),
     Output('filtered-data', 'data')],
    [Input('city-filter', 'value'),
     Input('food-type-filter', 'value'),
     Input('rating-filter', 'value')]
)
def update_dashboard(city, food_type, rating_range):
    # Load and filter data
    df = load_data()
    filtered_df = filter_dataframe(df, city, food_type, rating_range)
    
    # Create visualizations
    map_fig = create_scatter_map(filtered_df)
    food_type_fig = create_food_type_distribution(filtered_df)
    rating_fig = create_rating_distribution(filtered_df)
    
    # Create stats
    stats = html.Div([
        dbc.Row([
            dbc.Col([
                html.H5(f"Total Restaurants: {len(filtered_df)}", className='mb-2'),
                html.H5(f"Average Rating: {filtered_df['AverageRating'].mean():.2f}", className='mb-2'),
                html.H5(f"Most Common Food Type: {filtered_df['FoodType'].mode()[0]}", className='mb-2')
            ])
        ])
    ])
    
    return map_fig, food_type_fig, rating_fig, stats, filtered_df.to_json()

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
