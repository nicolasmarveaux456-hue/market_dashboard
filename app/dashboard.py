import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import streamlit as st

from src.data_loader import load_prices
from src.data_loader import load_returns
from src.data_loader import load_backtest_summary
from src.data_loader import load_performance_metrics

from src.charts import price_chart
from src.charts import returns_chart
from src.charts import strategy_vs_benchmark_chart


st.set_page_config(page_title="European Momentum Dashboard",layout="wide")

st.title("European Momentum Dashboard")

st.write("Interactive monitoring of the momentum strategy.")

# Load data
prices = load_prices()
returns = load_returns()
backtest_summary = load_backtest_summary()
performance_metrics = load_performance_metrics()


# Sidebar navigation
st.sidebar.header("Navigation")
section = st.sidebar.radio("Select a section",["Market Data","Strategy Performance"])


# Section 1 — Market Data
if section == "Market Data":
    st.header("Market Data Exploration")
    st.sidebar.subheader("Ticker Selection")
    st.sidebar.markdown("""
        Select a stock from the universe to explore :

        - historical prices
        - monthly returns
        """)
    ticker = st.sidebar.selectbox("Select a ticker",prices.columns)
    
    # Selected series
    price_series = prices[ticker]
    return_series = returns[ticker]
    
    # Price chart
    st.subheader("Historical Price")
    st.plotly_chart(price_chart(price_series, ticker),use_container_width=True)

    # Returns chart
    st.subheader("Monthly Returns")
    st.plotly_chart(returns_chart(return_series, ticker),use_container_width=True)


# Section 2 — Strategy Performance
if section == "Strategy Performance":
    st.header("Momentum Strategy Performance")
    st.write("""
        This section compares the momentum strategy with the FEZ benchmark.

        Strategy rules :
        - 12-1 momentum signal
        - top 30% stock selection
        - equal weighting
        - monthly rebalancing
        """)
    st.subheader("Equity Curve")
    st.plotly_chart(strategy_vs_benchmark_chart(backtest_summary),use_container_width=True)
    st.subheader("Performance Metrics")

    col1, col2, col3 = st.columns(3)
    strategy_cagr = performance_metrics.loc["CAGR", "Momentum Strategy"]
    strategy_vol = performance_metrics.loc["Annualized Volatility", "Momentum Strategy"]
    strategy_sharpe = performance_metrics.loc["Sharpe Ratio", "Momentum Strategy"]

    col1.metric("CAGR", f"{strategy_cagr:.2%}")
    col2.metric("Volatility", f"{strategy_vol:.2%}")
    col3.metric("Sharpe Ratio", f"{strategy_sharpe:.2f}")

    st.write("Full performance metrics table :")
    st.dataframe(performance_metrics,use_container_width=True)
    st.subheader("Interpretation")
    st.write("""
        The equity curve compares the cumulative performance of the momentum strategy
        against the FEZ benchmark.

        The performance metrics summarize :
        - CAGR : annualized compounded return
        - Volatility : annualized risk
        - Sharpe Ratio : risk-adjusted performance
        """)