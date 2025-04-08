#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# 🍽️ FoodPanda InsightPlate: Restaurant Analytics Dashboard
## Data-Driven Dining Decisions in the Philippines

This script provides data visualization and analysis of FoodPanda restaurant data
across Philippine cities. It can be run directly or converted to a Jupyter notebook.
"""

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

def setup_visualization_style():
    """Set up the visualization style for consistent, clean plots."""
    plt.style.use('seaborn')
    plt.rcParams['figure.figsize'] = [12, 8]
    plt.rcParams['font.size'] = 12

def load_and_clean_data():
    """Load and clean the FoodPanda restaurant datasets."""
    # Load the datasets
    restos = pd.read_csv('restos.csv')
    restos_2025 = pd.read_csv('restos_2025.csv')

    # Clean restos dataset
    # Convert Reviewers column from string format (e.g., "(100+)") to numeric
    restos['Reviewers'] = restos['Reviewers'].str.replace(r'[()+]', '', regex=True)
    restos['Reviewers'] = pd.to_numeric(restos['Reviewers'], errors='coerce').fillna(0)

    # Drop unnecessary columns from restos
    restos = restos.drop(columns=['StoreName', 'Location'])

    # Merge datasets
    restos_df = pd.concat([restos, restos_2025], ignore_index=True)

    # Clean merged dataset
    restos_df = restos_df.dropna(subset=['FoodType'])
    restos_df = restos_df.drop_duplicates()

    # Standardize city names
    restos_df['City'] = restos_df['City'].str.title()
    
    return restos_df

def print_basic_statistics(df):
    """Print basic statistics about the dataset."""
    print("\n=== Dataset Overview ===")
    print("-" * 25)
    print(f"Total number of restaurants: {len(df)}")
    print(f"Number of cities: {df['City'].nunique()}")
    print(f"Number of cuisine types: {df['FoodType'].nunique()}")
    print("\nTop 10 Cities by Number of Restaurants:")
    print("-" * 25)
    print(df['City'].value_counts().head(10))

def plot_rating_distribution(df):
    """Create visualizations for rating distribution analysis."""
    plt.figure(figsize=(15, 10))
    gs = GridSpec(2, 2)

    # Plot 1: Overall Rating Distribution
    plt.subplot(gs[0, 0])
    sns.histplot(data=df, x='AverageRating', bins=20)
    plt.title('Distribution of Restaurant Ratings')
    plt.xlabel('Average Rating')
    plt.ylabel('Number of Restaurants')

    # Plot 2: Top Cities by Average Rating
    plt.subplot(gs[0, 1])
    city_ratings = df.groupby('City')['AverageRating'].mean().sort_values(ascending=False)
    city_ratings.head(10).plot(kind='bar')
    plt.title('Top 10 Cities by Average Rating')
    plt.xticks(rotation=45)
    plt.xlabel('City')
    plt.ylabel('Average Rating')

    # Plot 3: Top Cuisine Types
    plt.subplot(gs[1, :])
    cuisine_counts = df['FoodType'].value_counts().head(15)
    cuisine_counts.plot(kind='bar')
    plt.title('Top 15 Most Common Cuisine Types')
    plt.xticks(rotation=45)
    plt.xlabel('Cuisine Type')
    plt.ylabel('Number of Restaurants')

    plt.tight_layout()
    plt.show()

def plot_review_analysis(df):
    """Create visualizations for review volume analysis."""
    plt.figure(figsize=(15, 10))
    gs = GridSpec(2, 2)

    # Plot 1: Review Volume Distribution
    plt.subplot(gs[0, 0])
    sns.histplot(data=df[df['Reviewers'] < df['Reviewers'].quantile(0.95)], 
                x='Reviewers', bins=50)
    plt.title('Distribution of Review Volumes\n(excluding outliers)')
    plt.xlabel('Number of Reviews')
    plt.ylabel('Number of Restaurants')

    # Plot 2: Top Cities by Total Reviews
    plt.subplot(gs[0, 1])
    city_reviews = df.groupby('City')['Reviewers'].sum().sort_values(ascending=False)
    city_reviews.head(10).plot(kind='bar')
    plt.title('Top 10 Cities by Total Reviews')
    plt.xticks(rotation=45)
    plt.xlabel('City')
    plt.ylabel('Total Reviews')

    # Plot 3: Rating vs Reviews Scatter Plot
    plt.subplot(gs[1, :])
    plt.scatter(df['Reviewers'], df['AverageRating'], alpha=0.5)
    plt.title('Relationship between Number of Reviews and Average Rating')
    plt.xlabel('Number of Reviews')
    plt.ylabel('Average Rating')

    plt.tight_layout()
    plt.show()

def plot_cuisine_analysis(df):
    """Create visualizations for cuisine type analysis."""
    # Get top 10 cuisine types
    top_cuisines = df['FoodType'].value_counts().head(10).index
    cuisine_data = df[df['FoodType'].isin(top_cuisines)]

    plt.figure(figsize=(15, 10))
    gs = GridSpec(2, 1, height_ratios=[2, 1])

    # Plot 1: Box plot of ratings by cuisine type
    plt.subplot(gs[0])
    sns.boxplot(data=cuisine_data, x='FoodType', y='AverageRating')
    plt.title('Rating Distribution by Cuisine Type')
    plt.xticks(rotation=45)
    plt.xlabel('Cuisine Type')
    plt.ylabel('Average Rating')

    # Plot 2: Average reviews by cuisine type
    plt.subplot(gs[1])
    cuisine_reviews = cuisine_data.groupby('FoodType')['Reviewers'].mean().sort_values(ascending=False)
    cuisine_reviews.plot(kind='bar')
    plt.title('Average Number of Reviews by Cuisine Type')
    plt.xticks(rotation=45)
    plt.xlabel('Cuisine Type')
    plt.ylabel('Average Number of Reviews')

    plt.tight_layout()
    plt.show()

def print_conclusions(df):
    """Generate and print conclusions from the analysis."""
    top_cities = df.groupby('City').size().sort_values(ascending=False).head(3)
    top_rated_cities = df.groupby('City')['AverageRating'].mean().sort_values(ascending=False).head(3)
    top_cuisines = df['FoodType'].value_counts().head(3)
    top_rated_cuisines = df.groupby('FoodType')['AverageRating'].mean().sort_values(ascending=False).head(3)

    print("\n=== Key Insights from the Analysis ===")
    print("-" * 35)
    print("\n1. City Analysis:")
    print(f"   - Top cities by number of restaurants: {', '.join(top_cities.index)}")
    print(f"   - Highest rated cities: {', '.join(top_rated_cities.index)}")
    
    print("\n2. Cuisine Analysis:")
    print(f"   - Most common cuisine types: {', '.join(top_cuisines.index)}")
    print(f"   - Highest rated cuisine types: {', '.join(top_rated_cuisines.index)}")
    
    print("\n3. Rating Patterns:")
    print(f"   - Average rating across all restaurants: {df['AverageRating'].mean():.2f}")
    print(f"   - Median number of reviews: {df['Reviewers'].median():.0f}")

def main():
    """Main function to run the analysis."""
    # Setup
    setup_visualization_style()
    
    # Load and process data
    df = load_and_clean_data()
    
    # Generate insights
    print_basic_statistics(df)
    plot_rating_distribution(df)
    plot_review_analysis(df)
    plot_cuisine_analysis(df)
    print_conclusions(df)

if __name__ == "__main__":
    main()
