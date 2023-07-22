def sevenBoom (arr):
    for i in arr:
        i = str(i)
        if "7" == i :
            message = "Boom!"
            break
        else :
            message = "there is no 7 in the array"
    return message

lst = [1, 2, 4, 7, 9]
print(sevenBoom (lst))