import streamlit as st
import pandas as pd
import plotly.express as px
from phik import phik_matrix
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
import random

data = pd.read_csv('./data/Housing.csv')

with st.expander('Show raw data'):
    st.dataframe(data.head(10))

with st.sidebar:

    st.slider(
    "Area:", min_value=data['area'].min().astype(int),
    max_value=data['area'].max().astype(int), value=data['area'].mean().astype(int), step=500,
    )
    st.slider(
    "Bedrooms:", min_value=data['bedrooms'].min().astype(int),
    max_value=data['bedrooms'].max().astype(int), value=data['bedrooms'].mean().astype(int), step=500,
    )
    st.slider(
    "Bathrooms:", min_value=data['bathrooms'].min().astype(int),
    max_value=data['bathrooms'].max().astype(int), value=data['bathrooms'].mean().astype(int), step=500,
    )
    st.slider(
    "Stories:", min_value=data['stories'].min().astype(int),
    max_value=data['stories'].max().astype(int), value=data['stories'].mean().astype(int), step=500,
    )
    st.slider(
    "Parking:", min_value=data['parking'].min().astype(int),
    max_value=data['parking'].max().astype(int), value=data['parking'].mean().astype(int), step=500,
    )

    st.radio(
        'Have you mainroad?',
        sorted(data['mainroad'].unique())
    )
    # ----------------------
    st.radio(
        'Have you guestroom?',
        sorted(data['guestroom'].unique())
    )
    # ----------------------
    st.radio(
        'Have you basement?',
        sorted(data['basement'].unique())
    )
    # ----------------------
    st.radio(
        'Have you hotwaterheating?',
        sorted(data['hotwaterheating'].unique())
    )
    # ----------------------
    st.radio(
        'Have you airconditioning?',
        sorted(data['airconditioning'].unique())
    )
    # ----------------------
    st.radio(
        'Have you prefarea?',
        sorted(data['prefarea'].unique())
    )
    # ----------------------
    st.radio(
        'Have you furnishingstatus?',
        sorted(data['furnishingstatus'].unique())
    )
    # ----------------------
corr_mat = data.phik_matrix().stack().reset_index(name="correlation")
fig = px.scatter(corr_mat, x="level_0", y="level_1", color="correlation",
                 size="correlation", color_continuous_scale="RdBu",
                 width=500, height=400)
fig.update_layout(xaxis=dict(tickangle=90),
                  yaxis=dict(tickangle=0),
                  xaxis_title="", yaxis_title="",
                  showlegend=False)
st.plotly_chart(fig)
# --------
fig = make_subplots(rows=2, cols=2, subplot_titles=['mainroad', 'prefarea',
                                    'basement', 'furnishingstatus'], 
                    specs=[[{'type':'pie'}, {'type':'pie'}],
                           [{'type':'pie'}, {'type':'pie'}]])
fig.add_trace(
    go.Pie(labels=data['mainroad'].value_counts().index, values=data['mainroad'].value_counts().tolist(), name='mainroad'),
    row=1, col=1
)
fig.add_trace(
    go.Pie(labels=data['prefarea'].value_counts().index, values=data['prefarea'].value_counts().tolist(), name='prefarea'),
    row=1, col=2
)
fig.add_trace(
    go.Pie(labels=data['basement'].value_counts().index, values=data['basement'].value_counts().tolist(), name='basement'),
    row=2, col=1
)
fig.add_trace(
    go.Pie(labels=data['furnishingstatus'].value_counts().index, values=data['furnishingstatus'].value_counts().tolist(), name='furnishingstatus'),
    row=2, col=2
)
fig.update_layout(height=600, width=800, title_text="Multiple Subplots Example")
fig.update_traces(showlegend=True)
st.plotly_chart(fig)

if st.button('Show res'):
    with st.spinner('Please wait...'):
        time.sleep(5)
        price = random.randint(data['price'].min(), data['price'].max())
        st.success(f'Complete!\n Price: {price}')