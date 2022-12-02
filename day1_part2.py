"""
--- Part Two ---

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

elves_inventory = []

with open("day1_input.txt", 'r') as f:
    lines = f.read().splitlines()
    temp_calories = 0
    for line in lines:
        if line != '':  # found an elf's calories
            temp_calories += int(line)
        else:  # found the end of what an elf carries
            elves_inventory.append(temp_calories)
            temp_calories = 0

elves_inventory.sort(reverse=True)

print(elves_inventory[0] + elves_inventory[1] + elves_inventory[2])