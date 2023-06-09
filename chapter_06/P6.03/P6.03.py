"""Write a program that adds all numbers from 2 to 10,000 to a list.Then remove the multiples of 2 (but not 2),
multiples of 3 (but not 3), and so on, up to the multiples of 100. Print the remaining values."""

numbers = list()
# add numbers from 2 to 10000 to the list
for i in range(2, 10001):
    numbers.append(i)
# remove multiples of 2, 3, ..., 100
for i in range(2, 101):
    numbers = [x for x in numbers if x % i != 0 or x == i]
print(numbers)
