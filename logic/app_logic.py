
class Game():
    """
    A class for ultimate tictactoe game
    it has a 3D matrix as instance variable where each list represent a subgrid.
    it also has a list of subgrid as instance variable, when a subgrid is won by a player it is claimed in this list.
    it also has a next player instance variable, which store the player who has to play next.
    it also has a outcome instance variable, where holds to be zero while playing the game and if a player wins it turns to 1.
    which helps to make sure there is no any move afterwards.
    There is couple of methods to manipulate the  game object
    """
    def __init__(self, game_id,player1="Player1",player2="Player2"):
        self.state = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        self.ustate = ["NC","NC","NC","NC","NC","NC","NC","NC","NC"]
        self.next_subgrid = ""
        self.next_player = 'x'
        self.outcome=0 #'x' or 'o '-winner & 0= pending
        self.gameId=game_id
        self.username1=player1
        self.username2=player2

    def getPlayers(self):
        """
        get the name of the players
        :return:
        """
        return [self.username1,self.username2]

    def setGamePlayers(self,player1,player2):
        """
        change the usernames of the player
        :param player1: first player
        :param player2: second player
        :return:
        """
        self.username1 = player1
        self.username2 = player2



    def getGameState(self):
        """
        get method to read the matrix of the game and the list of the status of the subgrid's
        :return: a list containing the matrix of the game and list of the status of the subgrid's
        """
        return [self.state,self.ustate]

    def setGameState(self,matrix,list,nextgrid,nextplayer,outcome):
        """
        set method to replace the state of the game with new matrix and replace the list of the status of the subgrid's
        :param matrix: the state of the game to be replaced
        :param list: the list of the status of the subgrid's to be replaced
        :return: n/a
        """
        self.state = matrix
        self.ustate = list
        self.next_subgrid=nextgrid
        self.next_player=nextplayer
        self.outcome=outcome


    def next_move(self, index1,index2,user):
        """
         A method to implement the next move, validating the move and print invalid move if it is an illegal move
        ,assign who is the next player who can make the move, assign which is the next subgrid that the player can play ,
        check if it satisfies the winning condition after the move and examine whether a winner can be determined

        :param index1: index of the subgrid playing
        :param index2: index of the position in the subgrid
        :param user: whose playing the move either x or o
        :return: n/a
        """
        if self._validate(index1, index2,user):
            if user == "x":
                self.state[index1][index2] = "x"
                self.next_player = "o"
            else:
                self.state[index1][index2] = 'o'
                self.next_player = "x"
            self.next_subgrid = index2
            self.winning_condition(index1,user)
            self.refree()
        else:
            raise ValueError("Illegal move")


    def winning_condition(self,index1,user):

        """
        check whether the matrix satisfies any winning condition, if it satisfies present a winner for the subgrid

        :param index1: index of the subgrid that we are looking for the winning condition
        :param user: who made the move before checking the winning condition

        :return: n/a
        """

        if self.state[index1][0] != " " and self.state[index1][0] == self.state[index1][1] and self.state[index1][1] == self.state[index1][2]:
            self.subgrid_win(index1,user)
        elif self.state[index1][3] != " " and self.state[index1][3] == self.state[index1][4] and self.state[index1][4] == self.state[index1][5]:
            self.subgrid_win(index1,user)
        elif self.state[index1][6] != " " and self.state[index1][6] == self.state[index1][7] and self.state[index1][7] == self.state[index1][8]:
            self.subgrid_win(index1,user)
        elif self.state[index1][0] != " " and self.state[index1][0] == self.state[index1][3] and self.state[index1][3] == self.state[index1][6]:
            self.subgrid_win(index1,user)
        elif self.state[index1][1] != " " and self.state[index1][1] == self.state[index1][4] and self.state[index1][4] == self.state[index1][7]:
            self.subgrid_win(index1,user)
        elif self.state[index1][2] != " " and self.state[index1][2] == self.state[index1][5] and self.state[index1][5] == self.state[index1][8]:
            self.subgrid_win(index1,user)
        elif self.state[index1][0] != " " and self.state[index1][0] == self.state[index1][4] and self.state[index1][4] == self.state[index1][8]:
            self.subgrid_win(index1,user)
        elif self.state[index1][2] != " " and self.state[index1][2] == self.state[index1][4] and self.state[index1][4] == self.state[index1][6]:
            self.subgrid_win(index1,user)


    def subgrid_win(self,index1,user):

        """
        present a winner for the subgrid and reset all the subgrid position as the winner move
        :param index1: index of the subgrid that is won
        :param user: who is the winner either x or o
        :return: n/a
        """
        self.ustate[index1] = user
        for element in range(len(self.state[0])):
            self.state[index1][element]=user



    def refree(self):
        """
        check all the subgrid for winning condition to present the ultimate winner
        if one of the condition is satisfied declare the winner by printing and changing the outcome instance variable from 0 to 1
        :param: n/a
        :return: n/a
        """
        if self.ustate[0] != "NC" and self.ustate[0] == self.ustate[1] and self.ustate[1] == self.ustate[2]:
            print(f"winner is {self.ustate[0]}")
            self.outcome=self.ustate[0]
        elif self.ustate[3] != "NC" and self.ustate[3] == self.ustate[4] and self.ustate[4] == self.ustate[5]:
            print(f"winner is {self.ustate[3]}")
            self.outcome = self.ustate[3]
        elif self.ustate[6] != "NC" and self.ustate[6] == self.ustate[7] and self.ustate[7] == self.ustate[8]:
            print(f"winner is {self.ustate[6]}")
            self.outcome = self.ustate[6]

        elif self.ustate[0] != "NC" and self.ustate[0] == self.ustate[3] and self.ustate[3] == self.ustate[6]:
            print(f"winner is {self.ustate[0]}")
            self.outcome = self.ustate[0]
        elif self.ustate[1] != "NC" and self.ustate[1] == self.ustate[4] and self.ustate[4] == self.ustate[7]:
            print(f"winner is {self.ustate[1]}")
            self.outcome = self.ustate[1]
        elif self.ustate[2] != "NC" and self.ustate[2] == self.ustate[5] and self.ustate[5] == self.ustate[8]:
            print(f"winner is {self.ustate[2]}")
            self.outcome = self.ustate[2]

        elif self.ustate[0] != "NC" and self.ustate[0] == self.ustate[4] and self.ustate[4] == self.ustate[8]:
            print(f"winner is {self.ustate[0]}")
            self.outcome = self.ustate[0]
        elif self.ustate[2] != "NC" and self.ustate[2] == self.ustate[4] and self.ustate[4] == self.ustate[6]:
            print(f"winner is {self.ustate[2]}")
            self.outcome = self.ustate[2]


    def _validate(self, index1 ,index2,user):
        """
        validate each move the player makes,
        check whether the box is empty,
        check if the players is playing in an unclaimed subgrid (not in a won grid),
        check if he plays in correct grid regards to the previous move,
        check if the correct player is playing regards to the previous player
        check if the winner is already determined

        if the next subgrid to play is already won by a player, the current player has the freedom to choose any remaining subgrid

        :param index1: the subgrid that we are validating
        :param index2: the position in the subgrid that we are validating
        :param user: the player either x or o
        :return: either True or False
        """
        if self.next_subgrid != "": #if the next subgrid is won by a player and cannot make a move on it, therefore choosing any remaining subgrids
            if self.ustate[self.next_subgrid] != "NC":
                self.next_subgrid = ""
        if (self.ustate[index1] == "NC" and (self.next_subgrid == index1 or self.next_subgrid == "") and self.next_player == user) and self.outcome == 0:
            if self.state[index1][index2] == " ":
                return True
            else:
                return False
        else:
            return False
    def __str__(self):
        result = ""
        for row in self.state:
            result += ' '.join(row) + '\n'
        return result


#-------------------------------------------------
#-------------------------------------------------

#Playing the Game

# y=Game()
# y.next_move(0,1,"x")
# y.next_move(1,0,"o")
# y.next_move(0,2,"x")
# y.next_move(2,0,"o")
# y.next_move(0,0,"x")
#
# y.next_move(8,1,'o')
# y.next_move(1,3,'x')
# y.next_move(3,1,"o")
# y.next_move(1,4,'x')
# y.next_move(4,1,'o')
# y.next_move(1,5,"x")
#
# y.next_move(5,2,"o")
# y.next_move(2,6,'x')
# y.next_move(6,2,"o")
# y.next_move(2,7,'x')
# y.next_move(7,2,'o')
# y.next_move(2,5,"x")
#
# y.next_move(5,3,"o")
#
#
#
# y.next_move(3,4,'x')
# y.next_move(4,2,'o')
# y.next_move(2,8,'x')
# print(y)
