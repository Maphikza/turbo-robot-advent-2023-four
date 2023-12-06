import time

def count_matches(winning_numbers, your_numbers):
    return len(winning_numbers & your_numbers)

# Start timing
start_time = time.time()

with open("lotto.txt", "r") as file:
    lotto_cards = [line.strip() for line in file if line.strip()]

total_cards = 0
card_copies = [1] * len(lotto_cards)  # Start with one copy of each card

for index, card in enumerate(lotto_cards):
    card_parts = card.split(":")[1].split("|")
    winning_numbers = set(card_parts[0].split())
    your_numbers = set(card_parts[1].split())

    match_count = count_matches(winning_numbers, your_numbers)
    total_cards += card_copies[index]

    for i in range(1, match_count + 1):
        next_index = index + i
        if next_index < len(lotto_cards):
            card_copies[next_index] += card_copies[index]

# End timing
end_time = time.time()

print("Total cards:", total_cards)
print("Time elapsed:", end_time - start_time)



