# streamlitApp.py

import streamlit as st
from config import file_paths, facebook_logo, twitter_logo, instagram_logo, linkedin_logo, youtube_logo
from utils import enhanced_two_step_selection
from ui_components import landing_page, display_team_members, display_social_media_links
from data_processing import fetch_matching_plant_names

def modified_app():
    # ... (all the Streamlit logic to construct the app as provided in the section you shared)
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
    # Display team members' profile pictures with clickable names at the very bottom
    st.write("#### Meet our Team:")
    cols = st.columns(len(team_members))
    
    # Custom CSS for centered text
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    for idx, (name, details) in enumerate(team_members.items()):
        image_path = base_path + details["image"]
        linkedin_url = details["linkedin"]
        
        # Convert image to base64 and display with the "circular-image" class
        img_base64 = get_image_base64(image_path)
        cols[idx].markdown(f'<a href="{linkedin_url}"><img src="data:image/jpeg;base64,{img_base64}" class="circular-image"></a>', unsafe_allow_html=True)
        
        # Display the member's name as a clickable link to their LinkedIn profile below the image
        cols[idx].markdown(f'<div class="centered-text"><a href="{linkedin_url}">{name}</a></div>', unsafe_allow_html=True)
        
        # Display role and expertise centered below the member's name
        cols[idx].markdown(f'<div class="centered-text"><strong>{details["role"]}<strong/></div>', unsafe_allow_html=True)
        cols[idx].markdown(f'<div class="centered-text"><strong>{details["expertise"]}<strong/></div>', unsafe_allow_html=True)


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
    #st.sidebar.markdown("Read our detailed [assessment publication](YOUR_LINK_HERE).")
    
     # Add the "About" section to the sidebar
    st.sidebar.markdown("### About")
    st.sidebar.markdown("""
    This web app is maintained by Desmond Lartey. 
    - [GitHub](https://github.com/desmond-lartey)
    - [Twitter](https://twitter.com/desmond_lartey)
    - [YouTube](YOUR_YOUTUBE_LINK_HERE)
    - [LinkedIn](https://www.linkedin.com/in/desmond-lartey/)
    
    [Read more about Urban Green](https://agro-nl.com/#urbis-green)
""")



import datetime

current_year = datetime.datetime.now().year
st.sidebar.markdown(f"© {current_year} Copyright Agro-NL Consult Solutions")

    

# Run the modified app
modified_app()
