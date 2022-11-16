import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_csv('NYC_Ferry_Ridership.csv')
df = df.head(100)

st.title('NYC Ferry Ridership')

st.caption('This dataset includes information on hourly NYC Ferry boardings by date, route, direction, ferry landing, and day of week. Boardings are the total number of people who boarded a vessel during the time period in question. This data forms the basis of internal NYC Ferry ridership tasks to guide service planning.')

if st.checkbox('Show first 100 records of NYC Ferry Ridership Dataset'):
    st.dataframe(df)

code = '''if st.checkbox('Show first 100 records of NYC Ferry Ridership Dataset'):
    '''
st.code(code, language='python')

## bar chart
st.subheader('Route')
route_type = df['Route'].value_counts()
st.bar_chart(route_type)

## line chart
st.subheader('Boardings')
board_count = df['Boardings'].value_counts()
st.line_chart(board_count)

code = '''
if st.checkbox('Show first 100 records of DOHMH Dog Bite Dataset'):
    st.dataframe(df)'''
st.code(code, language='python')