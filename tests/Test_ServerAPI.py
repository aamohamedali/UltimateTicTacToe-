import sys
sys.path.append("../")
import unittest
from ServerAPI.serverAPI import TicTacToeServer

class TestTicTacToeServer(unittest.TestCase):

    def setUp(self):
        self.server = TicTacToeServer()

    def test_save_user_page(self):
        username = 'test_user'
        expected_output = "user test_user is created!"
        result = self.server.save_user(username)
        self.assertEqual(result, expected_output)

    def test_load_user_page(self):
        username = 'test_user'
        expected_output = f"{username} Added to the game!"
        result = self.server.load_user(username)
        self.assertEqual(result, expected_output)

    def test_start_game(self):
        expected_output = "game started!"
        result = self.server.start()
        self.assertEqual(result, expected_output)

    def test_logging_game(self):
        expected_output = "log info"
        state = "state"
        database = "database"
        result = self.server.logging(state, database)
        self.assertEqual(result, expected_output)

    def test_remove_game(self):
        state = '123'
        expected_output = "Game is removed!"
        result = self.server.remove(state)
        self.assertEqual(result, expected_output)

    def test_restart_game(self):
        expected_output = "Game is restarted!"
        result = self.server.restart()
        self.assertEqual(result, expected_output)

    def test_stop_game(self):
        expected_output = "Game is stopped!"
        result = self.server.stop()
        self.assertEqual(result, expected_output)

    def test_retrieve_game(self):
        state = '123'
        expected_output = "Game is retrieved!"
        result = self.server.retrieve(state)
        self.assertEqual(result, expected_output)

    def test_user_info_update(self):
        username = 'test_user'
        expected_output = "user info updated"
        result = self.server.user_info_update(username)
        self.assertEqual(result, expected_output)

    def test_check_other_player_move(self):
        username = 'test_user'
        state = "THIS"
        expected_output = "current state: THIS"
        result = self.server.check_other_player_move(state)
        self.assertEqual(result, expected_output)

    def test_next_move(self):
        index1 = '0'
        index2 = '0'
        user = 'test_user'
        expected_output = "test_user Moved!"
        result = self.server.next_move(index1, index2, user)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
