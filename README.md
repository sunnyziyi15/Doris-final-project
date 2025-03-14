Interactive Visualization: U.S. Obesity, Income, and GDP (2023)
An interactive Streamlit application visualizing relationships between obesity prevalence rates, median household income, and GDP across the United States in 2023.


Overview
This project provides two main interactive visualizations built with Streamlit and Plotly Express:
1. Bubble Chart
Displays the correlation between state obesity prevalence rates, median household incomes, and GDP. Users can select states and filter ranges to explore customized insights.
2. Choropleth Map
Offers a visual geographic representation of obesity prevalence across U.S. states.
Interactive hover features display median household income and GDP.


Features
1. Interactive Filtering:
State selection via multi-select dropdown.
Range sliders for obesity prevalence and median household income.
2. Dynamic Bubble Chart:
Bubble size corresponds to GDP, enhancing visual comparison.
3. Interactive Choropleth Map:
Color-coded states by obesity rates.
Hover information for detailed economic insights.


Usage
You have two options to view and interact with this application:
1. Visit the deployed Streamlit application at:
https://sunnyziyi15-doris-final-project-code-t3ru7e.streamlit.app/
2. Local Run:
   Clone the repository and run the application locally with:
       streamlit run code.py


Installation
Dependencies (requirements.txt):
streamlit==1.32.2
pandas==2.2.1
plotly==5.20.0


Data Sources
- **GDP by State (2023)**: [U.S. Bureau of Economic Analysis (BEA)](https://www.bea.gov/data/gdp/gdp-state)  
- **Adult Obesity Prevalence Rates (2023)**: [Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/obesity/data-and-statistics/adult-obesity-prevalence-maps.html)  
- **Median Household Income by State (2023)**: [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/series/MEHOINUSA672N)

*Note: Data for Kentucky and Pennsylvania are currently unavailable.*

