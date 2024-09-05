from unittest import TestCase
from database.store import Persist
from logic.app_logic import Game

class TestStore(TestCase):

    def setUp(self):
        self.username1 = "Samdaman40"
        self.password = "Password"
        self.username2 = "TheGamer70943"
        self.game = Game()
        self.maxDiff = None

    def test_store_profile(self):
        Persist.store_profile(self.username1, self.password)
        profile = Persist.load_profile(self.username1)
        self.assertEqual(profile[0], self.username1)
        Persist.destroy_profile(self.username1)
    
    def test_store_profile_errors(self):
        Persist.store_profile(self.username1, self.password)
        self.assertRaises(IOError, Persist.store_profile, self.username1, self.password)
        Persist.destroy_profile(self.username1)

    def test_load_profile(self):
        Persist.store_profile(self.username1, self.password)
        profile = Persist.load_profile(self.username1)
        self.assertEqual(profile[0], self.username1)
        Persist.destroy_profile(self.username1)

    def test_load_profile_errors(self):
        self.assertRaises(IOError, Persist.load_profile, "a") 

    def test_destroy_profile(self):
        Persist.store_profile(self.username1, self.password)
        test = Persist.destroy_profile(self.username1)
        self.assertTrue(test)
    
    def test_destroy_profile_errors(self):
        Persist.store_profile(self.username1, self.password)
        Persist.destroy_profile(self.username1)
        self.assertRaises(IOError, Persist.destroy_profile, self.username1)

    def test_update_username(self):
        Persist.store_profile(self.username1, self.password)
        Persist.update_username(self.username1, "test")
        self.assertEqual(Persist.load_profile("test")[0], "test")
        Persist.destroy_profile("test")

    def test_update_username_errors(self):
        Persist.store_profile(self.username1, self.password)
        Persist.store_profile(self.username2, self.password)
        self.assertRaises(IOError, Persist.update_username, self.username1, self.username2)
        Persist.destroy_profile(self.username1)
        Persist.destroy_profile(self.username2)
        self.assertRaises(IOError, Persist.update_username, self.username1, "test")
    
    def test_update_password(self):
        Persist.store_profile(self.username1, self.password)
        successfulUpdate = Persist.update_password(self.username1, "test")
        self.assertTrue(successfulUpdate)
        Persist.destroy_profile(self.username1)

    def test_update_password_errors(self):
        self.assertRaises(IOError, Persist.update_password, self.username1, "test")        

    def test_verify_login_true(self):
        Persist.store_profile(self.username1, self.password)
        self.assertTrue(Persist.verify_login(self.username1, self.password))
        Persist.destroy_profile(self.username1)

    def test_verify_login_false(self):
        Persist.store_profile(self.username1, self.password)
        self.assertFalse(Persist.verify_login(self.username1, "test"))
        Persist.destroy_profile(self.username1)
        
    def test_store_game_state(self):
        Persist.store_profile(self.username1, self.password)
        Persist.store_profile(self.username2, self.password)
        Persist.store_game_state(self.game, self.username1, self.username2)
        new_game_state = Persist.load_game_state(self.game.gameId)
        self.assertEqual(self.game.state, new_game_state[0])
        self.assertEqual(self.game.ustate, new_game_state[1])
        self.assertEqual(self.game.next_subgrid, new_game_state[2])
        self.assertEqual(self.game.next_player, new_game_state[3])
        self.assertEqual(self.game.outcome, new_game_state[4])
        self.assertEqual(self.username1, new_game_state[5])
        self.assertEqual(self.username2, new_game_state[6])
        Persist.destroy_game_state(self.username1, self.username2)
        Persist.destroy_profile(self.username1)
        Persist.destroy_profile(self.username2)

    def test_store_game_state_errors(self):
        Persist.store_profile(self.username1, self.password)
        self.assertRaises(IOError, Persist.store_game_state, self.game, self.username1, self.username2)
        Persist.destroy_profile(self.username1)

    def test_load_game_state(self):
        Persist.store_profile(self.username1, self.password)
        Persist.store_profile(self.username2, self.password)
        Persist.store_game_state(self.game, self.username1, self.username2)
        new_game_state = Persist.load_game_state(self.game.gameId)
        self.assertEqual(self.game.state, new_game_state[0])
        self.assertEqual(self.game.ustate, new_game_state[1])
        self.assertEqual(self.game.next_subgrid, new_game_state[2])
        self.assertEqual(self.game.next_player, new_game_state[3])
        self.assertEqual(self.game.outcome, new_game_state[4])
        self.assertEqual(self.username1, new_game_state[5])
        self.assertEqual(self.username2, new_game_state[6])
        Persist.destroy_game_state(self.username1, self.username2)
        Persist.destroy_profile(self.username1)
        Persist.destroy_profile(self.username2)

    def test_load_game_state_errors(self):
        self.assertRaises(IOError, Persist.load_game_state, 123)

    def test_destroy_game_state(self):
        Persist.store_profile(self.username1, self.password)
        Persist.store_profile(self.username2, self.password)
        Persist.store_game_state(self.game, self.username1, self.username2)
        Persist.destroy_game_state(self.username1, self.username2)
        Persist.destroy_profile(self.username1)
        Persist.destroy_profile(self.username2)
        self.assertRaises(IOError, Persist.load_game_state, self.game.gameId)

    def test_destroy_game_state_errors(self):
        Persist.store_profile(self.username1, self.password)
        Persist.store_profile(self.username2, self.password)
        self.assertRaises(IOError, Persist.destroy_game_state, self.username1, self.username2)
        Persist.destroy_profile(self.username1)
        Persist.destroy_profile(self.username2)

    def test_add_win(self):
        Persist.store_profile(self.username1, self.password)
        Persist.add_win(self.username1)
        profile = Persist.load_profile(self.username1)
        self.assertEqual(profile[1], 1)
        Persist.destroy_profile(self.username1)

    def test_add_win_errors(self):
        self.assertRaises(IOError, Persist.add_win, "invalid username")

    def test_add_loss(self):
        Persist.store_profile(self.username1, self.password)
        Persist.add_loss(self.username1)
        profile = Persist.load_profile(self.username1)
        self.assertEqual(profile[2], 1)
        Persist.destroy_profile(self.username1)

    def test_add_loss_errors(self):
        self.assertRaises(IOError, Persist.add_loss, "invalid username")

    # def test_add_friend(self):
    #     Persist.store_profile(self.username1, self.password)
    #     Persist.store_profile(self.username2, self.password)
    #     Persist.add_friend(self.username1, self.username2)
    #     friends = Persist.load_friends_list(self.username1)
    #     self.assertEqual(friends[0], self.username2)
    #     Persist.destroy_profile(self.username1)
    #     Persist.destroy_profile(self.username2)

    # def test_remove_friend(self):
    #     Persist.store_profile(self.username1, self.password)
    #     Persist.store_profile(self.username2, self.password)
    #     Persist.add_friend(self.username1, self.username2)
    #     friends = Persist.load_friends_list(self.username1)
    #     self.assertEqual(friends[0], self.username2)
    #     Persist.remove_friend(self.username1, self.username2)
    #     new_friends = Persist.load_friends_list(self.username1)
    #     self.assertNotIn(self.username2, new_friends)
    #     Persist.destroy_profile(self.username1)
    #     Persist.destroy_profile(self.username2)

        

    

    

    