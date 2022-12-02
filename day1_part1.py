max_calories = 0

with open("day1_input.txt", 'r') as f:
    lines = f.read().splitlines()
    temp_calories = 0
    for line in lines:
        if line != '': # found an elf's calories
            temp_calories += int(line)
        else: # found the end of what an elf carries
            if temp_calories > max_calories:
                max_calories = temp_calories
            temp_calories = 0

print(max_calories)