import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")


st.title("Bubble Chart: Obesity Prevalence, Median Household Income, and GDP Across U.S. States")


obesity = pd.read_csv("Obesity.csv")
household = pd.read_csv("Household.csv")
gdp = pd.read_csv("GDP.csv")


obesity['State'] = obesity['State'].str.strip()
household['State'] = household['State'].str.strip()
gdp['State'] = gdp['State'].str.strip()


df = pd.merge(obesity, household, on="State", how="inner")
df = pd.merge(df, gdp, on="State", how="inner")


df['Prevalence'] = pd.to_numeric(df['Prevalence'], errors="coerce")
df['Median Household Income'] = pd.to_numeric(df['Median Household Income'], errors="coerce")
df['GDP_2023'] = pd.to_numeric(df['GDP_2023'], errors="coerce")


selected_states = st.multiselect(
    "Select States for Comparison",
    df["State"].unique(),
    default=[]  
)


obesity_range = st.slider(
    "Select Obesity Prevalence Range (%)",
    min_value=int(df["Prevalence"].min()),
    max_value=int(df["Prevalence"].max()),
    value=(int(df["Prevalence"].min()), int(df["Prevalence"].max()))
)


income_range = st.slider(
    "Select Median Household Income Range ($)",
    min_value=int(df["Median Household Income"].min()),
    max_value=int(df["Median Household Income"].max()),
    step=5000,
    value=(int(df["Median Household Income"].min()), int(df["Median Household Income"].max()))
)


filtered_df = df[
    (df["Prevalence"] >= obesity_range[0]) & 
    (df["Prevalence"] <= obesity_range[1]) & 
    (df["Median Household Income"] >= income_range[0]) & 
    (df["Median Household Income"] <= income_range[1])
]


if selected_states:
    filtered_df = filtered_df[filtered_df["State"].isin(selected_states)]


bubble_fig = px.scatter(
    filtered_df,
    x="Prevalence",
    y="Median Household Income",
    size="GDP_2023",
    hover_name="State",
    title="Relationship between State Obesity Prevalence Rates and Median Household Income in 2023 (Bubble Size Represents GDP)<br>*Kentucky and Pennsylvania data are missing*",
    size_max=60
)

bubble_fig.update_layout(
    title_font_size=20,
    height=500
)


st.plotly_chart(bubble_fig, use_container_width=True, key="unique_plotly_chart")


st.markdown(
    """
    <div style="font-size:21px; line-height:1.2;">
    From the Bubble Chart, we can observe:<br><br>
    1️⃣ <strong>General Inverse Relationship:</strong> States with higher obesity rates often show lower median household incomes, indicating a possible negative correlation between income and obesity prevalence.<br><br>
    2️⃣ <strong>GDP Variations:</strong> The bubble sizes, representing GDP, vary widely, suggesting that a higher GDP does not necessarily correlate with lower obesity or higher incomes.<br><br>
    3️⃣ <strong>Regional Disparities:</strong> Some states deviate from the overall trend, implying that additional factors such as regional culture, lifestyle, or urbanization may also influence obesity rates.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<hr style='margin:40px 0;'>", unsafe_allow_html=True)


st.title("Choropleth Map: State Obesity Prevalence Rates")


obesity = pd.read_csv("Obesity.csv")


obesity['State'] = obesity['State'].str.strip()


state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "District of Columbia": "DC",
    "Florida": "FL",
    "Georgia": "GA",
    "Guam": "GU",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Puerto Rico": "PR",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virgin Islands": "VI",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}

df["code"] = df["State"].map(state_abbrev)
df = df.dropna(subset=["code"])


df["Prevalence"] = pd.to_numeric(df["Prevalence"], errors="coerce")
df["Median Household Income"] = pd.to_numeric(df["Median Household Income"], errors="coerce")
df["GDP_2023"] = pd.to_numeric(df["GDP_2023"], errors="coerce")


choropleth_fig = px.choropleth(
    df,
    locations="code",
    locationmode="USA-states",
    color="Prevalence",
    scope="usa",
    color_continuous_scale="Viridis",
    title="A Visual Distribution of Obesity Prevalence Rates Across the U.S. (2023)<br>*Kentucky and Pennsylvania data are missing*",
    hover_data=["Median Household Income", "GDP_2023"],
    labels={
        "Prevalence": "Obesity Prevalence (%)",
        "Median Household Income": "Median Household Income (USD)",
        "GDP_2023": "GDP (USD)"
    }
)


choropleth_fig.update_layout(
    title_font_size=20  
)


choropleth_fig.update_layout(
    autosize=False,
    width=1000,
    height=700,
)



choropleth_fig.update_coloraxes(
    colorbar=dict(
        y=0.5,         
        len=0.8,       
        yanchor='middle'
    )
)


col1, col2 = st.columns([3, 2])
with col1:
    st.plotly_chart(choropleth_fig, use_container_width=False)

with col2:
    st.markdown(
        """
        <div style='margin-top:70px; font-size:21px;'>
        <h2 style='font-size:24px;'>Color Explanation</h2>
        <p style='font-size:21px; line-height:1.6;'>
        The closer the color is to yellow, the higher the obesity prevalence rate. Conversely, the closer it is to 
        dark blue or purple, the lower the obesity prevalence rate.<br><br>
        - <strong>Dark blue or purple</strong>: lowest obesity prevalence rates, around 25%<br>
        - <strong>Blue-green or green</strong>: moderate obesity prevalence rates, typically around 30%–35%<br>
        - <strong>Light green or yellow-green</strong>: moderately high obesity prevalence rates, roughly 35%–38%<br>
        - <strong>Yellow</strong>: highest obesity prevalence rates, reaching 40% or more<br><br>
        🔴 <strong>Highest Obesity Prevalence Rate:</strong> West Virginia - 41.2% (GDP: $102152)<br>
        🟢 <strong>Lowest Obesity Prevalence Rate:</strong> District of Columbia - 23.5% (GDP: $176502)
        </p>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    """
    <hr style='margin:40px 0;'>

    <div style='font-size:18px; line-height:1.6;'>
    📚 <strong>Data Sources:</strong><br>
    - GDP by State: [U.S. Bureau of Economic Analysis (BEA)](https://www.bea.gov/data/gdp/gdp-state)<br>
    - Obesity Prevalence Rates: [Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/obesity/data-and-statistics/adult-obesity-prevalence-maps.html)<br>
    - Median Household Income: [U.S. Census Bureau](https://www.census.gov/library/publications/2024/demo/p60-282.html)
    </div>
    """,
    unsafe_allow_html=True
)
