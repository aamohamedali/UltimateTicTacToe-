import sys
import os
import signal


sys.path.append("./")

from bottle import Bottle, run, request, static_file
from userInfo.users import User
from logic.app_logic import Game
from html_page.web_page import UltimateTicTacToeGame
from sessionManagement.session import Session
from database.store import Persist


class TicTacToeServer(Bottle):
    session = Session()
    Tictocgame=Game(session.session_id)#session.get_users_in_session().split(",")[0],session.get_users_in_session().split(",")[1])

    def __init__(self):
        super(TicTacToeServer, self).__init__()
        self.route("/", callback=self.begin)
        self.route("/begin", callback=self.begin)
        self.route("/registration", callback=self.registration)
        self.route("/register_user", callback=self.register_user, method="POST")
        self.route("/login", callback=self.login_game)
        self.route("/start_game", callback=self.start)
        self.route("/restart_game", callback=self.restart)
        self.route("/playing", callback=self.play)
        self.route("/login_user1", callback=self.login_user1, method="POST")
        self.route("/login_user2", callback=self.login_user2, method="POST")
        self.route("/logging", callback=self.logging)
        self.route("/save_user", callback=self.save_user, method="POST")
        self.route("/load_user/<username>", callback=self.load_user)
        self.route("/check_other_player_move/<username>/<state>", callback=self.check_other_player_move)
        self.route("/next_move", method="GET", callback=self.handle_next_move)
        self.route("/update_user/<username>", callback=self.user_update)
        self.route("/halt", callback=self.halt)
        self.route("/static/<fname>", callback=self.serve)
        self.route("/save_game", callback=self.save)
        self.route("/load_game", callback=self.load,method='POST')
        self.route("/load_gamepage", callback=self.loadpage)
    def loadpage(cls):
        return UltimateTicTacToeGame.loadGamepage(cls)

    def load(cls):
        objectAccess=Persist.load_game_state(request.forms.get("contentSelect"))
        cls.Tictocgame.setGameState(objectAccess[0],
                                    objectAccess[1],objectAccess[2],objectAccess[3],objectAccess[4])
        return UltimateTicTacToeGame.gamePage(cls.Tictocgame)


    def save(cls):
        Persist.store_game_state(cls.Tictocgame)
        # cls.session.get_users_in_session().split(",")[0],cls.session.get_users_in_session().split(",")[1])
        return UltimateTicTacToeGame.gamePage(cls.Tictocgame)

    def serve(self, fname):
        return static_file(fname, root='./html_page/')

    def halt(cls):
        sys.stderr.close()
        os.kill(os.getpid(), signal.SIGTERM)

    def restart(cls):
        cls.Tictocgame.setGameState([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
            ["NC","NC","NC","NC","NC","NC","NC","NC","NC"],"",'x',0)


        return UltimateTicTacToeGame.gamePage(cls.Tictocgame)
    def handle_next_move(self):
        index1 = int(request.query.index1)
        index2 = int(request.query.index2)
        user = request.query.user

        return self.next_move(index1,index2,user)


    @classmethod
    def saveUserPage(cls, username):
        """Send save_user request to users module with username and password as POST parameters.

        Returns:
            str: HTML page containing profile saving information from html construction module.
        """
        user_ip = request.environ.get('REMOTE_ADDR')
        user = User(username=username, client=user_ip)
        user.__save_user__()

        return f"user {username} is created!"

    @classmethod
    def loadUserPage(cls, username):
        """Send load_user request to users module with username as a parameter

        Args:
            username (str): The username of the user

        Returns:
            str: HTML page containing profile loading information from html construction module.
        """
        user = User(username=username)
        user.__load__user()
        return f"{username} Added to the game!"

    @classmethod
    def login_game(cls):
        """ Send login_game request to app_services module
            Returns:
            str: HTML page containing game page.
        """
        return UltimateTicTacToeGame.loginPage1()

    def login_user1(cls):
        """Authenticate a user profile by checking it in the database.

        Returns:
            The login page again if a username is invalid, otherwise the game page.
        """
        if Persist.verify_login(request.forms.get("username"), request.forms.get("password")):
            player1=User(request.forms.get("username"), request.forms.get("password"),"670.709.1.22")
            player1.save_user()
            cls.session.add_player(player1)

            return UltimateTicTacToeGame.loginPage2()
        else:
            return UltimateTicTacToeGame.loginPage1(cls, second_try=True)
    def login_user2(cls):
        """Authenticate a user profile by checking it in the database.

        Returns:
            The login page again if a username is invalid, otherwise the game page.
        """
        if Persist.verify_login(request.forms.get("username"), request.forms.get("password")):
            player2 = User(request.forms.get("username"), request.forms.get("password"),"123.123.0.19")
            player2.save_user()
            cls.session.add_player(player2)
            cls.Tictocgame.setGamePlayers(cls.session.get_users_in_session().split(",")[0],
                                          cls.session.get_users_in_session().split(",")[1])
            return cls.start_game()
        else:
            return UltimateTicTacToeGame.loginPage2(second_try=True)
    @classmethod
    def start_game(cls):
        """ Send start_game request to app_services module
            Returns:
            str: HTML page containing game page.
        """
        return UltimateTicTacToeGame.startPage()

    def begin_game(cls):
        """ Send start_game request to app_services module
            Returns:
            str: HTML page containing game page.
        """
        return UltimateTicTacToeGame.beginPage(cls)


    def registration_game(cls):
        """ Send start_game request to app_services module
            Returns:
            str: HTML page containing game page.
        """
        # app_services.start_game()
        return UltimateTicTacToeGame.registerPage()

    def register_user(self):
        """Register a user profile by storing it in the database.

        Returns:
            The registration page again if a username is invalid, otherwise the game page.
        """
        try:
            Persist.store_profile(request.forms.get("username"), request.forms.get("password"))
            return self.registration()
        except IOError:
            return UltimateTicTacToeGame.registerPage(second_try=True)

    @classmethod
    def logging_game(cls, state, database):
        """ Send logging request to app_services module
            Returns:
            str: HTML page containing game log info.
        """
        return "log info"

    @classmethod
    def play_game(cls):
        """ Send restart request to app_services module
            Returns:
            str: HTML page containing game log info.
        """
        return UltimateTicTacToeGame.gamePage(cls.Tictocgame)

    @classmethod
    def user_info_update(cls, username):
        """Send user_update request to users module with username as a parameter

        Args:
            username (str): The username of the user

        Returns:
            str: HTML page containing user updated information from html construction module.
        """

        user = User()
        user.update_username(username)
        return "user info updated"

    @classmethod
    def checkOtherPlayerMovePage(cls, state):
        """Send check_other_player_move request to game module with username as a parameter

        Args:
            username (str): The username of the user
            state (Array): The matrix of the game state

        Returns:
            str: HTML page containing information about whether the other player has moved.
        """
        return f"current state: {state}"

    def save_user(self, username):
        """Handler for saving a user profile."""
        return self.saveUserPage(username)

    def load_user(self, username):
        """Handler for loading a user profile."""

        return self.loadUserPage(username)

    def check_other_player_move(self, state):
        """Handler for checking the other player's move in the game.
            Args:
                state (Array): The matrix of the game state
        """

        return self.checkOtherPlayerMovePage(state)

    def next_move(cls, index1, index2, user):
        """Handler for the next move in the game.

        Args:
            index1 (int): The index of the row in the game grid.
            index2 (int): The index of the column in the game grid.
            user (str): The username of the user.

        Returns:
            str: HTML page containing information about the next move.
        """
        try:
            cls.Tictocgame.next_move(index1, index2, user)
        except ValueError as ve:
            # Handle the ValueError here
            error_message = str(ve)
            # You can choose to log the error, display a user-friendly message, or handle it as needed
            return UltimateTicTacToeGame.gamePage(cls.Tictocgame,"You made an illegal move")

        return UltimateTicTacToeGame.gamePage(cls.Tictocgame)


    def start(self):
        """Handler for starting the server."""
        return self.start_game()
    def begin(self):
        """Handler for starting the server."""
        return self.begin_game()

    def registration(self):
        """Handler for starting the server."""
        return self.registration_game()

    def logging(self,state, database):
        """Handler for logging into the game.
        Args:
            state (Array): The matrix of the game state
            Database (DB): The database to store the game

        """
        return self.logging_game(state, database)

    def play(self):
        """Handler for restarting the game."""
        return self.play_game()


    def user_update(self):
        """Handler for user update."""
        return self.user_info_update()


if __name__ == "__main__":
    server = TicTacToeServer()
    server.run(host="localhost", port=8080, debug=True)