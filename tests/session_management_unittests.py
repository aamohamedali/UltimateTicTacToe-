import unittest
from userInfo.users import User
from sessionManagement.session import Session
from database.store import Persist


class TestSession(unittest.TestCase):

    def test_terminate_session_good(self):
        user = ("test_user", "hello", "0000")
        session = Session(1234)
        self.assertTrue(session.terminate_session())

    def test_terminate_session_bad(self):
        new_session = Session(1234)
        new_session.session_id = None
        with self.assertRaises(ValueError):
            new_session.terminate_session()

    def test_add_player_good(self):
        user = User("test_user", "hello", "0000")
        new_session = Session(1234)
        new_session.add_player(user)
        new_player = next(iter(new_session.players))
        self.assertEqual(new_session.players[new_player], "0000")

    def test_add_players_bad(self):
        new_session = Session(1234)
        user = User("test_user", "hello")
        user2 = User("tyler", "1111")
        user3 = User("chad", "2222")
        new_session.add_player(user)
        new_session.add_player(user2)
        with self.assertRaises(ValueError):
            new_session.add_player(user3)

    def test_remove_players_good(self):
        new_session = Session(1234)
        user = User("test_user", "hello")
        user2 = User("tyler","1111", "0000")
        new_session.add_player(user)
        new_session.add_player(user2)
        new_session.remove_player(user)
        player_left = next(iter(new_session.players))
        self.assertEqual(new_session.players[player_left], "0000")

    def test_remove_players_bad(self):
        new_session = Session(1234)
        user = User("test_user", "hello")
        with self.assertRaises(ValueError):
            new_session.remove_player(user)

    def test_get_session_info_good(self):
        new_session = Session(1234)
        output = "Session ID: 1234 |"
        self.assertEqual(new_session.get_session_info().strip(), output)

    def test_get_session_info_bad(self):
        new_session = Session(1234)
        new_session.terminate_session()
        with self.assertRaises(IOError):
            new_session.get_session_info()

    def test_get_users_in_session_good(self):
        new_session = Session(1234)
        output = "test_user, tyler"
        user = User("test_user", "hello")
        user1 = User("tyler", "11111")
        new_session.add_player(user)
        new_session.add_player(user1)
        self.assertEqual(new_session.get_users_in_session().strip(), output)

    def test_get_users_in_session_bad(self):
        new_session = Session(1234)
        user = User("test_user", "hello")
        user1 = User("tyler", "11111")
        new_session.add_player(user)
        new_session.add_player(user1)
        new_session.terminate_session()
        with self.assertRaises(IOError):
            new_session.get_users_in_session()


if __name__ == '__main__':
    unittest.main()
