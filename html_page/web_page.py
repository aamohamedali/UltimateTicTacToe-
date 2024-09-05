

class UltimateTicTacToeGame:

    def loadGamepage(cls):
        html_content="""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Content Loader</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 50px auto;
        }
        select {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Select Content to Load</h1>
        <form action="load_game" method="POST">
            <select id="contentSelect" name="content">
                <option value="content1">Content 1</option>
                <option value="content2">Content 2</option>
                <option value="content3">Content 3</option>
                <option value="content1">Content 4</option>
                <option value="content1">Content 5</option>
                <option value="content1">Content 6</option>
                <option value="content1">Content 7</option>
                <option value="content1">Content 8</option>
                <option value="content1">Content 9</option>
                <option value="content1">Content 10</option>
            </select>
            <button type="submit">Load Content</button>
        </form>
        
    </div>
</body>
</html>
"""
        return html_content

    @classmethod
    def startPage(cls):
        """
        Returns the HTML code for the start page of the Ultimate Tic-Tac-Toe game.

        Returns:
            str: The HTML code for the start page.
        """
        start_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Tic-Tac-Toe - Start Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 30px;
        }
        button {
            padding: 15px 30px;
            font-size: 18px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Ultimate Tic-Tac-Toe!</h1>
        <button onclick="window.location.href='playing'">Start Game</button>
        <button onclick="window.location.href='load_gamepage'">Load Game</button>
    </div>
</body>
</html>"""
        return start_page_html

    def beginPage(cls):
        """
        Returns the HTML code for the start page of the Ultimate Tic-Tac-Toe game.

        Returns:
            str: The HTML code for the start page.
        """
        first_page__html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Tic-Tac-Toe</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            max-width: 600px;
            margin: 100px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
            line-height: 1.5;
            margin-bottom: 30px;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.3s ease-in-out;
        }
        .btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Ultimate Tic-Tac-Toe</h1>
        <p>Ultimate Tic-Tac-Toe is an exciting twist on the classic game of Tic-Tac-Toe, offering a strategic challenge for players of all ages.</p>
        <a href="registration" class="btn">Register Now</a>
        <a href="login" class="btn">Login</a>
    </div>
</body>
</html>
"""
        return first_page__html
    

        
    @classmethod
    def gamePage(cls,gameobject,message=""):
        """
        Returns the HTML code for the game page of the Ultimate Tic-Tac-Toe game.

        Returns:
            str: The HTML code for the game page.
    """
        if gameobject.outcome != 0:
            return cls.win_page(cls,gameobject)
        else:
            html_code1='''
    <style>
        body {
            margin: 0;
            background-color: #1d1b52;
            font-family: Arial, sans-serif;
        }
    
        .little_table.live,
        .big_table.live {
            border: 1px solid #21d6ff;
        }
    
        .little_table td {
            border: 1px solid #000;
            background-color: #15a870;
            cursor: pointer;
            text-align: center;
            padding: 0; /* Add this line to remove padding */
        }
    
        .little_table td button {
        width: 100px;
        height: 100px;
        border: none;
        background-color: inherit;
        cursor: pointer;
        font-size: 36px;
        font-weight: bold; /* Add this line to make the font bold */
        }
        .little_table td button:hover {
        background-color: #FFFFFF;
        transform: scale(1.2);
        }
        
        .little_table td button:active {
        background-color: yellow; /* Change the background color when pressed */
         /* Scale the button when pressed */
        }
    
    
        .big_table {
            border: 1px solid transparent;
            margin: 0 auto 20px;
            width: 700px;
            height: 700px;
        }
        
         .col-1_row-1 {
            border: 2px solid yellow; /* Set border width and color */
        }
        
        .little_table {
            border: 1px solid transparent;
            width: 100%;
            height: 100%;
        }
    
        td.red {
            background-color: #bd0835;
        }
    
        td.blue {
            background-color: #0b0b9b;
        }
    
        .little_table td.filled {
            cursor: pointer;
        }
    
        .blue {
            color: #010021;
        }
    
        .red {
            color: #260000;
        }
    
        div.marker {
            margin: auto;
            height: 100%;
            width: 100%;
            border-radius: 100%;
        }
    
        #turn {
            width: 560px;
            margin: auto;
            box-shadow: 0 0 5px 5px #0A0A0A;
            text-align: center;
            padding: 20px;
            font-size: 40px;
            text-shadow: 1px 1px 2px #ffffff;
            color: #21d6ff;
        }
    
        #newGame {
            width: 200px;
            margin: auto;
            font-size: 24px;
            padding: 10px 20px;
            text-align: center;
            box-shadow: 0 0 5px 5px #0A0A0A;
            background-color: #08A300;
            color: #056900;
            border: none;
            display: block;
            cursor: pointer;
            margin-top: 20px;
        }
        .panel {
            position: fixed;
            top: 20%;
            right: 10px;
            transform: translateY(-50%);
            background-color: #2980b9; /* Dark blue */
            color: #FFFFFF; /* Set font color to white */
            border: 2px solid #2980b9; /* Blue */
            border-radius: 10px;
            padding: 20px;
            z-index: 1000; /* Ensure panel appears above other elements */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Add shadow */
            width: 200px; /* Set width */
        }

        /* Style for the buttons inside the panel */
        .panel button {
            display: block;
            width: 100%;
            margin-bottom: 10px;
            margin-right: 60px;
            background-color: #3498db; /* Light blue */
            color: #fff; /* White text */
            border: none;
            padding: 10px 20px;
            text-align: center;
            font-size: 18px; /* Decrease font size */
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s ease; /* Smooth transition */
        }

        .panel button:hover {
            background-color: #2980b9; /* Darker blue on hover */
        }
        
        .panel button:last-child {
            margin-bottom: 0;
        }
        .game-container {
            margin-right: 260px; /* Adjust to leave space for the panel */
            padding: 20px; /* Add padding to separate from panel */
        }
        
    </style>
    '''

            html_code2 = '''
            <body>
                
                 <div class="panel">
                    <p style="font-weight: bold";>INSTRUCTION</p>
                    <p>{user1}'s  move</p>
                    <p> Your move could  be played {nsubgrid}</p>
                    <p style="color: black;font-weight: bold;">{error}</p>
                    <button onclick="window.location.href='halt'">Stop</button>
                    <button onclick="window.location.href='save_game'">Save game</button>
                    <button onclick="window.location.href='restart_game'">Restart game</button>
                </div>
                <div class="game-container">
                    <table class="big_table live">
                        <tr class="1">
                            <td class="1">
                                <table class="little_table col-1_row-1">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=0&index2=0&user={user}'"> {matrix[0][0]} </button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=0&index2=1&user={user}'"> {matrix[0][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=0&index2=2&user={user}'"> {matrix[0][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=0&index2=3&user={user}'"> {matrix[0][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=0&index2=4&user={user}'"> {matrix[0][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=0&index2=5&user={user}'"> {matrix[0][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=0&index2=6&user={user}'"> {matrix[0][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=0&index2=7&user={user}'"> {matrix[0][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=0&index2=8&user={user}'"> {matrix[0][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="2">
                                <table class="little_table col-2 row-1">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=1&index2=0&user={user}'"> {matrix[1][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=1&index2=1&user={user}'"> {matrix[1][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=1&index2=2&user={user}'"> {matrix[1][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=1&index2=3&user={user}'"> {matrix[1][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=1&index2=4&user={user}'"> {matrix[1][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=1&index2=5&user={user}'"> {matrix[1][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=1&index2=6&user={user}'"> {matrix[1][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=1&index2=7&user={user}'"> {matrix[1][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=1&index2=8&user={user}'"> {matrix[1][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="3">
                                <table class="little_table col-3 row-1">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=2&index2=0&user={user}'">{matrix[2][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=2&index2=1&user={user}'">{matrix[2][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=2&index2=2&user={user}'">{matrix[2][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=2&index2=3&user={user}'">{matrix[2][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=2&index2=4&user={user}'">{matrix[2][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=2&index2=5&user={user}'">{matrix[2][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=2&index2=6&user={user}'">{matrix[2][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=2&index2=7&user={user}'">{matrix[2][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=2&index2=8&user={user}'">{matrix[2][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr class="2">
                            <td class="1">
                                <table class="little_table col-1 row-2">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=3&index2=0&user={user}'">{matrix[3][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=3&index2=1&user={user}'">{matrix[3][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=3&index2=2&user={user}'">{matrix[3][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=3&index2=3&user={user}'">{matrix[3][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=3&index2=4&user={user}'">{matrix[3][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=3&index2=5&user={user}'">{matrix[3][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=3&index2=6&user={user}'">{matrix[3][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=3&index2=7&user={user}'">{matrix[3][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=3&index2=8&user={user}'">{matrix[3][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="2">
                                <table class="little_table col-2 row-2">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=4&index2=0&user={user}'">{matrix[4][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=4&index2=1&user={user}'">{matrix[4][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=4&index2=2&user={user}'">{matrix[4][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=4&index2=3&user={user}'">{matrix[4][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=4&index2=4&user={user}'">{matrix[4][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=4&index2=5&user={user}'">{matrix[4][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=4&index2=6&user={user}'">{matrix[4][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=4&index2=7&user={user}'">{matrix[4][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=4&index2=8&user={user}'">{matrix[4][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="3">
                                <table class="little_table col-3 row-2">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=5&index2=0&user={user}'">{matrix[5][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=5&index2=1&user={user}'">{matrix[5][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=5&index2=2&user={user}'">{matrix[5][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=5&index2=3&user={user}'">{matrix[5][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=5&index2=4&user={user}'">{matrix[5][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=5&index2=5&user={user}'">{matrix[5][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=5&index2=6&user={user}'">{matrix[5][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=5&index2=7&user={user}'">{matrix[5][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=5&index2=8&user={user}'">{matrix[5][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr class="3">
                            <td class="1">
                                <table class="little_table col-1 row-3">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=6&index2=0&user={user}'">{matrix[6][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=6&index2=1&user={user}'">{matrix[6][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=6&index2=2&user={user}'">{matrix[6][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=6&index2=3&user={user}'">{matrix[6][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=6&index2=4&user={user}'">{matrix[6][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=6&index2=5&user={user}'">{matrix[6][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=6&index2=6&user={user}'">{matrix[6][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=6&index2=7&user={user}'">{matrix[6][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=6&index2=8&user={user}'">{matrix[6][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="2">
                                <table class="little_table col-2 row-3">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=7&index2=0&user={user}'">{matrix[7][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=7&index2=1&user={user}'">{matrix[7][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=7&index2=2&user={user}'">{matrix[7][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=7&index2=3&user={user}'">{matrix[7][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=7&index2=4&user={user}'">{matrix[7][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=7&index2=5&user={user}'">{matrix[7][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=7&index2=6&user={user}'">{matrix[7][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=7&index2=7&user={user}'">{matrix[7][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=7&index2=8&user={user}'">{matrix[7][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                            <td class="3">
                                <table class="little_table col-3 row-3">
                                    <tr class="1">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=8&index2=0&user={user}'">{matrix[8][0]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=8&index2=1&user={user}'">{matrix[8][1]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=8&index2=2&user={user}'">{matrix[8][2]}</button></td>
                                    </tr>
                                    <tr class="2">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=8&index2=3&user={user}'">{matrix[8][3]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=8&index2=4&user={user}'">{matrix[8][4]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=8&index2=5&user={user}'">{matrix[8][5]}</button></td>
                                    </tr>
                                    <tr class="3">
                                        <td class="1"><button onclick="window.location.href='next_move?index1=8&index2=6&user={user}'">{matrix[8][6]}</button></td>
                                        <td class="2"><button onclick="window.location.href='next_move?index1=8&index2=7&user={user}'">{matrix[8][7]}</button></td>
                                        <td class="3"><button onclick="window.location.href='next_move?index1=8&index2=8&user={user}'">{matrix[8][8]}</button></td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </div>
                
            </body>
                '''
            if gameobject.next_player=="x":
                nextplayer="Player1"
            else:
                nextplayer= "Player 2"

            if gameobject.next_subgrid =="" or gameobject.ustate[gameobject.next_subgrid]=="x" or gameobject.ustate[gameobject.next_subgrid]=="o":
                nextsubgrid= "on any unclaimed subgrid"
            elif gameobject.next_subgrid== 0:
                nextsubgrid="only on top-left subgrid"
            elif gameobject.next_subgrid== 1:
                nextsubgrid="only on top-center subgrid"
            elif gameobject.next_subgrid== 2:
                nextsubgrid="only on top-right subgrid"
            elif gameobject.next_subgrid== 3:
                nextsubgrid="only on center-left subgrid"
            elif gameobject.next_subgrid== 4:
                nextsubgrid="only on center subgrid"
            elif gameobject.next_subgrid== 5:
                nextsubgrid="only on center-right subgrid"
            elif gameobject.next_subgrid== 6:
                nextsubgrid="only on bottom-left subgrid"
            elif gameobject.next_subgrid== 7:
                nextsubgrid="only on bottom-center subgrid"
            else:
                nextsubgrid="only on bottom-right subgrid"


            substitution={"matrix": gameobject.getGameState()[0],
                          "user": gameobject.next_player,
                          "user1": nextplayer ,
                          "nsubgrid" : nextsubgrid,
                          "error": message}
            html_code3=html_code2.format(**substitution)
            return html_code1+html_code3

    @classmethod
    def registerPage(cls, second_try=False):
        """
        Returns the HTML code for the registration page.

        Returns:
            str: The HTML code for the registration page.
        """
        register_page_css = """
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                width: 80%;
                max-width: 400px;
                padding: 20px;
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 20px;
            }
            form {
                display: flex;
                flex-direction: column;
            }
            label {
                color: #666;
                margin-bottom: 5px;
            }
            input[type="text"],
            input[type="password"] {
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 16px;
                transition: border-color 0.3s ease-in-out;
            }
            input[type="text"]:focus,
            input[type="password"]:focus {
                border-color: #007bff;
                outline: none;
            }
            select {
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 16px;
            }
            .btn-container {
                display: flex;
                justify-content: space-between;
                margin-top: 20px;
            }
            .btn {
                flex: 1;
                padding: 10px;
                border: none;
                border-radius: 4px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s ease-in-out;
            }
            .btn.register {
                background-color: #007bff;
                color: #fff;
            }
            .btn.register:hover {
                background-color: #0056b3;
            }
            .btn.next {
                background-color: #28a745;
                color: #fff;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
            .btn.next:hover {
                background-color: #218838;
            }
        </style>
    """
        register_page_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ultimate Tic-Tac-Toe - Register</title>
        </head>
        <body>
            <div class="container">
                <h1>Register</h1>
                <form action="/register_user" method="POST">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                    <p style="color: red; display: none;">Username already exists. Please try another username.</p>
                    <div class="btn-container">
                        <button class="btn register" type="submit">Register</button>
                    </div>
                </form>
                <div class="btn-container">
                    <a href="login" class="btn next">Login</a>
                </div>
            </div>
        </body>
        </html>
        """
        if second_try:
            register_page_html = register_page_html.replace('display: none;', 'display: block;');
        return register_page_css + register_page_html

    @classmethod
    def loginPage1(cls,second_try=False):
        """
        Returns the HTML code for the registration page.

        Returns:
            str: The HTML code for the registration page.
        """
        login_page_css = """
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                width: 80%;
                max-width: 400px;
                padding: 20px;
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 20px;
            }
            form {
                display: flex;
                flex-direction: column;
            }
            label {
                color: #666;
                margin-bottom: 5px;
            }
            input[type="text"],
            input[type="password"] {
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 16px;
                transition: border-color 0.3s ease-in-out;
            }
            input[type="text"]:focus,
            input[type="password"]:focus {
                border-color: #007bff;
                outline: none;
            }
            select {
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 16px;
            }
            .btn-container {
                display: flex;
                justify-content: space-between;
                margin-top: 20px;
            }
            .btn {
                flex: 1;
                padding: 10px;
                border: none;
                border-radius: 4px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s ease-in-out;
            }
            .btn.register {
                background-color: #007bff;
                color: #fff;
            }
            .btn.register:hover {
                background-color: #0056b3;
            }
            .btn.next {
                background-color: #28a745;
                color: #fff;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
            .btn.next:hover {
                background-color: #218838;
            }
        </style>
    """
        login_page_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ultimate Tic-Tac-Toe - Log In</title>
        </head>
        <body>
            <div class="container">
                <h1>Log In</h1>
                <form action="/login_user2" method="POST">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                    <p style="color: red; display: none;">Invalid Username or Password. Please try again.</p>
                    
                    <div class="btn-container">
                        <button class="btn Login" type="submit">Log In</button>
                    </div>
                </form>
                <div class="btn-container">    
                </div>
            </div>
        </body>
        </html>
        """
        if second_try:
            login_page_html = login_page_html.replace('display: none;', 'display: block;')
        return login_page_css + login_page_html

    def loginPage2(cls, second_try=False):
        """
        Returns the HTML code for the registration page.

        Returns:
            str: The HTML code for the registration page.
        """
        login_page_css = """
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                width: 80%;
                max-width: 400px;
                padding: 20px;
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 20px;
            }
            form {
                display: flex;
                flex-direction: column;
            }
            label {
                color: #666;
                margin-bottom: 5px;
            }
            input[type="text"],
            input[type="password"] {
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 16px;
                transition: border-color 0.3s ease-in-out;
            }
            input[type="text"]:focus,
            input[type="password"]:focus {
                border-color: #007bff;
                outline: none;
            }
            select {
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 16px;
            }
            .btn-container {
                display: flex;
                justify-content: space-between;
                margin-top: 20px;
            }
            .btn {
                flex: 1;
                padding: 10px;
                border: none;
                border-radius: 4px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s ease-in-out;
            }
            .btn.register {
                background-color: #007bff;
                color: #fff;
            }
            .btn.register:hover {
                background-color: #0056b3;
            }
            .btn.next {
                background-color: #28a745;
                color: #fff;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
            .btn.next:hover {
                background-color: #218838;
            }
        </style>
    """
        login_page_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ultimate Tic-Tac-Toe - Log In</title>
        </head>
        <body>
            <div class="container">
                <h1>Log In</h1>
                <form action="/login_user2" method="POST">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                    <p style="color: red; display: none;">Invalid Username or Password. Please try again.</p>

                    <div class="btn-container">
                        <button class="btn Login" type="submit">Log In</button>
                    </div>
                </form>
                <div class="btn-container">    
                </div>
            </div>
        </body>
        </html>
        """
        if second_try:
            login_page_html = login_page_html.replace('display: none;', 'display: block;')
        return login_page_css + login_page_html
    def win_page(cls,gameobject):
        html_code1="""
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Win Page</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            background-image: url('static/7.jpg');
            background-size: cover;
            background-position: center;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
            background-color: rgba(255, 255, 255, 0.5); /* Use RGBA with an alpha value to make the container slightly transparent */
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 40px;
            max-width: 400px;
            width: 90%;
        }

        h1 {
            font-size: 36px;
            margin-bottom: 20px;
            color: #21d6ff;
        }

        p {
            font-size: 18px;
            line-height: 1.6;
            margin-bottom: 30px;
        }

        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #21d6ff;
            color: #ffffff;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .button:hover {
            background-color: #1aa9cc;
        }
    </style>
</head>
"""
        html_code2="""
<body>
    <div class="container">
        <h1>Congratulations!</h1>
        <p>{user} has won the game!</p>
        <a href="restart_game" class="button">Play Again</a>
        <a href="halt" class="button">End</a>
    </div>
</body>
</html>
"""
        if gameobject.outcome == "x":
            temp="Player 1"
        else:
            temp="Player 2"
        substitution={"user": temp }

        return html_code1+html_code2.format(**substitution)