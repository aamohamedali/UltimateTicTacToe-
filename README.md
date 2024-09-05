## Team A Project

### Current Functionaliy
Currently it is possible to start the webserver, and be brought to a start page. Clicking start game brings the user to an empty ultimate tic tac toe grid. While all modules are implemented, the team has had difficulty combining the different components, especially with regards to user interaction with the game. For now, the user and session management module, logic module, and database module are not being used however they are imlpemented and ready to be used as soon as the issue is figured out. 

### To run unit tests
All unit tests are stored under the tests directory and are named for their respective module.
 
### To start webserver
Run python ServerAPI/serverAPI.py from root directory

### Documents
The docs folder contains documents for the entire project. The complete UML diagram is stored here as well as the individual components UML diagrams. An overview of each module as well as their individual UML diagrams are stored in their respective subdirectories within docs. The meeting notes are also found here as well as documentation for code reviews.

### Logic
For  logics, At this point i beleive i don't really need an app service module. My Team mates told me to leave the stub implementation rather than deleting. Therefore,I did  commented all the test cases for the app service module.

### User and Session
The user module represents a game user in each tic tac toe game. It has the required functionality for sprint 1, however we plan on adding to that in sprint 2.
The session management module is completed for sprint 1, however the implementation may change in sprint 2, depending on feedback from professor.

### Database
The database to store user profiles and gamestates is a standard SQLite database.
To run unitests for databases: \
From the root directory run:\
 python -m unittest tests.store_tests\
It is important to run this from the root as there is currently a bug where the database cannot be accessed properly unless code is run from the root. This will be resolved in sprint 2.
