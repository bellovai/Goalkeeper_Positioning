# Import from packages
import pandas as pd
import math
import os

# Import from files
from config import Config as cfg
from utils import *



# Empty lists and empty dataframe
location_list = []
x_s_list = []
y_s_list = []
x_gk_list = []
y_gk_list = []
outcome_list = []
x_opt_list = []
y_opt_list = []
delta = []
df_empty = pd.DataFrame()



# Iterate over all files in directory
for filename in os.listdir(cfg.directory):
    
    # Save current filepath
    filepath = os.path.join(cfg.directory, filename)
    # Check if file has json ending
    if filename.split('.')[1] == 'json':
        
        # From filepath to dataframe to list
        df = pd.read_json(filepath)
        df = relevant_shots(df)
        ls = dataframe_tolist(df)
        # Add lists to existing lists
        location_list.extend(ls[0])
        x_s_list.extend(ls[1])
        y_s_list.extend(ls[2])
        x_gk_list.extend(ls[3])
        y_gk_list.extend(ls[4])
        outcome_list.extend(ls[5])



# Add lists to dataframe
df_empty['location'] = location_list
df_empty['x_s'] = x_s_list
df_empty['y_s'] = y_s_list
df_empty['x_gk'] = x_gk_list
df_empty['y_gk'] = y_gk_list
df_empty['outcome'] = outcome_list

# Copy dataframe
df_final_shots = df_empty



# Apply method
df_optimal = get_togkp(df_final_shots)



# Iterate over all shots
for i in range(0, len(df_optimal)):
    # Add value to list
    delta.append(get_distance(df_optimal, i))

# Copy dataframe
df_distance = df_optimal

# Add list to dataframe
df_distance['distance'] = delta

# Display dataframe
print(df_distance)