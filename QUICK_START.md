# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Interactive Dashboard
```bash
streamlit run app.py
```

The dashboard will open in your browser automatically at `http://localhost:8501`

### Step 3: Run the Analysis Script (Optional)
```bash
python sentiment_trader_analysis.py
```

This will generate the visualization PNG and detailed analysis output.

## 📊 What You'll See

### Streamlit Dashboard Features:
1. **Overview**: Key metrics and executive summary
2. **Performance by Sentiment**: Detailed breakdown by market sentiment
3. **Trade Analysis**: BUY vs SELL, trade size impact
4. **Advanced Insights**: Correlations, top performers
5. **Methodology**: Technical details

### Analysis Script Output:
- Console output with detailed statistics
- `sentiment_trader_analysis.png` - Comprehensive visualization dashboard

## 🐛 Troubleshooting

### If Streamlit is not installed:
```bash
pip install streamlit
```

### If you get import errors:
```bash
pip install --upgrade pandas numpy matplotlib seaborn streamlit
```

### If data files are missing:
- Ensure `fear_greed_index.csv` and `historical_data.csv` are in the same directory as `app.py`

## 📧 Ready to Submit?

See `SUBMISSION_GUIDE.md` for complete submission instructions!

