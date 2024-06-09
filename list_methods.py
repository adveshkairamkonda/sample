my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
another_list = [4, 5, 6]
my_list.extend(another_list)
print(my_list)  # Output: [1, 2, 3, 4, 4, 5, 6]
my_list.insert(1, 5)
print(my_list)  # Output: [1, 5, 2, 3, 4, 4, 5, 6]
my_list.remove(2)
print(my_list)  # Output: [1, 5, 3, 4, 4, 5, 6]
popped_element = my_list.pop(1)
print(popped_element)  # Output: 5
print(my_list)  # Output: [1, 3, 4, 4, 5, 6]
index = my_list.index(3)
print(index)  # Output: 1
count = my_list.count(4)
print(count)  # Output: 2
my_list.sort()
print(my_list)  # Output: [1, 3, 4, 4, 5, 6]
my_list.reverse()
print(my_list)  # Output: [6, 5, 4, 4, 3, 1]
copy_of_list = my_list.copy()
print(copy_of_list)  # Output: [6, 5, 4, 4, 3, 1]


