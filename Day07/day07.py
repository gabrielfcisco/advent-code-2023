from collections import Counter


def part1(hand):

    card_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    categories = {
        "high": [],
        "one": [],
        "two": [],
        "three": [],
        "full": [],
        "four": [],
        "five": [],
    }

    for card in hand:
        count = list(Counter(card[0]).values())
        if 5 in count:
            categories["five"].append(card)
        elif 4 in count:
            categories["four"].append(card)
        elif 3 in count and 2 in count:
            categories["full"].append(card)
        elif 3 in count:
            categories["three"].append(card)
        elif 2 in count:
            if count.count(2) > 1:
                categories["two"].append(card)
            else:
                categories["one"].append(card)
        else:
            categories["high"].append(card)

    for category, data in categories.items():
        categories[category] = sorted(
            data, key=lambda x: [card_values[card] for card in x[0]], reverse=True)[::-1]

    sorted_hands = [hand for category in categories.values()
                    for hand in category]

    return sum((i + 1) * int(card[1])
               for i, card in enumerate(sorted_hands))


def part2(hand):

    card_values = {
        "J": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "Q": 11,
        "K": 12,
        "A": 13
    }

    categories = {
        "high": [],
        "one": [],
        "two": [],
        "three": [],
        "full": [],
        "four": [],
        "five": [],
    }

    for card in hand:

        jokers = card[0].count("J")
        count = [c for c in card[0] if c != 'J']

        count = sorted(Counter(count).values(), reverse=True)

        if not count:
            count.append(0)
        if count[0] + jokers == 5:
            categories["five"].append(card)
        elif count[0] + jokers == 4:
            categories["four"].append(card)
        elif count[0] + jokers == 3 and count[1] == 2:
            categories["full"].append(card)
        elif count[0] + jokers == 3:
            categories["three"].append(card)
        elif count[0] == 2 and (jokers or count[1] == 2):
            categories["two"].append(card)
        elif count[0] + jokers == 2:
            categories["one"].append(card)
        else:
            categories["high"].append(card)

    for category, data in categories.items():
        categories[category] = sorted(
            data, key=lambda x: [card_values[card] for card in x[0]], reverse=True)[::-1]

    sorted_hands = [hand for category in categories.values()
                    for hand in category]

    return sum((i + 1) * int(card[1])
               for i, card in enumerate(sorted_hands))


if __name__ == "__main__":
    with open("test.txt", "r", encoding="utf-8") as f:
        fileInput = f.read()
        lines = fileInput.split('\n')
        dataInput = [line.split(" ") for line in lines]
        print(f"Part 1: {part1(dataInput)}")
        print(f"Part 2: {part2(dataInput)}")
