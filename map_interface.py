import streamlit as st
import folium
from streamlit_folium import folium_static

def app():
    st.title("Map Display")
    
    # Create a folium map object
    m = folium.Map(location=[45.5236, -122.6750])
    
    # Display the map on Streamlit
    folium_static(m)
