badge_priorities_score = 0


def convert_item_to_score(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


with open("day3_input.txt", 'r') as f:
    rucksacks = f.read().splitlines()  # Each rucksack becomes a list element
    elf_group = []
    start = 0
    end = len(rucksacks)
    step = 3
    # Find each group of 3 elves, find their badge, and convert that item to a score
    for i in range(start, end, step):
        elf_group = rucksacks[i:i + step]
        badge = set(rucksacks[i]).intersection(rucksacks[i+1]).intersection(rucksacks[i+2]).pop()
        badge_priorities_score += convert_item_to_score(badge)

print(badge_priorities_score)
