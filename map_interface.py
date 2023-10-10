import streamlit as st
import leafmap.foliumap as leafmap

def app():
    st.title("Home")
    st.markdown(
        """
    A [streamlit](https://streamlit.io) app template for geospatial applications. 
    To create a direct link to a pre-selected menu, add `?page=<app name>` to the URL, e.g., `?page=upload`.
    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
