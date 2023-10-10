# utils.py

import base64

def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

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
        
        if selected_specific_colors:
            related_colors.extend(selected_specific_colors)
        else:
            related_colors.extend(specific_colors)
    
    return related_colors
