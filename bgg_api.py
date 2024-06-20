import requests
import xml.etree.ElementTree as ET

# Define the base URL for the BoardGameGeek XML API
BASE_URL = "https://boardgamegeek.com/xmlapi/boardgame"

def get_game_info(game_id):
    url = f"{BASE_URL}/{game_id}"

    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)

        print(f"Root tag: {root.tag}, attributes: {root.attrib}")

        game_element = root.find("boardgame")

        if game_element is not None:
            game_info = {}

            game_info["id"] = game_element.get("objectid", "N/A")
            game_info["year_published"] = game_element.find("yearpublished").text if game_element.find("yearpublished") is not None else "N/A"
            game_info["min_players"] = game_element.find("minplayers").text if game_element.find("minplayers") is not None else "N/A"
            game_info["max_players"] = game_element.find("maxplayers").text if game_element.find("maxplayers") is not None else "N/A"
            game_info["playing_time"] = game_element.find("playingtime").text if game_element.find("playingtime") is not None else "N/A"
            game_info["min_play_time"] = game_element.find("minplaytime").text if game_element.find("minplaytime") is not None else "N/A"
            game_info["max_play_time"] = game_element.find("maxplaytime").text if game_element.find("maxplaytime") is not None else "N/A"
            game_info["age"] = game_element.find("age").text if game_element.find("age") is not None else "N/A"

            primary_name = game_element.find("name[@primary='true']")
            game_info["primary_name"] = primary_name.text if primary_name is not None else "N/A"

            game_info["description"] = game_element.find("description").text if game_element.find("description") is not None else "N/A"
            game_info["thumbnail"] = game_element.find("thumbnail").text if game_element.find("thumbnail") is not None else "N/A"
            game_info["image"] = game_element.find("image").text if game_element.find("image") is not None else "N/A"

            print(f"Game ID: {game_info['id']}")
            print(f"Year Published: {game_info['year_published']}")
            print(f"Min Players: {game_info['min_players']}")
            print(f"Max Players: {game_info['max_players']}")
            print(f"Playing Time: {game_info['playing_time']} minutes")
            print(f"Min Play Time: {game_info['min_play_time']} minutes")
            print(f"Max Play Time: {game_info['max_play_time']} minutes")
            print(f"Age: {game_info['age']}+")
            print(f"Primary Name: {game_info['primary_name'].encode('utf-8').decode('cp1252', 'ignore')}")
            print(f"Description: {game_info['description'].encode('utf-8').decode('cp1252', 'ignore')}")
            print(f"Thumbnail: {game_info['thumbnail']}")
            print(f"Image: {game_info['image']}")

            categories = game_element.findall(".//boardgamecategory")
            print("\nCategories:")
            for category in categories:
                category_name = category.text
                category_id = category.get("objectid")
                print(f"- {category_name} (ID: {category_id})")

            mechanics = game_element.findall(".//boardgamemechanic")
            print("\nMechanics:")
            for mechanic in mechanics:
                mechanic_name = mechanic.text
                mechanic_id = mechanic.get("objectid")
                print(f"- {mechanic_name} (ID: {mechanic_id})")

            families = game_element.findall(".//boardgamefamily")
            print("\nFamilies:")
            for family in families:
                family_name = family.text
                family_id = family.get("objectid")
                print(f"- {family_name} (ID: {family_id})")
        else:
            print("No <boardgame> element found in the XML.")
    else:
        print(f"Failed to retrieve information for game ID {game_id}. HTTP Status Code: {response.status_code}")

game_id = 391163
get_game_info(game_id)
