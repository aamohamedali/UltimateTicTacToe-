# User Info Module
The updated userInfo module now implements just a User Class in the users.py file. The functionality has been reduced to the core needs of a User.
It now provides public user methods for updating a users name,password and users history.
update_username, which updates the calling Users username attribute and calls on the database module to update the users name in the database.
update_password, which updates the calling Users password attribute and calls on the database module to update the users password in the database.
update_user_history, that adds a win or loss to the calling Users history attribute, and wins or losses attribute and once again calls on the database module to update the Users info in the database.
A public method is also provided to display a users game history, providing a string showing the total games played, wins, losses and overall win/ratio.
There are also private methods: __save_user__, that saves a user to the database using the database module and __load_user__, which has planned functionality
for Sprint 2, which will load previously saved user information. The __load_user__ method may become a public method as the project progresses in Sprint 2. 
Some planned functionality that may be implemented along with the __load_user__ function is to implement a friends list for a User.


# Session Management Module
The updated sessionManagement module still implements a single Session class in the session.py file. The Session class represents a single
game session, where only 2 users can be present, it keeps track of the users in the session as well as the user client ids via a dictionary, it also generates a session id for each session. 
There are 4 public methods in the class, terminate_session, add_player, remove_player and get_session_info. 
terminate_session removes all users from the game session, and deletes the session instance. add_player adds a user object to the
session, only if there is a slot available to join. remove_player removes a user from the session, and if that leaves 0 users in the session, terminates the session.
get_session_info returns a string detailing the current session_id and the players in the session. There are also two private methods, __validate_session__ and __generate_id__.
__validate_session__ validates an active game session, checking that the session has a valid game id. __generate_id__ generates an id for a game session instance,
This is not a complete implementation and in sprint 2 I will look to add functionality to broaden the utility of the Session class. I will also look to generate a unique
session id.

# UML Diagram
Below is a UML diagram representing the planned organization and interaction of both modules. This is version 1 of the
diagram and implementation is likely to change.
[UML diagram](arch_user_UMLDiagram_sprint1.png) 