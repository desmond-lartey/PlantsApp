# ui_components.py

import streamlit as st
from utils import get_image_base64
from config import base_path, facebook_logo, twitter_logo, instagram_logo, linkedin_logo, youtube_logo, #team_members 

def landing_page():
    st.title("Sustainable Urban Green")
    
    # Create columns for images
    col1, col2, col3, col4 = st.columns(4)
    col1.image("https://camo.githubusercontent.com/3fb76db131464f02e8b35ddb0017e9b08979b8b6c6a88f3190e22ed591735ea0/68747470733a2f2f6167726f2d6e6c2e6e6c2f77702d636f6e74656e742f75706c6f6164732f323031392f30342f74726565732d62617265726f6f742d65313535373330333537373431302e6a7067", caption="", width=200)
    col2.image("https://agro-nl.nl/wp-content/uploads/2019/04/perennials-p9-min-e1557303326673.jpg", caption="", width=200)
    col3.image("https://camo.githubusercontent.com/8e2223dec81343b6da1c5e97b128c0e6417ed8f550e2142331409259224f7a91/68747470733a2f2f6167726f2d6e6c2e6e6c2f77702d636f6e74656e742f75706c6f6164732f323031392f30342f7368727562732d66756c6c2d67726f756e642d6d696e2d65313535373330333434343133312e6a7067", caption="", width=200)
    col4.image("https://camo.githubusercontent.com/6ab594e9620fd999f1e3b23d52f2ad34f86aa0a8d4711d16b2028e360061135c/68747470733a2f2f6167726f2d6e6c2e6e6c2f77702d636f6e74656e742f75706c6f6164732f323031392f30342f74726565732d6f70656e2d67726f756e642d65313535373330333532343130352e6a7067", caption="", width=200)

    st.write("""
    ### Objective
    We assess environmental challenges across landscapes, with a strong connection to green, sustainability, and their impacts on human well-being. Challenges include CO2, sun-city shadow/shading, and types of plants currently grown.
    
    ### Our Approach
    Plants have a role in sustainable landscapes. We have a catalogue of plant species with over 30 functional and ornamental qualities.
    """)

    st.write("[Read the documentation about the app](https://github.com/desmond-lartey/PlantsApp)")
    st.write("[Visit Agro-NL Consult Solutions B.V](https://agro-nl.com/)")

#def display_team_members():
    #st.write("#### Meet our Team:")
    #cols = st.columns(len(team_members))
    
    # Custom CSS for centered text
    #st.markdown("""
    #<style>
    #.centered-text {
        #text-align: center;
    #}
    #</style>
    #""", unsafe_allow_html=True)
    
    #for idx, (name, details) in enumerate(team_members.items()):
        #image_path = base_path + details["image"]
        #linkedin_url = details["linkedin"]
        
        # Convert image to base64 and display with the "circular-image" class
        #img_base64 = get_image_base64(image_path)
        #cols[idx].markdown(f'<a href="{linkedin_url}"><img src="data:image/jpeg;base64,{img_base64}" class="circular-image"></a>', unsafe_allow_html=True)
        
        # Display the member's name as a clickable link to their LinkedIn profile below the image
        #cols[idx].markdown(f'<div class="centered-text"><a href="{linkedin_url}">{name}</a></div>', unsafe_allow_html=True)
        
        # Display role and expertise centered below the member's name
        #cols[idx].markdown(f'<div class="centered-text"><strong>{details["role"]}<strong/></div>', unsafe_allow_html=True)
        #cols[idx].markdown(f'<div class="centered-text"><strong>{details["expertise"]}<strong/></div>', unsafe_allow_html=True)

def display_social_media_links():
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
