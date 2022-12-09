forest = []
visible_trees = []


def view_rows_left_to_right(trees):
    row_length = len(trees[0])
    col_length = len(trees)
    for row_index in range(row_length):
        max_height = -1
        for col_index in range(col_length):
            tree_height = trees[row_index][col_index]
            if tree_height > max_height:
                if (row_index, col_index) not in visible_trees:
                    visible_trees.append((row_index, col_index))
                max_height = tree_height
            if max_height == 9:
                break


def view_rows_right_to_left(trees):
    row_length = len(trees[0])
    col_length = len(trees)
    for row_index in range(row_length):
        max_height = -1
        for col_index in reversed(range(col_length)):
            tree_height = trees[row_index][col_index]
            if tree_height > max_height:
                if (row_index, col_index) not in visible_trees:
                    visible_trees.append((row_index, col_index))
                max_height = tree_height
            if max_height == 9:
                break


def view_columns_top_to_bottom(trees):
    row_length = len(trees[0])
    col_length = len(trees)
    for col_index in range(row_length):
        max_height = -1
        for row_index in range(col_length):
            if trees[row_index][col_index] > max_height:
                if (row_index, col_index) not in visible_trees:
                    visible_trees.append((row_index, col_index))
                max_height = trees[row_index][col_index]
            if max_height == 9:
                break


def view_columns_bottom_to_top(trees):
    row_length = len(trees[0])
    col_length = len(trees)
    for col_index in range(row_length):
        max_height = -1
        for row_index in reversed(range(col_length)):
            if trees[row_index][col_index] > max_height:
                if (row_index, col_index) not in visible_trees:
                    visible_trees.append((row_index, col_index))
                max_height = trees[row_index][col_index]
            if max_height == 9:
                break


with open('day8_input.txt', 'r') as f:
    forest_input = f.read().splitlines()
    for forest_row in forest_input:
        forest_row = forest_row.replace("\n", "")
        temp_row = []
        for tree in forest_row:
            temp_row.append(int(tree))
        forest.append(temp_row)


view_rows_left_to_right(forest)
view_rows_right_to_left(forest)
view_columns_top_to_bottom(forest)
view_columns_bottom_to_top(forest)

print(len(visible_trees))
