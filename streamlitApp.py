import streamlit as st
import pandas as pd
import base64
import datetime

# Define the paths to the Excel files
file_paths = {
    "Biodiversity": "data/biodiversity_corrected.xlsx",
    "Climate": "data/climate_corrected.xlsx",
    "Functional": "data/functional_corrected.xlsx",
    "Hazard": "data/hazards_corrected.xlsx",
    "Maintenance": "data/maintenance_corrected.xlsx",
    "Ornamental": "data/ornamental_corrected.xlsx",
    "Plants": "data/plants_corrected.xlsx"
}

def get_ph_ranges():
    """Return predefined pH range options."""
    return ["<5", "5-7", "7-9", ">9"]

def filter_by_ph(df, ph_range):
    """Filter the DataFrame by the selected pH range."""
    # Helper function to parse pH values from the dataset
    def parse_ph(value):
        try:
            # Convert comma decimals to point decimals and split the range
            low, high = map(lambda x: float(x.replace(',', '.')), value.split('-'))
        except ValueError:
            return (None, None)
        return (low, high)
    
    # Apply the helper function to the entire pH column
    df["ph_low"], df["ph_high"] = zip(*df["pH"].map(parse_ph))
    
    if ph_range == "<5":
        mask = df["ph_low"] < 5
    elif ph_range == "5-7":
        mask = (df["ph_low"] >= 5) & (df["ph_high"] <= 7)
    elif ph_range == "7-9":
        mask = (df["ph_low"] >= 7) & (df["ph_high"] <= 9)
    elif ph_range == ">9":
        mask = df["ph_high"] > 9
    
    return df[mask]

def modified_app():
    # Your landing_page code and the rest of the app go here...

    # Dropdown to select a file
    selected_files = st.multiselect("Select Files:", list(file_paths.keys()))
    
    selected_values_dict = {}
    for selected_file in selected_files:
        df = pd.read_excel(file_paths[selected_file])
        # Dropdown to select an attribute (column name)
        selected_attributes = st.multiselect(f"Select Attributes for {selected_file}:", df.columns.tolist(), key=selected_file)

        for attribute in selected_attributes:
            if attribute == "pH":  # Handle pH range selection
                selected_ph_range = st.selectbox(f"Select pH range for {selected_file}:", get_ph_ranges())
                df = filter_by_ph(df, selected_ph_range)
            # ... [other parts of your attribute handling logic]

    # Fetch matching plant names
    if st.button("Fetch Matching Plant Names"):
        if not selected_values_dict:
            st.warning("Please select attributes and values first.")
            return

        results = []
        for file, attr in selected_values_dict:
            if file not in file_paths:
                continue
            df = pd.read_excel(file_paths[file])
            mask = df[attr].isin(selected_values_dict[(file, attr)])
            results.extend(df[mask]["PlantID"].tolist())
        
        plants_df = pd.read_excel(file_paths["Plants"])
        matching_plant_ids = list(set(results))
        matching_plant_names = plants_df[plants_df["PlantID"].isin(matching_plant_ids)]["Plant name"].tolist()

        st.write("Matching Plant Names:")
        st.write(matching_plant_names)

# Run the modified app
modified_app()
