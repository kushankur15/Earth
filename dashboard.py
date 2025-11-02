import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config(layout="wide") 
st.header("World Wide Tsunami and Earthquake")

filename = r'G:/ML-Python/tsunami/earthquake_data_tsunami.csv'
df = pd.read_csv(filename)

fig1 = px.scatter_geo(df,
                        lat='latitude',
                        lon='longitude',
                        color='magnitude',
                        projection='robinson',
                        title='World Wide Earthquake Magnitude'
)
fig1.update_geos(showland=True, landcolor="LightGreen")

yearly_counts = df.groupby('Year').size().reset_index(name='Count')

fig2 = px.bar(
    yearly_counts,
    x='Year',
    y='Count',
    title='Number of Earthquakes per Year',
    color='Count', 
)

yearly_tsunami_counts = df.groupby(['Year', 'tsunami']).size().unstack(fill_value=0).reset_index()
yearly_tsunami_counts.columns = ['Year', 'No_Tsunami', 'Tsunami']

fig3 = px.bar(
    yearly_tsunami_counts.melt(id_vars='Year', value_vars=['No_Tsunami', 'Tsunami']),
    x='Year',
    y='value',
    color='variable',
    barmode='group',
    title='Tsunami vs Non-Tsunami Earthquakes per Year'
)

fig4 = px.box(df, y='magnitude', title='Magnitude Spread')

fig5 = px.scatter(
    df, x='depth', y='magnitude', color='tsunami',
    title='Depth vs Magnitude (colored by Tsunami occurrence)',
)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, use_container_width=True, key='chart1')
with col2:
    st.plotly_chart(fig2, use_container_width=True, key='chart2')

col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(fig3, use_container_width=True, key='chart3')
with col4:
    st.plotly_chart(fig4, use_container_width=True, key='chart4')

# Last chart full width
st.plotly_chart(fig5, use_container_width=True, key='chart5')