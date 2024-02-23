import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, select-box and sub-header

st.title("Weather Forecast for the Next 1 to 5 Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # get the temperature/sky data from backend
    filtered_data = get_data(place, days, option)

    if option == "Temperature":
        temperatures = [dictionary["main"]["temp"] for dictionary in filtered_data]
        temperatures = [temp/10 for temp in temperatures]
        dates = [dictionary["dt_txt"] for dictionary in filtered_data]

        # create a temperature plot
        figure = px.line(x=dates, y=temperatures,
                         labels={"x": "Dates", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        sky_conditions = [dictionary["weather"][0]["main"] for dictionary
                          in filtered_data]
        images = {"Clear": "images/clear.png",
                  "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        image_paths = [images[condition] for condition in sky_conditions]
        captions = [dictionary["dt_txt"] for dictionary in filtered_data]
        st.image(image_paths, width=115, caption=captions)
