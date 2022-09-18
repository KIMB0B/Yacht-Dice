from player import Player
import os, sys

player1 = Player(name="김정욱")
while(True):      
    player1.Roll()
    turn = True
    while(turn == True):
        os.system("clear")
        print(f"{player1.name}님의 주사위 : {player1.dices}")
        if input().upper() == 'B':
            boardView = True
            while(True):
                os.system("clear")
                boardResult = player1.ShowBoard().upper()
                if boardResult == 'B':
                    break
                elif boardResult == '1':
                    player1.status += player1.handRankings['ace']['check']
                    print(player1.status)
                    turn = False
                    break
                else:
                    pass