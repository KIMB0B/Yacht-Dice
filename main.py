from operator import index
from textwrap import indent
from player import Player
import os, platform
import unicodedata

# 운영체제에 따라 터미널 명령어 변경
if platform.system() == 'Windows':
    close = 'cls'
else:
    close = 'clear'

def fill_str(input_s:str, max_size:int, fill_char:str=" "):
    """
    길이가 긴 문자는 2칸으로 체크하고, 짧으면 1칸으로 체크해 설정한 길이의 남은 곳을 설정한 문자로 채웁니다. 
        args :  input_s->입력할 문자열(str)
                max_size->최대 길이(int)
                fill_char->남은 길이만큼 채울 문자(str)
        return : 입력된 문자열에 빈칸을 설정한 문자로 채운 문자열(str)
    """
    l = 0 
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else: 
            l+=1
    return input_s+fill_char*(max_size-l)

def showPlayer():
    """
    화면을 초기화하고 현재 플레이어 리스트를 출력
        args : none
        return : none
    """
    os.system(close)
    print("플레이어 목록 👩 ", end='')
    for player in playerList:
        print(f"{playerList.index(player)+1}. {player.name}", end='')
        if playerList.index(player) != len(playerList)-1:
            print(", ", end='')
    print(' 👨\n')

playerList = []

while(True): # 최초 첫번째 플레이어 정보 입력받기
    os.system(close)
    firstPlayerName = input("첫번째 플레이어 이름을 입력해주세요 : ")
    if firstPlayerName == "1" or firstPlayerName == "2" or firstPlayerName == "3" or firstPlayerName == "4" or firstPlayerName.strip() == "":
        input("올바르지 않은 플레이어 이름입니다. (플레이어 이름을 1, 2, 3, 4, 공백은 사용할 수 없습니다)...")
    else:
        playerList.append(Player(firstPlayerName))
        break

