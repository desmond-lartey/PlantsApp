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
    selected_attribute = st.selectbox("Select an Attribute:", df.columns.tolist())

    # Depending on the attribute, provide a dropdown or multiselect for values
    if selected_attribute in ["Climate Zone From", "Climate Zone Till"]:
        # Assuming 10 climate zones as an example
        climate_zones = list(range(1, 11))  
        selected_values = st.multiselect(f"Select Values for {selected_attribute}:", climate_zones)
    else:
        unique_values = df[selected_attribute].dropna().unique().tolist()
        selected_value = st.selectbox(f"Select a Value for {selected_attribute}:", unique_values)

    # Further filtering and logic can be added later

# Run the app
app()
