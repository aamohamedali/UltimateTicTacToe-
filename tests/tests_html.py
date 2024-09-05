import sys
sys.path.append("../")

import unittest
from html_page.web_page import UltimateTicTacToeGame


class TestUltimateTicTacToe(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
    def test_startPage(self):
        expected_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ultimate Tic-Tac-Toe - Start Page</title>
        </head>
        <body>
            <div>
                <h1>Welcome to Ultimate Tic-Tac-Toe!</h1>
                <button onclick="window.location.href='gamePage'">Start new game</button>
            </div>
        </body>
        </html>
        """

        self.assertEqual(UltimateTicTacToeGame.startPage(), expected_html)

    def test_gamePage(self):
        expected_html = UltimateTicTacToeGame.html_code
        self.assertEqual(UltimateTicTacToeGame.gamePage(), expected_html)

    
    def test_registerPage(self):
        expected_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ultimate Tic-Tac-Toe - Register</title>
        </head>
        <body>
            <div>
                <h1>Register</h1>
                <form action="register" method="post">
                    <label for="username">Username:</label><br>
                    <input type="text" id="username" name="username"><br>
                    <label for="password">Password:</label><br>
                    <input type="password" id="password" name="password"><br><br>
                    <input type="submit" value="Register">
                </form>
            </div>
        </body>
        </html>
        """

        self.assertEqual(UltimateTicTacToeGame.registerPage(), expected_html)



if __name__ == '__main__':
    unittest.main()


