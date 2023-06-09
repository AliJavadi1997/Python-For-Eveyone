"""Write a program that reads numbers and adds them to a list if they aren’t already contained in the list.
When the list contains ten numbers, the program displays the contents and quits."""


def add_to_list():
    my_list = list()
    for i in range(10):
        num = int(input('Please enter a number: '))
        if num not in my_list:
            my_list.append(num)
    print(my_list)


add_to_list()
