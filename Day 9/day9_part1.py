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

    def update_x_coord(self, direction, distance):
        if direction == 'L':
            self.set_x_coord(self.get_x_coord()-distance)
        else:  # R
            self.set_x_coord(self.get_x_coord()+distance)

    def get_y_coord(self):
        return self._y_coord

    def set_y_coord(self, y):
        self._y_coord = y

    def update_y_coord(self, direction, distance):
        if direction == 'U':
            self.set_y_coord(self.get_y_coord()+distance)
        else:  # D
            self.set_y_coord(self.get_y_coord()-distance)

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

    def delta_knots(self, lead, follower):
        delta_x = lead.get_x_coord() - follower.get_x_coord()
        delta_y = lead.get_y_coord() - follower.get_y_coord()
        delta = (delta_x, delta_y)
        return delta

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
            print('\t\tThe tail is not adjacent to the head')
            (head_x, head_y) = self.get_head_coords()
            (tail_x, tail_y) = self.get_tail_coords()
            delta_x, delta_y = self.delta_knots(self.get_head(), self.get_tail())
            if direction == 'U' or direction == 'D':
                # Vertical move, pull to x value
                self.get_tail().set_x_coord(self.get_head().get_x_coord())
                print('\t\tMoved the tail to the head\'s column')
                # Now move y value to adjacent tile in the set direction
                if direction == 'U':
                    self.get_tail().set_y_coord(self.get_head().get_y_coord() - 1)
                    print('\t\tMoved tail up towards the head')
                else:
                    self.get_tail().set_y_coord(self.get_head().get_y_coord() + 1)
                    print('\t\tMoved tail down towards the head')
            else:
                # Horizontal move, pull to y value
                self.get_tail().set_y_coord(self.get_head().get_y_coord())
                print('\t\tMoved the tail to the head\'s row')
                # Now move x value to adjacent tile in the set direction
                if direction == 'L':
                    self.get_tail().set_x_coord(self.get_head().get_x_coord() + 1)
                    print('\t\tMoved tail left towards the head')
                else:
                    self.get_tail().set_x_coord(self.get_head().get_x_coord() - 1)
                    print('\t\tMoved tail right towards the head')

    def move_rope(self, current_command):
        direction, distance = current_command.split()
        # Move Head, then Tail
        for move in range(int(distance)):
            print('Before move: ')
            print('\tHead: ' + str(self.get_head_coords()))
            print('\tTail: ' + str(self.get_tail_coords()))
            if direction == 'U':  # y++
                self.get_head().move_up()
                print("\tMoved head 1 up")
                self.drag_tail(direction)
            elif direction == 'D':  # y--
                self.get_head().move_down()
                print("\tMoved head 1 down")
                self.drag_tail(direction)
            elif direction == 'L':  # x--:
                self.get_head().move_left()
                print("\tMoved head 1 left")
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
