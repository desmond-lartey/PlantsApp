# Consolidating the entire modified Streamlit app

script = """
import streamlit as st
import pandas as pd

# Dictionary to map file selection to its path
file_paths = {
    "Biodiversity": "data/biodiversity_corrected.xlsx",
    "Climate": "data/climate_corrected.xlsx",
    "Functional": "data/functional_corrected.xlsx",
    "Hazard": "data/hazards_corrected.xlsx",
    "Maintenance": "data/maintenance_corrected.xlsx",
    "Ornamental": "/mnt/data/ornamental_corrected.xlsx",  # Ensure to update the path based on your directory structure
    "Plants": "data/plants_corrected.xlsx"
}

def landing_page():
    st.title("Sustainable Green")

    # Create columns for images
    col1, col2, col3, col4 = st.columns(4)
    # Display images side by side
    col1.image("https://agro-nl.nl/wp-content/uploads/2019/04/trees-bareroot-e1557303577410.jpg", caption="Plant Image 1", width=200)
    col2.image("https://agro-nl.nl/wp-content/uploads/2019/04/perennials-bareroot-min-e1557303366820.jpg", caption="Plant Image 2", width=200)
    col3.image("https://agro-nl.nl/wp-content/uploads/2019/04/perennials-multiplates-min-e1557303346561.jpg", caption="Plant Image 3", width=200)
    col4.image("https://agro-nl.nl/wp-content/uploads/2019/04/perennials-p9-min-e1557303326673.jpg", caption="Plant Image 4", width=200)

    st.write("""
    ### What do we want to do?
    We assess environmental challenges across landscapes, with a strong connection to green, sustainability, and their impacts on human well-being. Challenges include CO2, sun-city shadow/shading, and types of plants currently grown.
    
    ### Our Solution
    Plants have a role in sustainable landscapes. We have a catalogue of plant species with over 30 functional qualities.
    """)

    st.write("[Read the documentation about the app](https://github.com/desmond-lartey/PlantsApp)")  # Display documentation link
    st.write("[Visit Agro-NL Consult SolutionS B.V](https://agro-nl.nl/)")

def get_general_colors(colors):
    general_colors = ['yellow', 'red', 'green', 'white', 'violet', 'purple', 'orange', 'cream']
    return [color for color in general_colors if any(color in col for col in colors)]

def get_specific_colors(general_color, colors):
    return [color for color in colors if general_color in color]

def enhanced_two_step_selection(df, column_name):
    unique_colors = sorted(df[column_name].dropna().unique().tolist())
    general_colors = get_general_colors(unique_colors)
    
    selected_general_colors = st.multiselect(f"Select General Colors for {column_name}:", general_colors)
    
    related_colors = []
    for general_color in selected_general_colors:
        specific_colors = get_specific_colors(general_color, unique_colors)
        selected_specific_colors = st.multiselect(f"Select Specific Colors related to {general_color}:", specific_colors)
        related_colors.extend(selected_specific_colors)
    
    return related_colors

def app():
    landing_page()
    
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
            elif selected_file == "Ornamental" and attribute == "flower color":
                selected_values = enhanced_two_step_selection(df, attribute)
            else:
                unique_values = sorted(df[attribute].dropna().unique().tolist())
                selected_values = st.multiselect(f"Select Values for {attribute} in {selected_file}:", unique_values, key=f"{selected_file}_{attribute}")
            selected_values_dict[(selected_file, attribute)] = selected_values

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

# Run the app
app()
"""

script
