def main():
    results = []
    play_hand = 'y'
    while play_hand == 'y' or play_hand == 'Y':
        deck = new_deck()
        player_hand, dealer_hand = deal_cards(deck)
        player_count = count_hand(player_hand)
        dealer_count = count_hand(dealer_hand)
        print("Your hand is:     ", player_hand, "Your hand value: ", player_count)
        print("Dealers hand is:  ", dealer_hand[0],  '?')
        natural = natural_check(player_count,dealer_count)
        if natural != True:
            player_hand, player_count = hitloop(player_hand,dealer_hand,deck)
            if min(player_count) <= 21:
                dealer_hand, dealer_count = dealer_play(dealer_hand, dealer_count,deck)             
        player_count = count_hand(player_hand)
        dealer_count = count_hand(dealer_hand)
        print("Your hand is:     ", player_hand, "Your hand value: ", player_count)
        print("Dealers hand is:  ", dealer_hand, "Dealer value:    ", dealer_count)
        result = eval_win(player_hand, dealer_hand)
        print(result)
        results.append(result)
        play_hand = input('play another hand? ')
    return results

def new_deck():
    import numpy as np
    import random as random
    #Make deck
    values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    deck = values * 4

    # Shuffle Deck
    random.shuffle(deck)

    # Cut Deck
    cutat = np.random.randint(0,len(deck))
    deck = deck[cutat:] + deck[:cutat]
    return deck

def deal_cards(deck):
    # Deal 2 cards
    player_hand = []
    dealer_hand = []
    for i in [0, 1]:
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
    return player_hand, dealer_hand

def count_hand(hand):
    counters = hand.copy()
    A_index = [0] * len(hand)
    if 'A' not in hand:
        for card in list(range(0, len(hand))):
            if isinstance(hand[card], str):
                counters[card] = 10
            else:
                counters[card] = counters[card]
        count = [sum(counters)]
    else:
        count = 0;
        for card in list(range(0, len(hand))):
            if hand[card] == 'A':
                A_index[card] = 1
            elif isinstance(hand[card], str):
                count = count + 10
            else:
                count = count + hand[card]
        A_count = [sum(A_index), sum(A_index) + 10]
        count = [ A_count[0] + count , A_count[1] + count]
    return count

def natural_check(player_count, dealer_count):
    if 21 in player_count or 21 in dealer_count:
        return True

def hitloop(player_hand,dealer_hand,deck):
    player_count = count_hand(player_hand)
    answer = input('Hit? (y/n) ') # get decision from user
    while answer == 'Y' or answer == 'y':
        player_hand.append(deck.pop())
        player_count = count_hand(player_hand)
        print("Your hand is:     ", player_hand, "Your hand value: ", player_count)
        print("Dealers hand is:  ", dealer_hand[0],  '?')
        if 21 in player_count:
            print('WIN')
            input('Press Enter to Continue')
            return player_hand, player_count
            break
        elif min(player_count) < 21:
            answer = input('Hit? (y/n) ') # get decision from user
        else:
            print ('BUST! Your count =', min(player_count))
            input('Press Enter to Continue')
            break
    return player_hand, player_count

def decision_rule(player_count):
    if max(player_count) < 17:
        response = 'y'
    else:
        response = 'n'
    return response

def dealer_play(dealer_hand, dealer_count,deck):
    while max(count_hand(dealer_hand)) < 17:
        dealer_hand.append(deck.pop())
        dealer_count = count_hand(dealer_hand)
        if min(dealer_count) > 21:
            print('Dealer Bust')
    return dealer_hand,dealer_count

def eval_win(player_hand, dealer_hand):
    player_count = count_hand(player_hand)
    dealer_count = count_hand(dealer_hand)

    #check for Aces
    if 'A' in player_hand and player_count[1] <= 21:
        player_count = player_count[1]
    else:
        player_count = player_count[0]
        
    if 'A' in dealer_hand and dealer_count[1] <= 21:
        dealer_count = dealer_count[1]
    else:
        dealer_count = dealer_count[0]
    print('Your count:', player_count, 'Dealer count:', dealer_count)

    #Evaluate
    if player_count > 21:
        return 'LOSS!'
    elif dealer_count > 21:
        return 'WIN!'
    elif player_count == dealer_count:
        return 'Draw'
    elif player_count > dealer_count:
        return 'WIN!'
    elif player_count < dealer_count:
        return 'LOSS!'

results = main()
print(results)