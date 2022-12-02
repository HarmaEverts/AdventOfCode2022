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
