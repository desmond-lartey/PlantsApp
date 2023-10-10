import streamlit as st
import folium
from streamlit_folium import folium_static

def app():
    st.title("Home")
    
    # create a folium map object
    m = folium.Map(location=[45.5236, -122.6750])

    # display map on streamlit
    folium_static(m)
