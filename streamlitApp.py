#!/usr/bin/env python
# coding: utf-8

# In[4]:




# In[5]:


import streamlit as st


# In[12]:

import streamlit as st
import pandas as pd

# Dictionary to map file selection to its path
file_paths = {
    "Biodiversity": "/mnt/data/biodiversity_corrected.xlsx",
    "Climate": "/mnt/data/climate_corrected.xlsx",
    "Functional": "/mnt/data/functional_corrected.xlsx",
    "Hazard": "/mnt/data/hazards_corrected.xlsx",
    "Maintenance": "/mnt/data/maintenance_corrected.xlsx",
    "Ornamental": "/mnt/data/ornamental_corrected.xlsx",
    "Plants": "/mnt/data/plants_corrected.xlsx"
}

def app():
    # Dropdown to select a file
    selected_file = st.selectbox("Select a File:", list(file_paths.keys()))

    # Load the selected file
    df = pd.read_excel(file_paths[selected_file])

    # Dropdown to select an attribute (column name)
    selected_attribute = st.selectbox("Select an Attribute:", df.columns.tolist())

    # Dropdown to select a value from the chosen attribute's unique values
    unique_values = df[selected_attribute].dropna().unique().tolist()
    selected_value = st.selectbox("Select a Value:", unique_values)

    # Button to fetch matching data
    if st.button("Fetch Matching Data"):
        matching_data = df[df[selected_attribute] == selected_value]
        st.write(matching_data["PlantID"].tolist())

    # Button to fetch matching plant names (assuming "Plant name" column exists in "plants_corrected.xlsx")
    if st.button("Fetch Matching Plant Names"):
        plants_df = pd.read_excel(file_paths["Plants"])
        matching_plant_ids = df[df[selected_attribute] == selected_value]["PlantID"].tolist()
        matching_plant_names = plants_df[plants_df["PlantID"].isin(matching_plant_ids)]["Plant name"].tolist()
        st.write(matching_plant_names)

# Run the app
app()

streamlit run streamlitApp.py.

# In[ ]:

