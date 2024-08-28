def get_even_num(myNum):
    evenNum = []
    for num in myNum:
        if num % 2 == 0:
            evenNum.append(num)
    return evenNum
    
original_list = [1, 2, 3, 4, 6, 7, 8]
even_list = get_even_num(original_list)
print("Original list:", original_list)
print("even_list:", even_list)