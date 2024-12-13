from dataclasses import dataclass
from random import sample
from time import sleep, time


@dataclass
class Player:
    """
    Represents a player in the game.

    Attributes:
        id (str): Unique identifier for the player.
        position (int): Current position of the player. Defaults to 0.
        eliminated (bool): Whether the player is eliminated. Defaults to False.
    """

    id: str
    position: int = 0
    eliminated: bool = False

    def move(self):
        """
        Increments the player's position by 1 if not eliminated.

        This method simulates the player advancing in the game.
        """
        if not self.eliminated:
            self.position += 1

    def eliminate(self):
        """
        Marks the player as eliminated when they move during a "Red" light.

        This method simulates the player being eliminated in the game.
        """
        self.eliminated = True


class SquidGame:
    """
    Simulates the 'Red Light, Green Light' game from Squid Game.

    Attributes:
        total_players (int): Total number of players in the game.
        players (list[Player]): List of players participating in the game.
    """

    def __init__(self, total_players: int = 456) -> None:
        if total_players <= 0:
            raise ValueError("The number of players must be greater than 0.")

        self.total_players = total_players
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

    def get_remaining_players(self) -> list[Player]:
        """
        Retrieves the list of players who are still active in the game.

        Returns:
            list[Player]: A list of players who have not been eliminated.
        """
        return [p for p in self.players if not p.eliminated]

    def get_moving_players(self, move_percentage: int) -> list[Player]:
        """
        Selects a subset of remaining players who will attempt to move.

        Args:
            move_percentage (int): The percentage of remaining players that will attempt to move.

        Returns:
            list[Player]: A random sample of players who will move, based on the specified percentage.
        """
        remaining_players: list[Player] = self.get_remaining_players()
        total_remaining: int = len(remaining_players)
        num_to_move = int(total_remaining * (move_percentage / 100))
        return sample(remaining_players, min(num_to_move, total_remaining))

    def get_stationary_players(self, moving_players: list[Player]) -> list[Player]:
        """
        Identifies players who chose to stay still in the current round.

        Args:
            moving_players (list[Player]): The list of players who attempted to move.

        Returns:
            list[Player]: A list of players who did not attempt to move during the current round.
        """
        return [p for p in self.get_remaining_players() if p not in moving_players]

    def get_eliminated_players(self) -> list[Player]:
        """
        Retrieves the list of players who have been eliminated.

        Returns:
            list[Player]: A list of players who are no longer in the game.
        """
        return [p for p in self.players if p.eliminated]


if __name__ == "__main__":
    game = SquidGame()
    remaining_players = game.start_game()

    print("Remaining Players:")
    for player in remaining_players:
        print(f"Player {player.player_id} at position {player.position}")
