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
    # Multiselect to select files
    selected_files = st.multiselect("Select Files:", list(file_paths.keys()))

    combined_df = pd.DataFrame()

    for selected_file in selected_files:
        # Load the selected file
        df = pd.read_excel(file_paths[selected_file])
        combined_df = pd.concat([combined_df, df])

    # Multiselect for pH values
    ph_values = list(range(15))
    selected_ph_values = st.multiselect("Select pH Values:", ph_values)
    
    # Filtering logic for pH
    if selected_ph_values:
        combined_df = combined_df[combined_df['ph'].isin(selected_ph_values)]

    # Multiselect for Climate Zone From and Till
    climate_zones = list(range(1, 11))  # Assuming 10 climate zones as an example
    selected_zones_from = st.multiselect("Select Climate Zone From:", climate_zones)
    selected_zones_till = st.multiselect("Select Climate Zone Till:", climate_zones)

    # Filtering logic for Climate Zones
    if selected_zones_from:
        combined_df = combined_df[combined_df['Climate Zone From'].isin(selected_zones_from)]
    if selected_zones_till:
        combined_df = combined_df[combined_df['Climate Zone Till'].isin(selected_zones_till)]

    # Display results
    st.write("Matching Plant IDs:", combined_df["PlantID"].tolist())

    # Matching plant names logic
    plants_df = pd.read_excel(file_paths["Plants"])
    matching_plant_ids = combined_df["PlantID"].tolist()
    matching_plant_names = plants_df[plants_df["PlantID"].isin(matching_plant_ids)]["Plant name"].tolist()
    st.write("Matching Plant Names:", matching_plant_names)

# Run the app
app()