while(True):
    showPlayer()
    command1 = input("1. 플레이어 관리, 2. 게임방법, 3. 게임 시작, Q. 게임 종료\n-> ")

    if command1 == "1": # 플레이어 관리
        while(True):
            showPlayer()
            playerCommand = input("1. 플레이어 추가, 2. 플레이어 삭제 , B. 돌아가기\n-> ")
            if playerCommand == "1": # 플레이어 추가
                showPlayer()
                if len(playerList) >= 4:
                    input("최대 플레이어수는 4명입니다. 더 이상 추가할 수 없습니다...")
                else:
                    while(True):
                        showPlayer()
                        inputOverlap = False # 중복된 이름이 있을 시 True로 변경
                        inputNotGood = False # 조건에 맞지 않는 이름이 입력될 시 True로 변경
                        inputPlayerName = input("추가할 플레이어 이름을 입력해주세요 : ")
                        for player in playerList:
                            if player.name == inputPlayerName:
                                inputOverlap = True
                                break
                            elif inputPlayerName == "1" or inputPlayerName == "2" or inputPlayerName == "3" or inputPlayerName == "4" or inputPlayerName.strip() == "":
                                inputNotGood = True
                                break
                        if inputOverlap == True: # 중복된 이름값이 입력된 경우
                            input("이미 존재하는 플레이어 이름입니다. 다른 이름을 입력해주세요...")
                            break
                        elif inputNotGood == True: # 조건에 맞지 않는 이름값이 입력된 경우
                            input("올바르지 않은 플레이어 이름입니다. (플레이어 이름을 1, 2, 3, 4, 공백은 사용할 수 없습니다)...")
                            break
                        else: # 올바른 경우
                            playerList.append(Player(inputPlayerName))
                            break
            elif playerCommand == "2": # 플레이어 삭제
                showPlayer()
                if len(playerList) <= 1:
                    input("최소 한 명의 플레이어는 존재해야 합니다...")
                else:
                    showPlayer()
                    deletePlayerName = input("삭제할 플레이어 이름/번호를 입력해주세요 : ")
                    delCheckPlayer = False # 삭제할 값이 있을 시 True로 변경
                    for player in playerList:
                        try:
                            if player.name == deletePlayerName: # 이름 입력으로 삭제
                                delCheckPlayer = True
                                if input(f"{player.name}님을 삭제하려면 Y를 입력해 주세요 : ").upper() == "Y":
                                    playerList.remove(player)
                                else:
                                    input(f"{player.name}님을 삭제하지 않았습니다...")
                                break
                            elif playerList.index(player) == int(deletePlayerName)-1: # 번호 입력으로 삭제
                                delCheckPlayer = True
                                if input(f"{playerList[int(deletePlayerName)-1].name}님을 삭제하려면 Y를 입력해 주세요 : ").upper() == "Y":
                                    playerList.pop(int(deletePlayerName)-1)
                                else:
                                    input(f"{playerList[int(deletePlayerName)-1].name}님을 삭제하지 않았습니다...")
                                break
                        except ValueError:
                            pass
                    if delCheckPlayer == False: # 삭제할 이름/번호가 없을 시
                        input("목록에 해당 플레이어 이름/번호가 없습니다...")
            elif playerCommand.upper() == "B": # 돌아가기
                break
            else:
                pass

    elif command1 == "2": # 게임 방법
        showPlayer()
        print("[YATCH 룰]")
        print("1. 주사위 5개를 던진다")
        print("2. 이 중 원하는 주사위들은 고정해 두고 나머지 주사위들을 다시 던진다. \n   다시 던지기는 한 라운드에 두 번까지 가능하며, 앞에서 고정했던 주사위도 원한다면 고정을 풀어 다시 던질 수 있다.")
        print("3. 이렇게 해서 나온 값을 반드시 점수판에 기록해야한다. 기록할 칸이 없는 경우 아무칸에 0으로 기록한다.")
        print("※ 기록 방법 : 점수판의 족보 이름 앞에 있는 숫자/기호를 입력한다. 기록이 완료되면 아무 키나 눌러 나온 후 이어서 진행한다.")
        print("4. 점수판이 12칸이니 총 12라운드를 하면 게임이 끝난다. 점수판의 점수 총합이 더 큰 플레이어가 승자가 된다.")
        print("\n=======================================================================================================================\n")
        print("[족보]")
        print(fill_str("┌", 17, "-")+fill_str("┬", 70, "-") + fill_str("┬", 18, "-")+"-┐")
        print(fill_str("| 이름", 17) + fill_str("| 설명", 70) + fill_str("| 예시", 18, " ")+" |")
        print(fill_str("├", 17, "-") + fill_str("┼", 70, "-") + fill_str("┼", 18, "-")+"-┤")
        print(fill_str("| Aces", 17) + fill_str("| 1이 나온 주사위 눈의 합", 70) + "| 2 2 3 5 6 =  0점"+" |")
        print(fill_str("| Dual", 17) + fill_str("| 2이 나온 주사위 눈의 합", 70) + "| 2 2 2 2 5 =  8점"+" |")
        print(fill_str("| Triple", 17) + fill_str("| 3이 나온 주사위 눈의 합", 70) + "| 1 3 3 3 4 =  9점"+" |")
        print(fill_str("| Quad", 17) + fill_str("| 4이 나온 주사위 눈의 합", 70) + "| 2 3 4 4 4 = 12점"+" |")
        print(fill_str("| Penta", 17) + fill_str("| 5이 나온 주사위 눈의 합", 70) + "| 3 4 5 5 5 = 17점"+" |")
        print(fill_str("| Hexa", 17) + fill_str("| 6이 나온 주사위 눈의 합", 70) + "| 1 2 3 6 6 = 12점"+" |")
        print(fill_str("| --Bonus", 17) + fill_str("| 상단항목에서 합이 63점이 넘을 경우 35점을 추가한다.", 70)+fill_str("|", 18, " ")+" |")
        print(fill_str("| Choice", 17) + fill_str("| 주사위 5개의 눈의 총합", 70) + "| 2 2 3 5 6 = 18점"+" |")
        print(fill_str("| Poker", 17) + fill_str("| 주사위 4개 이상의 눈이 동일할 때, 주사위 5개의 합", 70) + "| 3 3 3 3 5 = 17점"+" |")
        print(fill_str("| Full House", 17) + fill_str("| 눈이 동일한 주사위가 각각 3개와 2개가 있을 때, 주사위 5개의 합", 70)+"| 2 2 2 3 3 = 12점"+" |")
        print(fill_str("| Small Straight", 17) + fill_str("| 주사위 4개 이상의 눈이 이어지는 수일 때, 고정 17점", 70) + "| 1 2 3 4 6 = 15점"+" |")
        print(fill_str("| Large Straight", 17) + fill_str("| 주사위 5개의 눈이 이어지는 수일 때, 고정 30점", 70) + "| 2 3 4 5 6 = 30점"+" |")
        print(fill_str("| Yacht", 17) + fill_str("| 주사위 5개의 눈이 모두 같을 때, 고정 50점", 70) + "| 4 4 4 4 4 = 50점"+" |")
        print(fill_str("└", 17, "-")+fill_str("┴", 70, "-") + fill_str("┴", 18, "-")+"-┘")
        input("\n뒤로 가려면 아무 키나 눌러주세요...")

    elif command1 == "3": # 게임 시작
        os.system(close)
        for round in range(1, 13):
            for player in playerList:
                player.Play(round)

    elif command1.upper() == "Q": # 게임 종료
        os.system(close)
        QuitCommand = input("정말 게임을 종료하시려면 Y를 입력해 주세요 : ")
        if QuitCommand.upper() == "Y":
            print("잘가요~~")
            break
        else:
            pass