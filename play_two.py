from collections import deque

def count_matches(winning_numbers, your_numbers):
    return len(winning_numbers.intersection(your_numbers))

with open("lotto.txt", "r") as file:
    lotto_cards = [line.strip() for line in file if line.strip()]

total_cards = len(lotto_cards)  # Start with the original set of cards
queue = deque()

# Add initial set of cards to the queue
for card_index in range(len(lotto_cards)):
    queue.append((card_index, lotto_cards[card_index]))

while queue:
    card_index, card = queue.popleft()
    card_parts = card.split(":")[1].split("|")
    winning_numbers = set(card_parts[0].split())
    your_numbers = set(card_parts[1].split())

    match_count = count_matches(winning_numbers, your_numbers)

    # Generate copies of the next cards in sequence based on match count
    for i in range(1, match_count + 1):
        next_card_index = card_index + i
        if next_card_index < len(lotto_cards):
            queue.append((next_card_index, lotto_cards[next_card_index]))
            total_cards += 1  # Count each new copy

print(total_cards)


