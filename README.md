# Trader Behavior Insights - Bitcoin Market Sentiment Analysis

## 📊 Project Overview

This project analyzes the relationship between Bitcoin's Fear/Greed Index and Hyperliquid trader performance to uncover patterns and insights that can drive smarter trading strategies.

**Key Question**: How does market sentiment (Fear/Greed Index) correlate with trader performance?
Live Application
Streamlit Dashboard (Deployed)

Use the interactive dashboard here:
https://trader-behavior-insights-udfbxqzxeqpenabliqusjq.streamlit.app/

## 🎯 Key Findings

- **Best Performing Sentiment**: Extreme Greed (Avg PnL: $130.21, Win Rate: 89.17%)
- **Worst Performing Sentiment**: Extreme Fear (Avg PnL: $71.03, Win Rate: 76.22%)
- **Total Analysis**: 104,402 trades analyzed, $10.25M total PnL
- **Insight**: Trade size (correlation: 0.16) has stronger impact than sentiment (correlation: 0.009)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Required packages (see requirements.txt)

### Installation

1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure data files are in the same directory:
   - `fear_greed_index.csv`
   - `historical_data.csv`

### Running the Application

**Option 1: Streamlit Dashboard (Interactive)**
```bash
streamlit run app.py
```

**Option 2: Python Script Analysis**
```bash
python sentiment_trader_analysis.py
```

## 📁 Project Structure

```
.
├── app.py                          # Streamlit interactive dashboard
├── sentiment_trader_analysis.py    # Complete analysis script
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── ANALYSIS_REPORT.md              # Detailed analysis report
├── sentiment_trader_analysis.png   # Visualization dashboard
├── fear_greed_index.csv           # Bitcoin Fear/Greed Index data
└── historical_data.csv            # Hyperliquid trader data
```

## 📈 Features

### Streamlit Dashboard (`app.py`)
- **Interactive Visualizations**: Explore data through multiple views
- **Performance Metrics**: Key statistics and KPIs
- **Sentiment Analysis**: Detailed breakdown by market sentiment
- **Trade Analysis**: BUY vs SELL, trade size impact
- **Advanced Insights**: Correlations, top performers, daily analysis

### Analysis Script (`sentiment_trader_analysis.py`)
- Comprehensive data cleaning and preparation
- Statistical analysis and correlation studies
- Performance metrics by sentiment category
- Visualization generation
- Detailed insights and recommendations

## 📊 Analysis Sections

1. **Overview**: Executive summary and key metrics
2. **Performance by Sentiment**: Detailed breakdown of each sentiment category
3. **Trade Analysis**: BUY vs SELL, trade size impact
4. **Advanced Insights**: Correlations, top/bottom days, account analysis
5. **Methodology**: Technical details and data processing

## 🔍 Key Insights

### 1. Momentum Strategy During Extreme Greed
- Evidence: Highest average PnL ($130.21) and win rate (89.17%)
- Recommendation: Consider trend-following strategies during extreme greed

### 2. Trade Size Matters More
- Evidence: Trade size correlation (0.16) is 18x stronger than sentiment (0.009)
- Recommendation: Focus on position sizing and risk management

### 3. Sentiment as Context, Not Signal
- Evidence: Weak direct correlation suggests sentiment alone isn't a strong predictor
- Recommendation: Use sentiment as a filter with other technical indicators

## 📊 Dataset Information

### Fear/Greed Index
- **Source**: Alternative.me Fear & Greed Index
- **Records**: 2,644 daily readings
- **Date Range**: February 2018 - May 2025
- **Metrics**: Value (0-100), Classification (5 categories)

### Historical Trader Data
- **Source**: Hyperliquid exchange historical data
- **Records**: 211,224 total trades
- **Analyzed**: 104,402 trades with valid PnL
- **Date Range**: December 2023 - May 2025
- **Metrics**: Execution price, size, side, PnL, fees, account, etc.

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib/Seaborn**: Data visualization
- **Streamlit**: Interactive web dashboard

## 📝 Methodology

1. **Data Loading**: Import and validate both datasets
2. **Data Cleaning**: Remove invalid records, standardize formats
3. **Data Merging**: Combine trader data with sentiment by date
4. **Analysis**: Statistical analysis, correlation studies, performance metrics
5. **Visualization**: Create comprehensive charts and dashboards
6. **Insights**: Generate actionable recommendations

## ⚠️ Limitations

1. Time period covers Dec 2023 - May 2025 (may not represent all market cycles)
2. Only closed positions analyzed (excludes open positions)
3. Multiple factors influence PnL beyond sentiment
4. Correlation is weak, suggesting sentiment is one of many factors

## 📧 Contact & Submission

**For Job Application Submission:**
- Email: saami@bajarangs.com, nagasai@bajarangs.com, chetan@bajarangs.com
- CC: sonika@primetrade.ai
- Subject: "Junior Data Scientist – Trader Behavior Insights"

## 📄 License

This project is created for analysis and portfolio demonstration purposes.

---

**Created by**: Olivechaitanya  
**Date**: 2025  
**Purpose**: Junior Data Scientist Application - Trader Behavior Insights Analysis

