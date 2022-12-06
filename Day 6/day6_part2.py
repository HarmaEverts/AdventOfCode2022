def check_for_duplicate(signal):
    for item in signal:
        if signal.count(item) > 1:
            return True
    return False


def find_marker(stream):
    temp_set = []
    for i in enumerate(stream):
        temp_set = stream[i[0]:i[0]+14]
        if not check_for_duplicate(temp_set):
            return i[0]+14


with open('day6_input.txt', 'r') as f:
    message = f.readline()
    marker = find_marker(message)
    print(marker)
