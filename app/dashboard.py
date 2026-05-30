import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import streamlit as st

from src.data_loader import load_prices
from src.data_loader import load_returns

from src.charts import price_chart
from src.charts import returns_chart


st.set_page_config(page_title="European Momentum Dashboard",layout="wide")

st.title("European Momentum Dashboard")

st.write("Interactive monitoring of the momentum strategy.")

# Load data
prices = load_prices()
returns = load_returns()

# Sidebar
st.sidebar.header("Market Data")
st.sidebar.markdown("""
    Select a stock from the universe to explore:

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