import streamlit as st
import pandas as pd

# Create a DataFrame with the coordinates
place = pd.DataFrame({
    'lat': [32.2154437],
    'lon': [35.7808215]
})

# Use Streamlit to display the map
st.map(place)
