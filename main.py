import streamlit as st
import plotly.express as px

# Add title, text input, slider, select-box and sub-header

st.title("Weather Forecast for the Next 1 to 5 Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
