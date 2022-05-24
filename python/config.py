# Import from packages
import pandas as pd



class Config:

    # Directory
    directory = '/Users/gian-andrea/Documents/Masterarbeit (offline)/statsbomb360-euro2020/events/'

    # Filepath
    filepath = directory + '3788742.json'

    # Shot columns
    shot = ['possession_team', 'shot', 'location']

    # Half of wingspan
    half_wingspan = 3

    # Dict with goalpost coordinates
    data = {'x': [0, 0, 120, 120], 'y': [36, 44, 36, 44]}
    # Dataframe with goalpost coordinates
    df_posts = pd.DataFrame(data)