# IMPORT STATEMENTS AND VARIABLE DECLARATIONS:
# Frissst we make import random then we define suits , ranks ,and values with a boolean fuction as playing
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

# CLASS DEFINTIONS:
# then we define card abd we pass suit and ranks in it
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
# then we define a str function        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
# the we make class of deck to store all the 52 cards


class Deck:
# make a instance of deck as a empty sets and pass the cards value in it    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
# this elf .deck will be used to get decks card and its ranks

#  make a str function to get the use of deck_como
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
# deck shuffel function to shuffel the cards                
    def shuffle(self):
        random.shuffle(self.deck)
# deal function to get a card from deck fuction        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
# hand class for getting the card in hands
class Hand:
# make an empty value for thir hands    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
# add cards in there hands    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
# adjust ace if a user have ace in his hand next ace will be trated as 1    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
# make chips class for betting in the game
class Chips:
# make and initial instance for the bet    
    def __init__(self):
        self.total = 100
        self.bet = 0
# fuction for the winning bet         
    def win_bet(self):
        self.total += self.bet
# function for lossing the bet    
    def lose_bet(self):
        self.total -= self.bet
        

# FUNCTION DEFINITIONS:
# function for taking bet from user how much bet they wiil be given to the game
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break
# make a instance of function for use
# what would happen whrn the hit procees occur
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
# for hit_stand functiom    
def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

# this function use to show card but dealer card should be hidden
    
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
# this function is use for end of the functiom    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
# this fuction is show if user are busted    
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()
# this function show if player wins the  game
def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()
# this function is used when dealer bust
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
# this function is use whe dealer win    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
# this is for draw     
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
    
# GAMEPLAY!
# GAmeplaye Function
while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100
    
    # Prompt the Player for their bet:
    take_bet(player_chips)
    
    # Show the cards:
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    # If Player hasn't busted, play Dealer's hand        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Test different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    # Inform Player of their chips total    
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break

