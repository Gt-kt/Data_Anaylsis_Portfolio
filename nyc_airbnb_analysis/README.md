# NYC Airbnb Data Analysis

## Overview
This analysis explores the Airbnb market in New York City using the 2019 dataset. The analysis includes price distributions, geographical patterns, room type analysis, and predictive modeling.

## Results Summary

### Visualizations

#### 1. Price Distribution (price_distribution.png)
- Shows the distribution of Airbnb prices across different NYC boroughs
- Helps identify which boroughs are most expensive/affordable
- Reveals price outliers and typical price ranges per borough
- Key insight: Manhattan shows the highest median prices, followed by Brooklyn

#### 2. Room Type Analysis (room_type_analysis.png)
- Compares average prices across different room types (Entire home/apt, Private room, Shared room)
- Shows the distribution of listings by room type
- Includes review counts for each room type
- Key insight: Entire homes/apartments command the highest prices but might not have the most reviews

#### 3. Price Heatmap (price_heatmap.html)
- Interactive map showing price density across NYC
- Darker areas indicate higher concentration of expensive listings
- Helps identify premium and budget-friendly neighborhoods
- Key insight: Clear price hotspots around central Manhattan and popular Brooklyn areas

#### 4. Clustering Map (clusters_map.html)
- Interactive visualization of 5 distinct listing clusters
- Clusters are based on price, latitude, and longitude
- Size of points indicates price
- Key insight: Shows clear geographical patterns in pricing and listing characteristics

### Statistical Reports

#### 1. Neighborhood Statistics (neighborhood_statistics.csv)
Contains for each borough:
- Mean price
- Median price
- Number of listings
- Useful for understanding borough-level market dynamics

#### 2. Room Type Statistics (room_type_statistics.csv)
Contains for each room type:
- Average price
- Total number of listings
- Total number of reviews
- Helps understand the popularity and pricing strategies for different accommodation types

### Machine Learning Results

#### Price Prediction Model
- Features used: latitude, longitude, minimum_nights, number_of_reviews, reviews_per_month
- R² Score: [will be populated after running]
- RMSE: [will be populated after running]
- Useful for hosts to price their listings competitively

#### Clustering Analysis
- Identified 5 distinct clusters of listings
- Clusters based on price and location
- Helps understand different market segments in NYC Airbnb landscape

## How to Use These Results

1. **For Hosts:**
   - Use price distribution and heatmaps to price listings competitively
   - Understand how room type affects pricing
   - Use prediction model to estimate appropriate prices

2. **For Guests:**
   - Find neighborhoods within their budget
   - Understand price variations across boroughs
   - Compare prices for different room types

3. **For Market Analysis:**
   - Understand market segmentation through clustering
   - Analyze supply distribution across boroughs
   - Identify price trends and patterns

## Technical Notes
- Price outliers above 99th percentile were removed for better analysis
- Missing values in reviews_per_month were filled with 0
- Geographic visualizations are interactive and can be opened in a web browser 