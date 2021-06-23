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

# Top 10 Happiest Countries
st.text("--------------------------------------------------------------------------------------------------")
st.markdown("What are the Top 10 Happiest Countries?")
happy_ten = whr[:10]

fig, ax = plt.subplots(figsize=(12,8))
plt.barh(happy_ten['Country name'], happy_ten['Ladder score'], color='royalblue', height=0.8)
ax.invert_yaxis()
ax.set_title('Top Ten Happiest Countries', fontsize=25)
plt.xticks([])

for i, j in enumerate(happy_ten['Ladder score']):
    plt.text(j, i, " " + str(round(j, 2)))

st.pyplot(fig)

# Regions of the top 25 happiest countries
st.text("--------------------------------------------------------------------------------------------------")
st.markdown("Which Regions contain the Happiest Countries?")
happy_25 = whr.sort_values('Ladder score', ascending=False)[:25]
happy_25['Regional indicator'].unique().tolist()
region_25 = {}

for i in happy_25['Regional indicator']:
    if i not in region_25:
        region_25[i] = 1
    else:
        region_25[i] += 1

labels, counts = [], []
for key in region_25:
    labels.append(key)
    counts.append(region_25[key])

fig2, ax2 = plt.subplots(figsize=(12,5))

plt.barh(labels, counts, color='royalblue', height=0.8)
ax2.invert_yaxis()
plt.xticks([])
for i, j in enumerate(counts):
    plt.text(j, i, " " + str(round(j, 2)), fontsize=15)

st.pyplot(fig2)

# Ladder score stats
ladderten_min = happy_ten['Ladder score'].min()
ladderten_max = happy_ten['Ladder score'].max()
ladderten_average = happy_ten['Ladder score'].mean()
ladderten = {
    "Min": ladderten_min,
    "Max": ladderten_max,
    "Average": ladderten_average
}

# GDP per capita stats
gdpten_min = happy_ten['Logged GDP per capita'].min()
gdpten_max = happy_ten['Logged GDP per capita'].max()
gdpten_average = happy_ten['Logged GDP per capita'].mean()
gdpten = {
    "Min": gdpten_min,
    "Max": gdpten_max,
    "Average": gdpten_average
}

# Social support stats
socialten_min = happy_ten['Social support'].min()
socialten_max = happy_ten['Social support'].max()
socialten_average = happy_ten['Social support'].mean()
socialten = {
    "Min": socialten_min,
    "Max": socialten_max,
    "Average": socialten_average
}


# Healthy expectancy stats
healthten_min = happy_ten['Healthy life expectancy'].min()
healthten_max = happy_ten['Healthy life expectancy'].max()
healthten_average = happy_ten['Healthy life expectancy'].mean()
healthten = {
    "Min": healthten_min,
    "Max": healthten_max,
    "Average": healthten_average
}

# Freedom of choice stats
freeten_min = happy_ten['Freedom to make life choices'].min()
freeten_max = happy_ten['Freedom to make life choices'].max()
freeten_average = happy_ten['Freedom to make life choices'].mean()
freeten = {
    "Min": freeten_min,
    "Max": freeten_max,
    "Average": freeten_average
}

# Generosity stats
generosityten_min = happy_ten['Generosity'].min()
generosityten_max = happy_ten['Generosity'].max()
generosityten_average = happy_ten['Generosity'].mean()
generosityten = {
    "Min": generosityten_min,
    "Max": generosityten_max,
    "Average": generosityten_average
}


# Ladder Score and GDP per capita
st.text("--------------------------------------------------------------------------------------------------")
st.markdown("GDP vs Ladder Score")

ladderrel = whr['Ladder score']
gdprel = whr['Logged GDP per capita']

figlad, ax = plt.subplots(figsize=(15,7))
plt.scatter(gdprel, ladderrel)

ax.set_title('Relationship between GDP per capita in Happiness')
ax.set_xlabel('GDP per Capita')
ax.set_ylabel('Ladder Score (Happiness)')

# calc the trendline
z = np.polyfit(gdprel, ladderrel, 1)
p = np.poly1d(z)
plt.plot(gdprel,p(gdprel),"r--")

st.pyplot(figlad)

st.text("--------------------------------------------------------------------------------------------------")
if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(whr)