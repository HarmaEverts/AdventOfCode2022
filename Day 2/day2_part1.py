duel_outcomes = {'A X': 4,  # Draw + Rock
                 'B X': 1,  # Loss + Rock
                 'C X': 7,  # Win + Rock
                 'A Y': 8,  # Win + Paper
                 'B Y': 5,  # Draw + Paper
                 'C Y': 2,  # Loss + Paper
                 'A Z': 3,  # Loss + Scissors
                 'B Z': 9,  # Win + Scissors
                 'C Z': 6}  # Draw + Scissors
my_score = 0

# Open the strategy guide
with open('day2_input.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.strip('\n')
        my_score += duel_outcomes[line]

print(my_score)
