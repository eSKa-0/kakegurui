import random

class Player:
    def __init__(self, name:str, buyin:int):
        self.name = name
        self.cards = []
        self.chips = buyin
        self.betamount = 0
    def showCards(self):
        for i in self.cards:
            if i[1] == "h":
                print(f"{i[0]} of hearts")
            if i[1] == "s":
                print(f"{i[0]} of spades")
            if i[1] == "c":
                print(f"{i[0]} of clubs")
            if i[1] == "d":
                print(f"{i[0]} of diamonds")
    def bet(self) -> int:
        self.betamount = input("how much do you want to bet?(numbers only)")
        return(self.betamount)
class TexasHoldem:
    def __init__(self, players:list):
        self.shoe = [("A","h"), ("2", "h"), ("3", "h"), ("4", "h"), ("5", "h"), ("6", "h"), ("7", "h"), ("8", "h"), ("9", "h"), ("10", "h"), ("J", "h"), ("Q", "h"), ("K", "h"), ("A", "d"), ("2", "d"), ("3", "d"), ("4", "d"), ("5", "d"), ("6", "d"), ("7", "d"), ("8", "d"), ("9", "d"), ("10", "d"), ("J", "d"), ("Q", "d"), ("K", "d"), ("A", "s"), ("2", "s"), ("3", "s"), ("4", "s"), ("5", "s"), ("6", "s"), ("7", "s"), ("8", "s"), ("9", "s"), ("10", "s"), ("J", "s"), ("Q", "s"), ("K", "s"), ("A", "c"), ("2", "c"), ("3", "c"), ("4", "c"), ("5", "c"), ("6", "c"), ("7", "c"), ("8", "c"), ("9", "c"), ("10", "c"), ("J", "c"), ("Q", "c"), ("K", "c")]
        self.table = []
        self.players = players
    def countshoe(self):
        amountbuffer = 0
        for i in self.shoe:
            amountbuffer = amountbuffer + 1
        return amountbuffer
    def deal(self):
        for i in self.players:
            nbuffer = random.randint(0, self.countshoe()-1)
            i.cards.append(self.shoe.pop(nbuffer))
    def showPlayers(self):
        for i in self.players:
            print(i.name)
    def flop(self):
        nbuffer = random.randint(0, self.countshoe()-2)
        self.table.append(self.shoe.pop(nbuffer))
        nbuffer = random.randint(0, self.countshoe()-2)
        self.table.append(self.shoe.pop(nbuffer))
        nbuffer = random.randint(0, self.countshoe()-2)
        self.table.append(self.shoe.pop(nbuffer))
        print(f"flop:\n\t{self.table}")
    def bettime(self):
        ask = input("do you want to 1.check, 2.fold, 3.bet")
        if ask == "3":
            for i in self.players:
                i.bet()
    def reset(self) -> None:
        self.table = []
        for i in self.players:
            i.cards = []

lastro = Player("Milo", 300)
game = TexasHoldem([lastro])
game.showPlayers()
playing = True
while playing == True:
    if game.countshoe() > 0:    
        game.deal()
        game.deal()
        lastro.showCards()
        game.bettime()
        game.flop()
        game.bettime()
        game.reset()
    else:
        if input("restart shoe?(y/n)") == "y" or "Y":
            pass
        else:
            playing = False