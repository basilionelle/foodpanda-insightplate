# 🍜 FoodPanda InsightPlate 📊

> Transform raw restaurant data into delicious insights! 🚀

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-%23FA0F00.svg?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 🎯 About The Project

FoodPanda InsightPlate is your personal food discovery assistant that helps you find the perfect restaurant for any craving. Using data visualization, we transform thousands of customer reviews into clear, actionable insights.

### 🎯 Why Use InsightPlate?

Ever spent too much time scrolling through endless restaurant options? We've been there! InsightPlate helps you:

- See at a glance which restaurants consistently delight customers
- Discover hidden gems in your neighborhood
- Find the best-rated cuisines near you
- Make confident dining choices backed by data

### 👥 Made for Food Lovers

InsightPlate is perfect for you if you want to:

- 🔍 Find trustworthy, highly-rated restaurants
- 🌟 Discover exciting new cuisines in your area
- 📊 Compare options based on real customer experiences
- 🗺️ Explore great food across different locations
- 💡 Make smarter dining decisions

### 🍳 How It Helps

We make your food ordering experience better by:

- 📊 Showing clear visual ratings and trends
- 🏷️ Helping you find your favorite cuisine types
- ⭐ Highlighting the most-loved restaurants near you
- 📈 Revealing what local foodies recommend

## 🍝 What You'll Love

- 🌟 **Top Picks**: Instantly see the highest-rated restaurants
- 🍜 **Cuisine Explorer**: Find the perfect food type for your mood
- 📍 **Local Gems**: Discover amazing restaurants in your area
- 📈 **Smart Insights**: See what dishes and places are trending
- 🖥️ **Easy to Use**: Simple, beautiful, and intuitive design

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

### CANVA PPT 

https://www.canva.com/design/DAGjqxCYYPQ/Jj4D43aY-VJQKeBTo468YQ/edit

**Quick Start:**

```python
# Load and peek at the data
import pandas as pd
df = pd.read_csv('restos.csv')
print(df.head())
```

### Option 2: Local Development

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/foodpanda-insightplate.git
cd foodpanda-insightplate

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start Jupyter
jupyter notebook Final-InsightPlate.ipynb
```

**Troubleshooting:**

- If you see `ModuleNotFoundError`, run: `pip install -r requirements.txt`
- For visualization issues, try: `pip install --upgrade matplotlib seaborn`
- Jupyter not starting? Check: `jupyter --version`

## 📊 Visualizations

### 1. Restaurant Distribution Map 🗺️

Interactive map showing restaurant locations across the Philippines

- Color-coded by average ratings:
  - 🟢 4.5+ (Excellent)
  - 🟡 4.0-4.4 (Very Good)
  - 🟠 3.5-3.9 (Good)
  - 🔴 Below 3.5 (Average)

- Bubble size indicates number of reviews
- Click on locations to filter data

### 2. Food Type Distribution 🍝

Bar chart showing top 10 cuisines in the selected city

- Interactive filtering by:
  - City
  - Rating range

- Color intensity indicates popularity
- Hover for detailed restaurant counts

### 3. Rating Distribution 📈

Histogram showing rating distribution for:

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

Choose what you want to see:

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

---

### Made with ❤️ for Food Lovers

[Back to Top ⬆️](#-about-the-project)
