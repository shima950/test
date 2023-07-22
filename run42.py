def asc_des_none(arr, word):
    if word =='Asc':
        arr.sort()
    if word =='Des':
        arr.sort(reverse = True)
    return (arr)

print(asc_des_none([2, 3, 5, 7], 'Des'))
print(asc_des_none([5, 8, 4, 6], 'Asc'))
print(asc_des_none([5, 8, 4, 6], 'None'))