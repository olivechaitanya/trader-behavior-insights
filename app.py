"""
Bitcoin Market Sentiment vs Trader Performance Dashboard
==========================================================
Interactive Streamlit application for analyzing the relationship between
Bitcoin Fear/Greed Index and Hyperliquid trader performance.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Trader Behavior Insights",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .stMetric {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title and Header
st.markdown('<h1 class="main-header">📊 Trader Behavior Insights Dashboard</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("🔍 Analysis Controls")
    st.markdown("### Dataset Information")
    st.info("""
    **Fear/Greed Index**: 2,644 daily readings  
    **Trader Data**: 104,402 trades analyzed  
    **Date Range**: Dec 2023 - May 2025
    """)
    
    st.markdown("### Navigation")
    page = st.radio(
        "Select Analysis View",
        ["📈 Overview", "🎯 Performance by Sentiment", "💰 Trade Analysis", "📊 Advanced Insights", "🔬 Methodology"]
    )

# Load data function with caching
@st.cache_data
def load_data():
    """Load and prepare datasets"""
    # Load Fear/Greed Index
    fear_greed = pd.read_csv('fear_greed_index.csv')
    fear_greed['date'] = pd.to_datetime(fear_greed['date'])
    
    # Create sentiment score mapping
    sentiment_map = {
        'Extreme Fear': 1,
        'Fear': 2,
        'Neutral': 3,
        'Greed': 4,
        'Extreme Greed': 5
    }
    fear_greed['sentiment_score'] = fear_greed['classification'].map(sentiment_map)
    
    # Load Trader Data - try full file first, then sample
    import os
    if os.path.exists('historical_data.csv'):
        trader_data = pd.read_csv('historical_data.csv')
    elif os.path.exists('historical_data_sample.csv'):
        trader_data = pd.read_csv('historical_data_sample.csv')
    else:
        st.error("No data file found! Please ensure historical_data.csv or historical_data_sample.csv exists.")
        st.stop()
    
    # Clean trader data
    trader_data['Timestamp IST'] = pd.to_datetime(
        trader_data['Timestamp IST'], 
        format='%d-%m-%Y %H:%M', 
        errors='coerce'
    )
    trader_data['date'] = trader_data['Timestamp IST'].dt.date
    trader_data['date'] = pd.to_datetime(trader_data['date'])
    
    # Clean numeric columns
    numeric_cols = ['Execution Price', 'Size USD', 'Closed PnL', 'Fee']
    for col in numeric_cols:
        if col in trader_data.columns:
            trader_data[col] = pd.to_numeric(trader_data[col], errors='coerce')
    
    # Filter valid data
    trader_data = trader_data.dropna(subset=['date', 'Closed PnL'])
    trader_data = trader_data[trader_data['Closed PnL'] != 0]
    
    # Merge datasets
    merged_data = trader_data.merge(
        fear_greed[['date', 'value', 'classification', 'sentiment_score']],
        on='date',
        how='left'
    )
    merged_data = merged_data.dropna(subset=['classification'])
    
    return merged_data, fear_greed

# Load data
try:
    merged_data, fear_greed = load_data()
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.stop()

# Page 1: Overview
if page == "📈 Overview":
    st.header("Executive Summary")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Trades",
            f"{len(merged_data):,}",
            help="Number of trades analyzed"
        )
    
    with col2:
        total_pnl = merged_data['Closed PnL'].sum()
        st.metric(
            "Total PnL",
            f"${total_pnl:,.0f}",
            help="Total profit/loss across all trades"
        )
    
    with col3:
        avg_pnl = merged_data['Closed PnL'].mean()
        st.metric(
            "Avg PnL/Trade",
            f"${avg_pnl:.2f}",
            help="Average profit/loss per trade"
        )
    
    with col4:
        win_rate = (merged_data['Closed PnL'] > 0).sum() / len(merged_data) * 100
        st.metric(
            "Win Rate",
            f"{win_rate:.2f}%",
            help="Percentage of profitable trades"
        )
    
    st.markdown("---")
    
    # Key Findings
    st.subheader("🎯 Key Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🏆 Best Performing Sentiment: Extreme Greed**
        - Average PnL: $130.21 per trade
        - Win Rate: 89.17%
        - Total PnL: $2.7M from 20,853 trades
        
        **💡 Insight**: Momentum/trend-following strategies appear most effective
        """)
    
    with col2:
        st.markdown("""
        **⚠️ Worst Performing Sentiment: Extreme Fear**
        - Average PnL: $71.03 per trade
        - Win Rate: 76.22%
        - Total PnL: $739K from 10,406 trades
        
        **💡 Insight**: Contrarian strategies show lower returns than expected
        """)
    
    st.markdown("---")
    
    # Quick Stats
    st.subheader("📊 Quick Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Trade Distribution by Sentiment:**")
        sentiment_counts = merged_data['classification'].value_counts()
        for sentiment, count in sentiment_counts.items():
            pct = count / len(merged_data) * 100
            st.write(f"- {sentiment}: {count:,} trades ({pct:.2f}%)")
    
    with col2:
        st.markdown("**Performance Summary:**")
        st.write(f"- Winning trades: {(merged_data['Closed PnL'] > 0).sum():,}")
        st.write(f"- Losing trades: {(merged_data['Closed PnL'] < 0).sum():,}")
        st.write(f"- Median PnL: ${merged_data['Closed PnL'].median():.2f}")
        st.write(f"- Std Dev: ${merged_data['Closed PnL'].std():.2f}")

