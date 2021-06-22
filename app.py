import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

happy_ten = whr[:10]

fig, ax = plt.subplots(figsize=(12,8))
plt.barh(happy_ten['Country name'], happy_ten['Ladder score'], color='royalblue', height=0.8)
ax.invert_yaxis()
ax.set_title('Top Ten Happiest Countries', fontsize=25)
plt.xticks([])

for i, j in enumerate(happy_ten['Ladder score']):
    plt.text(j, i, " " + str(round(j, 2)))

st.pyplot(fig)

st.markdown("### Raw Data")
if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(whr)