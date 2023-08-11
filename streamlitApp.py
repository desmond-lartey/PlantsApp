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
        if attribute in ["climate zone from", "climate zone till"]:
            # Force the options to be a predefined set of climate zones
            climate_zones = ["1a", "1b", "2a", "2b", "3a", "3b", "4a", "4b", "5a", "5b", "6a", "6b", "7a", "7b", "8a", "8b", "9a", "9b", "10a", "10b", "11a", "11b", "12a", "12b", "13a", "13b", "14a", "14b"]
            selected_values = st.multiselect(f"Select Values for {attribute}:", climate_zones)
        else:
            unique_values = sorted(df[attribute].dropna().unique().tolist())
            selected_values = st.multiselect(f"Select Values for {attribute}:", unique_values)
        selected_values_dict[attribute] = selected_values

    # This is where you can add further logic and filtering based on the selected values

# Run the app
app()
