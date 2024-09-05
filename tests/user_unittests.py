import unittest
from userInfo.users import User
from sessionManagement.session import Session
from database.store import Persist

stub_user_history = ['W', 'L', 'W']


class TestUser(unittest.TestCase):
    def test_create_password_good(self):
        user = User("tyler")
        user.update_password("password")
        self.assertEqual(user.password, "password")

    def test_create_password_bad(self):
        user = User("tyler")
        with self.assertRaises(ValueError):
            user.update_password("bad")

    def test_update_username_good(self):
        user = User("tyler")
        user.update_username("tyler")
        self.assertEqual(user.username, "tyler")

    def test_update_username_bad(self):
        user = User("tyler")
        with self.assertRaises(ValueError):
            user.update_username("")

    def test_update_user_history_good(self):
        user = User("tyler")
        user.history = stub_user_history
        user.update_user_history("W")
        wins = 0
        for wins in range(len(user.history)):
            if wins == "W":
                wins += 1
        self.assertEqual(wins, 3)

    def test_update_user_history_bad(self):
        user = User("tyler")
        user.history = stub_user_history
        with self.assertRaises(ValueError):
            user.update_user_history("R")

    def test_user_history_good(self):
        user = User("tyler")
        user.update_user_history("W")
        user.update_user_history("W")
        user.update_user_history("L")
        history = user.user_history()
        self.assertEqual(history, "Total Games Played: 3, Wins: 2, Losses: 1, Win/Loss Ratio: 2.00")

    def test_user_history_bad(self):
        user = User("tyler")
        user.history = []
        with self.assertRaises(ValueError):
            user.user_history()

    def test_verify_user_login_good(self):
        user1 = User("user1", "tyler")
        user1.save_user()
        self.assertTrue(User.verify_user_login("user1", "tyler"))
        Persist.destroy_profile("user1")

    def test_verfiy_user_login_bad(self):
        user1 = User("user1", "tyler")
        user1.update_username("Tyler")
        user1.save_user()
        with self.assertRaises(IOError):
            login_user = User.verify_user_login("user1", "tyler")
        Persist.destroy_profile("Tyler")

    def test_save_user_good(self):
        user = User()
        user.update_username("Tyler")
        self.assertTrue(user.save_user())
        Persist.destroy_profile("Tyler")

    def test_save_user_bad(self):
        user = User("tyler")
        user.save_user()
        user2 = User("tyler")
        with self.assertRaises(IOError):
            user2.save_user()
        Persist.destroy_profile("tyler")

    def test_load_user_good(self):
        user = User("tyler", "riggs")
        user.save_user()
        new_user = User.load_user("tyler")
        self.assertEqual(new_user.username, "tyler")

    def test_load_user_bad(self):
        user = User("tyler")
        with self.assertRaises(IOError):
            new_user = User.load_user("tyler")


if __name__ == '__main__':
    unittest.main()
