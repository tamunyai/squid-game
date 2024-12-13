import unittest

from squid_game import Player, SquidGame


class TestPlayer(unittest.TestCase):
    """
    Test cases for the Player class.
    """

    def test_player_initialization(self):
        """
        Test the initialization of a Player object.
        Ensures the player has the correct ID, starting position, and elimination status.
        """
        player = Player(id="001")
        self.assertEqual(player.id, "001")
        self.assertEqual(player.position, 0)
        self.assertFalse(player.eliminated)

    def test_player_move(self):
        """
        Test the movement functionality of a Player.
        Ensures the player's position updates correctly and
        that eliminated players do not move.
        """
        player = Player(id="001")
        player.move()
        self.assertEqual(player.position, 1)

        player.eliminate()
        player.move()
        self.assertEqual(player.position, 1)

    def test_player_eliminate(self):
        """
        Test the elimination functionality of a Player.
        Ensures the player's elimination status changes correctly.
        """
        player = Player(id="001")
        self.assertFalse(player.eliminated)

        player.eliminate()
        self.assertTrue(player.eliminated)


class TestSquidGame(unittest.TestCase):
    """
    Test cases for the SquidGame class.
    """

    def setUp(self):
        """
        Set up the SquidGame instance with a total of 10 players before each test.
        """
        self.game = SquidGame(total_players=10)

    def test_game_initialization(self):
        """
        Test the initialization of the SquidGame.
        Ensures the game starts with the correct number of players,
        all players in the correct initial state (position 0, not eliminated).
        """
        self.assertEqual(len(self.game.players), 10)

        for player in self.game.players:
            self.assertIsInstance(player, Player)
            self.assertEqual(player.position, 0)
            self.assertFalse(player.eliminated)

    def test_get_remaining_players(self):
        """
        Test the get_remaining_players method.
        Ensures that the method returns the correct number of remaining players,
        and that eliminating a player reduces the number of remaining players.
        """
        self.assertEqual(len(self.game.get_remaining_players()), 10)

        self.game.players[0].eliminate()
        self.assertEqual(len(self.game.get_remaining_players()), 9)

    def test_get_eliminated_players(self):
        """
        Test the get_eliminated_players method.
        Ensures that eliminated players are correctly tracked.
        """
        self.assertEqual(len(self.game.get_eliminated_players()), 0)

        self.game.players[0].eliminate()
        self.game.players[1].eliminate()
        self.assertEqual(len(self.game.get_eliminated_players()), 2)

    def test_get_moving_players(self):
        """
        Test the get_moving_players method.
        Ensures that the correct number of players move, based on the specified percentage.
        """
        moving_players = self.game.get_moving_players(move_percentage=50)
        self.assertGreaterEqual(len(moving_players), 0)
        self.assertLessEqual(len(moving_players), 5)  # At most 50% of 10 players

    def test_get_stationary_players(self):
        """
        Test the get_stationary_players method.
        Ensures that the sum of moving and stationary players equals the total number of remaining players.
        """
        moving_players = self.game.get_moving_players(move_percentage=50)
        stationary_players = self.game.get_stationary_players(moving_players)
        self.assertEqual(
            len(moving_players) + len(stationary_players),
            len(self.game.get_remaining_players()),
        )

    def test_reset(self):
        """
        Test the reset functionality of the SquidGame.
        Ensures that after resetting, all players return to their initial state.
        """
        self.game.players[0].eliminate()
        self.assertEqual(len(self.game.get_remaining_players()), 9)

        self.game.reset()
        self.assertEqual(len(self.game.get_remaining_players()), 10)

        for player in self.game.players:
            self.assertEqual(player.position, 0)
            self.assertFalse(player.eliminated)

    def test_start_game(self):
        """
        Test the start method of SquidGame.
        Ensures the game starts correctly and no players are eliminated at the start.
        """
        remaining_players = self.game.start(light_interval=1, game_duration=2)
        self.assertTrue(len(remaining_players) <= 10)
        self.assertTrue(all(not player.eliminated for player in remaining_players))


if __name__ == "__main__":
    unittest.main()
