import streamlit as st
import pandas as pd

# Dictionary to map file selection to its path
file_paths = {
    "Biodiversity": "data/biodiversity_corrected.xlsx",
    "Climate": "data/climate_corrected.xlsx",
    "Functional": "data/functional_corrected.xlsx",
    "Hazard": "data/hazards_corrected.xlsx",
    "Maintenance": "data/maintenance_corrected.xlsx",
    "Ornamental": "data/ornamental_corrected.xlsx",
    "Plants": "data/plants_corrected.xlsx"
}

def app():
    # Dropdown to select a file
    selected_file = st.selectbox("Select a File:", list(file_paths.keys()))
    
    # Load the selected file
    df = pd.read_excel(file_paths[selected_file])

    # Dropdown to select an attribute (column name)
    selected_attributes = st.multiselect("Select Attributes:", df.columns.tolist())

    selected_values_dict = {}

    for attribute in selected_attributes:
        unique_values = sorted(df[attribute].dropna().unique().tolist())
        selected_values = st.multiselect(f"Select Values for {attribute}:", unique_values)
        selected_values_dict[attribute] = selected_values

    # Further filtering and logic can be added later

# Run the app
app()
