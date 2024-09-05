# Store Module

This module is implementing a SQLite3 database system. This is implemented through the use of the Persist class. The Persist class consists solely of static methods, as there is no reason to instantiate a class whose sole purpose is to manage persistant storage. It contains functionality for managing user profiles, game states, and friends lists.\
Note that not all features listed here are fully implemented as of the end of sprint 1.\
[UML diagram](arch_store_UML_diagram.pdf) \
[Entity Relationship Diagram](arch_store_entity_relationship_diagram.pdf)

## User Profiles

The managing of user profiles is done through the use of 3 methods. store_profile stores the user profile, load_profile loads the user profile from storage, and destroy_profile removes the user profile from storage permanantly. In addition to this, each user profile contains an attribute for wins and losses. There are two methods, add_win and add_loss, to increment these respectively. In addition there are also methods to update username and update password.

## Game Sessions

The mananaging of game sessions is done through the use of 3 methods. store_game_state stores the 2D list game state as a single concatenated string, load_game_state loads this string as a 2D list so it can be used by the logic module, and destroy_game_state removes a game state from storage permantly.

## Friends List

The managing of friends lists is done through the use of 3 methods. add_friend adds a friend to each of the argument user's friends list, remove_friend removes a friend from each of the argument user's friends list, load_friends_list returns a tuple of all of the friends of a user.