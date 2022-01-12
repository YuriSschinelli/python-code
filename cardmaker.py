import random
def crianaipe(n):
    if n == 1:
        n = str('cups')
    elif n == 2:
        n = str('spades')
    elif n == 3:
        n = str('diamonds')
    elif n == 4:
        n = str('clubs')
    return n
def facecard(c):
    if c == 11:
        c = str('jester')
    elif c == 12:
        c = str('Queen')
    elif c == 13:
        c = str('King')
    elif c == 1:
        c = str('Ace')
    elif c == 0:
        c = str('Joker')
    return c
def criacarta(n,c):
  carta = []
  carta.append(n)
  carta.append(c)
  return carta
def criaset(n,c):
    deck = []
    for i in range(0,5):
        n = random.randrange(0,11)
        n = facecard(n)
        naipe = random.randrange(1,4)
        naipe = crianaipe(naipe)
        deck.append(criacarta(n,naipe))
    return deck
naipe = 0
n = 0
deck = criaset(n,naipe)
print(deck)
