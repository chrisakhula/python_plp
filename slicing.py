# list slicing in python
my_list = ['p','r','o','g','r','a','m','i']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# When we slice lists, the start index is inclusive but the end index is exclusive.


# adding element to a python list

numbers = [24, 14, 30, 54]

print('Before append: ', numbers)

# using append method
numbers.append(32)

print('After append: ', numbers)

prime_numbers = [2, 3, 5]
print('List1: ', prime_numbers)

even_numbers = [4, 6, 8]
print('List2: ', even_numbers)

#join two lists
prime_numbers.extend(even_numbers)
print('List after append: ', prime_numbers)
