import streamlit as st

# Custom CSS to center-align the title
title_style = """
    <style>
        .title {
            text-align: center;
        }
    </style>
"""

# Display the custom CSS
st.markdown(title_style, unsafe_allow_html=True)

# Center-aligned title
st.markdown("<h1 class='title'>حي العمور</h1>", unsafe_allow_html=True)

# Define the zoom level (you can adjust this as needed)
zoom_level = 30

# Modify the Google Maps URL to include the zoom level
google_maps_url = f'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3375.5836358763736!2d35.778246574557436!3d32.21544821247477!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x151c85e548325d0b%3A0x7bba8399a6eedfd6!2z2K3ZiiDYp9mE2LnZhdmI2LE!5e0!3m2!1sen!2sjo!4v1694723145386!5m2!1sen!2sjo&z={zoom_level}'

# Display the Google Maps iframe with the modified URL
st.components.v1.html(
    f'<iframe src="{google_maps_url}" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
    width=350,
    height=500,
)
