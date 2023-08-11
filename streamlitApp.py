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
    mask = True
    for attribute in selected_attributes:
        if attribute == "ph":
            range_input = st.text_input(f"Enter {attribute} range (e.g., 5-8 or 5-8,5):")
            try:
                parts = range_input.split('-')
                # Replace comma with dot and convert to float
                lower_bound = float(parts[0].replace(',', '.'))
                upper_bound = float(parts[1].replace(',', '.'))
                mask &= (df[attribute] >= lower_bound) & (df[attribute] <= upper_bound)
            except ValueError:
                st.write("Please enter a valid range.")
                return  # Exit the current execution cycle of the app
        else:
            unique_values = df[attribute].dropna().unique().tolist()
            selected_value = st.selectbox(f"Select a Value for {attribute}:", unique_values)
            attribute_value_dict[attribute] = selected_value
            mask &= (df[attribute] == selected_value)

    # Button to fetch matching data
    if selected_attributes and st.button("Fetch Matching Data"):
        matching_data = df[mask]
        st.write(matching_data["PlantID"].tolist())

    # Button to fetch matching plant names
    if selected_attributes and st.button("Fetch Matching Plant Names"):
        plants_df = pd.read_excel(file_paths["Plants"])
        matching_plant_ids = df[mask]["PlantID"].tolist()
        matching_plant_names = plants_df[plants_df["PlantID"].isin(matching_plant_ids)]["Plant name"].tolist()
        st.write(matching_plant_names)

# Run the app
app()
