"""Tic Tac Toe Game user implementation, including a user class for storing user information.

Classes:
    User - a User instance.
"""
from database.store import Persist
import re


class User:
    """Game user, identified with username and password.

    Attributes:
        username (str): username for individual user, set to none unless argument provided.
        password (str): password for individual user, set to none until user updates.
        client (str): client id for individual user, set to none unless argument provided.
        history (list): list of user game history, in order, wins and losses added as user plays games.
        wins (int): number of wins.
        losses (int): number of losses.

    Methods:
        update_username(new_user): updates a users name.
        update_password(new_password): updates a users password.
        update_history(): updates a users game history.
        user_history(): displays a users game history, along with win/loss.
        verify_user_login(user): check if provided credentials can be used to log in.
        save_user(): saves user info to database.
        load_user(): loads user info from database.


    """

    def __init__(self, username=None, password=None, client=None):
        """Creates a user object instance.

        Args:
            username (str): username for individual, defaults to None if no argument provided.
            password (str): password for individual, defaults to None if no argument provided.
            client (str): client id for user, associated with players ip, defaults to None if no argument provided.

        """
        self.username = username
        self.password = password
        self.client = client
        self.history = []
        self.wins = 0
        self.losses = 0

    def update_username(self, new_username):
        """Update the username for a  user object instance, only updates locally.

        Args:
            new_username (str): A username defined by user.

        Return:
            bool: True if name updated and successfully stored.

        Raises:
            ValueError: if new username is not a valid string.

        """
        valid_user = re.compile(r'^[A-Za-z\d]{1,15}$')
        try:
            if new_username is None:
                raise ValueError("Username cannot be empty")
            if not valid_user.match(new_username):
                raise ValueError("Username must be 1-15 alphanumerical characters")
            else:
                self.username = new_username
                return True
        except ValueError as e:
            raise ValueError(e)
        except IOError as e:
            raise IOError(e)

    def update_password(self, new_password):
        """Update the password for a  user object instance, only updates locally.

        Args:
            new_password (str): A username defined by user.

        Return:
            bool: True if pass updated and successfully stored.

        Raises:
            ValueError: if new password is not a valid string.

        """
        valid_pass = re.compile(r'^[A-Za-z\d]{5,15}$')
        try:
            if new_password is None:
                raise ValueError("Password cannot be empty")
            if not valid_pass.match(new_password):
                raise ValueError("Password must be 5-15 alphanumerical characters")
            else:
                self.password = new_password
                return True
        except ValueError as e:
            raise ValueError(e)
        except IOError as e:
            raise IOError(e)

    def update_user_history(self, result):
        """Updates the users history after completing a game.

        Args:
            result (str): Either "W" or "L" for win or loss.

        Raises:
            ValueError: if result is not "W" or "L".

        """
        try:
            if result == 'W':
                self.history.append(result)
                self.wins += 1
            elif result == 'L':
                self.history.append(result)
                self.losses += 1
            else:
                raise ValueError("Invalid game result")
        except (ValueError, IOError) as e:
            raise e

    def user_history(self):
        """Display a users game history.

        Returns:
            history (str): A string showing total wins, losses, games played and overall win/loss.

        Raises:
            ValueError: If user history doesn't exist.

        """
        try:
            length = len(self.history)
            if length == 0:
                raise ValueError("User History is empty.")
            else:
                if self.wins > 0 and self.losses == 0:
                    ratio = self.wins
                else:
                    ratio = self.wins / self.losses
            return f"Total Games Played: {length}, Wins: {self.wins}, Losses: {self.losses}, Win/Loss Ratio: {ratio:.2f}"
        except ValueError as e:
            raise ValueError(e)


    def verify_user_login(username, password):
        """Checks if user is in database and can log in.

        Args:
            username (str): Username to check if user in database.
            password (str): Password for username given.

        Returns:
            True: if user information is in database and can log in.

        Raises:
            IOError: if user information has not been previously saved to database.

        """
        try:
            if Persist.verify_login(username, password):
                print("User can be logged in")
                return True
            else:
                raise IOError("Profile does not exist, create a user profile first")
        except IOError as e:
            raise e

    def save_user(self):
        """Saves user info to database.

        Returns:
            bool: True if user successfully saved to database.

        Raises:
            IOError: if user not saved to database.

        """
        try:
            if Persist.verify_login(self.username, self.password):
                database_profile = Persist.load_profile(self.username)
                if database_profile[1] == self.wins and database_profile[2] == self.losses: #Check if data is up to date
                    return True
                if database_profile[1] != self.wins: #wins stored in local user will be more than in database
                    diff = self.wins - database_profile[1]
                    for i in range(diff):
                        Persist.add_win(self.username)
                if database_profile[2] != self.losses:
                    diff = self.losses-database_profile[2]
                    for i in range(diff):
                        Persist.add_loss(self.username)
                return True
            else:
                Persist.store_profile(self.username, self.password) #Profile isn't in database
                for result in self.history:
                    if result == 'W':
                        Persist.add_win(self.username)
                    if result == 'L':
                        Persist.add_loss(self.username)
                return True
        except IOError as e:
            raise e

    def load_user(username):
        """Loads user info from database.

        Returns:
            user: Returns a new user object with previously stored info.

        Raises:
            IOError: if unable to load user information.

        """
        try:
            profile_info = Persist.load_profile(username)
            if profile_info:
                Persist.destroy_profile(username) #have to do this bc cannot save a profile with existing username
                new_user = User()
                new_user.username = profile_info[0]
                new_user.wins = profile_info[1]
                new_user.losses = profile_info[2]
                for i in range(new_user.wins):
                    new_user.history.append('W')
                for i in range(new_user.losses):
                    new_user.history.append('L')
                return new_user
            else:
                raise IOError("Unable to load user information from database")
        except IOError as e:
            raise e