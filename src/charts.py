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


def drawdown_chart(backtest_summary):
    strategy_equity = backtest_summary["Strategy Equity"]
    fez_equity = backtest_summary["FEZ Equity"] 
    strategy_drawdown = (strategy_equity / strategy_equity.cummax()) - 1
    fez_drawdown = (fez_equity / fez_equity.cummax()) - 1
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=strategy_drawdown.index,y=strategy_drawdown,mode="lines",name="Momentum Strategy"))
    fig.add_trace(go.Scatter(x=fez_drawdown.index,y=fez_drawdown,mode="lines",name="FEZ Benchmark"))
    fig.update_layout(title="Drawdown: Momentum Strategy vs FEZ Benchmark",xaxis_title="Date",yaxis_title="Drawdown")
    return fig


def rolling_volatility_chart(backtest_summary, window=12):
    strategy_rolling_vol = (backtest_summary["Strategy Return"].rolling(window).std()*(12 ** 0.5))
    fez_rolling_vol = (backtest_summary["FEZ Return"].rolling(window).std()*(12 ** 0.5))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=strategy_rolling_vol.index,y=strategy_rolling_vol,mode="lines",name="Momentum Strategy"))
    fig.add_trace(go.Scatter(x=fez_rolling_vol.index,y=fez_rolling_vol,mode="lines",name="FEZ Benchmark"))
    fig.update_layout(title="12-Month Rolling Volatility",xaxis_title="Date",yaxis_title="Annualized Volatility")
    return fig


def turnover_chart(transaction_costs_summary):
    fig = px.line(x=transaction_costs_summary.index,y=transaction_costs_summary["Turnover"],title="Monthly Portfolio Turnover")
    fig.update_layout(xaxis_title="Date",yaxis_title="Turnover")
    return fig


def gross_vs_net_chart(transaction_costs_summary):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=transaction_costs_summary.index,y=transaction_costs_summary["Gross Equity"],mode="lines",name="Gross Momentum Strategy"))
    fig.add_trace(go.Scatter(x=transaction_costs_summary.index,y=transaction_costs_summary["Net Equity"],mode="lines",name="Net Momentum Strategy"))
    fig.update_layout(title="Gross vs Net Momentum Strategy",xaxis_title="Date",yaxis_title="Portfolio Value (Base = 100)")
    return fig