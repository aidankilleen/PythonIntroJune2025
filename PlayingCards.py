# PlayingCards.py

# Playing Card class
from random import shuffle


class Card:
    # NB: we don't declare member variables here
    # constructor
    def __init__ (self, suit, value):
        # member variables are declared in the constructor
        self.suit = suit # 1=H, 2=S, 3=D, 4=C
        self.value = value # 1=A, 2=2 ... 10=10, 11=J, 12=Q, 13=K
        self.SUITS=["", "H", "S", "D", "C"]
        self.VALUES=["", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def display(self):
        print (self)

    def __str__(self):
        return f"{self.VALUES[self.value]}{self.SUITS[self.suit]} "

class Deck:

    def __init__(self):
        self.cards = [Card(suit, value) for suit in range(1,5) for value in range(1, 14)]
        pass

    def display(self):
        for index, card in enumerate(self.cards):
            print (card, end="")
            if index == 12 or index==25 or index==38 :
                print()
        print()

    def shuffle(self):
        shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    deck.display()

    while True:
        card = deck.deal()
        print (card)

        answer = input("f to finish")

        if answer == "f":
            break






    # print ("*" * 25)


    # c = Card(1, 1)
    # print (c.suit, c.value)
    # c.display()
    # print (c)

    # cards = [Card(suit, value) for suit in range(1,5) for value in range(1, 14)]

    # # enumerate with an index
    # for i in range(len(cards)):
    #     print (cards[i], end="")

    #     if i == 12 or i==25 or i==38 :
    #         print()

    # print()
    # print ("*" * 25)

    # #for card in cards:

    # #    print (card, end="")











