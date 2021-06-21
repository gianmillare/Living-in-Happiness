import streamlit as st
import pandas as pd
import numpy as np

st.title("World Happiness Analysis")
st.markdown("### An analysis on the 2021 World Happiness Report. In this app, I analyze the commonalities of the top ten" 
            " happiest countries, and provide statistics on constituents of a country's happiness score.")

@st.cache(persist=True)
def load_data():
    data = pd.read_csv('resources/WHR2020.csv')
    data = data.sort_values("Ladder score", ascending=False)
    whr = data[['Country name', 'Regional indicator', 'Ladder score',
          'Logged GDP per capita', 'Social support', 'Healthy life expectancy',
          'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']]
    return whr

whr = load_data()

st.markdown("### Raw Data")
st.write(whr)