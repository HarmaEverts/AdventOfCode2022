class CommSystem:
    def __init__(self):
        self._cycle = 0
        self._value = 1
        self._screen = []
        for i in range(6):
            self._screen.append([])
        for i in self._screen:
            for j in range(40):
                i.append('.')

    def update_cycle(self):
        if self._cycle % 40 == self._value or self._cycle % 40 == self._value-1 or self._cycle % 40 == self._value+1:
            if self._cycle > 39:
                row_number = int(self._cycle / 40)
                column_number = self._cycle % 40
            else:
                row_number = 0
                column_number = self._cycle
            self._screen[row_number][column_number] = '#'
        self._cycle += 1

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

    def print_screen(self):
        for i in self._screen:
            print(''.join(i))


my_comm = CommSystem()

with open('day10_input.txt', 'r') as f:
    commands = f.read().splitlines()
    for line in commands:
        my_comm.execute_command(line)

my_comm.print_screen()
