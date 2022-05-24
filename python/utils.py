# Import from packages
import math



# Full dataframe to shot dataframe
def filter_shots(df):

    # Create dataframe with all shots
    df = df[['possession_team', 'shot', 'location']].dropna().reset_index(drop = True)
    
    # From shot location to shot coordinates
    df['x_s'], df['y_s'] = zip(*df['location'])

    # Return
    return df



# Shot dataframe to completed shot dataframe filtered for relevant shots
def relevant_shots(df):
    
    # Create shot dataframe
    df = filter_shots(df)

    # Create empty lists for gk coordinates and outcome
    x_gk = []
    y_gk = []
    outcome = []

    # Append values to empty lists
    for j in range (0, len(df)):
        # Append outcome values to empty list
        outcome.append(df.iloc[j]['shot']['outcome']['name'])
        # Unnest shot data
        shot = df.iloc[1]['shot']['freeze_frame']
        # Append gk coordinates to empty lists
        for i in range (0, len(shot)):
            if shot[i]['position']['name'] == 'Goalkeeper':
                x_gk.append(shot[i]['location'][0])
                y_gk.append(shot[i]['location'][1])
    
    # Add lists to dataframe
    df['x_gk'] = x_gk
    df['y_gk'] = y_gk
    df['outcome'] = outcome

    # Return relevant shots
    return df.where((df['outcome'] == 'Goal') | (df['outcome'] == 'Saved') | (df['outcome'] == 'Saved To Post')).dropna().reset_index(drop = True)



# Dataframe columns to lists
def dataframe_tolist(df):
    
    # Save dataframe columns in lists
    possession_team_list = df['possession_team'].tolist()
    location_list = df['location'].tolist()
    x_s_list = df['x_s'].tolist()
    y_s_list = df['y_s'].tolist()
    x_gk_list = df['x_gk'].tolist()
    y_gk_list = df['y_gk'].tolist()
    outcome_list = df['outcome'].tolist()
    
    # Return lists
    return location_list, x_s_list, y_s_list, x_gk_list, y_gk_list, outcome_list



# Calculate slope of bisector
def bisector_slope(x, y):
    
    # Calculate slope from shot location to goalposts
    m1 = (36-y)/(120-x)
    m2 = (44-y)/(120-x)
    
    # Return
    return (m1+m2)/2



# Calculate angle in radians between the two lines from shot location to goalposts
def angle(x, y):
    
    # Calculate slope from shot location to goalposts
    m1 = (36-y)/(120-x)
    m2 = (44-y)/(120-x)
    
    # Return absolute value of the angle in radians
    return abs((math.atan((m1-m2)/(1+m1*m2))))



# Rotate lower goalpost coordinates counterclockwise by angle/2 in radians around shot location
def rotate(x, y):
    
    # Apply function
    ang = angle(x, y)/2
    
    # Calculate rotation
    x_rot = x + math.cos(ang) * (120 - x) - math.sin(ang) * (36 - y)
    y_rot = y + math.sin(ang) * (120 - x) + math.cos(ang) * (36 - y)
    
    # Return
    return x_rot, y_rot



# Calculate perpendicular distance from point to line
def distance_to_line(a, b, x1, y1, x2, y2):
    
    # Save points that connect to a line
    p1 = x1, y1
    p2 = x2, y2
    # Save point from which the distance is calculated
    p3 = a, b
    
    # Convert points to arrays
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    p3 = np.asarray(p3)
    
    # Return
    return norm(np.cross(p2-p1, p1-p3))/norm(p2-p1)



# Calculate distance between GKP and TOGKP
def get_distance(df, row):
    
    # Save coordinates
    x1 = df.at[row, 'x_opt']
    y1 = df.at[row, 'y_opt']
    x2 = df.at[row, 'x_gk']
    y2 = df.at[row, 'y_gk']

    # Return
    return round(math.dist([x1, y1], [x2, y2]), 2)



# Calculate TOGKP
def get_togkp(df):
    
    # Iterate over all shots
    for i in range(0, len(df)):

        # Shot location
        x_s = df.at[i, 'x_s']
        y_s = df.at[i, 'y_s']

        # Goalkeeper location
        x_gk = df.at[i, 'x_gk']
        y_gk = df.at[i, 'y_gk']

        # Bisector angle in radians
        ang_rad = angle(x_s, y_s)/2

        # Bisector slope
        m = bisector_slope(x_s, y_s)

        # Distance from shot location to optimal location
        x = (math.cos(ang_rad)*half_wingspan)/math.sin(ang_rad)

        # Shift from shot location to optimal location
        x_shift = x/(math.sqrt(1+m*m))
        y_shift = x_shift*m

        # Optimal location
        x_opt = round(x_s + x_shift, 2)
        y_opt = round(y_s + y_shift, 2)

        # Add value to list
        x_opt_list.append(x_opt)
        y_opt_list.append(y_opt)

    # Add list to dataframe
    df['x_opt'] = x_opt_list
    df['y_opt'] = y_opt_list

    # Return dataframe
    return df