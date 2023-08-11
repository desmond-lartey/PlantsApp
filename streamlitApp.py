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

def climate_zone_to_number(zone):
    try:
        num, letter = int(zone[:-1]), zone[-1]
        letter_value = ord(letter) - ord('a')
        return num + 0.1 * letter_value
    except:
        return 0

def app():
    # Multiselect to select files
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
    if st.button("Fetch Matching Plant IDs"):
        results = []
        plants_df = pd.read_excel(file_paths["Plants"])
        for key, selected_values in selected_values_dict.items():
            selected_file, attr = key.split("_")
            df = pd.read_excel(file_paths[selected_file])

            if "climate zone from" in key:
                zones_as_numbers = [climate_zone_to_number(zone) for zone in selected_values]
                mask = df["climate zone from"].apply(climate_zone_to_number) <= max(zones_as_numbers)
            elif "climate zone till" in key:
                zones_as_numbers = [climate_zone_to_number(zone) for zone in selected_values]
                mask = df["climate zone till"].apply(climate_zone_to_number) >= min(zones_as_numbers)
            else:
                mask = df[attr].isin(selected_values)

            results.extend(df[mask]["PlantID"].tolist())

        st.write("Matching Plant IDs:", list(set(results)))

        matching_plant_names = plants_df[plants_df["PlantID"].isin(results)]["Plant name"].tolist()
        st.write("Matching Plant Names:", matching_plant_names)

# Run the app
app()
