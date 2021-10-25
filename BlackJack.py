import random
# 21 Game

####### Planning
# Compare Sum of Dealer_D vs Player_P
# If P Sum > 21 : bust
# If P Sum > 21 : Option Hit or Stay
# If P option Stay : compare D sum v P sum
# If P Sum <= 21 and > D sum : P wins
# If P sum < D sum : P loses 

##################

# Dealer/player cards
dealer_cards = []
player_cards = []
    # Deal cards 
# Dealer Cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has * and ", dealer_cards[1])

# Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("You have ", player_cards)
    # Display cards 
# Sum Dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins. You lose.")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

# Sum Player Cards
while sum(player_cards) < 21:
    action_taken =str(input("Hit or Stay?"))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards: ")
    else:
        print("Dealer has " + str(sum(dealer_cards)) + " with", dealer_cards)
        print("You have " + str(sum(player_cards)) + " with", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print(" Dealer wins.")
        else:
            print("You Win!")
            break

if sum(player_cards) > 21:
    print("You Busted. Dealer Wins.")    

if sum(player_cards) == 21:
    print("You have 21! You Win! BlackJack!!!")




