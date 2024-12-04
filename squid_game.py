# NB: When using the while loop, time.sleep(5) has an issue where it sometimes
# does not sleep for the full 5 seconds, resulting in an extra round; uncomment
# line 62 to see what I mean.

from random import sample
from time import sleep, time


class Player:
    def __init__(self, id: int, position: int = 0) -> None:
        self.id = id
        self.position = position


class SquidGame:
    def __init__(self, num_of_players: int = 456) -> None:
        self.players = self._get_players(num_of_players)

    def _get_players(self, num_of_players: int) -> list[Player]:
        return [Player(id) for id in range(1, num_of_players + 1)]

    def start_game(self, num_of_players: int = 456) -> None:
        """
        Starts the game with the specified number of players (456 by default).

        Simulates Squid Game's “Red Light, Green Light”.
        Players are allowed to move during "Green Light" and
            are eliminated if they move during "Red Light."
        The game alternates between "Green" and "Red" lights for
            30 seconds (6 rounds, each lasting 5 seconds).
        """
        players = {
            str(player_id): {"position": 0}  # Start line position
            for player_id in range(1, num_of_players + 1)
        }

        light_color = "Green"
        start_time = time()

        # It is unclear whether the game should run for 30 seconds or 6 rounds, so I just did both.
        for _ in range(6):  # Stop this game after 6 rounds.
            # while time.time() - start_time < 30:  # Stop this game after 30 seconds.
            moved_players = []
            eliminated_players = []

            if light_color == "Green":
                moved_players = self.move_players(
                    list(players), 80
                )  # Move 80% of players

                # Update player positions
                for player in moved_players:
                    if player in players:
                        players[player]["position"] += 1

            elif light_color == "Red":
                moved_players = self.move_players(
                    list(players), 5
                )  # Move 5% of players
                eliminated_players = moved_players

                # Remove eliminated players
                for player in eliminated_players:
                    if player in players:
                        players.pop(player)

            # Determine the players that did not move
            static_players = [
                player for player in players if player not in moved_players
            ]

            print(f"{light_color} Light")
            print(f'Moved: {", ".join(moved_players)}')
            print(f'Static: {", ".join(static_players)}')
            print(
                f'Eliminated: {", ".join(eliminated_players) if eliminated_players else "None"}.'
            )
            print()

            # sleep(5)  # Wait 5 seconds
            # Alternate between "Green" and "Red" light.
            light_color = ["Green", "Red"][(light_color == "Green")]

            # print(f"Time elapsed: {round(time.time() - start_time)} seconds.\n")

        # If a player moved forward two times out of the three
        #   times when there was green light, the player wins.
        # Remove players that have not reached the finish line.
        players = {k: v for k, v in players.items() if v["position"] > 1}

        print(f'Winners: {", ".join(players) if players else "None"}.')

    def move_players(self, players: list, percentage: int) -> list:
        """Randomly select a percentage of players to move (randomly)."""
        num_of_players = len(players)
        percentage = min(percentage, 100)
        count = int(num_of_players * (percentage / 100))
        return sample(players, count)


if __name__ == "__main__":
    game = SquidGame()
    game.start_game()
