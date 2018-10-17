def max_num_in_list(a_list):
    max = a_list[0]
    for nmbr in a_list:
        if nmbr > max:
            max = nmbr
    return max

lst_mnbrs = [2,5,10,1,3]
print(max_num_in_list("Het maximum is: {0}".format(lst_mnbrs)))