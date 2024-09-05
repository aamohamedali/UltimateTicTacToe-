import sqlite3 as sql


con = sql.connect("database/project.db")
cur = con.cursor()
cur.execute(
    'CREATE TABLE IF NOT EXISTS "Profile" ("Username" TEXT, "Password" TEXT, "Wins" INTEGER, "Losses" INTEGER, "ID" INTEGER NOT NULL UNIQUE, PRIMARY KEY("ID" AUTOINCREMENT))')
cur.execute(
    'CREATE TABLE IF NOT EXISTS "GameState" ("GameState" TEXT, "GameStateU" TEXT, "NextGrid" TEXT, "NextPlayer" TEXT, "Outcome" TEXT, "Player1ID" INTEGER, "Player2ID" INTEGER, "ID" INTEGER NOT NULL UNIQUE, PRIMARY KEY("ID"), FOREIGN KEY("Player1ID") REFERENCES "Profile"("ID"), FOREIGN KEY("Player2ID") REFERENCES "Profile"("ID"))')
cur.close()


class Persist:
    """Persist class to store objects needed for game in peristance storage
    
    Methods:
        store_profile: Store a user profile
        load_profile: Load a user profile with username, wins, and losses
        destroy profile: Destroy a user profile and all related entities
        store_game_state: Store a game between two players
        load_game_state: Load a game between two players
        destroy_game_state: Destroy a stored game between two players
        add_win: Add a win stat to a user
        add_loss: add a loss stat to a user
        add_friend: Add a friend to a user's friend list
        remove_friend: Remove a friend from a user's friend 
        load_friends_list: Load a list of a user's friends
    """

    def store_profile(username, password):
        """Store a user profile. Stores their username and password.

        Args:
            username: A user's username
            password: A user's password

        Returns:
            True if the profile is successfully stored

        Raises:
            IOError if the profile cannot be saved (same username)
        """
        cur = con.cursor()
        inUseUsername = cur.execute(f"SELECT Username FROM Profile WHERE username='{username}'").fetchone()
        if inUseUsername:
            raise IOError("Username in use")
        cur.execute(
            f"INSERT INTO Profile(username, password, wins, losses) VALUES('{username}', '{password}', '{0}', '{0}')")
        con.commit()
        cur.close()
        return True

    def load_profile(username):
        """Loads a user profile. Does not return password!!!!!!
        
        Args:
            username: A user's username
            
        Returns:
            A tuple containing all relevant information to the user
            0 index is username
            1 index is wins
            2 index is losses

        Raises:
            IOError if the profile does not exist
        """
        cur = con.cursor()
        profileData = cur.execute(f"SELECT Username, Wins, Losses FROM Profile WHERE Username='{username}'").fetchone()
        if profileData is None:
            raise IOError("Username does not exist")
        cur.close()
        return profileData

    def destroy_profile(username):
        """Deletes a user profile from db. Note this deletes a username, 
        password, and any other entities associated with them.
        
        Args:
            username: The username of the profile we want to delete
            
        Returns:
            True if the profile is successfully deleted

        Raises:
            IOerror if the profile does not exist
        """
        cur = con.cursor()
        usernameID = cur.execute(f"SELECT ID FROM Profile WHERE Username = '{username}'").fetchone()
        if usernameID is None:
            raise IOError("Profile does not exist")
        usernameID = usernameID[0]
        cur.execute(f"DELETE FROM Profile WHERE ID='{usernameID}'")
        con.commit()
        cur.close()
        return True

    def update_username(oldUsername, newUsername):
        """Updates username in db.
        
        Args:
            oldUsername: The old username of the profile.
            newUsername: The new username for the profile.
            
        Returns:
            True if username is updated
            
        Raises:
            IOError if profile does not exist or username is taken
         """
        cur = con.cursor()
        usernameID = cur.execute(f"SELECT ID FROM Profile WHERE Username = '{oldUsername}'").fetchone()
        if usernameID is None:
            raise IOError("Profile does not exist")
        usernameID = usernameID[0]
        if cur.execute(f"SELECT ID FROM Profile WHERE Username = '{newUsername}'").fetchone() is not None:
            raise IOError("Username taken")
        cur.execute(f"UPDATE Profile SET Username='{newUsername}' WHERE ID = '{usernameID}'")
        con.commit()
        cur.close()
        return True

    def update_password(username, newPassword):
        """Updates password in db.
        
        Args:
            username: Username of prodile whose password we want to change
            newPassword: New password for profile
            
        Returns:
            True if password is successfully updated
        
        Raises:
            IOError if profile does not exist
        """
        cur = con.cursor()
        usernameID = cur.execute(f"SELECT ID FROM Profile WHERE Username = '{username}'").fetchone()
        if usernameID is None:
            raise IOError("Profile does not exist")
        usernameID = usernameID[0]
        cur.execute(f"UPDATE Profile SET Password='{newPassword}' WHERE ID = '{usernameID}'")
        con.commit()
        cur.close()
        return True
    
    def verify_login(username, password):
        """Verifies login credentials
        
        Args:
            username: Username of profile we want to verify
            password: Password of profile we want to verify
            
        Returns:
            True if login is successful
        """
        cur = con.cursor()
        profileData = cur.execute(f"SELECT Password FROM Profile WHERE Username='{username}'").fetchone()
        if profileData is None:
            return False
        if profileData[0] == password:
            return True
        return False
    
    def store_game_state(game_object):
        """Store a game if the players wish to pick it up again later

        Args:
            game_object: game object from app_logic.py
            username1: Player 1's username
            username2: Player 2's username

        Returns:
            True if game state is successfully stored

        Raises:
            IOError if usernames are invalid
        """
        cur = con.cursor()
        id1 = cur.execute(f"SELECT ID FROM Profile WHERE Username = '{game_object.getplayers()[0]}'").fetchone()
        if id1 is None:
            raise IOError("Username 1 is invalid")
        id1 = id1[0]
        id2 = cur.execute(f"SELECT ID FROM Profile WHERE Username = '{game_object.getplayers()[1]}'").fetchone()
        if id2 is None:
            raise IOError("Username 2 is invalid")
        id2 = id2[0]
        game_state_string = ""
        for row in game_object.state:
            for cell in row:
                game_state_string += cell
        game_ustate_string = ""
        for i in game_object.ustate:
            game_ustate_string += i + ","
        cur.execute(
            f"INSERT INTO GameState(GameState, GameStateU, NextGrid, NextPlayer, Outcome, Player1ID, Player2ID, ID)\
                  VALUES('{game_state_string}', '{game_ustate_string}', '{game_object.next_subgrid}', '{game_object.next_player}', '{game_object.outcome}', '{id1}', '{id2}', {game_object.gameId})")
        con.commit()
        cur.close()
        return True

    def load_game_state(gameID):
        """Load a game in progress between two player's

        Args:
            gameID: The ID of the game we want to load

        Returns:
            A List with the game data
            0 index is the game state as a 2D list
            1 index is the game ustate as a list
            2 index is the next grid as a string/int
            3 index is the next player as a string
            4 index is the outcome as a string/int
            5 index is the username of player 1
            6 index is the username of player 2

        Raises:
            IOError if there is no game state with ID
        """
        cur = con.cursor()
        ## Pull gamestate from DB
        data = cur.execute(
            f"SELECT GameState, GameStateU, NextGrid, NextPlayer, Outcome, Player1ID, Player2ID FROM GameState WHERE ID = '{gameID}'").fetchone()
        if data is None:
            raise IOError("No game state associated with given gameID")
        game_state_string = data[0]
        game_ustate_string = data[1]
        game_state = []
        for i in range(0, len(game_state_string), 9):
            row = []
            for j in game_state_string[i:i + 9]:
                row.append(j)
            game_state.append(row)
        game_ustate = game_ustate_string.split(",")
        game_ustate.pop(-1)
        complete_data = []
        complete_data.append(game_state)
        complete_data.append(game_ustate)
        for i in range(2, len(data)-2):
            complete_data.append(data[i])
        if complete_data[2] != "":
            complete_data[2] = int(complete_data[2])
        if complete_data[4] == "0":
            complete_data[4] = 0
        usernames = cur.execute(f"SELECT Username FROM Profile WHERE ID = '{data[5]}' OR ID = '{data[6]}'").fetchall()
        complete_data.append(usernames[0][0])
        complete_data.append(usernames[1][0])
        cur.close()
        return complete_data

    def destroy_game_state(username1, username2):
        """Destroy a stored game state
        
        Args:
            username1: Player 1's username
            username2: Player 2's username
            
        Returns:
            True if game state is successfully destroyed

        Raises:
            IOError if no gamestate exists associated with the users or users do not exist
        """
        ## Get IDs associated with usernames
        cur = con.cursor()
        id1 = cur.execute(f"SELECT ID FROM Profile WHERE Username = '{username1}'").fetchone()
        if id1 is None:
            raise IOError("Username 1 is invalid")
        id1 = id1[0]
        id2 = cur.execute(f"SELECT ID FROM Profile WHERE Username = '{username2}'").fetchone()
        if id2 is None:
            raise IOError("Username 2 is invalid")
        id2 = id2[0]
        ## Check if game state actually exists
        err = cur.execute(
            f"SELECT GameState FROM GameState WHERE Player1ID='{id1}' AND Player2ID='{id2}' OR Player1ID='{id2}' AND Player2ID='{id1}'").fetchone()
        if err is None:
            raise IOError("No game state associated with users")
        ## Delete game state
        cur.execute(
            f"DELETE FROM GameState WHERE Player1ID='{id1}' AND Player2ID='{id2}' OR Player1ID='{id2}' AND Player2ID='{id1}'").fetchone()
        cur.close()
        return True

    def add_win(username):
        """Adds a win to the username's win stat
        
        Args:
            username: username of player who's win stat is to be updated
            
        Returns:
            True if stat is successfully updated

        Raises:
            IOError if no profile associated with username
        """
        cur = con.cursor()
        usernameID = cur.execute(f"SELECT ID FROM Profile WHERE Username = '{username}'").fetchone()
        if not usernameID:
            raise IOError("Profile does not exist")
        usernameID = usernameID[0]
        wins = cur.execute(f"SELECT Wins FROM Profile WHERE ID = '{usernameID}'").fetchone()[0]
        wins += 1
        cur.execute(f"UPDATE Profile SET Wins='{wins}' WHERE ID = '{usernameID}'")
        con.commit()
        cur.close()
        return True

    def add_loss(username):
        """Adds a loss to the username's win stat
        
        Args:
            username: username of player who's loss stat is to be updated
            
        Returns:
            True if stat is successfully updated

        Raises:
            IOError if no profile associated with username
        """
        cur = con.cursor()
        usernameID = cur.execute(f"SELECT ID FROM Profile WHERE Username = '{username}'").fetchone()
        if not usernameID:
            raise IOError("Profile does not exist")
        usernameID = usernameID[0]
        losses = cur.execute(f"SELECT Losses FROM Profile WHERE ID = '{usernameID}'").fetchone()[0]
        losses += 1
        cur.execute(f"UPDATE Profile SET Losses='{losses}' WHERE ID = '{usernameID}'")
        con.commit()
        cur.close()
        return True

    def add_friend(username1, username2):
        """Adds each username to the other's friendslist
        
        Args:
            username1: username of one friend
            username2: username of other friend
            
        Returns:
            True if friendship is successfully added
            
        Raises:
            IOError if either username does not have a profile associated with it
        """
        return False

    def remove_friend(username1, username2):
        """Removes each player from eachhother's friendslist
        
        Args:
            username1: username of one friend
            username2: username of other friend
            
        Returns:
            True if friendship is successfully removed
            
        Raises:
            IOError if either username does not have a profile associated with it
        """
        return False

    def load_friends_list(username):
        """Returns the friends list of the given user
        
        Args:
            username: username of profile of friends list we want
            
        Returns:
            tuple containing the usernames of the friends
            
        Raises:
            IOError if username is not associated with a profile
        """
        return ("example")