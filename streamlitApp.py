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
    selected_files = st.multiselect("Select Files:", list(file_paths.keys()))
    
    selected_values_dict = {}
    for selected_file in selected_files:
        df = pd.read_excel(file_paths[selected_file])

        # Dropdown to select an attribute (column name)
        selected_attributes = st.multiselect(f"Select Attributes for {selected_file}:", df.columns.tolist(), key=selected_file)

        for attribute in selected_attributes:
            if attribute in ["climate zone from", "climate zone till"]:
                # Force the options to be a predefined set of climate zones
                climate_zones = ["1a", "1b", "2a", "2b", "3a", "3b", "4a", "4b", "5a", "5b", "6a", "6b", "7a", "7b", "8a", "8b", "9a", "9b", "10a", "10b", "11a", "11b", "12a", "12b", "13a", "13b", "14a", "14b"]
                selected_values = st.multiselect(f"Select Values for {attribute} in {selected_file}:", climate_zones, key=f"{selected_file}_{attribute}")
            else:
                unique_values = sorted(df[attribute].dropna().unique().tolist())
                selected_values = st.multiselect(f"Select Values for {attribute} in {selected_file}:", unique_values, key=f"{selected_file}_{attribute}")
            selected_values_dict[f"{selected_file}_{attribute}"] = selected_values

    # Filtering logic based on the selected values
    results = []
    for selected_file, df_path in file_paths.items():
        df = pd.read_excel(df_path)
        mask = pd.Series([True] * len(df))
        for attribute, values in selected_values_dict.items():
            file_name, attr = attribute.split('_')
            if file_name == selected_file:
                if attr in ["climate zone from", "climate zone till"]:
                    if attr == "climate zone from":
                        mask &= df[attr].apply(lambda x: any(zone <= x for zone in values))
                    elif attr == "climate zone till":
                        mask &= df[attr].apply(lambda x: any(zone >= x for zone in values))
                else:
                    mask &= df[attr].isin(values)
        results.extend(df[mask]["PlantID"].tolist())

    # Fetch matching plant names
    plants_df = pd.read_excel(file_paths["Plants"])
    matching_plant_names = plants_df[plants_df["PlantID"].isin(results)]["Plant name"].tolist()
    st.write("Matching Plant Names:", matching_plant_names)

# Run the app
app()
