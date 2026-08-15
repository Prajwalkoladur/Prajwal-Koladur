import streamlit as st

def sidebar_filters(df):
    """Create sidebar filters for the Superstore data."""
    st.sidebar.title("Filters")
    
    filters = {}
    
    # Get available columns for filtering
    filter_cols = [col for col in df.columns if col not in ['Order ID', 'Row ID']]
    
    # Region filter
    if 'Region' in df.columns:
        regions = df['Region'].unique()
        filters['region'] = st.sidebar.multiselect('Region', regions, default=list(regions))
    
    # Category filter
    if 'Category' in df.columns:
        categories = df['Category'].unique()
        filters['category'] = st.sidebar.multiselect('Category', categories, default=list(categories))
    
    # Year filter
    if 'Order Date' in df.columns:
        years = sorted(df['Order Date'].dt.year.unique())
        filters['year'] = st.sidebar.multiselect('Year', years, default=years)
    
    return filters

def apply_filters(df, filters):
    """Apply filters to the dataframe."""
    df_filtered = df.copy()
    
    # Apply region filter
    if 'region' in filters and filters['region']:
        df_filtered = df_filtered[df_filtered['Region'].isin(filters['region'])]
    
    # Apply category filter
    if 'category' in filters and filters['category']:
        df_filtered = df_filtered[df_filtered['Category'].isin(filters['category'])]
    
    # Apply year filter
    if 'year' in filters and filters['year']:
        if 'Order Date' in df_filtered.columns:
            df_filtered = df_filtered[df_filtered['Order Date'].dt.year.isin(filters['year'])]
    
    return df_filtered
