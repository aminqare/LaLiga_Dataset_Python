import pandas as pd

def get_season_table(df_laliga, season_name):
    season_data = df_laliga[df_laliga['season'] == season_name]
    sorted_data = season_data.sort_values(by=['points', 'goal_difference'], ascending=[False, False])
    
    return sorted_data
