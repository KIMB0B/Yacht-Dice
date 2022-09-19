from player import Player
import os, sys
import platform

# 운영체제에 따라 터미널 명령어 변경
if platform.system() == 'Windows':
    close = 'cls'
else:
    close = 'close'

def play(player:Player, round:int):
    """
    플레이어 한명의 한 라운드를 진행합니다.
        args :  player->Player클래스 변수의 하나의 플레이어
                round->현재의 라운드
    """
    turn = 1
    player.Roll()
    while(turn <= 3):
        os.system(close)
        print(f"ROUND [{round}/12]\tNAME [{player.name}]\tTURN [{turn}/3]\n\n")
        print(f"{player.dices}\n\n")
        print("R : 다시 굴리기, B : 점수판 보기")
        mainCommand = input().upper()
        if mainCommand == 'B': # 보드 확인 커맨드 입력 시
            boardView = True
            while(True):
                os.system(close)
                boardCommand = player.ShowBoard().upper()
                if boardCommand == 'B': # 다시 주사위 확인
                    break
                elif boardCommand in player.handRankings.keys(): # 점수 입력 후 턴 종료
                    if player.status & player.handRankings[boardCommand]['check'] == 0: # 아직 점수가 들어가지 않은 족보가 입력될 시
                        player.status += player.handRankings[boardCommand]['check']
                        turn = 999
                        break
                    else:
                        pass
                else: # 예외 입력, 다시 보드 확인 루프 진입
                    pass
        elif mainCommand == 'R': # 주사위 다시 굴리기 커맨드 입력 시
            if turn != 3:
                player.Roll()
                turn += 1

player1 = Player(name="김정욱")
player2 = Player(name="송수진")

for round in range(1, 13):
    play(player1, round)
    play(player2, round)