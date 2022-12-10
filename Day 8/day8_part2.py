forest = []
weighed_forest = []
highest_scenic_score = 0


def calculate_tree_score(row, column):
    tree_value = forest[row][column]
    # Look up
    up_score = 0
    for row_index in reversed(range(0, row, 1)):
        up_score += 1
        if forest[row_index][column] >= tree_value:
            break
    # Look down
    down_score = 0
    for row_index in range(row+1, row_length):
        down_score += 1
        if forest[row_index][column] >= tree_value:
            break
    # Look left
    left_score = 0
    for col_index in reversed(range(0, column, 1)):
        left_score += 1
        if forest[row][col_index] >= tree_value:
            break
    # Look right
    right_score = 0
    for col_index in range(column+1, col_length):
        right_score += 1
        if forest[row][col_index] >= tree_value:
            break
    return up_score * down_score * left_score * right_score


def find_highest_scenic_score():
    highest_score = 0
    for row_index in range(row_length):
        for col_index in range(col_length):
            scenic_tree_score = calculate_tree_score(row_index, col_index)
            if scenic_tree_score > highest_score:
                highest_score = scenic_tree_score
    return highest_score


with open('day8_input.txt', 'r') as f:
    forest_input = f.read().splitlines()
    for forest_row in forest_input:
        forest_row = forest_row.replace("\n", "")
        temp_row = []
        for tree in forest_row:
            temp_row.append(int(tree))
        forest.append(temp_row)

row_length = len(forest[0])
col_length = len(forest)

highest_scenic_score = find_highest_scenic_score()
print(highest_scenic_score)
