import plotly.express as px


def price_chart(price_series, ticker):
    fig = px.line(x=price_series.index,y=price_series.values,title=f"{ticker} Historical Price")
    fig.update_layout(xaxis_title="Date",yaxis_title="Price")
    return fig


def returns_chart(return_series, ticker):
    fig = px.bar(x=return_series.index,y=return_series.values,title=f"{ticker} Monthly Returns")
    fig.update_layout(xaxis_title="Date",yaxis_title="Return")
    return fig