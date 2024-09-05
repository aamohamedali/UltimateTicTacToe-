import unittest
from logic.app_logic import Game


class TestAppLogic(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_getGameState(self):
        # Test if getGameState returns the correct state and ustate
        self.game.next_move(0,0,"x")
        state, ustate = self.game.getGameState()
        self.assertEqual(state, [
            ['x', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']])
        self.assertEqual(ustate, ["NC", "NC", "NC", "NC", "NC", "NC", "NC", "NC", "NC"])

    def test_setGameState(self):
        # Test if setGameState updates the state and ustate correctly
        new_state = [
            ['x', 'x', 'x', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'o', 'o', 'o', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        new_ustate = ["x","o", "NC", "NC", "NC", "NC", "NC", "NC", "NC"]
        self.game.setGameState(new_state, new_ustate)
        state, ustate = self.game.getGameState()
        self.assertEqual(state, new_state)
        self.assertEqual(ustate, new_ustate)

    def test_next_move_valid(self):
        # Test a valid move
        self.game.next_move(0, 0, 'x')
        self.assertEqual(self.game.state[0][0], 'x')

    def test_next_move_invalid(self):
        # Test an invalid move
        # For simplicity, let's assume (0, 0) is already occupied
        self.game.state[0][0] = 'x'
        with self.assertRaises(ValueError):
            self.game.next_move(0, 0, 'o')

    def test_winning_condition_valid(self):
        # Test winning condition
        # For simplicity, let's simulate a winning condition in a row
        self.game.state[0] = ['x', 'x', 'x', 'E', 'E', 'E', 'E', 'E', 'E']
        self.game.winning_condition(0, 'x')
        self.assertEqual(self.game.ustate[0], 'x')

    def test_winning_condition_invalid(self):
        # Test non winning condition
        # For simplicity, let's simulate a non winning condition in a row
        self.game.state[0] = ['x', 'E', 'x', 'x', 'E', 'E', 'E', 'E', 'E']
        self.game.winning_condition(0, 'x')
        self.assertNotEqual(self.game.ustate[0], 'x')

    def test_subgridWinner_valid(self):
        # Test subgrid winning condition
        # For simplicity, let's simulate a winning condition in a row
        self.game.subgrid_win(1,"o")
        self.assertEqual(self.game.ustate[1], 'o')

    def test_subgridWinner_invalid(self):
        # Test subgrid winning condition
        # For simplicity, let's simulate a winning condition in a row
        self.game.subgrid_win(1,"o")
        self.assertNotEqual(self.game.ustate[1], 'x')
        self.assertNotEqual(self.game.ustate[0], 'o')

    def test_refree_valid(self):
        # Test all the subgrid for ultimate winner
        # For simplicity, let's simulate a winning condition in a row of subgrid
        self.game.ustate = ["x", "x", "x", "NC", "NC", "NC", "NC", "NC", "NC"]
        self.game.refree()
        self.assertEqual(1,self.game.outcome)

    def test_refree_invalid(self):
        # Test all the subgrid for ultimate winner
        # For simplicity, let's simulate a not winning condition in the subgrids

        self.game.ustate = ["x", "x", "o", "x", "NC", "NC", "NC", "NC", "NC"]
        self.game.refree()
        self.assertNotEqual(1,self.game.outcome)

    def test_validate_true(self):
        # Test all the subgrid for ultimate winner
        # For simplicity, let's simulate a not winning condition in the subgrids
        self.game.state = [
            ['x', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'x', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        self.game.ustate = ["NC", "NC", "NC", "NC", "NC", "NC", "NC", "NC", "NC"]
        self.assertTrue(self.game._validate(0,3,"x"))
        self.game.next_move(0,3,"x")
        # self.game.next_subgrid=3
        self.assertTrue(self.game._validate(3, 5,"o"))

    def test_validate_false(self):
        # Test all the subgrid for ultimate winner
        # For simplicity, let's simulate a not winning condition in the subgrids
        self.game.state=[
            ['x', 'x', 'x', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'x', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        self.game.ustate=["x", "NC", "NC", "NC", "NC", "NC", "NC", "NC", "NC"]
        self.game.next_subgrid = ""
        self.game.next_player = "x"
        self.game.outcome = 0

        self.assertFalse(self.game._validate(0, 3,"x"))# subgrid already won by x
        self.assertFalse(self.game._validate(1, 2,"x"))# already played on that box
        self.game.ustate=["x", "x", "x", "NC", "NC", "NC", "NC", "NC", "NC"]# simulating a ultimate winner
        self.game.refree()
        self.assertFalse(self.game._validate(1, 3,"x"))# cannot play after winning the game
        self.game.outcome = 0
        self.game.ustate = ["x", "NC", "NC", "NC", "NC", "NC", "NC", "NC", "NC"]
        self.game.next_move(5,4,"x")
        self.assertFalse(self.game._validate(4,2,"x"))#should be the next player
        self.assertFalse(self.game._validate(5, 2, "o"))  # should be the next player

if __name__ == '__main__':
    unittest.main()