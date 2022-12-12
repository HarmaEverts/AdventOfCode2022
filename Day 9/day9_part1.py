class Knot:
    def __init__(self):
        self._x_coord = 0
        self._y_coord = 0
        self._unique_knot_locations = [(0, 0)]

    def get_coords(self):
        coords = (self._x_coord, self._y_coord)
        return coords

    def set_coords(self, x, y):
        self._x_coord = x
        self._y_coord = y

    def get_x_coord(self):
        return self._x_coord

    def set_x_coord(self, x):
        self._x_coord = x

    def get_y_coord(self):
        return self._y_coord

    def set_y_coord(self, y):
        self._y_coord = y

    def move_right(self):
        self._x_coord += 1

    def move_left(self):
        self._x_coord -= 1

    def move_up(self):
        self._y_coord += 1

    def move_down(self):
        self._y_coord -= 1

    def get_unique_knot_locations(self):
        return self._unique_knot_locations

    def add_unique_knot_location(self, x, y):
        self._unique_knot_locations.append((x, y))

    def has_location_been_visited(self, x, y):
        if (x, y) in self._unique_knot_locations:
            return True
        return False


class Rope:
    def __init__(self):
        self._Head = Knot()
        self._Tail = Knot()

    def get_head_coords(self):
        return self._Head.get_coords()

    def set_head_coords(self, head_x, head_y):
        self._Head.set_coords(head_x, head_y)

    def get_head(self):
        return self._Head

    def get_tail_coords(self):
        return self._Tail.get_coords()

    def set_tail_coords(self, tail_x, tail_y):
        self._Tail.set_coords(tail_x, tail_y)

    def get_tail(self):
        return self._Tail

    def is_tail_adjacent_to_head(self):
        (head_x, head_y) = self.get_head_coords()
        (tail_x, tail_y) = self.get_tail_coords()
        if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
            return True
        return False

    def is_diagonal(self):
        (head_x, head_y) = self.get_head_coords()
        (tail_x, tail_y) = self.get_tail_coords()
        if abs(head_x - tail_x) == 1 and abs(head_y - tail_y) == 1:
            return True
        return False

    def drag_tail(self, direction):
        if not self.is_tail_adjacent_to_head():
            if direction == 'U' or direction == 'D':
                # Vertical move, pull to x value
                self.get_tail().set_x_coord(self.get_head().get_x_coord())
                # Now move y value to adjacent tile in the set direction
                if direction == 'U':
                    self.get_tail().set_y_coord(self.get_head().get_y_coord() - 1)
                else:
                    self.get_tail().set_y_coord(self.get_head().get_y_coord() + 1)
            else:
                # Horizontal move, pull to y value
                self.get_tail().set_y_coord(self.get_head().get_y_coord())
                # Now move x value to adjacent tile in the set direction
                if direction == 'L':
                    self.get_tail().set_x_coord(self.get_head().get_x_coord() + 1)
                else:
                    self.get_tail().set_x_coord(self.get_head().get_x_coord() - 1)

    def move_rope(self, current_command):
        direction, distance = current_command.split()
        # Move Head, then Tail
        for move in range(int(distance)):
            if direction == 'U':  # y++
                self.get_head().move_up()
                self.drag_tail(direction)
            elif direction == 'D':  # y--
                self.get_head().move_down()
                self.drag_tail(direction)
            elif direction == 'L':  # x--:
                self.get_head().move_left()
                self.drag_tail(direction)
            else:  # R x++
                self.get_head().move_right()
                self.drag_tail(direction)
            if not self.get_tail().has_location_been_visited(self.get_tail().get_x_coord(), self.get_tail().get_y_coord()):
                self.get_tail().add_unique_knot_location(self.get_tail().get_x_coord(), self.get_tail().get_y_coord())


with open('day9_test_input.txt', 'r') as f:
    my_rope = Rope()
    commands = f.read().splitlines()
    for command in commands:
        my_rope.move_rope(command)

print(len(my_rope.get_tail().get_unique_knot_locations()))
