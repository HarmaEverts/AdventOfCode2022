priorities_score = 0


def convert_item_to_score(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


with open("day3_input.txt", 'r') as f:
    rucksacks = f.read().splitlines()  # Each rucksack becomes a list element
    for rucksack in rucksacks:
        halfway_point = int(len(rucksack) / 2)
        compartment1 = rucksack[:halfway_point]
        compartment2 = rucksack[halfway_point:]
        common_item = set(compartment1).intersection(compartment2).pop()
        # Convert common_item to score and add to total
        priorities_score += convert_item_to_score(common_item)

print(priorities_score)
