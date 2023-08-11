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

    # Consolidate results from all selected files
    all_matching_data = []
    all_matching_plant_names = []

    for selected_file in selected_files:
        # Load the selected file
        df = pd.read_excel(file_paths[selected_file])

        # Multiselect to select multiple attributes
        selected_attributes = st.multiselect(f"Select Attributes for {selected_file}:", df.columns.tolist())

        mask = True
        for attribute in selected_attributes:
            if attribute == "ph":
                ph_values = [str(i) for i in range(15)]
                selected_ph_values = st.multiselect(f"Select pH values for {selected_file}:", ph_values)
                selected_ph_values = [float(i) for i in selected_ph_values]
                mask &= df[attribute].isin(selected_ph_values)
            # Add logic for "Climate Zone From" and "Climate Zone Till" if necessary
            else:
                unique_values = df[attribute].dropna().unique().tolist()
                selected_value = st.selectbox(f"Select a Value for {attribute} in {selected_file}:", unique_values)
                mask &= (df[attribute] == selected_value)

        matching_data = df[mask]
        all_matching_data.extend(matching_data["PlantID"].tolist())

        # Matching plant names logic
        plants_df = pd.read_excel(file_paths["Plants"])
        matching_plant_ids = matching_data["PlantID"].tolist()
        matching_plant_names = plants_df[plants_df["PlantID"].isin(matching_plant_ids)]["Plant name"].tolist()
        all_matching_plant_names.extend(matching_plant_names)

    # Display results
    st.write("Matching Plant IDs:", list(set(all_matching_data)))
    st.write("Matching Plant Names:", list(set(all_matching_plant_names)))

# Run the app
app()
