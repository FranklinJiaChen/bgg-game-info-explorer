# Get info on board games using Board Game Geek


## bgg_extract_rank.py
gets yearpublished, rank, bayesaverage, average, usersrated
and other info of interested board games

in file, update ids_to_keep to the interested board games.
update ranks by getting the csv file by downloading and replacing the
rank csv file: https://boardgamegeek.com/data_dumps/bg_ranks

## bgg_api.py
get a variety of info on a game such as min/max players, playing time, age, description, image, mechanics, families and category

in file, update game_id to desired game.

## to-do
I want to combine the info of the two .py file into one csv.
