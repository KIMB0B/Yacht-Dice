import random
import os, platform

# 운영체제에 따라 터미널 명령어 변경
if platform.system() == 'Windows':
    close = 'cls'
else:
    close = 'clear'

""" 글자/배경 색 설정 """
BLACK_BG = '\033[40m'
BRIGHT_WHITE_BG = '\033[107m'
BLACK = '\033[30m'
BRIGHT_RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
class Player:
    """
        한명의 유져 클래스입니다.
            args : name->사용자명(str)
            return : 유져 클래스 변수(Player)
        """
    def __init__(self, name: str):
        self.name = name
        self.status = 0
        self.score = 0
        self.dices = list()
        self.handRankings = {
            "1" : {"name" : "ace"           , "check" : 0b000000000001, "score" : 0}, 
            "2" : {"name" : "dual"          , "check" : 0b000000000010, "score" : 0},
            "3" : {"name" : "triple"        , "check" : 0b000000000100, "score" : 0},
            "4" : {"name" : "quad"          , "check" : 0b000000001000, "score" : 0},
            "5" : {"name" : "penta"         , "check" : 0b000000010000, "score" : 0},
            "6" : {"name" : "hexa"          , "check" : 0b000000100000, "score" : 0},
            "7" : {"name" : "choice"        , "check" : 0b000001000000, "score" : 0},
            "8" : {"name" : "poker"         , "check" : 0b000010000000, "score" : 0},
            "9" : {"name" : "fullHouse"     , "check" : 0b000100000000, "score" : 0},
            "0" : {"name" : "smallStraight" , "check" : 0b001000000000, "score" : 0},
            "-" : {"name" : "largeStraight" , "check" : 0b010000000000, "score" : 0},
            "=" : {"name" : "yacht"         , "check" : 0b100000000000, "score" : 0}
        }

    def Roll(self):
        """ 
        해당 플레이어의 주사위를 굴리고 족보 점수를 갱신합니다. 
            args : none
            return : none
        """
        self.dices.clear()
        for i in range(0, 5):
            self.dices.append(random.randint(1, 6))

        ## 점수가 아직 입력되지 않은 족보의 보드판에서 점수 확인 ##
        for key in self.handRankings:
            if self.handRankings[key]['check'] & self.status == 0:
                if key == '1' or key == '2' or key == '3' or key == '4' or key == '5' or key == '6': # ACE ~ HEXA 보드판 점수 확인
                    self.handRankings[key].update({'score' : len([i for i in self.dices if i == int(key)])*int(key)})
                elif key == '7': # CHOICE 보드판 점수 확인
                    self.handRankings[key].update({'score' : sum(self.dices)})
    
    def ShowBoard(self):
        """ 
        점수판을 확인하고, 명령어를 입력받습니다. 
            args : none
            return : 점수판 확인 후 실행할 명령어(str)
        """
        print(BRIGHT_WHITE_BG+BLACK+"┌------------------┬------┐"+END)
        print(BRIGHT_WHITE_BG+BLACK+"| 족보             | 점수 |"+END)
        for i in self.handRankings:
            color = BOLD + BRIGHT_RED if self.status & self.handRankings[i]['check'] != 0 else BLACK
            print(BRIGHT_WHITE_BG+BLACK+"├------------------┼------┤"+END)
            print(BRIGHT_WHITE_BG+BLACK+"| " + color + f"{i}. {'%-13s' % self.handRankings[i]['name']}" + END + BRIGHT_WHITE_BG + BLACK + " | " + color + f"{'%-3s' % self.handRankings[i]['score']}점" + END + BRIGHT_WHITE_BG + BLACK + "|"+END)
        print(BRIGHT_WHITE_BG+BLACK+"└------------------┴------┘"+END)
        print("\nB : 돌아가기, 1 ~ = : 점수 입력")
        return input("->")

    def Play(self, round:int):
        """
        플레이어 한명의 한 라운드를 진행합니다.
            args :  round->현재의 라운드
            return : none
        """
        print(f"{self.name}님의 {round}라운드를 시작합니다.\n\nPress Enter...")
        input()
        turn = 1
        self.Roll()
        while(turn <= 3):
            os.system(close)
            print(f"ROUND [{round}/12]\tNAME [{self.name}]\tTURN [{turn}/3]\n\n")
            print(f"{self.dices}\n\n")
            print("R : 다시 굴리기, B : 점수판 보기")
            mainCommand = input("->").upper()
            if mainCommand == 'B': # 보드 확인 커맨드 입력 시
                while(True):
                    os.system(close)
                    boardCommand = self.ShowBoard().upper()

                    if boardCommand == 'B': # 다시 주사위 확인
                        break

                    elif boardCommand in self.handRankings.keys(): # 족보 key 입력 시
                        ## 점수가 아직 입력되지 않은 족보의 점수 입력 ##
                        if self.status & self.handRankings[boardCommand]['check'] == 0:
                            self.status += self.handRankings[boardCommand]['check']
                            if boardCommand == '1' or boardCommand == '2' or boardCommand == '3' or boardCommand == '4' or boardCommand == '5' or boardCommand == '6': # ACE ~ HEXA 점수 입력
                                self.handRankings[boardCommand].update({'score' : len([i for i in self.dices if i == int(boardCommand)])*int(boardCommand)})
                            elif boardCommand == '7': # CHOICE 점수 입력
                                self.handRankings[boardCommand].update({'score' : sum(self.dices)})
                            
                            turn = 999
                            break
                        ## 점수가 아직 입력되지 않은 족보의 점수 입력 ##
                        else: # 이미 점수가 입력된 족보일 시 pass
                            pass

                    else: # 예외 입력 시 다시 보드 확인 루프 진입
                        pass
            elif mainCommand == 'R': # 주사위 다시 굴리기 커맨드 입력 시
                if turn != 3:
                    self.Roll()
                    turn += 1
        os.system(close)
        print(f"{self.name}님이 {self.handRankings[boardCommand]['name']}에 {self.handRankings[boardCommand]['score']}점을 넣고 {round}라운드를 종료했습니다.\n\n")