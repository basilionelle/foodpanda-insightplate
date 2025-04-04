# 🍜 FoodPanda InsightPlate 📊

> Transform raw restaurant data into delicious insights! 🚀

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Dash Version](https://img.shields.io/badge/dash-2.9.3-brightgreen)
![Plotly Version](https://img.shields.io/badge/plotly-5.13.1-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## 🎯 About The Project

FoodPanda InsightPlate is an interactive data visualization dashboard designed to enhance the food delivery experience in the Philippines. Our mission is to help consumers make informed dining decisions by providing clear, visual insights into restaurant performance across different cities.

### 🎯 Motivation

With the explosive growth of food delivery platforms, consumers often face decision paralysis when choosing where to order. We solve this by:

- Visualizing restaurant ratings and popularity across cities
- Making it easy to discover top-rated cuisines in any area
- Helping users find hidden gems through advanced filtering


### 👥 Target Users

1. **Food Delivery Customers**
   - Looking for highly-rated restaurants
   - Exploring new cuisines in their area
   - Comparing options across different locations

2. **Restaurant Owners**
   - Analyzing market performance
   - Understanding customer preferences
   - Identifying growth opportunities

### 🔍 Problem Solution

We address common food delivery challenges by:

- Aggregating and visualizing thousands of customer reviews
- Providing interactive filters for cuisine type and ratings
- Offering clear geographical insights through our interactive map
- Making data-driven decisions accessible through an intuitive interface


### 👥 Team Members

- Carl Alamay
- Nelle Basilio
- Sean Columbres
- Reever Lacson
- Josh Ng

## 🌟 Features

- 🗺️ **Interactive Map**: Explore restaurants across the Philippines
- 📊 **Dynamic Charts**: Filter and analyze restaurant data in real-time
- 🏷️ **Food Type Analysis**: Discover popular cuisines by city
- ⭐ **Rating Distribution**: Analyze rating patterns
- 🎨 **Modern UI**: Beautiful design with smooth animations

## 🛠️ Tech Stack

- **Python**: The core programming language
- **Dash & Plotly**: For creating interactive visualizations
- **Pandas**: For data manipulation and analysis
- **Google Colab**: For easy deployment and sharing

## 🚀 Quick Start

### Option 1: Google Colab (Recommended)

1. Open our [Interactive Dashboard Notebook](https://colab.research.google.com/drive/14JU08uudxqV2B6Ea_Oc9ZFwzwSKSHcMb) in Google Colab

2. Run the first cell to install dependencies:

   ```python
   !pip install dash==2.9.3 dash-bootstrap-components==1.4.1 plotly==5.13.1 pandas==1.5.3 jupyter-dash==0.4.2
   ```

3. Restart the runtime (Runtime > Restart runtime)
4. Run all cells (Runtime > Run all)
5. Upload your data files when prompted
6. Explore the dashboard in a new tab! 🎉

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/foodpanda-insightplate.git

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
python FinalCode.py
```

## 📊 Visualizations

### 1. Restaurant Distribution Map 🗺️
- Interactive map showing restaurant locations across the Philippines
- Color-coded by average ratings:
  - 🟢 4.5+ (Excellent)
  - 🟡 4.0-4.4 (Very Good)
  - 🟠 3.5-3.9 (Good)
  - 🔴 Below 3.5 (Average)
- Bubble size indicates number of reviews
- Click on locations to filter data

### 2. Food Type Distribution 🍽️
- Bar chart showing top 10 cuisines in the selected city
- Interactive filtering by:
  - City
  - Rating range
- Color intensity indicates popularity
- Hover for detailed restaurant counts

### 3. Rating Distribution 📈
- Histogram showing rating distribution for:
  - Selected city
  - Chosen food type
- Shows the spread of ratings across restaurants
- Hover for detailed counts in each rating bracket

### 4. Quick Stats Dashboard 📊
- Total number of restaurants in filtered selection
- Average rating for filtered restaurants
- Most common food type in selection
- Updates dynamically with filters

## 🎯 Interactive Features

### 1. Dynamic Filters
- **City Filter**: Focus on specific locations
- **Food Type Filter**: Explore different cuisines
- **Rating Range Filter**: Find top-rated restaurants

### 2. Real-time Updates
- All visualizations update instantly when filters change
- Smooth transitions between states
- Responsive design for all screen sizes

### 3. Hover Interactions
- Detailed tooltips on map markers
- Restaurant counts on bar charts
- Rating breakdowns on histograms

## 📚 Documentation

Check out our detailed documentation:
- [Data Preprocessing](docs/preprocessing.md)
- [Dashboard Features](docs/features.md)
- [API Reference](docs/api.md)
- [Contributing Guide](CONTRIBUTING.md)

## 🤝 Contributing

We love contributions! Please check our [Contributing Guide](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FoodPanda for the inspiration
- Our amazing DATA101 professors
- The open-source community

---

<p align="center">Made with ❤️ by Team InsightPlate</p>

<p align="center">
  <a href="#-project-overview">Back to Top ⬆️</a>
</p>
