# Bitcoin Market Sentiment vs Trader Performance Analysis Report

## Executive Summary

This analysis explores the relationship between Bitcoin's Fear/Greed Index and Hyperliquid trader performance, analyzing **104,402 trades** from December 2023 to May 2025 to uncover patterns and trading insights.

---

## Dataset Overview

### Fear/Greed Index Dataset
- **Records**: 2,644 daily sentiment readings
- **Date Range**: February 1, 2018 to May 2, 2025
- **Sentiment Classifications**: Extreme Fear, Fear, Neutral, Greed, Extreme Greed

### Historical Trader Data
- **Total Records**: 211,224 trades
- **Analyzed Records**: 104,402 trades with valid PnL data
- **Date Range**: December 14, 2023 to May 1, 2025
- **Key Metrics**:
  - Total PnL: **$10,254,486.95**
  - Average PnL per trade: **$98.22**
  - Median PnL per trade: **$6.05**
  - Win Rate: **83.20%** (86,863 winning trades)

---

## Key Findings

### 1. Performance by Market Sentiment

| Sentiment | Trade Count | Total PnL | Avg PnL | Win Rate |
|-----------|-------------|-----------|---------|----------|
| **Extreme Greed** | 20,853 | $2,715,171.31 | **$130.21** | **89.17%** |
| Greed | 25,176 | $2,150,129.27 | $85.40 | 76.89% |
| Fear | 29,808 | $3,357,155.44 | $112.60 | 87.29% |
| Neutral | 18,159 | $1,292,920.68 | $71.23 | 82.39% |
| **Extreme Fear** | 10,406 | $739,110.25 | **$71.03** | **76.22%** |

### 2. Critical Insights

#### Best Performing Sentiment: **Extreme Greed**
- **Average PnL**: $130.21 per trade
- **Win Rate**: 89.17% (highest among all sentiments)
- **Total PnL**: $2.7M from 20,853 trades
- **Insight**: Momentum/trend-following strategies appear most effective during extreme greed periods

#### Worst Performing Sentiment: **Extreme Fear**
- **Average PnL**: $71.03 per trade (lowest)
- **Win Rate**: 76.22% (lowest)
- **Total PnL**: $739K from 10,406 trades
- **Insight**: Contrarian strategies during extreme fear show lower returns than expected

### 3. Trade Distribution by Sentiment

- **Fear**: 28.55% of trades (most common)
- **Greed**: 24.11% of trades
- **Extreme Greed**: 19.97% of trades
- **Neutral**: 17.39% of trades
- **Extreme Fear**: 9.97% of trades (least common)

### 4. Correlation Analysis

- **Fear/Greed Value vs PnL**: 0.0092 (very weak positive correlation)
- **Sentiment Score vs PnL**: 0.0065 (very weak positive correlation)
- **Trade Size vs PnL**: 0.1627 (moderate positive correlation)

**Interpretation**: While sentiment shows a weak direct correlation with PnL, the relationship is more nuanced when analyzed by sentiment categories.

### 5. BUY vs SELL Performance

- **BUY Trades Average PnL**: $101.65
- **SELL Trades Average PnL**: $96.41
- **Insight**: BUY trades slightly outperform SELL trades, but the difference is marginal

### 6. Performance by Trade Size

Larger trades consistently show higher absolute PnL across all sentiment categories:

| Trade Size | Extreme Fear | Extreme Greed | Fear | Greed | Neutral |
|------------|--------------|---------------|------|-------|---------|
| < $100 | -$1.01 | $4.62 | $1.50 | $2.31 | $0.66 |
| $100-$500 | $1.15 | $25.96 | $9.01 | $13.82 | $5.01 |
| $500-$1K | $15.41 | $57.40 | $23.45 | $22.30 | $18.48 |
| $1K-$5K | $19.88 | $149.39 | $76.01 | $66.55 | $71.55 |
| > $5K | $405.57 | $816.06 | $513.61 | $449.54 | $370.13 |

**Key Insight**: Trade size has a stronger impact on PnL than sentiment alone.

---

## Top Performing Days

