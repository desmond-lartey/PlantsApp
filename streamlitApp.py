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

import base64

def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")
        
# Custom CSS to make images circular
st.markdown("""
<style>
.circular-image {
    border-radius: 50%;
    overflow: hidden;
    width: 150px;
    height: 150px;
    background-size: cover;
    background-position: center;
}
</style>
""", unsafe_allow_html=True)

# Social Media Logos (Links to publicly available logos; remember to use proper licensing in production)
facebook_logo = "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"
twitter_logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2HPo_08r3lhM_9yz3cufBPh9cwU5UMXay8Bisn0KZOQ&s"
instagram_logo = "https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg"
linkedin_logo = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
youtube_logo = "https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg"

# Base path for the local data directory
base_path = "data/"

# Define the team members with their respective image filenames and LinkedIn profile URLs
team_members = {
    "Alina Lomans": {"image": "Alina Lomans.jpg", "linkedin": "LinkedIn_Profile_URL_1"},
    "Desmond Lartey": {"image": "Desmond Lartey.jpeg", "linkedin": "LinkedIn_Profile_URL_2"},
    "Hua Wang": {"image": "Huan Wang.jpeg", "linkedin": "LinkedIn_Profile_URL_3"},
    "Monica Bonu": {"image": "Monica Bonu.jpeg", "linkedin": "LinkedIn_Profile_URL_3"},
    # ... and so on for all members
}


def landing_page():
    st.title("Sustainable Urban Green")
    
    # Create columns for images
    col1, col2, col3, col4 = st.columns(4)
    # Display images side by side
    col1.image("https://camo.githubusercontent.com/3fb76db131464f02e8b35ddb0017e9b08979b8b6c6a88f3190e22ed591735ea0/68747470733a2f2f6167726f2d6e6c2e6e6c2f77702d636f6e74656e742f75706c6f6164732f323031392f30342f74726565732d62617265726f6f742d65313535373330333537373431302e6a7067", caption="", width=200)
    col2.image("https://agro-nl.nl/wp-content/uploads/2019/04/perennials-p9-min-e1557303326673.jpg", caption="", width=200)
    col3.image("https://camo.githubusercontent.com/8e2223dec81343b6da1c5e97b128c0e6417ed8f550e2142331409259224f7a91/68747470733a2f2f6167726f2d6e6c2e6e6c2f77702d636f6e74656e742f75706c6f6164732f323031392f30342f7368727562732d66756c6c2d67726f756e642d6d696e2d65313535373330333434343133312e6a7067", caption="", width=200)
    col4.image("https://camo.githubusercontent.com/6ab594e9620fd999f1e3b23d52f2ad34f86aa0a8d4711d16b2028e360061135c/68747470733a2f2f6167726f2d6e6c2e6e6c2f77702d636f6e74656e742f75706c6f6164732f323031392f30342f74726565732d6f70656e2d67726f756e642d65313535373330333532343130352e6a7067", caption="", width=200)

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
        selected_specific_colors = st.multiselect(f"Select Specific Colors related to {general_color} (optional):", specific_colors)
        
        # If specific colors are selected, add them to the results
        if selected_specific_colors:
            related_colors.extend(selected_specific_colors)
        else:
            related_colors.extend(specific_colors)
    
    return related_colors

def modified_app():
    # Custom CSS
    st.markdown("""
        <style>
            body {
                background-image: url("https://images.pexels.com/photos/6143369/pexels-photo-6143369.jpeg");
                background-size: cover;
                background-repeat: no-repeat;
            }
        </style>
    """, unsafe_allow_html=True)
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

    # Create some space using CSS padding
    st.markdown('<div style="padding: 50px;"></div>', unsafe_allow_html=True)


# Display team members' profile pictures with clickable names at the very bottom
    st.write("#### Meet our Team:")
    cols = st.columns(len(team_members))
    
    for idx, (name, details) in enumerate(team_members.items()):
        image_path = base_path + details["image"]
        linkedin_url = details["linkedin"]
        
        # Convert image to base64 and display with the "circular-image" class
        img_base64 = get_image_base64(image_path)
        cols[idx].markdown(f'<a href="{linkedin_url}"><img src="data:image/jpeg;base64,{img_base64}" class="circular-image"></a>', unsafe_allow_html=True)
        
        # Display the member's name as a clickable link to their LinkedIn profile below the image
        cols[idx].markdown(f"[{name}]({linkedin_url})")

     # Social Media Links with Logos
    st.write("#### Connect with us on Social Media:")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.image(facebook_logo, width=32)
    col1.write("[Facebook](https://www.facebook.com/)")
    
    col2.image(twitter_logo, width=32)
    col2.write("[Twitter](https://twitter.com/)")
    
    col3.image(instagram_logo, width=32)
    col3.write("[Instagram](https://www.instagram.com/)")
    
    col4.image(linkedin_logo, width=32)
    col4.write("[LinkedIn](https://www.linkedin.com/in/alina-lomans-agro-nl-cs-urbis-green-b44a56b0/)")
    
    col5.image(youtube_logo, width=32)
    col5.write("[YouTube](https://www.youtube.com/)")

    # Link to the publication in the sidebar
    st.sidebar.markdown("Read our detailed [assessment publication](YOUR_LINK_HERE).")
    
     # Add the "About" section to the sidebar
    st.sidebar.markdown("### About")
    st.sidebar.markdown("""
    This web app is maintained by Desmond Lartey. 
    You can follow me on social media:
    - [GitHub](https://github.com/desmond-lartey)
    - [Twitter](https://twitter.com/desmond_lartey)
    - [YouTube](YOUR_YOUTUBE_LINK_HERE)
    - [LinkedIn](https://www.linkedin.com/in/desmond-lartey/)
    
    Source code and documentation here: [https://github.com/desmond-lartey/PlantsApp/blob/Fires/README.md](https://github.com/desmond-lartey/PlantsApp/blob/Fires/README.md)
    """)

import datetime

current_year = datetime.datetime.now().year
st.markdown(f"© {current_year} Copyright Agro-NL Consult Solutions B.V.")

    
    
# Run the modified app
modified_app()
