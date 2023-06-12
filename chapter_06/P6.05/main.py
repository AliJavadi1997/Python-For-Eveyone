# Modify the largest.py program in Section6.3 to mark both the smallest and the largest elements.

def largest_and_smallest(int_list):
    largest = int_list[0]
    smallest = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > largest:
            largest = int_list[i]
        if int_list[i] < smallest:
            smallest = int_list[i]
    return smallest, largest
