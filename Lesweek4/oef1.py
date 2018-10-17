def print_list(a_list, name_list):
    print("verzameling {0}".format(name_list))
    for item in a_list:
        print("item {0} zit op positie {1}".format(item, a_list.index(item)))

list1 = [1,2,3,4]
list2 = [1.0,1.1,1.2,1.3,1.4,1.5]
list3 = ["jan","piet","joris"]

print_list("list1", list1)
print_list("list2", list2)
print_list("list3", list3)
