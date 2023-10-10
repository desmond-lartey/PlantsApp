# data_processing.py

import pandas as pd
from config import file_paths

def fetch_matching_plant_names(selected_values_dict):
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

    return matching_plant_names
