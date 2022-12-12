class Monkey:
    def __init__(self):
        self.name = ''
        self.number = 0
        self.items = []
        self.operation = ''
        self.divisible_by = -1
        self.test_true = -1
        self.test_false = -1
        self.old = 'old'
        self.operand = ''
        self.value = 0
        self.no_of_inspections = 0


class Troop:
    def __init__(self):
        self._troop = []

    def add_monkey(self, monkey):
        self._troop.append(monkey)

    def get_troop(self):
        return self._troop

    def play_round(self):
        for monkey in self._troop:
            self.throw_items(monkey)

    def throw_items(self, monkey):
        if not monkey.items == []:  # Monkey does not have empty hands
            for current_item in monkey.items:
                monkey.no_of_inspections += 1
                # Inspect item: execute operation
                if monkey.operand == '*':
                    if monkey.value == 'old':
                        current_item *= current_item
                    else:
                        current_item *= int(monkey.value)
                elif monkey.operand == '+':
                    if monkey.value == 'old':
                        current_item += current_item
                    else:
                        current_item += int(monkey.value)
                else:
                    print('Operand not supported')
                # Reduce worry level
                current_item = int(current_item/3)
                if current_item % monkey.divisible_by == 0:
                    self._troop[monkey.test_true].items.append(current_item)
                else:
                    self._troop[monkey.test_false].items.append(current_item)
            # Now delete the items that were thrown to other monkeys
            # (could not do that immediately because it messed with the for loop)
            monkey.items = []


my_troop = Troop()

with open('day11_input.txt', 'r') as f:
    monkey_commands = f.read().splitlines()
    for command in monkey_commands:
        if command == '':  # End of monkey definition
            continue
        elif command[:6] == 'Monkey':  # Found new monkey
            current_monkey = Monkey()
            my_troop.add_monkey(current_monkey)
            current_monkey.name = command
            current_monkey.number = int(command[7])
        elif command[2] == 'S':  # Starting items
            starting_items = command[18:].split(', ')
            for item in starting_items:
                current_monkey.items.append(int(item))
        elif command[2] == 'O':  # Operation
            current_monkey.operation = command[19:]
            current_monkey.operand = current_monkey.operation[4]
            current_monkey.value = current_monkey.operation[6:]  # Can be 'old' or an integer
        elif command[2] == 'T':  # Test
            current_monkey.divisible_by = int(command[21:])
        elif command[:11] == '    If true':  # true
            current_monkey.test_true = int(command[29:])
        elif command[:12] == '    If false':  # false
            current_monkey.test_false = int(command[30:])

for i in range(20):
    my_troop.play_round()

monkey_operations = []
for monkey in my_troop.get_troop():
    monkey_operations.append(monkey.no_of_inspections)

monkey_operations.sort(reverse=True)

result = monkey_operations[0]*monkey_operations[1]

print(result)