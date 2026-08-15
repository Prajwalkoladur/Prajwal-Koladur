import streamlit as st

st.set_page_config(page_title="SuperStore Analytics Dashboard", layout="wide")

st.title("🏪 SuperStore Analytics Dashboard")

st.markdown("""
## Welcome to SuperStore Analytics!

This dashboard provides comprehensive analytics for the SuperStore dataset. 
Navigate through different analysis pages using the sidebar to explore:

- **Executive Overview**: Key metrics and sales trends
- **Sales Analysis**: Detailed sales performance across time periods
- **Profit Analysis**: Profit distribution and performance by categories
- **Regional Analysis**: Regional performance metrics
- **State Analysis**: State-wise sales and profit insights
- **City Analysis**: City-level detailed analytics

Select a page from the sidebar to begin exploring the data.
""")

st.sidebar.success("Select a page above to get started!")
