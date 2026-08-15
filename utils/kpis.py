import pandas as pd

def calc_kpis(df):
    """Calculate key performance indicators from the data."""
    kpis = {
        'total_sales': df['Sales'].sum() if 'Sales' in df.columns else 0,
        'total_profit': df['Profit'].sum() if 'Profit' in df.columns else 0,
        'total_orders': df['Order ID'].nunique() if 'Order ID' in df.columns else 0,
        'total_quantity': df['Quantity'].sum() if 'Quantity' in df.columns else 0,
    }
    
    # Calculate profit margin
    if kpis['total_sales'] > 0:
        kpis['profit_margin'] = (kpis['total_profit'] / kpis['total_sales']) * 100
    else:
        kpis['profit_margin'] = 0
    
    # Calculate average order value
    if kpis['total_orders'] > 0:
        kpis['avg_order_value'] = kpis['total_sales'] / kpis['total_orders']
    else:
        kpis['avg_order_value'] = 0
    
    return kpis

def top_bottom_summary(df):
    """Generate top and bottom performing insights."""
    summary = []
    
    # Top region by sales
    if 'Region' in df.columns and 'Sales' in df.columns:
        top_region = df.groupby('Region')['Sales'].sum().idxmax()
        top_sales = df.groupby('Region')['Sales'].sum().max()
        summary.append(f"🏆 Top Region: {top_region} (${top_sales:,.0f})")
    
    # Top category
    if 'Category' in df.columns and 'Sales' in df.columns:
        top_category = df.groupby('Category')['Sales'].sum().idxmax()
        top_cat_sales = df.groupby('Category')['Sales'].sum().max()
        summary.append(f"📊 Top Category: {top_category} (${top_cat_sales:,.0f})")
    
    # Most profitable segment
    if 'Segment' in df.columns and 'Profit' in df.columns:
        top_segment = df.groupby('Segment')['Profit'].sum().idxmax()
        top_seg_profit = df.groupby('Segment')['Profit'].sum().max()
        summary.append(f"💰 Most Profitable Segment: {top_segment} (${top_seg_profit:,.0f})")
    
    # Least profitable category
    if 'Category' in df.columns and 'Profit' in df.columns:
        bottom_category = df.groupby('Category')['Profit'].sum().idxmin()
        bottom_profit = df.groupby('Category')['Profit'].sum().min()
        summary.append(f"⚠️ Least Profitable Category: {bottom_category} (${bottom_profit:,.0f})")
    
    return "\n".join(summary) if summary else "No insights available for the selected filters."
