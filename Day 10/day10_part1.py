class CommSystem:
    def __init__(self):
        self._cycle = 0
        self._value = 1
        self._log = []

    def update_cycle(self):
        self._cycle += 1
        if self._cycle % 40 == 20:
            self._log.append(self._cycle * self._value)

    def update_value(self, value):
        self._value += value

    def execute_command(self, command):
        if command[0] == 'a':
            (function, value) = command.split()
        else:
            function = command
        if function == 'noop':
            self.update_cycle()
        elif function == 'addx':
            self.update_cycle()
            self.update_cycle()
            self.update_value(int(value))
        else:
            print('Unknown command')

    def get_log_total(self):
        total = 0
        for entry in self._log:
            total += entry
        return total


my_comm = CommSystem()

with open('day10_input.txt', 'r') as f:
    commands = f.read().splitlines()
    for line in commands:
        my_comm.execute_command(line)

result = my_comm.get_log_total()
print(str(result))
