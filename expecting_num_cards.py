from math import comb, factorial



def need_one_card(num_cards_known: int, max_range: int = 30):
    cards_remaining = 52 - num_cards_known
    total_combinations = comb(cards_remaining, 2)
    # print(total_combinations)

    for n in range(max_range):
        outcomes_with_card = comb(n, 2) + comb(n, 1) * (cards_remaining - n)
        chance_of_finding = round(outcomes_with_card / total_combinations, 4)
        print(f"For {n} \"out\" card(s), {chance_of_finding}%")

    print("\n\n")

def main():

    # Written for clarity, not efficiency
    # --- What is the probability that you receive a card from a pile of n cards? ---
    print("-- Probability of receiving n cards --")

    # Pre-flop shown only (2/7 revealed). You need one card
    print("Pre-flop case:")
    need_one_card(2, 5)

    # Flop shown only (5/7 revealed). You need one card
    print("Flop case:")
    need_one_card(5)

    # Turn shown (6/7 revealed). You need one card
    print("Turn case:")
    need_one_card(5)

if __name__ == "__main__":
    main()

