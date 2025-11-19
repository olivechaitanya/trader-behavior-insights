"""
Bitcoin Market Sentiment vs Trader Performance Analysis
=======================================================
This script analyzes the relationship between Bitcoin Fear/Greed Index
and Hyperliquid trader performance to uncover trading insights.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

print("=" * 80)
print("BITCOIN MARKET SENTIMENT vs TRADER PERFORMANCE ANALYSIS")
print("=" * 80)
print()

# ============================================================================
# 1. LOAD AND PREPARE DATA
# ============================================================================
print("Step 1: Loading datasets...")
print("-" * 80)

# Load Fear/Greed Index
fear_greed = pd.read_csv('fear_greed_index.csv')
print(f"[OK] Fear/Greed Index: {len(fear_greed):,} records")
print(f"  Date range: {fear_greed['date'].min()} to {fear_greed['date'].max()}")

# Load Historical Trader Data
print("\nLoading historical trader data (this may take a moment)...")
trader_data = pd.read_csv('historical_data.csv')
print(f"[OK] Historical Trader Data: {len(trader_data):,} records")

# Display basic info
print(f"\nTrader Data Columns: {list(trader_data.columns)}")
print(f"\nFirst few trader records:")
print(trader_data.head())

# ============================================================================
# 2. DATA CLEANING AND PREPARATION
# ============================================================================
print("\n" + "=" * 80)
print("Step 2: Data Cleaning and Preparation")
print("-" * 80)

# Clean Fear/Greed data
fear_greed['date'] = pd.to_datetime(fear_greed['date'])
fear_greed = fear_greed.sort_values('date')

# Create sentiment score mapping (0-100 scale, but we'll use value column)
# Classification mapping for easier analysis
sentiment_map = {
    'Extreme Fear': 1,
    'Fear': 2,
    'Neutral': 3,
    'Greed': 4,
    'Extreme Greed': 5
}
fear_greed['sentiment_score'] = fear_greed['classification'].map(sentiment_map)

# Clean Trader Data
print("\nCleaning trader data...")

# Convert timestamp to datetime
# The timestamp appears to be in IST format "DD-MM-YYYY HH:MM"
trader_data['Timestamp IST'] = pd.to_datetime(trader_data['Timestamp IST'], 
                                               format='%d-%m-%Y %H:%M', 
                                               errors='coerce')

# Extract date for merging
trader_data['date'] = trader_data['Timestamp IST'].dt.date
trader_data['date'] = pd.to_datetime(trader_data['date'])

# Clean numeric columns
numeric_cols = ['Execution Price', 'Size USD', 'Closed PnL', 'Fee']
for col in numeric_cols:
    if col in trader_data.columns:
        trader_data[col] = pd.to_numeric(trader_data[col], errors='coerce')

# Filter out invalid data
trader_data = trader_data.dropna(subset=['date', 'Closed PnL'])
trader_data = trader_data[trader_data['Closed PnL'] != 0]  # Focus on closed positions

print(f"[OK] Cleaned trader data: {len(trader_data):,} records with valid PnL")
print(f"  Date range: {trader_data['date'].min()} to {trader_data['date'].max()}")

# ============================================================================
# 3. MERGE DATASETS
# ============================================================================
print("\n" + "=" * 80)
print("Step 3: Merging Datasets")
print("-" * 80)

# Merge trader data with sentiment data
merged_data = trader_data.merge(
    fear_greed[['date', 'value', 'classification', 'sentiment_score']],
    on='date',
    how='left'
)

print(f"[OK] Merged dataset: {len(merged_data):,} records")
print(f"  Records with sentiment data: {merged_data['classification'].notna().sum():,}")
print(f"  Records without sentiment data: {merged_data['classification'].isna().sum():,}")

# Filter to only records with sentiment data
merged_data = merged_data.dropna(subset=['classification'])
print(f"[OK] Final dataset for analysis: {len(merged_data):,} records")

# ============================================================================
# 4. EXPLORATORY DATA ANALYSIS
# ============================================================================
print("\n" + "=" * 80)
print("Step 4: Exploratory Data Analysis")
print("-" * 80)

# Basic statistics
print("\n4.1 Basic Statistics:")
print(f"  Total trades: {len(merged_data):,}")
print(f"  Total PnL: ${merged_data['Closed PnL'].sum():,.2f}")
print(f"  Average PnL per trade: ${merged_data['Closed PnL'].mean():,.2f}")
print(f"  Median PnL per trade: ${merged_data['Closed PnL'].median():,.2f}")
print(f"  Winning trades: {(merged_data['Closed PnL'] > 0).sum():,} ({(merged_data['Closed PnL'] > 0).sum() / len(merged_data) * 100:.2f}%)")
print(f"  Losing trades: {(merged_data['Closed PnL'] < 0).sum():,} ({(merged_data['Closed PnL'] < 0).sum() / len(merged_data) * 100:.2f}%)")

# Sentiment distribution
print("\n4.2 Sentiment Distribution:")
sentiment_counts = merged_data['classification'].value_counts()
for sentiment, count in sentiment_counts.items():
    pct = count / len(merged_data) * 100
    print(f"  {sentiment:20s}: {count:6,} trades ({pct:5.2f}%)")

# ============================================================================
# 5. PERFORMANCE BY SENTIMENT
# ============================================================================
print("\n" + "=" * 80)
print("Step 5: Performance Analysis by Market Sentiment")
print("-" * 80)

# Calculate performance metrics by sentiment
performance_by_sentiment = merged_data.groupby('classification').agg({
    'Closed PnL': ['count', 'sum', 'mean', 'median', 'std'],
    'Size USD': 'mean'
}).round(2)

performance_by_sentiment.columns = ['Trade_Count', 'Total_PnL', 'Avg_PnL', 'Median_PnL', 'Std_PnL', 'Avg_Trade_Size']
# Sort by sentiment order
sentiment_order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
performance_by_sentiment = performance_by_sentiment.reindex(sentiment_order)

print("\n5.1 Performance Metrics by Sentiment:")
print(performance_by_sentiment)

# Win rate by sentiment
win_rate_by_sentiment = merged_data.groupby('classification').apply(
    lambda x: (x['Closed PnL'] > 0).sum() / len(x) * 100
).round(2)

print("\n5.2 Win Rate by Sentiment:")
for sentiment, win_rate in win_rate_by_sentiment.items():
    print(f"  {sentiment:20s}: {win_rate:5.2f}%")

# ============================================================================
# 6. VISUALIZATIONS
# ============================================================================
print("\n" + "=" * 80)
print("Step 6: Creating Visualizations")
print("-" * 80)

# Create figure with subplots
fig = plt.figure(figsize=(20, 12))

# 6.1 PnL Distribution by Sentiment
ax1 = plt.subplot(2, 3, 1)
sentiment_order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
sns.boxplot(data=merged_data, x='classification', y='Closed PnL', order=sentiment_order, ax=ax1)
ax1.set_title('PnL Distribution by Market Sentiment', fontsize=14, fontweight='bold')
ax1.set_xlabel('Market Sentiment', fontsize=12)
ax1.set_ylabel('Closed PnL (USD)', fontsize=12)
ax1.tick_params(axis='x', rotation=45)
ax1.axhline(y=0, color='r', linestyle='--', alpha=0.5)

# 6.2 Average PnL by Sentiment
ax2 = plt.subplot(2, 3, 2)
avg_pnl = merged_data.groupby('classification')['Closed PnL'].mean().reindex(sentiment_order)
colors = ['#8B0000', '#FF4500', '#FFD700', '#32CD32', '#006400']
bars = ax2.bar(range(len(avg_pnl)), avg_pnl.values, color=colors)
ax2.set_xticks(range(len(avg_pnl)))
ax2.set_xticklabels(avg_pnl.index, rotation=45, ha='right')
ax2.set_title('Average PnL by Market Sentiment', fontsize=14, fontweight='bold')
ax2.set_ylabel('Average PnL (USD)', fontsize=12)
ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
# Add value labels on bars
for i, (bar, val) in enumerate(zip(bars, avg_pnl.values)):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'${val:.2f}',
             ha='center', va='bottom' if height >= 0 else 'top', fontsize=10)

# 6.3 Win Rate by Sentiment
ax3 = plt.subplot(2, 3, 3)
win_rates = merged_data.groupby('classification').apply(
    lambda x: (x['Closed PnL'] > 0).sum() / len(x) * 100
).reindex(sentiment_order)
bars = ax3.bar(range(len(win_rates)), win_rates.values, color=colors)
ax3.set_xticks(range(len(win_rates)))
ax3.set_xticklabels(win_rates.index, rotation=45, ha='right')
ax3.set_title('Win Rate by Market Sentiment', fontsize=14, fontweight='bold')
ax3.set_ylabel('Win Rate (%)', fontsize=12)
ax3.set_ylim([0, 100])
# Add value labels
for bar, val in zip(bars, win_rates.values):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
             f'{val:.1f}%',
             ha='center', va='bottom', fontsize=10)

# 6.4 Trade Volume by Sentiment
ax4 = plt.subplot(2, 3, 4)
trade_counts = merged_data.groupby('classification').size().reindex(sentiment_order)
bars = ax4.bar(range(len(trade_counts)), trade_counts.values, color=colors)
ax4.set_xticks(range(len(trade_counts)))
ax4.set_xticklabels(trade_counts.index, rotation=45, ha='right')
ax4.set_title('Number of Trades by Market Sentiment', fontsize=14, fontweight='bold')
ax4.set_ylabel('Number of Trades', fontsize=12)
# Add value labels
for bar, val in zip(bars, trade_counts.values):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(val):,}',
             ha='center', va='bottom', fontsize=10)

# 6.5 Total PnL by Sentiment
ax5 = plt.subplot(2, 3, 5)
total_pnl = merged_data.groupby('classification')['Closed PnL'].sum().reindex(sentiment_order)
bars = ax5.bar(range(len(total_pnl)), total_pnl.values, color=colors)
ax5.set_xticks(range(len(total_pnl)))
ax5.set_xticklabels(total_pnl.index, rotation=45, ha='right')
ax5.set_title('Total PnL by Market Sentiment', fontsize=14, fontweight='bold')
ax5.set_ylabel('Total PnL (USD)', fontsize=12)
ax5.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
# Add value labels
for bar, val in zip(bars, total_pnl.values):
    height = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2., height,
             f'${val:,.0f}',
             ha='center', va='bottom' if height >= 0 else 'top', fontsize=10)

# 6.6 Buy vs Sell Performance by Sentiment
ax6 = plt.subplot(2, 3, 6)
buy_sell_pnl = merged_data.groupby(['classification', 'Side'])['Closed PnL'].mean().unstack()
buy_sell_pnl = buy_sell_pnl.reindex(sentiment_order)
x = np.arange(len(sentiment_order))
width = 0.35
if 'BUY' in buy_sell_pnl.columns:
    ax6.bar(x - width/2, buy_sell_pnl['BUY'].values, width, label='BUY', color='#32CD32', alpha=0.8)
if 'SELL' in buy_sell_pnl.columns:
    ax6.bar(x + width/2, buy_sell_pnl['SELL'].values, width, label='SELL', color='#FF4500', alpha=0.8)
ax6.set_xticks(x)
ax6.set_xticklabels(sentiment_order, rotation=45, ha='right')
ax6.set_title('Average PnL: BUY vs SELL by Sentiment', fontsize=14, fontweight='bold')
ax6.set_ylabel('Average PnL (USD)', fontsize=12)
ax6.legend()
ax6.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.savefig('sentiment_trader_analysis.png', dpi=300, bbox_inches='tight')
print("[OK] Saved visualization: sentiment_trader_analysis.png")

# ============================================================================
# 7. ADVANCED ANALYSIS
# ============================================================================
print("\n" + "=" * 80)
print("Step 7: Advanced Analysis")
print("-" * 80)

# 7.1 Correlation Analysis
print("\n7.1 Correlation Analysis:")
correlation = merged_data[['Closed PnL', 'value', 'sentiment_score', 'Size USD']].corr()
print("\nCorrelation Matrix:")
print(correlation[['Closed PnL']].sort_values('Closed PnL', ascending=False))

# 7.2 Performance by Trade Size and Sentiment
print("\n7.2 Performance by Trade Size Categories:")
merged_data['Trade_Size_Category'] = pd.cut(
    merged_data['Size USD'],
    bins=[0, 100, 500, 1000, 5000, float('inf')],
    labels=['< $100', '$100-$500', '$500-$1K', '$1K-$5K', '> $5K']
)

size_sentiment_perf = merged_data.groupby(['Trade_Size_Category', 'classification'])['Closed PnL'].mean().unstack()
print(size_sentiment_perf.round(2))

# 7.3 Best and Worst Performing Sentiment Periods
print("\n7.3 Top 10 Best Performing Days (by Total PnL):")
daily_perf = merged_data.groupby(['date', 'classification'])['Closed PnL'].agg(['sum', 'count', 'mean']).reset_index()
daily_perf = daily_perf.sort_values('sum', ascending=False)
print(daily_perf.head(10).to_string(index=False))

print("\n7.4 Top 10 Worst Performing Days (by Total PnL):")
print(daily_perf.tail(10).to_string(index=False))

# 7.4 Account-level Analysis
print("\n7.5 Top 10 Accounts by Total PnL:")
account_perf = merged_data.groupby('Account').agg({
    'Closed PnL': ['sum', 'mean', 'count']
}).round(2)
account_perf.columns = ['Total_PnL', 'Avg_PnL', 'Trade_Count']
account_perf = account_perf.sort_values('Total_PnL', ascending=False)
print(account_perf.head(10))

# ============================================================================
# 8. KEY INSIGHTS
# ============================================================================
print("\n" + "=" * 80)
print("Step 8: Key Insights and Recommendations")
print("-" * 80)

print("\nKEY FINDINGS:")
print("-" * 80)

# Calculate key metrics
best_sentiment = avg_pnl.idxmax()
worst_sentiment = avg_pnl.idxmin()
best_win_rate = win_rates.idxmax()
worst_win_rate = win_rates.idxmin()

print(f"\n1. BEST PERFORMING SENTIMENT:")
print(f"   • {best_sentiment}: Average PnL = ${avg_pnl[best_sentiment]:.2f}")
print(f"   • Win Rate = {win_rates[best_sentiment]:.2f}%")

print(f"\n2. WORST PERFORMING SENTIMENT:")
print(f"   • {worst_sentiment}: Average PnL = ${avg_pnl[worst_sentiment]:.2f}")
print(f"   • Win Rate = {win_rates[worst_sentiment]:.2f}%")

print(f"\n3. HIGHEST WIN RATE:")
print(f"   • {best_win_rate}: {win_rates[best_win_rate]:.2f}% win rate")

print(f"\n4. CORRELATION INSIGHTS:")
corr_value = correlation.loc['Closed PnL', 'value']
corr_sentiment = correlation.loc['Closed PnL', 'sentiment_score']
print(f"   • Fear/Greed Value vs PnL: {corr_value:.4f}")
print(f"   • Sentiment Score vs PnL: {corr_sentiment:.4f}")

# Trading recommendations
print(f"\nTRADING RECOMMENDATIONS:")
print("-" * 80)

if avg_pnl['Extreme Fear'] > avg_pnl['Extreme Greed']:
    print("   • Consider contrarian strategy: Extreme Fear periods show better returns")
elif avg_pnl['Extreme Greed'] > avg_pnl['Extreme Fear']:
    print("   • Momentum strategy may work: Extreme Greed periods show better returns")

if win_rates['Extreme Fear'] > win_rates['Extreme Greed']:
    print("   • Higher win rate during Extreme Fear - may indicate buying opportunities")
elif win_rates['Extreme Greed'] > win_rates['Extreme Fear']:
    print("   • Higher win rate during Extreme Greed - trend following may be effective")

if corr_value > 0.1:
    print("   • Positive correlation detected: Higher sentiment → Better performance")
elif corr_value < -0.1:
    print("   • Negative correlation detected: Lower sentiment → Better performance (contrarian)")
else:
    print("   • Weak correlation: Sentiment may not be a strong predictor")

# Side analysis
buy_avg = merged_data[merged_data['Side'] == 'BUY']['Closed PnL'].mean()
sell_avg = merged_data[merged_data['Side'] == 'SELL']['Closed PnL'].mean()
print(f"\n   • BUY trades average: ${buy_avg:.2f}")
print(f"   • SELL trades average: ${sell_avg:.2f}")

if buy_avg > sell_avg:
    print("   • BUY trades outperform SELL trades on average")
else:
    print("   • SELL trades outperform BUY trades on average")

print("\n" + "=" * 80)
print("Analysis Complete! Check 'sentiment_trader_analysis.png' for visualizations.")
print("=" * 80)

