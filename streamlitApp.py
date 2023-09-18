import streamlit as st
import pandas as pd

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

def landing_page():
    st.title("Sustainable Green")
    
    # Create columns for images
    col1, col2, col3, col4 = st.columns(4)
    # Display images side by side
    col1.image("https://camo.githubusercontent.com/3fb76db131464f02e8b35ddb0017e9b08979b8b6c6a88f3190e22ed591735ea0/68747470733a2f2f6167726f2d6e6c2e6e6c2f77702d636f6e74656e742f75706c6f6164732f323031392f30342f74726565732d62617265726f6f742d65313535373330333537373431302e6a7067", caption="#", width=200)
    col2.image("https://agro-nl.nl/wp-content/uploads/2019/04/perennials-p9-min-e1557303326673.jpg", caption="#", width=200)
    col3.image("https://camo.githubusercontent.com/8e2223dec81343b6da1c5e97b128c0e6417ed8f550e2142331409259224f7a91/68747470733a2f2f6167726f2d6e6c2e6e6c2f77702d636f6e74656e742f75706c6f6164732f323031392f30342f7368727562732d66756c6c2d67726f756e642d6d696e2d65313535373330333434343133312e6a7067", caption="#", width=200)
    col4.image("https://camo.githubusercontent.com/6ab594e9620fd999f1e3b23d52f2ad34f86aa0a8d4711d16b2028e360061135c/68747470733a2f2f6167726f2d6e6c2e6e6c2f77702d636f6e74656e742f75706c6f6164732f323031392f30342f74726565732d6f70656e2d67726f756e642d65313535373330333532343130352e6a7067", caption="#", width=200)

    st.write("""
    ### What do we want to do?
    We assess environmental challenges across landscapes, with a strong connection to green, sustainability, and their impacts on human well-being. Challenges include CO2, sun-city shadow/shading, and types of plants currently grown.
    
    ### Our Solution
    Plants have a role in sustainable landscapes. We have a catalogue of plant species with over 30 functional qualities.
    """)

    st.write("[Read the documentation about the app](https://github.com/desmond-lartey/PlantsApp)")
    st.write("[Visit Agro-NL Consult SolutionS B.V](https://agro-nl.nl/)")

def get_general_colors():
    return ['yellow', 'red', 'green', 'white', 'violet', 'purple', 'orange', 'cream']

def enhanced_two_step_selection(df, column_name):
    unique_colors = sorted(df[column_name].dropna().str.lower().unique().tolist())
    
    general_colors = get_general_colors()
    
    selected_general_colors = st.multiselect(f"Select General Colors for {column_name}:", general_colors)
    
    related_colors = []
    for general_color in selected_general_colors:
        specific_colors = [color for color in unique_colors if general_color in color]
        selected_specific_colors = st.multiselect(f"Select Specific Colors related to {general_color}:", specific_colors)
        related_colors.extend(selected_specific_colors)
    
    return related_colors

def modified_app():
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
                # Use the enhanced two-step selection for the flower color column in the Ornamental file
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

    # Link to the publication in the sidebar
    st.sidebar.markdown("Read our detailed [assessment publication](YOUR_LINK_HERE).")

# Run the modified app
modified_app()
