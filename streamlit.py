import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_csv('NYC_Ferry_Ridership.csv')
df = df.head(100)

st.title('NYC Ferry Ridership')

st.caption('This is the hourly information for NYC Ferry boarding by data, route, direction, and landing.')

if st.checkbox('Show first 100 records of NYC Ferry Ridership Dataset'):
    st.dataframe(df)

code = '''if st.checkbox('Show first 100 records of NYC Ferry Ridership Dataset'):
    st.dataframe(df)'''
st.code(code, language='python')

## bar chart
st.subheader('Route')
route_type = df['Route'].value_counts()
st.bar_chart(route_type)

## line chart
st.subheader('Boardings')
board_count = df['Boardings'].value_counts()
st.line_chart(board_count)