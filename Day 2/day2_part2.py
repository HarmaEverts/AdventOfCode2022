duel_outcomes = {'A X': 3,  # Loss + Scissors
                 'B X': 1,  # Loss + Rock
                 'C X': 2,  # Loss + Paper
                 'A Y': 4,  # Draw + Rock
                 'B Y': 5,  # Draw + Paper
                 'C Y': 6,  # Draw + Scissors
                 'A Z': 8,  # Win + Paper
                 'B Z': 9,  # Win + Scissors
                 'C Z': 7}  # Win + Rock
my_score = 0

# Open the strategy guide
with open('day2_input.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.strip('\n')
        my_score += duel_outcomes[line]

print(my_score)
