import random

my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(my_list[3])
rand = random.randint(0, (len(my_list)-1))
my_returned_value = my_list.pop(rand)
my_list.append(10)
my_list.extend('1')
my_list.reverse()
my_list = my_list + my_list
print(my_list)
print(my_returned_value)
print(len(my_list))