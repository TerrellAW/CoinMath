import random

class Person:
    def __init__ (self, name, coins):
        self.name = name
        self.coins = coins

def simulate(personA, personB, personACoinAmount, personBCoinAmount):
    while personA.coins > 0 and personB.coins > 0:
        chance = random.randint(0, 1)
        if chance == 0:
            personA.coins += 1
            personB.coins -= 1
        else:
            personB.coins += 1
            personA.coins -= 1
    if personA.coins == 0:
        print(personA.name + " has lost all their coins!")
        print(personB.name + " has won!")
    else:
        print(personB.name + " has lost all their coins!")
        print(personA.name + " has won!")

    return personA.coins > 0

def run_sims(num_sims):
    personA_wins = 0

    for i in range(num_sims):
        personA = Person(personAName, personACoinAmount)
        personB = Person(personBName, personBCoinAmount)
        
        if simulate(personA, personB, personACoinAmount, personBCoinAmount):
            personA_wins += 1
        
    win_percentage = (personA_wins / num_sims) * 100
    return win_percentage

personACoinAmount = 1
personBCoinAmount = 10
personAName = "A"
personBName = "B"
personA = Person(personAName, personACoinAmount)
personB = Person(personBName, personBCoinAmount)

print(f"{personAName} win percentage: {run_sims(100000)}%")