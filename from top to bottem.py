from random import random


def printIntro():
    print("this program simulates a game between two")
    print("there is two players A and B")
    print("probability(a number between 0 and 1 )is used ")

def getInputs():
    a = eval(input("what is the prob.player A wins?"))
    b = eval(input("what is the prob.player b wins?"))
    n = eval(input("how many games to simulate?"))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a,b):
    return a == 15 or b == 15

def PrintSummary(winsA , winsB):
    n = winsA + winsB
    print("\nGames simulated %d"%n)
    print("Wins for A:{0}({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B:{0}({1:0.1%})".format(winsB, winsB/n))

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    PrintSummary(winsA, winsB)

main()