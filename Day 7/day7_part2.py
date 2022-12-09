class File:
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size


class Directory:
    def __init__(self):
        self._parent = None
        self._name = None
        self._subdirectories = []
        self._files = []
        self._directory_size = 0

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def add_subdirectory(self, subdirectory):
        self._subdirectories.append(subdirectory)

    def add_file(self, file):
        self._files.append(file)

    def get_subdirectory(self, name):
        if len(self._subdirectories) > 0:
            for subdir in self._subdirectories:
                if subdir.get_name() == name:
                    return subdir

    def find_subdirectory(self, name):
        if self._subdirectories:
            for subdir in self._subdirectories:
                if subdir.get_name() == name:
                    return True
        return False

    def has_subdirectory(self):
        if self._subdirectories:
            return True
        return False

    def get_subdirectories(self):
        return self._subdirectories

    def get_files(self):
        return self._files

    def total_file_size(self):
        total = 0
        for file in self._files:
            total += file.get_size()
        return total

    def calculate_directory_size(self):
        self._directory_size = self.total_file_size()
        if self.has_subdirectory():
            for subdir in self.get_subdirectories():
                subdir.calculate_directory_size()
                self._directory_size += subdir.get_directory_size()

    def get_directory_size(self):
        return self._directory_size


def find_all_directories(directory):
    all_dir_sizes.append(directory.get_directory_size())
    if directory.has_subdirectory():
        for subdirectory in directory.get_subdirectories():
            find_all_directories(subdirectory)


def create_structure(commands):
    root_directory = Directory()
    root_directory.set_name('Filesystem')
    current_directory = root_directory
    for line in commands:
        if line[0:4] == '$ cd':  # Change directory
            if line[4:7] == ' ..':  # Move up
                current_directory = current_directory.get_parent()
            else:  # Move into
                directory_name = line[5:]
                if current_directory.find_subdirectory(directory_name):
                    current_directory = current_directory.get_subdirectory(directory_name)
                else:  # Somehow, directory does not exist yet
                    temp_directory = Directory()
                    temp_directory.set_name(line[5:])
                    temp_directory.set_parent(current_directory)
                    current_directory.add_subdirectory(temp_directory)
                    current_directory = temp_directory
        elif line[0:4] == '$ ls':  # Inspect directory
            pass
        elif line[0:3] == 'dir':  # Found directory
            temp_dir = Directory()
            temp_dir.set_name(line[4:])
            temp_dir.set_parent(current_directory)
            current_directory.add_subdirectory(temp_dir)
        else:  # Found file
            [temp_size, temp_filename] = line.split(' ')
            temp_file = File(temp_filename, int(temp_size))
            current_directory.add_file(temp_file)
    return root_directory


def print_dir_tree(dir_tree, level):
    print(level*'\t' + "dir " + dir_tree.get_name() + " with size " + str(dir_tree.get_directory_size()) + " contains: ")
    for directory in dir_tree.get_subdirectories():
        print_dir_tree(directory, level+1)
    for file in dir_tree.get_files():
        print((level+1)*'\t' + "file " + file.get_name() + " with size " + str(file.get_size()))


with open('day7_input.txt', 'r') as f:
    filesystem_input = f.read().splitlines()
    filesystem = create_structure(filesystem_input)
    filesystem.calculate_directory_size()
    all_dir_sizes = []
    find_all_directories(filesystem)
    total_used = filesystem.get_subdirectory('/').get_directory_size()
    free_space = 70000000 - total_used
    to_be_deleted = 30000000 - free_space
    all_dir_sizes.sort()
    result = 0
    for dir_size in all_dir_sizes:
        if dir_size > to_be_deleted:
            result = dir_size
            break
    print(result)