# Page 2: Performance by Sentiment
elif page == "🎯 Performance by Sentiment":
    st.header("Performance Analysis by Market Sentiment")
    
    # Performance metrics table
    st.subheader("Performance Metrics")
    
    performance_by_sentiment = merged_data.groupby('classification').agg({
        'Closed PnL': ['count', 'sum', 'mean', 'median'],
        'Size USD': 'mean'
    }).round(2)
    
    performance_by_sentiment.columns = ['Trade Count', 'Total PnL', 'Avg PnL', 'Median PnL', 'Avg Trade Size']
    sentiment_order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
    performance_by_sentiment = performance_by_sentiment.reindex(sentiment_order)
    
    st.dataframe(performance_by_sentiment.style.format({
        'Trade Count': '{:,.0f}',
        'Total PnL': '${:,.2f}',
        'Avg PnL': '${:.2f}',
        'Median PnL': '${:.2f}',
        'Avg Trade Size': '${:,.2f}'
    }), use_container_width=True)
    
    st.markdown("---")
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Average PnL by Sentiment")
        avg_pnl = merged_data.groupby('classification')['Closed PnL'].mean().reindex(sentiment_order)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = ['#8B0000', '#FF4500', '#FFD700', '#32CD32', '#006400']
        bars = ax.bar(range(len(avg_pnl)), avg_pnl.values, color=colors)
        ax.set_xticks(range(len(avg_pnl)))
        ax.set_xticklabels(avg_pnl.index, rotation=45, ha='right')
        ax.set_ylabel('Average PnL (USD)', fontsize=12)
        ax.set_title('Average PnL by Market Sentiment', fontsize=14, fontweight='bold')
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        
        for i, (bar, val) in enumerate(zip(bars, avg_pnl.values)):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'${val:.2f}',
                   ha='center', va='bottom' if height >= 0 else 'top', fontsize=10)
        
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        st.subheader("Win Rate by Sentiment")
        win_rates = merged_data.groupby('classification').apply(
            lambda x: (x['Closed PnL'] > 0).sum() / len(x) * 100
        ).reindex(sentiment_order)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(range(len(win_rates)), win_rates.values, color=colors)
        ax.set_xticks(range(len(win_rates)))
        ax.set_xticklabels(win_rates.index, rotation=45, ha='right')
        ax.set_ylabel('Win Rate (%)', fontsize=12)
        ax.set_title('Win Rate by Market Sentiment', fontsize=14, fontweight='bold')
        ax.set_ylim([0, 100])
        
        for bar, val in zip(bars, win_rates.values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{val:.1f}%',
                   ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()
        st.pyplot(fig)
    
    st.markdown("---")
    
    # PnL Distribution
    st.subheader("PnL Distribution by Sentiment")
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.boxplot(data=merged_data, x='classification', y='Closed PnL', 
                order=sentiment_order, ax=ax)
    ax.set_title('PnL Distribution by Market Sentiment', fontsize=14, fontweight='bold')
    ax.set_xlabel('Market Sentiment', fontsize=12)
    ax.set_ylabel('Closed PnL (USD)', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.axhline(y=0, color='r', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig)

# Page 3: Trade Analysis
elif page == "💰 Trade Analysis":
    st.header("Trade Analysis")
    
    # Define sentiment order and colors
    sentiment_order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
    colors = ['#8B0000', '#FF4500', '#FFD700', '#32CD32', '#006400']
    
    # BUY vs SELL
    st.subheader("BUY vs SELL Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        buy_avg = merged_data[merged_data['Side'] == 'BUY']['Closed PnL'].mean()
        buy_count = len(merged_data[merged_data['Side'] == 'BUY'])
        st.metric("BUY Trades", f"{buy_count:,}", f"Avg: ${buy_avg:.2f}")
    
    with col2:
        sell_avg = merged_data[merged_data['Side'] == 'SELL']['Closed PnL'].mean()
        sell_count = len(merged_data[merged_data['Side'] == 'SELL'])
        st.metric("SELL Trades", f"{sell_count:,}", f"Avg: ${sell_avg:.2f}")
    
    # BUY vs SELL by Sentiment
    st.subheader("BUY vs SELL Performance by Sentiment")
    buy_sell_pnl = merged_data.groupby(['classification', 'Side'])['Closed PnL'].mean().unstack()
    buy_sell_pnl = buy_sell_pnl.reindex(sentiment_order)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(sentiment_order))
    width = 0.35
    
    if 'BUY' in buy_sell_pnl.columns:
        ax.bar(x - width/2, buy_sell_pnl['BUY'].values, width, label='BUY', color='#32CD32', alpha=0.8)
    if 'SELL' in buy_sell_pnl.columns:
        ax.bar(x + width/2, buy_sell_pnl['SELL'].values, width, label='SELL', color='#FF4500', alpha=0.8)
    
    ax.set_xticks(x)
    ax.set_xticklabels(sentiment_order, rotation=45, ha='right')
    ax.set_ylabel('Average PnL (USD)', fontsize=12)
    ax.set_title('Average PnL: BUY vs SELL by Sentiment', fontsize=14, fontweight='bold')
    ax.legend()
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("---")
    
    # Trade Size Analysis
    st.subheader("Performance by Trade Size")
    
    merged_data['Trade_Size_Category'] = pd.cut(
        merged_data['Size USD'],
        bins=[0, 100, 500, 1000, 5000, float('inf')],
        labels=['< $100', '$100-$500', '$500-$1K', '$1K-$5K', '> $5K']
    )
    
    size_sentiment_perf = merged_data.groupby(['Trade_Size_Category', 'classification'])['Closed PnL'].mean().unstack()
    size_sentiment_perf = size_sentiment_perf.reindex(columns=sentiment_order)
    
    st.dataframe(size_sentiment_perf.style.format('${:.2f}'), use_container_width=True)
    
    # Visualization
    fig, ax = plt.subplots(figsize=(14, 6))
    size_sentiment_perf.plot(kind='bar', ax=ax, color=colors)
    ax.set_title('Average PnL by Trade Size and Sentiment', fontsize=14, fontweight='bold')
    ax.set_xlabel('Trade Size Category', fontsize=12)
    ax.set_ylabel('Average PnL (USD)', fontsize=12)
    ax.legend(title='Sentiment', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

# Page 4: Advanced Insights
elif page == "📊 Advanced Insights":
    st.header("Advanced Insights & Correlations")
    
    # Correlation Analysis
    st.subheader("Correlation Analysis")
    
    correlation = merged_data[['Closed PnL', 'value', 'sentiment_score', 'Size USD']].corr()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Correlation Matrix:**")
        st.dataframe(correlation.style.format('{:.4f}').background_gradient(cmap='coolwarm', axis=None), 
                    use_container_width=True)
    
    with col2:
        st.markdown("**Key Correlations:**")
        corr_value = correlation.loc['Closed PnL', 'value']
        corr_sentiment = correlation.loc['Closed PnL', 'sentiment_score']
        corr_size = correlation.loc['Closed PnL', 'Size USD']
        
        st.metric("Fear/Greed Value vs PnL", f"{corr_value:.4f}")
        st.metric("Sentiment Score vs PnL", f"{corr_sentiment:.4f}")
        st.metric("Trade Size vs PnL", f"{corr_size:.4f}")
        
        st.info("""
        **Insight**: Trade size has a stronger correlation (0.16) 
        with PnL than sentiment alone (0.009), suggesting position 
        sizing is more critical than sentiment timing.
        """)
    
    st.markdown("---")
    
    # Top/Bottom Days
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top 10 Best Performing Days")
        daily_perf = merged_data.groupby(['date', 'classification'])['Closed PnL'].agg(['sum', 'count', 'mean']).reset_index()
        daily_perf = daily_perf.sort_values('sum', ascending=False)
        st.dataframe(
            daily_perf.head(10).style.format({
                'sum': '${:,.2f}',
                'count': '{:,.0f}',
                'mean': '${:.2f}'
            }),
            use_container_width=True,
            hide_index=True
        )
    
    with col2:
        st.subheader("Top 10 Worst Performing Days")
        st.dataframe(
            daily_perf.tail(10).style.format({
                'sum': '${:,.2f}',
                'count': '{:,.0f}',
                'mean': '${:.2f}'
            }),
            use_container_width=True,
            hide_index=True
        )
    
    st.markdown("---")
    
    # Top Accounts
    st.subheader("Top 10 Accounts by Total PnL")
    account_perf = merged_data.groupby('Account').agg({
        'Closed PnL': ['sum', 'mean', 'count']
    }).round(2)
    account_perf.columns = ['Total PnL', 'Avg PnL', 'Trade Count']
    account_perf = account_perf.sort_values('Total PnL', ascending=False)
    
    st.dataframe(
        account_perf.head(10).style.format({
            'Total PnL': '${:,.2f}',
            'Avg PnL': '${:.2f}',
            'Trade Count': '{:,.0f}'
        }),
        use_container_width=True
    )

# Page 5: Methodology
elif page == "🔬 Methodology":
    st.header("Methodology & Technical Details")
    
    st.markdown("""
    ### Data Sources
    
    1. **Bitcoin Fear/Greed Index**
       - Source: Alternative.me Fear & Greed Index
       - Records: 2,644 daily readings
       - Date Range: February 2018 - May 2025
       - Metrics: Value (0-100), Classification (5 categories)
    
    2. **Hyperliquid Trader Data**
       - Source: Historical trading data from Hyperliquid exchange
       - Records: 211,224 total trades
       - Analyzed: 104,402 trades with valid PnL
       - Date Range: December 2023 - May 2025
       - Metrics: Execution price, size, side, PnL, fees, etc.
    
    ### Data Processing
    
    1. **Data Cleaning**
       - Removed trades with missing or zero PnL
       - Standardized date formats
       - Validated numeric columns
    
    2. **Data Merging**
       - Merged trader data with sentiment data by date
       - Matched 104,402 trades with sentiment classifications
    
    3. **Feature Engineering**
       - Created sentiment score (1-5 scale)
       - Categorized trade sizes
       - Calculated performance metrics
    
    ### Analysis Methods
    
    1. **Descriptive Statistics**
       - Mean, median, standard deviation by sentiment
       - Win rate calculations
       - Trade distribution analysis
    
    2. **Correlation Analysis**
       - Pearson correlation coefficients
       - Relationship strength assessment
    
    3. **Comparative Analysis**
       - Performance by sentiment category
       - BUY vs SELL comparison
       - Trade size impact analysis
    
    ### Key Metrics
    
    - **Total PnL**: Sum of all closed position profits/losses
    - **Average PnL**: Mean profit/loss per trade
    - **Win Rate**: Percentage of profitable trades
    - **Trade Size**: USD value of each trade
    
    ### Limitations
    
    1. Time period covers Dec 2023 - May 2025 (may not represent all market cycles)
    2. Only closed positions analyzed (excludes open positions)
    3. Multiple factors influence PnL beyond sentiment
    4. Correlation is weak, suggesting sentiment is one of many factors
    
    ### Tools & Technologies
    
    - **Python 3.x**
    - **Pandas**: Data manipulation and analysis
    - **NumPy**: Numerical computations
    - **Matplotlib/Seaborn**: Data visualization
    - **Streamlit**: Interactive dashboard
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p><strong>Trader Behavior Insights Dashboard</strong></p>
    <p>Analysis of Bitcoin Market Sentiment vs Hyperliquid Trader Performance</p>
    <p>Data Period: December 2023 - May 2025 | Total Trades Analyzed: 104,402</p>
</div>
""", unsafe_allow_html=True)

