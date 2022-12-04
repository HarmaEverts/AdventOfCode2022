overlapping_pairs = 0


def one_range_contains_other(elf_pair):
    section1 = elf_pair[0].split('-')
    section2 = elf_pair[1].split('-')
    elf1_range = range(int(section1[0]), int(section1[1]) + 1)
    elf2_range = range(int(section2[0]), int(section2[1]) + 1)
    if elf1_range.start in elf2_range and elf1_range[-1] in elf2_range:  # Range 1 contains range 2
        return True
    elif elf2_range.start in elf1_range and elf2_range[-1] in elf1_range:  # Range 2 contains range 1
        return True
    else:
        return False


with open('day4_input.txt', 'r') as f:
    cleaning_assignments = f.read().splitlines()
    for cleaning_assignment in cleaning_assignments:
        pair = cleaning_assignment.split(',')
        if one_range_contains_other(pair):
            overlapping_pairs += 1

print(overlapping_pairs)
