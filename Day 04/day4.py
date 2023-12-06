from collections import Counter

def get_cards(file):
    cards = [card.split(': ')[1].split(' | ') for card in open(file).read().splitlines()]
    for card in cards:
        card[0] = set(card[0].split(' '))
        card[1] = set(card[1].split(' '))
        card[0].discard('')
        card[1].discard('')
    return cards

def get_num_matches(card):
    return len(card[0].intersection(card[1]))

def get_card_prize(card):
    num_matches = get_num_matches(card)
    return 2**(num_matches - 1) if num_matches > 0 else 0

def get_total_prize(cards):
    result = 0
    for card in cards:
        result += get_card_prize(card)
    return result

def get_total_scratchcards(cards):
    cards_counter = Counter({i+1: 1 for i in range(len(cards))})
    for i, card in enumerate(cards):
        for j in range(get_num_matches(card)):
            cards_counter[(i + 1) + (j + 1)] += cards_counter[i + 1]
    return sum(cards_counter.values())

def solve_advent_day4(file):
    cards = get_cards(file)
    print("Part 1: ", get_total_prize(cards))
    print("Part 2: ", get_total_scratchcards(cards))

solve_advent_day4('input.txt')
