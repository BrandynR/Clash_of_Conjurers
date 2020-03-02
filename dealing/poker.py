class Game:
    playerOnesHand = []
    playerTwosHand = []
    playerOneScore = 0
    playerTwoScore = 0
    result = 0

    def __init__(self, cards):
    cards = cards.split()
self.playerOnesHand = Hand(cards[0:5])
self.playerTwosHand = Hand(cards[5:10])
self.play();

def play(self):
self.playerOneScore = self.playerOnesHand.getScore();
self.playerTwosCore = self.playerTwosHand.getScore();


if (self.playerOneScore > self.playerTwoScore):
    result = 1
else:
    result = 2

class Hand:
    cards = []
    values = []
    def setValues(self):
    for card in self.cards:
self.values.append(card.value)
self.values.sort()

print len(self.values)

def isFlush(self):
currentSuit = self.cards[0].suit
for card in self.cards:
    if card.suit != currentSuit:
        return False
currentSuit = card.suit
return True

def isRoyalFlush(self):
for card in self.cards:
    self.values.append(card.value)

low = min(self.values)

if low == 10 and (low + 1 in self.values) and (low + 2 in self.values) and (low + 3 in self.values) and (low + 4 in self.values):
    return True
else:
    return False

    def isFourOfAKind(self):
    cardOneCount = self.values.count(self.values[0])
cardTwoCount = self.values.count(self.values[len(self.values) - 1])

if cardOneCount == 4 | cardTwoCount == 4:
    return True
else: 
    return False

    def isThreeOfAKind(self):
    cardOneCount = self.values.count(self.values[0])
cardTwoCount = self.values.count(self.values[len(self.values) - 1])

if cardOneCount == 3 | cardTwoCount == 3:
    return True
else: 
    return False

    def isStraight(self):
    low = min(self.values)

if low == 10 and (low + 1 in self.values) and (low + 2 in self.values) and (low + 3 in self.values) and (low + 4 in self.values):
    return True;

    def isFullHouse(self):
    self.values = []
for card in self.cards:
    self.values.append(card.value)

self.values.sort()
cardOneCount = self.values.count(self.values[0])
cardTwoCount = self.values.count(self.values[len(self.values) - 1])

if (cardOneCount == 2 and cardTwoCount == 3 ) | (cardOneCount == 3 and cardTwoCount == 2):
    return True
else: 
    return False

    def isTwoPair(self):
    cardOneCount = self.values.count(self.values[0])
cardTwoCount = self.values.count(self.values[4])
cardThreeCount = self.values.count(self.values[2])

if(cardOneCount == 2 and cardTwoCount == 2) | (cardOneCount == 2 and cardThreeCount == 2) | (cardTwoCount == 2 and cardThreeCount == 2):
    return True;
return False;

def isPair(self):
cardOneCount = self.values.count(self.values[0])
cardTwoCount = self.values.count(self.values[4])
cardThreeCount = self.values.count(self.values[2])

if(cardOneCount == 2 ^ cardTwoCount == 2 ^ cardTwoCount == 3):
    return True;
return False;

def __init__(self, cards):
for c in cards:
    self.cards.append(Card(c))

self.setValues()

def getScore(self):
score = 0
if self.isRoyalFlush(): score = 140000
elif self.isFlush() and self.isStraight():score = 110000
elif self.isFlush():
