from math import comb, factorial


def need_cards(cards_remaining: int = 50, cards_needed: int = 1):
    max_range = 30
    # cards_remaining = 50
    cards_to_be_shown = 7 - (52 - cards_remaining)

    total_combinations = comb(cards_remaining, cards_to_be_shown)
    # print(total_combinations)

    for n in range(20):
        outcomes_with_card = 0
        for i in range(cards_to_be_shown):
            # Pick one from the outs, then the rest from the deck
            if cards_needed < cards_to_be_shown - i: # Allows for picking 2 or more cards
                continue
            else :
                outcomes_with_card += comb(n, cards_to_be_shown - i) * comb(cards_remaining - n - cards_to_be_shown + i, i)

        chance_of_finding = round((outcomes_with_card / total_combinations)*100, 2)
        print(f"For {n} \"out\" card(s), {chance_of_finding}%")
    print("\n\n")


def main():

    # Written for clarity, not efficiency
    # --- What is the probability that you receive a card from a pile of n cards? ---
    print("---- Probability of receiving n cards ----")

    # Pre-flop shown only (2/7 revealed). You need one card
    print("Pre-flop case:")
    need_cards(50, 1)
    need_cards(50, 2)

    # cards_remaining = 50
    # total_combinations = comb(cards_remaining, 5)
    # print(total_combinations)

    # for n in range(20):
    #     outcomes_with_card = 0
    #     for i in range(5):
    #         outcomes_with_card += comb(n, 5-i)*comb(cards_remaining - n - 5 + i, i)
    #     chance_of_finding = round(outcomes_with_card / total_combinations, 6)
    #     print(f"For {n} \"out\" card(s), {chance_of_finding}%")

    # need_one_card(2)

    # Flop shown only (5/7 revealed). You need one card
    # print("Flop case:")
    # need_cards(47)
    # need_one_card(5)

    # Turn shown (6/7 revealed). You need one card
    # print("Turn case:")
    # need_cards(46)
    # need_one_card(6)

if __name__ == "__main__":
    main()

