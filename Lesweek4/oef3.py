list_numbers = []

for nmbr in range(1,483,13):
    list_numbers.append(nmbr)

    print(list_numbers)
    list_numbers.reverse()
    print(list_numbers)

    list_numbers.remove(469)
    print(list_numbers)
    list_numbers.pop(-5)
    print(list_numbers)

    del list_numbers[0]
    print(list_numbers)

