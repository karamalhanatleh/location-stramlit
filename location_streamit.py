
import streamlit as st

# Custom CSS to style the iframe
iframe_style = """
    <style>
        .responsive-iframe {
            width: 70%;
            height: 170vh; /* Adjust this value as needed */
        }
    </style>
"""

# Display the custom CSS
st.markdown(iframe_style, unsafe_allow_html=True)

# Center-aligned title
st.markdown("<h1 style='text-align: center;'>حي العمور</h1>", unsafe_allow_html=True)

# Display the Google Maps iframe with responsive dimensions
st.components.v1.html(
    '<iframe class="responsive-iframe" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3375.5836358763736!2d35.778246574557436!3d32.21544821247477!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x151c85e548325d0b%3A0x7bba8399a6eedfd6!2z2K3ZiiDYp9mE2LnZhdmI2LE!5e0!3m2!1sen!2sjo!4v1694723145386!5m2!1sen!2sjo" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
    width=600,  # You can adjust this width if needed
    height=500,  # You can adjust this height if needed
)

