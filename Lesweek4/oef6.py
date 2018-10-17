import random

def get_random_item(a_list):
    return a_list[random.randint(0,len(a_list))]

lst_nmbrs = [15,2,3,74,5,6,87,8,9]
lst_months = ["jan", "feb", "mar", "apr", "may", "june", "july"]

print(get_random_item(lst_nmbrs))
print(get_random_item(lst_months))