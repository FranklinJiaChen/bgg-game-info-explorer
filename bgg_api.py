import requests
import xml.etree.ElementTree as ET
from boardgame_object import BoardGame

# Define the base URL for the BoardGameGeek XML API
BASE_URL = "https://boardgamegeek.com/xmlapi/boardgame"

def get_game_info(game_id) -> BoardGame:
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

        print(f"Root tag: {root.tag}, attributes: {root.attrib}")
        game_element = root.find("boardgame")

        if game_element is not None:
            new_board_game = BoardGame()
            game_info = {}

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

def main():
    game_ids = [391163, 1]
    board_games = [get_game_info(game_id) for game_id in game_ids]
    for game in board_games:
        game.print_all_info()

if __name__ == "__main__":
    main()
