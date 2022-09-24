from player import Player
import os, platform

# 운영체제에 따라 터미널 명령어 변경
if platform.system() == 'Windows':
    close = 'cls'
else:
    close = 'clear'

def showPlayer():
    """
    화면을 초기화하고 현재 플레이어 리스트를 출력
        args : none
        return : none
    """
    os.system(close)
    print("플레이어 목록 👩 ", end='')
    for player in playerList:
        print(f"{player.name}", end='')
        if playerList.index(player) != len(playerList)-1:
            print(", ", end='')
    print(' 👨\n')

playerList = []
playerList.append(Player(input("첫번째 플레이어 이름을 입력해주세요 : ")))

while(True):
    showPlayer()
    command1 = input("1. 플레이어 관리, 2. 게임방법, 3. 게임 시작, Q. 게임 종료\n-> ")

    if command1 == "1": # 플레이어 관리
        while(True):
            showPlayer()
            playerCommand = input("1. 플레이어 추가, 2. 플레이어 삭제 , B. 돌아가기\n-> ")
            if playerCommand == "1":
                showPlayer()
                playerList.append(Player(input("추가할 플레이어 이름을 입력해주세요 : ")))
            elif playerCommand == "2":
                showPlayer()
                deletePlayerName = input("삭제할 플레이어 이름을 입력해주세요 : ")
                for player in playerList:
                    if player.name == deletePlayerName:
                        playerList.remove(player)
            elif playerCommand.upper() == "B":
                break
            else:
                pass

    elif command1 == "2": # 게임 방법
        pass

    elif command1 == "3": # 게임 시작
        os.system(close)
        for round in range(1, 13):
            for player in playerList:
                player.Play(round)

    elif command1.upper() == "Q": # 게임 종료
        break