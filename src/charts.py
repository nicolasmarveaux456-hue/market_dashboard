import plotly.express as px
import plotly.graph_objects as go


def price_chart(price_series, ticker):
    fig = px.line(x=price_series.index,y=price_series.values,title=f"{ticker} Historical Price")
    fig.update_layout(xaxis_title="Date",yaxis_title="Price")
    return fig


def returns_chart(return_series, ticker):
    fig = px.bar(x=return_series.index,y=return_series.values,title=f"{ticker} Monthly Returns")
    fig.update_layout(xaxis_title="Date",yaxis_title="Return")
    return fig


def strategy_vs_benchmark_chart(backtest_summary):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=backtest_summary.index,y=backtest_summary["Strategy Equity"],mode="lines",name="Momentum Strategy"))
    fig.add_trace(go.Scatter(x=backtest_summary.index,y=backtest_summary["FEZ Equity"],mode="lines",name="FEZ Benchmark"))
    fig.update_layout(title="Momentum Strategy vs FEZ Benchmark",xaxis_title="Date",yaxis_title="Portfolio Value (Base = 100)")
    return fig