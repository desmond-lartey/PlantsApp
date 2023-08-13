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
    st.title("Sustainable Green")
    col1, col2, col3, col4 = st.columns(4)
    col1.image("https://agro-nl.nl/wp-content/uploads/2019/04/trees-bareroot-e1557303577410.jpg", caption="Plant Image", width=150)
    col2.image("https://agro-nl.nl/wp-content/uploads/2019/04/perennials-bareroot-min-e1557303366820.jpg", caption="Plant Image", width=150)
    col3.image("https://agro-nl.nl/wp-content/uploads/2019/04/perennials-multiplates-min-e1557303346561.jpg", caption="Plant Image", width=150)
    col4.image("https://agro-nl.nl/wp-content/uploads/2019/04/perennials-p9-min-e1557303326673.jpg", caption="Plant Image", width=150)
    st.write("""
    ### What do we want to do?
    We assess environmental challenges across landscapes, with a strong connection to green, sustainability, and their impacts on human well-being. Challenges include CO2, sun-city shadow/shading, and types of plants currently grown.
    
    ### Our Solution
    Plants have a role in sustainable landscapes. We have a catalogue of plants species with over 30 functional qualities.
    
    """)
    st.write("[Go to main project page](#)")  # Replace # with the actual link to your main project page
    st.write("[Visit Agro-NL Consult SolutionS B.V](https://agro-nl.nl/)")

def check_ph_match(ph_string, ph_values):
    segments = ph_string.replace(",", ".").split(",")
    for segment in segments:
        if '-' in segment:
            low, high = map(float, segment.strip().split('-'))
            if any(low <= ph_val <= high for ph_val in ph_values):
                return True
        else:
            if float(segment.strip()) in ph_values:
                return True
    return False

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
            if selected_file == 'Climate' and attribute == 'PH':
                ph_options = [str(i) for i in range(1, 15)] + [f"{i}-{i+2}" for i in range(1, 13)]
                selected_ph = st.multiselect('Select pH value or range:', ph_options)

                ph_values = []
                for ph_val in selected_ph:
                    if '-' in ph_val:
                        ph_start, ph_end = map(float, ph_val.split('-'))
                        ph_values.extend(list(range(int(ph_start), int(ph_end) + 1)))
                    else:
                        ph_values.append(float(ph_val))

                # Filter the DataFrame based on the pH values
                mask = df[attribute].astype(str).apply(lambda x: check_ph_match(x, ph_values))
                selected_values_dict[(selected_file, attribute)] = df[mask]["PlantID"].tolist()
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
        for file, attribute in selected_values_dict:
            if file not in file_paths:
                continue
            df = pd.read_excel(file_paths[file])

            if not (file == 'Climate' and attribute == 'PH'):
                mask = df[attribute].isin(selected_values_dict[(selected_file, attribute)])
                results.extend(df[mask]["PlantID"].tolist())

        plants_df = pd.read_excel(file_paths["Plants"])
        matching_plant_ids = list(set(results))
        matching_plant_names = plants_df[plants_df["PlantID"].isin(matching_plant_ids)]["Plant name"].tolist()

        st.write("Matching Plant Names:")
        st.write(matching_plant_names)

# Run the app
app()
