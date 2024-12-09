import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import folium
from folium.plugins import HeatMap
import plotly.express as px

# Load and initial data exploration
df = pd.read_csv('C:/Users/c/Downloads/Bank_analysis/nyc_airbnb_analysis/Data/AB_NYC_2019.csv')

# Data cleaning and preparation
def clean_data(df):
    # Remove outliers in price
    df = df[df['price'] <= df['price'].quantile(0.99)]
    
    # Handle missing values
    df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
    
    return df

df = clean_data(df)

# Price Analysis by Neighborhood
def analyze_neighborhood_prices():
    neighborhood_prices = df.groupby('neighbourhood_group')['price'].agg(['mean', 'median', 'count'])
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='neighbourhood_group', y='price', data=df)
    plt.title('Price Distribution by Borough')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('price_distribution.png')
    
    return neighborhood_prices

# Geographic visualization
def create_price_heatmap():
    map_ny = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], 
                       zoom_start=11)
    
    heat_data = [[row['latitude'], row['longitude'], row['price']] 
                 for idx, row in df.iterrows()]
    
    HeatMap(heat_data).add_to(map_ny)
    map_ny.save('price_heatmap.html')

# Room type analysis
def analyze_room_types():
    room_type_stats = df.groupby('room_type').agg({
        'price': ['mean', 'count'],
        'number_of_reviews': 'sum'
    }).round(2)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='room_type', y='price', data=df)
    plt.title('Average Price by Room Type')
    plt.tight_layout()
    plt.savefig('room_type_analysis.png')
    
    return room_type_stats

# Price prediction model
def build_price_prediction_model():
    # Feature engineering
    features = ['latitude', 'longitude', 'minimum_nights', 'number_of_reviews', 'reviews_per_month']
    X = df[features]
    y = df['price']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    return model, r2, rmse

# Clustering analysis
def perform_clustering():
    # Prepare data for clustering
    cluster_features = ['price', 'latitude', 'longitude']
    X_cluster = df[cluster_features]
    
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_cluster)
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=5, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)
    
    # Visualize clusters
    fig = px.scatter_mapbox(df, 
                           lat='latitude', 
                           lon='longitude', 
                           color='cluster',
                           size='price',
                           mapbox_style="carto-positron",
                           zoom=10)
    fig.write_html('clusters_map.html')
    
    return df['cluster'].value_counts()

# Main analysis execution
if __name__ == "__main__":
    print("Starting NYC Airbnb Analysis...")
    
    # Run analyses
    neighborhood_stats = analyze_neighborhood_prices()
    create_price_heatmap()
    room_type_stats = analyze_room_types()
    model, r2_score, rmse = build_price_prediction_model()
    cluster_stats = perform_clustering()
    
    # Save results to CSV
    neighborhood_stats.to_csv('neighborhood_statistics.csv')
    room_type_stats.to_csv('room_type_statistics.csv')
    
    print("Analysis complete! Check the output files for results.") 