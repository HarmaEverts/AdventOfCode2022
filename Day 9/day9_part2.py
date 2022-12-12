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

    def add_unique_knot_location(self):
        if not self.has_location_been_visited(self._x_coord, self._y_coord):
            self._unique_knot_locations.append((self._x_coord, self._y_coord))

    def has_location_been_visited(self, x, y):
        if (x, y) in self._unique_knot_locations:
            return True
        return False


class Rope:
    def __init__(self, no_of_knots):
        self._knots = []
        self._length = no_of_knots
        for i in range(no_of_knots):
            self._knots.append(Knot())

    def delta_knots(self, lead, follower):
        delta_x = lead.get_x_coord() - follower.get_x_coord()
        delta_y = lead.get_y_coord() - follower.get_y_coord()
        delta = (delta_x, delta_y)
        return delta

    def get_head_coords(self):
        return self._knots[0].get_coords()

    def set_head_coords(self, head_x, head_y):
        self._knots[0].set_coords(head_x, head_y)

    def get_head(self):
        return self._knots[0]

    def get_tail_coords(self):
        return self._knots[self._length-1].get_coords()

    def set_tail_coords(self, tail_x, tail_y):
        self._knots[self._length-1].set_coords(tail_x, tail_y)

    def get_tail(self):
        return self._knots[self._length-1]

    def is_knot_adjacent_to_knot(self, leader, follower):
        (head_x, head_y) = leader.get_coords()
        (tail_x, tail_y) = follower.get_coords()
        if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
            return True
        return False

    def is_diagonal(self, leader, follower):
        (head_x, head_y) = leader.get_coords()
        (tail_x, tail_y) = follower.get_coords()
        if abs(head_x - tail_x) == 1 and abs(head_y - tail_y) == 1:
            return True
        return False

    def drag_tail(self, leader, follower):
        if not self.is_knot_adjacent_to_knot(leader, follower):
            delta_x, delta_y = self.delta_knots(leader, follower)
            if abs(delta_x) == 0 or abs(delta_x) == 1:
                follower.set_x_coord(leader.get_x_coord())
                if delta_y == 2:
                    follower.set_y_coord(leader.get_y_coord() - 1)
                else:  # delta_y == -2
                    follower.set_y_coord(leader.get_y_coord() + 1)
            elif abs(delta_y) == 0 or abs(delta_y) == 1:
                follower.set_y_coord(leader.get_y_coord())
                if delta_x == 2:
                    follower.set_x_coord(leader.get_x_coord() - 1)
                else:  # delta_x == -2
                    follower.set_x_coord(leader.get_x_coord() + 1)
            elif abs(delta_x) == 2 and abs(delta_y) == 2:
                if delta_x == 2:
                    if delta_y == 2:
                        follower.set_coords(leader.get_x_coord()-1, leader.get_y_coord()-1)
                    elif delta_y == -2:
                        follower.set_coords(leader.get_x_coord()-1, leader.get_y_coord()+1)
                elif delta_x == -2:
                    if delta_y == 2:
                        follower.set_coords(leader.get_x_coord()+1, leader.get_y_coord()-1)
                    elif delta_y == -2:
                        follower.set_coords(leader.get_x_coord()+1, leader.get_y_coord()+1)
            else:
                print('Unexpected: not -2 <= delta_x <= 2')

    def move_rope(self, current_command):
        direction, distance = current_command.split()
        print(current_command)
        # Move Head, then Tail
        for move in range(int(distance)):
            if direction == 'U':  # y++
                self.get_head().move_up()
                for i in range(self._length-1):
                    leader = self._knots[i]
                    follower = self._knots[i+1]
                    self.drag_tail(leader, follower)
            elif direction == 'D':  # y--
                self.get_head().move_down()
                for i in range(self._length - 1):
                    leader = self._knots[i]
                    follower = self._knots[i + 1]
                    self.drag_tail(leader, follower)
            elif direction == 'L':  # x--:
                self.get_head().move_left()
                for i in range(self._length - 1):
                    leader = self._knots[i]
                    follower = self._knots[i + 1]
                    self.drag_tail(leader, follower)
            else:  # R x++
                self.get_head().move_right()
                for i in range(self._length - 1):
                    leader = self._knots[i]
                    follower = self._knots[i + 1]
                    self.drag_tail(leader, follower)
            self._knots[self._length-1].add_unique_knot_location()


with open('day9_input.txt', 'r') as f:
    my_rope = Rope(10)
    commands = f.read().splitlines()
    for command in commands:
        my_rope.move_rope(command)

print(len(my_rope.get_tail().get_unique_knot_locations()))
