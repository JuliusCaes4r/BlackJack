import random
from art import logo

print(logo)
usercards = []
computercards = []

#N1 start
def start():
    #N2 user and computer get 2 random card
    def dealcards():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card
    
    for _ in range(2):
        usercards.append(dealcards())
        computercards.append(dealcards())
    print(f"your cards: {usercards}")
    print(f"dealer cards {computercards}")

    #N3 add the user and computer scores
    def calculate_scores(cards, player):
        #N3.1 if the user has blackjack win
        if sum(cards) == 21:
            print(f"{player} have BLACKJACK, you won!!")
            exit()
        #N4.1 do they have 11(ace) and its over 21, 11 count as a 1
        elif 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
            #if 11(ase) count as a 1 and it still more than 21 lose
            if sum(cards) > 21:
                print(f"{player} have more than 21, you lost..")
                exit()
        #
        elif sum(cards) > 21:
            print(f"{player} have more than 21, you lost..")
            exit()
        
    def winner(userc, compc):
        if sum(userc) == sum(compc):
            print("draw")
        elif sum(userc) > sum(compc):
            print("you won!!")
        elif sum(userc) < sum(compc):
            print("dealer won!!")
        

    #datvalos kompiuteris da useris kartebi (gamodzaxeba)
    calculate_scores(usercards,"you")
    calculate_scores(computercards,"dealer")

    def getAnotherCard():
        usercards.append(dealcards())
        print(f"your cards: {usercards}")
        calculate_scores(usercards,"you")
    
    def computerplays():
        while sum(computercards) < 16:
            computercards.append(dealcards())
            print(f"dealer cards: {computercards}")
        calculate_scores(computercards,"dealer")
        winner(usercards, computercards)
    
    #gsurt tu ara gagrdzeleba?
    if input("Do you want to continue? [y/n]: ") == "y":
        tf = True
        while tf:
            getAnotherCard()
            if input("Do you want to continue? [y/n]: ") == "y":
                continue
            else:
                tf = False
    if "n": 
        computerplays()
start()








