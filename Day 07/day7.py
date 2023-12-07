card_strengths = {'A': 'm', 'K': 'l', 'Q': 'k', 'J': 'j', 'T': 'i', '9': 'h', '8': 'g', '7': 'f', '6': 'e', '5': 'd', '4': 'c', '3': 'b', '2': 'a'}
card_strengths_joker = {'A': 'm', 'K': 'l', 'Q': 'k', 'J': 'a', 'T': 'j', '9': 'i', '8': 'h', '7': 'g', '6': 'f', '5': 'e', '4': 'd', '3': 'c', '2': 'b'}

def get_hands(file):
    return [(line.split(' ')[0], int(line.split(' ')[1])) for line in open(file).read().splitlines()]

def get_hand_value(hand):
    distincts = set(hand)
    if len(distincts) == 1:
        return 7
    elif len(distincts) == 2:
        aux_hand = hand.replace(hand[0], "")
        if len(aux_hand) == 1 or len(aux_hand) == 4:
            return 6
        return 5
    elif len(distincts) == 3:
        aux_hand = hand.replace(hand[0], "")
        if len(aux_hand) == 2:
            return 4
        elif len(aux_hand) == 4:
            aux_hand = aux_hand.replace(aux_hand[0], "")
            if len(aux_hand) == 2:
                return 3
            return 4
        return 3
    elif len(distincts) == 4:
        return 2
    return 1

def get_hand_strength(hand, strengths):
    return ''.join([strengths[card] for card in hand])

def transform_joker(hand):
    from collections import Counter
    try:
        return hand.replace('J', Counter(hand.replace('J', '')).most_common(1)[0][0])
    except:
        return 'AAAAA'
    
def get_total_winnings(hands):
    hands = sorted(hands, key=lambda x: (get_hand_value(x[0]), get_hand_strength(x[0], card_strengths)))
    return sum([(i + 1) * hand[1] for i, hand in enumerate(hands)])

def get_total_winnings_joker(hands):
    hands = sorted(hands, key=lambda x: (get_hand_value(transform_joker(x[0])), get_hand_strength(x[0], card_strengths_joker)))
    return sum([(i + 1) * hand[1] for i, hand in enumerate(hands)])

print(get_total_winnings(get_hands("input.txt")))
print(get_total_winnings_joker(get_hands("input.txt")))
