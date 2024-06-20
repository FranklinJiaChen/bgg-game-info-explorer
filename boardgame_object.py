class BoardGame:
    def __init__(self) -> None:
        self.id = None
        self.year_published = None
        self.min_players = None
        self.max_players = None
        self.playing_time = None
        self.min_play_time = None
        self.max_play_time = None
        self.age = None
        self.primary_name = None
        self.description = None
        self.thumbnail = None
        self.image = None
        self.categories = []
        self.mechanics = []
        self.families = []
        self.rank = None
        self.users_rated = None
        self.average_rating = None
        self.bayes_average_rating = None

    def __str__(self) -> str:
        return f"{self.primary_name} ({self.year_published})"

    def __repr__(self) -> str:
        return f"BoardGame({self.primary_name}, {self.year_published})"

    def print_all_info(self) -> None:
        print(f"Game ID: {self.id}")
        print(f"Year Published: {self.year_published}")
        print(f"Min Players: {self.min_players}")
        print(f"Max Players: {self.max_players}")
        print(f"Playing Time: {self.playing_time} minutes")
        print(f"Min Play Time: {self.min_play_time} minutes")
        print(f"Max Play Time: {self.max_play_time} minutes")
        print(f"Age: {self.age}+")
        print(f"Primary Name: {self.primary_name}")
        print(f"Description: {self.description}")
        print(f"Thumbnail: {self.thumbnail}")
        print(f"Image: {self.image}")
        print("\nCategories:")
        for category in self.categories:
            print(f"- {category}")
        print("\nMechanics:")
        for mechanic in self.mechanics:
            print(f"- {mechanic}")
        print("\nFamilies:")
        for family in self.families:
            print(f"- {family}")
        print(f"Rank: {self.rank}")
        print(f"Users Rated: {self.users_rated}")
        print(f"Average Rating: {self.average_rating}")
        print(f"Bayes Average Rating: {self.bayes_average_rating}")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "year_published": self.year_published,
            "min_players": self.min_players,
            "max_players": self.max_players,
            "playing_time": self.playing_time,
            "min_play_time": self.min_play_time,
            "max_play_time": self.max_play_time,
            "age": self.age,
            "primary_name": self.primary_name,
            "description": self.description,
            "thumbnail": self.thumbnail,
            "image": self.image,
            "categories": self.categories,
            "mechanics": self.mechanics,
            "families": self.families,
            "rank": self.rank,
            "users_rated": self.users_rated,
            "average_rating": self.average_rating,
            "bayes_average_rating": self.bayes_average_rating
        }
