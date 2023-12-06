with open("lotto.txt", "r") as file:
    lotto_numbers_list = file.read().split("\n")

total_sum = 0

for card in lotto_numbers_list:
    if not card:
        continue  # Skip empty lines

    card_parts = card.split(":")[1].split("|")
    winning_numbers = set(card_parts[0].split())
    your_numbers = set(card_parts[1].split())

    matches = winning_numbers.intersection(your_numbers)
    points = 0

    if matches:
        points = 1  # Initial point for the first match
        for _ in range(len(matches) - 1):
            points *= 2  # Double the points for each additional match

    total_sum += points

print(total_sum)
