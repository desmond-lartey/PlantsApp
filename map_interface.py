import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

def display_map(plants_with_locations_df):
    st.title("Map Display")

    # Extract latitude and longitude values from the 'Location' and 'Genus Mapped Location' columns
    plants_with_locations_df['Individual_Latitude'] = plants_with_locations_df['Location'].str.extract(r'\((-?\d+\.\d+),').astype(float)
    plants_with_locations_df['Individual_Longitude'] = plants_with_locations_df['Location'].str.extract(r',\s*(-?\d+\.\d+)\)').astype(float)

    plants_with_locations_df['Genus_Latitude'] = plants_with_locations_df['Genus Mapped Location'].str.extract(r'\((-?\d+\.\d+),').astype(float)
    plants_with_locations_df['Genus_Longitude'] = plants_with_locations_df['Genus Mapped Location'].str.extract(r',\s*(-?\d+\.\d+)\)').astype(float)

    def correct_coordinates(row, lat_col, lon_col):
        lat = row[lat_col]
        lon = row[lon_col]
        if lat < -90 or lat > 90:
            return lon, lat
        return lat, lon

    # Correct the coordinates
    plants_with_locations_df['Individual_Latitude'], plants_with_locations_df['Individual_Longitude'] = zip(*plants_with_locations_df.apply(correct_coordinates, args=('Individual_Latitude', 'Individual_Longitude'), axis=1))
    plants_with_locations_df['Genus_Latitude'], plants_with_locations_df['Genus_Longitude'] = zip(*plants_with_locations_df.apply(correct_coordinates, args=('Genus_Latitude', 'Genus_Longitude'), axis=1))

    # Let users toggle between individual plant locations and genus-based locations
    display_option = st.radio("Display Option:", ["Individual Plants", "Genus"])

    unique_individual_locations = plants_with_locations_df[["Individual_Latitude", "Individual_Longitude"]].drop_duplicates().dropna()
    st.write(f"Number of unique individual plant locations: {len(unique_individual_locations)}")

    unique_genus_locations = plants_with_locations_df[["Genus_Latitude", "Genus_Longitude"]].drop_duplicates().dropna()
    st.write(f"Number of unique genus locations: {len(unique_genus_locations)}")

    if display_option == "Individual Plants":
        locations = plants_with_locations_df[["Individual_Latitude", "Individual_Longitude", "Plant name"]].dropna().values
    else:
        locations = plants_with_locations_df[["Genus_Latitude", "Genus_Longitude", "Extracted Genus"]].dropna().values

    # Create an expander for the description
    with st.expander("Learn More About the locations", expanded=False):
        st.write("""
        ### Our Approach
        Based on the experience of plants, We begin by assigning specific geographic coordinates to each plant, based on its most commonly found location, its native habitat. Many plants share common characteristics at the genus level, we further aggregate these plants to highlight genus-specific locations. This approach offers a detailed view of individual plants but also provides a broader perspective at the genus level.
        """)

    # Your existing code for generating the folium map
    m = folium.Map(location=[0, 0], zoom_start=2)  

    # Add a marker cluster
    marker_cluster = MarkerCluster().add_to(m)
    for loc in locations:
        folium.Marker([loc[0], loc[1]], tooltip=loc[2]).add_to(marker_cluster)

    # Display the map on Streamlit
    folium_static(m)
