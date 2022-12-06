stack_input = []


def clean_up_stacks():
    for row_index, row in enumerate(stacks):
        for col_index, item in reversed(list(enumerate(row))):
            if stacks[row_index][col_index][0] != '[':
                del stacks[row_index][col_index]
        stacks[row_index].reverse()
    return stacks


def convert_input(stack_information):
    my_stacks = [[]]
    list(enumerate(stack_information))
    for index, stack_info in enumerate(stack_information):
        # First part defines the stacks
        # Split up line into groups of 4 characters
        boxes = [(stack_info[i:i + 4]) for i in range(0, len(stack_info), 4)]
        # Put each item onto its corresponding stack
        for i, item in enumerate(boxes):
            if i >= len(my_stacks):
                my_stacks.append([])
            my_stacks[i].append(item)
        # Second part defines the moves
        if stack_info == '':
            my_moves = stack_information[index + 1:]
            return [my_stacks, my_moves]


def execute(move, my_stacks):
    source_stack = int(move[3])-1
    target_stack = int(move[5])-1
    intermediate_stack = []
    for i in range(int(move[1])):
        box = my_stacks[source_stack].pop()
        intermediate_stack.append(box)
    my_stacks[target_stack].extend(reversed(intermediate_stack))
    return my_stacks


def parse_moves(my_stacks):
    for move in moves:
        assignment = move.split(' ')
        execute(assignment, my_stacks)
    return my_stacks


with open('day5_input.txt', 'r') as f:
    stack_input = f.read().splitlines()

[stacks, moves] = convert_input(stack_input)
stacks = clean_up_stacks()
stacks = parse_moves(stacks)

result = ''
for stack in stacks:
    result += stack[len(stack)-1][1]

print(result)