### Best Days (by Total PnL)
1. **March 3, 2025 (Fear)**: $616,413 from 945 trades
2. **December 12, 2024 (Extreme Greed)**: $599,152 from 1,417 trades
3. **February 4, 2025 (Greed)**: $416,877 from 797 trades

### Worst Days (by Total PnL)
1. **April 23, 2025 (Greed)**: -$419,020 from 4,139 trades
2. **November 28, 2024 (Extreme Greed)**: -$127,075 from 228 trades
3. **August 4, 2024 (Fear)**: -$122,672 from 65 trades

**Note**: Even during "favorable" sentiment periods, individual days can show significant losses, highlighting the importance of risk management.

---

## Top Performing Accounts

| Account | Total PnL | Avg PnL | Trade Count |
|---------|-----------|---------|-------------|
| 0xb1231a4a2dd02f2276fa3c5e2a2f3436e6bfed23 | $2,143,383 | $341.36 | 6,279 |
| 0x083384f897ee0f19899168e3b1bec365f52a9012 | $1,600,230 | $923.92 | 1,732 |
| 0xbaaaf6571ab7d571043ff1e313a9609a10637864 | $940,164 | $94.04 | 9,997 |

---

## Trading Recommendations

### 1. **Momentum Strategy During Extreme Greed**
- **Evidence**: Extreme Greed shows highest average PnL ($130.21) and win rate (89.17%)
- **Action**: Consider trend-following strategies when sentiment reaches extreme greed levels
- **Risk**: Be cautious of potential reversals; use stop-losses

### 2. **Trade Size Matters More Than Sentiment**
- **Evidence**: Trade size correlation (0.1627) is 18x stronger than sentiment correlation (0.0092)
- **Action**: Focus on position sizing and risk management over sentiment timing
- **Insight**: Larger trades show better absolute returns across all sentiment levels

### 3. **BUY Slightly Outperforms SELL**
- **Evidence**: BUY trades average $101.65 vs SELL trades $96.41
- **Action**: Slight bias toward long positions, but difference is marginal
- **Note**: Consider market conditions and individual trade setups over general bias

### 4. **Sentiment as a Filter, Not a Signal**
- **Evidence**: Weak direct correlation (0.0092) suggests sentiment alone is not a strong predictor
- **Action**: Use sentiment as a context filter rather than a primary trading signal
- **Best Use**: Combine sentiment with other technical/fundamental indicators

### 5. **Risk Management is Critical**
- **Evidence**: Even during favorable sentiment periods, significant losses can occur
- **Action**: Always implement proper risk management regardless of sentiment
- **Example**: April 23, 2025 showed -$419K loss during Greed sentiment

---

## Limitations and Considerations

1. **Time Period**: Analysis covers December 2023 to May 2025 - may not represent all market cycles
2. **Weak Correlation**: Direct sentiment-PnL correlation is very weak (0.0092)
3. **Market Regime**: Results may vary in different market conditions (bull vs bear markets)
4. **Selection Bias**: Only closed positions with non-zero PnL are analyzed
5. **Multiple Factors**: PnL is influenced by many factors beyond sentiment (price action, timing, leverage, etc.)

---

## Conclusion

While the Fear/Greed Index shows a **weak direct correlation** with trader performance, **categorical analysis reveals meaningful patterns**:

1. **Extreme Greed periods** offer the best risk-adjusted returns (highest win rate and average PnL)
2. **Trade size** has a stronger impact on PnL than sentiment alone
3. **Sentiment should be used as context** rather than a primary trading signal
4. **Risk management remains paramount** regardless of sentiment levels

The data suggests that **momentum/trend-following strategies during extreme greed periods** may be more effective than contrarian strategies during extreme fear, contrary to some traditional market wisdom.

---

## Files Generated

1. **sentiment_trader_analysis.py**: Complete analysis script
2. **sentiment_trader_analysis.png**: Comprehensive visualization dashboard
3. **ANALYSIS_REPORT.md**: This summary report

---

*Analysis Date: Generated from data covering December 2023 - May 2025*
*Total Trades Analyzed: 104,402*
*Total PnL Analyzed: $10,254,486.95*

