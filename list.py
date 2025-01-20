# list type in python
# The list class provides a mutable sequence of elements

empty_list = list()
print('empty_list ->', empty_list)
list_str = list('hello')
print('list_str ->', list_str)
list_tup = list((1, 2, (3, 5, 7)))
print('list_tup ->', list_tup)
empty_list = []
print('empty_list ->', empty_list)
list_syn = [3, 4, 'a', 'b']
print('list_syn ->', list_syn)
print("'a' in list_syn ->", 1 not in list_syn)
empty_list.append(5)
print('empty_list ->', empty_list)
empty_list.append([6,7])
print('empty_list ->', empty_list)
last_elem = empty_list.pop()
print('last_elem ->', last_elem)
print('empty_list ->', last_elem)
empty_list.extend([6, 7])
print('empty_list ->', empty_list)
first_elem = empty_list.pop(0)
print('first_elem ->', first_elem)
print('empty_list ->', empty_list)
empty_list.insert(0, 10)
print('empty_list ->', empty_list)
empty_list.insert(3, 100)
print('empty_list ->', empty_list)
empty_list.remove(7)
print('empty_list ->', empty_list)
empty_list.clear()
print('empty_list ->', empty_list)
print('list_str ->', list_str)
print('min(list_str) ->', min(list_str))
print('max(list_str) ->', max(list_str))
print('sorted(list_str) ->', sorted(list_str))
print('list_str ->', list_str)
list_str.sort()
print('list_str ->', list_str)
list_str.reverse()
print('list_str ->', list_str)
print('list_str.count("o") ->', list_str.count("o"))
print('list_str.index("o") ->', list_str.index("o"))
