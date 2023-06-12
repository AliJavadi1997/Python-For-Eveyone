# Write list functions that carry out the following tasks for a list of integers. For each function, provide a test
# program.

int_list = [1, 3, 2, 2, 5, 4, 6, 8, 2, 9, 6, 9, 0, 4, 6, 3, 7, 7]


def swap(int_list):
    """Swap the first and last elements in the list"""
    int_list[-1], int_list[0] = int_list[0], int_list[-1]
    return int_list


def shift_to_right(int_list):
    """Shift all elements by one to the right and move the last element into the first position"""
    my_list = list()
    my_list.append(int_list[-1])
    for i in range(len(int_list) - 1):
        my_list.append(int_list[i])
    return my_list


def replace_even(int_list):
    """Replace all even elements with 0"""
    for i in range(len(int_list)):
        if int_list[i] % 2 == 0:
            int_list[i] = 0
    return int_list


def replace_with_neighbour(int_list):
    """Replace each element except the first and last by the larger of its two neighbors"""
    for i in range(1, len(int_list) - 1):
        if int_list[i-1] > int_list[i+1]:
            int_list[i], int_list[i-1] =  int_list[i-1], int_list[i]
        else:
            int_list[i], int_list[i+1] = int_list[i+1], int_list[i]
    return int_list


def remove_middle(int_list):
    """Remove the middle element if the list length is odd, or the middle two elements if the length is even"""
    if len(int_list) % 2 == 1:
        middle_index = len(int_list) // 2
        int_list.pop(middle_index)
    else:
        first_middle_index = len(int_list) // 2 - 1
        second_middle_index = len(int_list) // 2
        int_list.pop(second_middle_index)
        int_list.pop(first_middle_index)
    return int_list


def move_evens(int_list):
    """Move all even elements to the front, otherwise preserving the order of the elements"""
    even_list = list()
    odd_list = list()
    for i in range(len(int_list)):
        if int_list[i] % 2 == 0:
            even_list.append(int_list[i])
        else:
            odd_list.append(int_list[i])
    return even_list + odd_list


def second_largest(int_list):
    """Return the second-largest element in the list"""
    largest = 0
    largest_2nd = 0
    for i in range(len(int_list)):
        if int_list[i] > largest_2nd:
            if int_list[i] > largest:
                largest = int_list[i]
            else:
                largest_2nd = int_list[i]
    return largest_2nd


def increasing_order(int_list):
    if int_list == sorted(int_list):
        return True
    else:
        return False


def two_adjacent(int_list):
    """Return true if the list contains two adjacent duplicate elements"""
    adjacent = 0
    for i in range(len(int_list) - 1):
        if int_list[i] == int_list[i+1]:
            adjacent += 1
    if adjacent == 2:
        return True
    else:
        return False


def duplicate(int_list):
    """Return true if the list contains duplicate elements (which need not be adjacent)."""
    is_duplicate = False
    for i in range(len(int_list)):
        for j in range(i, len(int_list)):
            if int_list[i] == int_list[j]:
                is_duplicate = True
    return is_duplicate

