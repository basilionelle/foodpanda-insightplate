# 🍜 FoodPanda InsightPlate 📊

> Transform raw restaurant data into delicious insights! 🚀

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-%23FA0F00.svg?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

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




## 🌟 Features

- 🗺️ **Interactive Map**: Explore restaurants across the Philippines
- 📊 **Dynamic Charts**: Filter and analyze restaurant data in real-time
- 🏷️ **Food Type Analysis**: Discover popular cuisines by city
- ⭐ **Rating Distribution**: Analyze rating patterns
- 🎨 **Modern UI**: Beautiful design with smooth animations

## 🛠️ Tech Stack

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical visualizations
- **Jupyter**: Interactive notebook environment
- **Google Colab**: Cloud deployment and sharing

## 🚀 Quick Start

### Option 1: Google Colab (Recommended)

1. Open the notebook in Google Colab by clicking the badge above
2. Upload the data files when prompted:
   - `restos.csv`
   - `restos_2025.csv`
3. Run all cells sequentially
4. Explore the interactive visualizations! 🎉

<details>
<summary>📝 Quick Data Preview</summary>

```python
# Load and peek at the data
import pandas as pd
df = pd.read_csv('restos.csv')
print(df.head())
```
</details>

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/foodpanda-insightplate.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook Final-InsightPlate.ipynb
```

<details>
<summary>🔧 Troubleshooting Tips</summary>

- If you see `ModuleNotFoundError`, run: `pip install -r requirements.txt`
- For visualization issues, try: `pip install --upgrade matplotlib seaborn`
- Jupyter not starting? Check: `jupyter --version`
</details>

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
