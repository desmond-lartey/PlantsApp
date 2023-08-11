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

    # Multiselect to select multiple attributes
    selected_attributes = st.multiselect("Select Attributes:", df.columns.tolist())

    attribute_value_dict = {}
    for attribute in selected_attributes:
        unique_values = df[attribute].dropna().unique().tolist()
        selected_value = st.selectbox(f"Select a Value for {attribute}:", unique_values)
        attribute_value_dict[attribute] = selected_value

    # Button to fetch matching data
if selected_attributes and st.button("Fetch Matching Data"):
    mask = True
    for attr, value in attribute_value_dict.items():
        mask &= (df[attr] == value)
    matching_data = df[mask]
    st.write(matching_data["PlantID"].tolist())

# Button to fetch matching plant names (assuming "Plant name" column exists in "plants_corrected.xlsx")
if selected_attributes and st.button("Fetch Matching Plant Names"):
    mask = True
    for attr, value in attribute_value_dict.items():
        mask &= (df[attr] == value)
    plants_df = pd.read_excel(file_paths["Plants"])
    matching_plant_ids = df[mask]["PlantID"].tolist()
    matching_plant_names = plants_df[plants_df["PlantID"].isin(matching_plant_ids)]["Plant name"].tolist()
    st.write(matching_plant_names)


# Run the app
app()
