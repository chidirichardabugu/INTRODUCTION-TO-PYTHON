def set_duplicate(number):
    unique_number = set(number)
    sorted_number = sorted(unique_number, reverse=True)
    return sorted_number


original_list =[2,8,7,18,31,31,5,16,3,2,8]
new_list=set_duplicate(original_list)
print(new_list)