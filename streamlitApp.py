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

def landing_page():
    st.title("Sustainable Green Concept Plan for Agro-NL Consult SolutionS B.V")
    
    st.write("""
    ### Why do we do this?
    Countries are at different phases of spatial development. Population increase and growing economies with less plan for nature put countries at risk of environmental hazards. Our urban green concept aims to initiate a dialogue among municipalities, localities, and governments on the need for a high-level focus on sustainability.
    
    ### What do we want to do?
    We assess environmental challenges across landscapes, with a strong connection to green, sustainability, and their impacts on human well-being. Challenges include CO2, sun/city shadow/shading, and types of plants currently grown.
    
    ### Our Solution
    We provide innovative solutions including vertical greening, roof greening, and strong root plants for snow storms. Our goal is to create sustainable, functional green spaces in cities, making them healthier and more livable.
    
    ### Our Unique Proposition
    Agro-NL is unique in the European plant market, emphasizing Green, plants, and climate-sustainability.
    """)
    
    #st.image("path_to_plant_image_1.jpg", caption="Sample Plant Image 1", use_column_width=True)  # Replace with the actual path or URL
    #st.image("path_to_plant_image_2.jpg", caption="Sample Plant Image 2", use_column_width=True)  # Replace with the actual path or URL
    st.image("https://link-to-image-from-unsplash-or-pixabay.jpg", caption="Plant Image", use_column_width=True)

    st.write("[Go to main project page](#)")  # Replace # with the actual link to your main project page
    st.write("[Visit Agro-NL Consult SolutionS B.V](https://agro-nl.nl/)")

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
