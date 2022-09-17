import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.dices = list()
        self.handRankings = {}

    def Roll(self):
        """ 해당 플레이어의 주사위를 굴리고 족보 점수를 갱신합니다. """

        self.dices.clear()
        for i in range(0, 5):
            self.dices.append(random.randint(1, 6))
        
        self.handRankings = {
            "ace"           : {"check" : 0b000000000001, "score" : len([i for i in self.dices if i == 1])*1}, 
            "dual"          : {"check" : 0b000000000010, "score" : len([i for i in self.dices if i == 2])*2},
            "triple"        : {"check" : 0b000000000100, "score" : len([i for i in self.dices if i == 3])*3},
            "quad"          : {"check" : 0b000000001000, "score" : len([i for i in self.dices if i == 4])*4},
            "penta"         : {"check" : 0b000000010000, "score" : len([i for i in self.dices if i == 5])*5},
            "hexa"          : {"check" : 0b000000100000, "score" : len([i for i in self.dices if i == 6])*6},
            "choice"        : {"check" : 0b000001000000, "score" : sum(self.dices)},
            "poker"         : {"check" : 0b000010000000, "score" : 0},
            "fullHouse"     : {"check" : 0b000100000000, "score" : 0},
            "smallStraight" : {"check" : 0b001000000000, "score" : 0},
            "largeStraight" : {"check" : 0b010000000000, "score" : 0},
            "yacht"         : {"check" : 0b100000000000, "score" : 0}
        }
    
    def ShowBoard(self):
        """ 점수판을 확인합니다. """
        print("┌---------------┬------┐")
        print("| 족보          | 점수 |")
        for i in self.handRankings:
            print("├---------------┼------┤")
            print(f"| {'%-13s' % i} | {'%-3s' % self.handRankings[i]['score']}점|")
        print("└---------------┴------┘")
            
player1 = Player(name="김정욱")
player1.Roll()
print(f"{player1.name}님의 주사위 : {player1.dices}")
player1.ShowBoard()