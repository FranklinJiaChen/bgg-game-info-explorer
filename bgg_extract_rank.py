import pandas as pd

df = pd.read_csv('boardgames_ranks.csv')

# kennerspiel_des_jahres_winners = [
#     {"year": 2011, "name": "7 Wonders", "bgg_id": 68448},
#     {"year": 2012, "name": "Village", "bgg_id": 104006},
#     {"year": 2013, "name": "Legends of Andor", "bgg_id": 127398},
#     {"year": 2014, "name": "Istanbul", "bgg_id": 148949},
#     {"year": 2015, "name": "Broom Service", "bgg_id": 172308},
#     {"year": 2016, "name": "Isle of Skye: From Chieftain to King", "bgg_id": 176494},
#     {"year": 2017, "name": "Exit: The Game", "bgg_id": 203417},
#     {"year": 2018, "name": "Quacks of Quedlinburg", "bgg_id": 244521},
#     {"year": 2019, "name": "Wingspan", "bgg_id": 266192},
#     {"year": 2020, "name": "The Crew: The Quest for Planet Nine", "bgg_id": 284083},
#     {"year": 2021, "name": "Paleo", "bgg_id": 300531},
#     {"year": 2022, "name": "Living Forest", "bgg_id": 328479},
#     {"year": 2023, "name": "Challengers!", "bgg_id": 359970}
# ]
# ids_to_keep = [game["bgg_id"] for game in kennerspiel_des_jahres_winners]

## kennerspiel des jahres winner ids
ids_to_keep = [68448, 104006, 127398, 148949, 172308, 176494, 203417, 244521, 266192, 284083, 300531, 328479, 359970]

filtered_df = df[df['id'].isin(ids_to_keep)]
filtered_df_sorted = filtered_df.sort_values(by='rank')
filtered_df_sorted.to_csv('kennerspiel_des_jahres_bgg.csv', index=False)
