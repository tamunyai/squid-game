from random import sample
from time import sleep, time


class Player:
    def __init__(self, player_id: int, position: int = 0) -> None:
        """
        Initializes a player with a unique ID and an initial position.

        Args:
            player_id (int): The unique identifier for the player.
            position (int, optional): The initial position of the player. Defaults to 0.
        """
        self.player_id = player_id
        self.position = position

    def move(self):
        """
        Increments the player's position by 1 when they move.

        This method simulates the player advancing in the game.
        """
        self.position += 1


class SquidGame:
    def __init__(self, total_players: int = 456) -> None:
        """
        Initializes the Squid Game with a given number of players.

        Args:
            total_players (int, optional): The total number of players in the game. Defaults to 456.
        """
        self.players = self._create_players(total_players)

    def _create_players(self, total_players: int) -> list[Player]:
        """
        Creates a list of Player objects.

        Args:
            total_players (int): The total number of players to be created.

        Returns:
            list[Player]: A list of Player objects representing the players in the game.
        """
        return [Player(player_id) for player_id in range(1, total_players + 1)]

    def start_game(
        self,
        light_interval: int = 5,
        game_duration: int = 30,
        current_light: str = "Green",
    ) -> list[Player]:
        """
        Simulates the Squid Game's "Red Light, Green Light" game.

        The game alternates between "Green Light" (where players move) and "Red Light" (where players who move are eliminated).
        The game runs for a specified duration or until all players are eliminated.

        Args:
            light_interval (int, optional): The interval (in seconds) between each light switch. Defaults to 5.
            game_duration (int, optional): The total duration (in seconds) of the game. Defaults to 30.
            current_light (str, optional): The starting light ("Green" or "Red"). Defaults to "Green".

        Returns:
            list[Player]: A list of remaining players after the game ends.
        """
        rounds = 0
        start_time = time()
        while time() - start_time < game_duration:
            rounds += 1
            move_percentage = 80 if current_light == "Green" else 5
            total_players = len(self.players)
            players_to_move_count = int(total_players * (move_percentage / 100))
            moving_players = sample(self.players, players_to_move_count)
            stationary_players = [p for p in self.players if p not in moving_players]

            # Update positions for moving players
            for player in moving_players:
                player.move()

            # Eliminate players who moved during Red light
            if current_light == "Red":
                self.players = stationary_players

            # Output for current round
            print(f"Round {rounds}: {current_light} Light")
            self._print_players("Moved", moving_players)
            self._print_players("Static", stationary_players)
            self._print_eliminated(moving_players, current_light)
            print()

            # Wait for the next interval before switching light
            sleep(light_interval)

            # Alternate between "Green" and "Red" light.
            current_light = "Red" if current_light == "Green" else "Green"

        # Return the list of remaining players (those who are not eliminated)
        return self.players

    def _print_players(self, label: str, players: list[Player]) -> None:
        """
        Helper function to print the list of players who moved or stayed still.

        Args:
            label (str): The label indicating whether the players "Moved" or were "Static".
            players (list[Player]): The list of players who either moved or stayed still.
        """
        print(f'{label}: {", ".join([str(player.player_id) for player in players])}')

    def _print_eliminated(
        self, moving_players: list[Player], current_light: str
    ) -> None:
        """
        Helper function to print the list of players who were eliminated during the current round.

        Args:
            moving_players (list[Player]): The list of players who attempted to move during the current round.
            current_light (str): The current light ("Green" or "Red").
        """
        if moving_players and current_light == "Red":
            print(
                f'Eliminated: {", ".join([str(p.player_id) for p in moving_players])}.'
            )
        else:
            print("Eliminated: None.")


if __name__ == "__main__":
    game = SquidGame()
    remaining_players = game.start_game()

    print("Remaining Players:")
    for player in remaining_players:
        print(f"Player {player.player_id} at position {player.position}")
