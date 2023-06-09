fom random import randint
# make a list of random int
list_int = []
for i in range(10):
    list_int.append(randint(0, 11))

# print even index elements
even_index = []
for i in range(len(list_int)):
    if i % 2 == 0:
        even_index.append(list_int[i])
print(f"Even index elements:\t{even_index}")

# print all even elements
even_int = []
for i in range(len(list_int)):
    if list_int[i] % 2 == 0:
        even_int.append(list_int[i])
print(f"Even elements:\t{even_int}")

# print all elements in reverse order
reverse_list = list_int.reverse()
print(f"All elements in reverse order:\t{reverse_list}")

# print only the first and last element
print(f"Only the first and last element:\t{list_int[0]}, {list_int[-1]}")

