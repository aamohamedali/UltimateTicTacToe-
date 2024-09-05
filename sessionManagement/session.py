"""Tic Tac Toe Game session implementation, including a session class for keeping track of players in a game

Classes:
    Session - a game session instance
"""
import random

from userInfo.users import User

class Session:
    """A game session for tic-tac-toe match between two players

        Attributes:
            players (dict): Dictionary of users and respective clients in session.
            session_id (int): id for game session, matched with a Game object.

        Methods:
            terminate_session(): terminate the session
            add_player(player): add a player to the game session.
            remove_player(): remove a player from the game session.
            get_session_info(): return the sessions info.
            get_users_in_session(): return the usernames of users in a session.

        Special Methods:
            __validate_session__(): validate the session is active.
        """

    def __init__(self):
        """Creates an empty game session.

        Args:
            game_id(int): id for game session, matched with a Game.

        """
        self.players = {}
        self.session_id = random.randint(0,10000)

    def terminate_session(self):
        """End a game session.

        Returns:
            bool: True if game session ended successfully, False otherwise.

        Raises:
            ValueError: if the function is called on an invalid session.

        """
        try:
            if self.__validate_session__():
                self.players.clear()
                self.session_id = None
                return True
            else:
                raise ValueError("Invalid Session")
        except ValueError:
            raise ValueError("Invalid Session")

    def add_player(self, user):
        """Removes a player from the game.

        Args:
            user (User): a user in the current session.

        Returns:
            bool: True if player successfully added to the session.

        Raises:
            ValueError: if the session is full or session invalid.

        """
        try:
            if self.__validate_session__() and user not in self.players:
                if len(self.players) == 2:
                    raise ValueError("Game session is full")
                self.players[user] = user.client
                return True
            else:
                raise ValueError("Invalid session")
        except ValueError as e:
            raise ValueError(e)

    def remove_player(self, user):
        """Removes a player from the game, terminates game if removing the last player in the session.

        Args:
            user (User): a user in the current session.

        Returns:
            bool: True if player successfully removed.

        Raises:
            ValueError: if the player is not in the game session, or if removing leaves no players in Session.

        """
        try:
            if self.__validate_session__() and user in self.players:
                del self.players[user]
                if len(self.players) == 0:
                    self.terminate_session()
                return True
            else:
                raise ValueError("Player not in game session")
        except ValueError as e:
            raise ValueError(e)

    def get_session_info(self):
        """Gets the information about the current session.

        Returns:
            str: session id, along with each users name and client.

        Raises:
            IOError: if the function is called on an invalid session.

        """
        try:
            if self.session_id is None:
                raise IOError("Error getting session info - session doesnt exist.")
            else:
                if self.__validate_session__():
                    user_info = ", ".join(
                        f"User: {user.username}, Client: {user.client}" for user, client in self.players.items())
                    return f"Session ID: {self.session_id} | {user_info}"
        except IOError as e:
            raise IOError(e)

    def get_users_in_session(self):
        """Gets the usernames of the Users in a session.

        Returns:
            str: Each username, seperated by a comma.

        Raises:
            IOError: if the function is called on an invalid session.

        """
        try:
            if self.session_id is None:
                raise IOError("Error getting user info from session - session doesnt exist.")
            if self.__validate_session__():
                users_info = ", ".join(f"{user.username}" for user in self.players)
                return users_info
        except IOError as e:
            raise IOError(e)


    def __validate_session__(self):
        """Validates an in progress session. Checks that a session has an id.

        """
        return bool(self.session_id)
