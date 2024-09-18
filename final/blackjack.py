import random

#---------------------------------------Deck Values-------------------------------------------------------
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    for suit in suits:
        for rank in ranks:                  #Creates Deck with all numbers and face cards
            deck.append((rank, suit))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)    #Shuffles the deck so its random every game
    return deck

def draw_card(deck, index):       #Randomly draws the card from the create_deck 
    return deck[index]

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            aces += 1
            value += 11
        else:                     #The math to all up how much your cards value is.
            value += int(rank)

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value
#---------------------------------Print Format-------------------------------------------------
def hand_format(hand):
    hand_comma = ""
    for i in range(len(hand)):
        rank, suit = hand[i]
        hand_comma += f"{rank} of {suit}"     #Formats the print statements to look much neater
        if i < len(hand) - 1: 
            hand_comma += ", "  
    return hand_comma

#-----------------------Print Displays--------------------------------------------------------------
def display_game(player_hand, dealer_hand, reveal_dealer=False):
    print("\nPlayer's Hand:", hand_format(player_hand), "Value:", calculate_hand_value(player_hand))
    if reveal_dealer:
        print("Dealer's Hand:", hand_format(dealer_hand), "Value:", calculate_hand_value(dealer_hand))
    else:
        print("Dealer's Hand: [{} , {}]".format(dealer_hand[0][0] + ' of ' + dealer_hand[0][1], dealer_hand[1][0] + ' of ' + dealer_hand[1][1]))

def player_turn(deck, player_hand, dealer_hand, index):
    playing = True
    while playing:
        display_game(player_hand, dealer_hand, reveal_dealer=False)
        player_value = calculate_hand_value(player_hand)

        if player_value == 21:
            print("Blackjack! You win!")
            return index
        elif player_value > 21:
            print("You bust! Dealer wins.")
            return index

        action = input("Do you want to hit (h) or stand (s)? ").lower()
        if action == 'h':
            player_hand.append(draw_card(deck, index))
            index += 1
        elif action == 's':
            playing = False

    return index

def dealer_turn(deck, dealer_hand, index):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck, index))
        index += 1
    
#---------------------------------------Game Implementation-------------------------------------------------------------
def play_blackjack():
    print("Welcome to Blackjack!")

    playing = True
    while playing:
        deck = shuffle_deck(create_deck())
        index = 0

        player_hand = [draw_card(deck, index), draw_card(deck, index + 1)]
        index += 2
        dealer_hand = [draw_card(deck, index), draw_card(deck, index + 1)]
        index += 2

        index = player_turn(deck, player_hand, dealer_hand, index)
        if index == -1:
            continue

        dealer_turn(deck, dealer_hand, index)

        display_game(player_hand, dealer_hand, reveal_dealer=True)
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        if dealer_value > 21:
            print("Dealer busts! You win!")
        elif player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing")
            playing = False


if __name__ == "__main__":
    play_blackjack()
