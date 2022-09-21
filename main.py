from player import Player

player1 = Player(name="김정욱")
player2 = Player(name="송수진")

for round in range(1, 13):
    player1.Play(round)
    player2.Play(round)