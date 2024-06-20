import requests
import xml.etree.ElementTree as ET
import pandas as pd
from boardgame_object import BoardGame

# Define the base URL for the BoardGameGeek XML API
BASE_URL = "https://boardgamegeek.com/xmlapi/boardgame"

def get_game_info(game_id: int) -> BoardGame:
    """
    Retrieve information for a specific game from the BoardGameGeek XML API.

    Parameters:
    - game_id: The unique identifier for the game on BoardGameGeek.

    Returns:
    - A BoardGame object with the information retrieved from the API.
    """
    url = f"{BASE_URL}/{game_id}"

    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)

        game_element = root.find("boardgame")

        if game_element is not None:
            new_board_game = BoardGame()

            new_board_game.id = game_element.get("objectid", "N/A")
            new_board_game.year_published = game_element.find("yearpublished").text if game_element.find("yearpublished") is not None else "N/A"
            new_board_game.min_players = game_element.find("minplayers").text if game_element.find("minplayers") is not None else "N/A"
            new_board_game.max_players = game_element.find("maxplayers").text if game_element.find("maxplayers") is not None else "N/A"
            new_board_game.playing_time = game_element.find("playingtime").text if game_element.find("playingtime") is not None else "N/A"
            new_board_game.min_play_time = game_element.find("minplaytime").text if game_element.find("minplaytime") is not None else "N/A"
            new_board_game.max_play_time = game_element.find("maxplaytime").text if game_element.find("maxplaytime") is not None else "N/A"
            new_board_game.age = game_element.find("age").text if game_element.find("age") is not None else "N/A"

            new_board_game.primary_name = game_element.find("name[@primary='true']").text if game_element.find("name[@primary='true']") is not None else "N/A"

            new_board_game.description = game_element.find("description").text if game_element.find("description") is not None else "N/A"
            new_board_game.thumbnail = game_element.find("thumbnail").text if game_element.find("thumbnail") is not None else "N/A"
            new_board_game.image = game_element.find("image").text if game_element.find("image") is not None else "N/A"

            new_board_game.categories = [category.text for category in game_element.findall(".//boardgamecategory")]

            new_board_game.mechanics = [mechanic.text for mechanic in game_element.findall(".//boardgamemechanic")]

            new_board_game.families = [family.text for family in game_element.findall(".//boardgamefamily")]
        else:
            print("No <boardgame> element found in the XML.")
    else:
        print(f"Failed to retrieve information for game ID {game_id}. HTTP Status Code: {response.status_code}")

    return new_board_game

def update_game_rank(board_game: BoardGame) -> BoardGame:
    """
    Update the rank information for a specific game from the BoardGameGeek rank csv.
    """
    df = pd.read_csv('boardgames_ranks.csv')
    game_id = board_game.id
    game_rank_info = df[df['id'] == int(game_id)]
    if not game_rank_info.empty:
        board_game.rank = game_rank_info['rank'].values[0]
        board_game.users_rated = game_rank_info['usersrated'].values[0]
        board_game.average_rating = game_rank_info['average'].values[0]
        board_game.bayes_average_rating = game_rank_info['bayesaverage'].values[0]
    else:
        print(f"Rank information not found for game ID {game_id}")

    return board_game

def to_csv(board_games: list) -> None:
    """
    Write the information for a list of BoardGame objects to a CSV file.
    """
    data = []
    for game in board_games:
        data.append(game.to_dict())

    df = pd.DataFrame(data)
    df.to_csv("data/boardgames_info.csv", index=False)

def main():
    game_ids = [68448, 104006, 127398, 148949, 172308, 176494,
                203417, 244521, 266192, 284083, 300531, 328479,
                359970] # kennerspiel des jahres winner ids
    board_games = [update_game_rank(get_game_info(game_id)) for game_id in game_ids]
    to_csv(board_games)

if __name__ == "__main__":
    main()
