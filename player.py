import random

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
        self.handRankings = {}

    def Roll(self):
        """ 
        해당 플레이어의 주사위를 굴리고 족보 점수를 갱신합니다. 
            args : none
            return : none
        """
        self.dices.clear()
        for i in range(0, 5):
            self.dices.append(random.randint(1, 6))
        
        self.handRankings = {
            "1" : {"name" : "ace"           , "check" : 0b000000000001, "score" : len([i for i in self.dices if i == 1])*1}, 
            "2" : {"name" : "dual"          , "check" : 0b000000000010, "score" : len([i for i in self.dices if i == 2])*2},
            "3" : {"name" : "triple"        , "check" : 0b000000000100, "score" : len([i for i in self.dices if i == 3])*3},
            "4" : {"name" : "quad"          , "check" : 0b000000001000, "score" : len([i for i in self.dices if i == 4])*4},
            "5" : {"name" : "penta"         , "check" : 0b000000010000, "score" : len([i for i in self.dices if i == 5])*5},
            "6" : {"name" : "hexa"          , "check" : 0b000000100000, "score" : len([i for i in self.dices if i == 6])*6},
            "7" : {"name" : "choice"        , "check" : 0b000001000000, "score" : sum(self.dices)},
            "8" : {"name" : "poker"         , "check" : 0b000010000000, "score" : 0},
            "9" : {"name" : "fullHouse"     , "check" : 0b000100000000, "score" : 0},
            "0" : {"name" : "smallStraight" , "check" : 0b001000000000, "score" : 0},
            "-" : {"name" : "largeStraight" , "check" : 0b010000000000, "score" : 0},
            "=" : {"name" : "yacht"         , "check" : 0b100000000000, "score" : 0}
        }
    
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