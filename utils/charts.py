import plotly.express as px
import pandas as pd

def line_chart(df, x_col, y_col, title, freq="ME"):
    """Create a line chart."""
    if x_col not in df.columns or y_col not in df.columns:
        return None
    
    # Group by x_col and sum y_col for monthly/temporal data
    if 'Date' in x_col:
        # Map frequency abbreviations
        freq_map = {'M': 'ME', 'Q': 'QE', 'Y': 'YE'}
        freq = freq_map.get(freq, freq)
        df_grouped = df.set_index(x_col).resample(freq)[y_col].sum().reset_index()
    else:
        df_grouped = df.groupby(x_col, as_index=False)[y_col].sum()
    
    fig = px.line(df_grouped, x=x_col, y=y_col, title=title, markers=True)
    fig.update_xaxes(title_text=x_col)
    fig.update_yaxes(title_text=y_col)
    return fig

def bar_chart(df, x_col, y_col, title, top_n=None):
    """Create a bar chart."""
    if x_col not in df.columns or y_col not in df.columns:
        return None
    
    df_grouped = df.groupby(x_col, as_index=False)[y_col].sum().sort_values(y_col, ascending=False)
    
    # Limit to top N if specified
    if top_n:
        df_grouped = df_grouped.head(top_n)
    
    fig = px.bar(df_grouped, x=x_col, y=y_col, title=title, color=y_col, color_continuous_scale='Blues')
    fig.update_xaxes(title_text=x_col)
    fig.update_yaxes(title_text=y_col)
    return fig

def scatter_chart(df, x_col, y_col, color_col, title):
    """Create a scatter chart."""
    if x_col not in df.columns or y_col not in df.columns:
        return None
    
    color_col_valid = color_col if color_col in df.columns else None
    
    fig = px.scatter(df, x=x_col, y=y_col, color=color_col_valid, title=title, 
                    hover_data=['Order ID'] if 'Order ID' in df.columns else None)
    fig.update_xaxes(title_text=x_col)
    fig.update_yaxes(title_text=y_col)
    return fig

def histogram(df, col, title):
    """Create a histogram."""
    if col not in df.columns:
        return None
    
    fig = px.histogram(df, x=col, title=title, nbins=30)
    fig.update_xaxes(title_text=col)
    fig.update_yaxes(title_text="Frequency")
    return fig
