#تابعی ایجاد کنید که لیستی از اعداد و یک رشته  را در ورودی بگیرد و فهرستی از اعداد را طبق قوانین زیر برگرداند

def asc_des_none(arr, word):
    if word == 'Asc':
        return sorted(arr)
    elif word == 'Des':
        return sorted(arr)[::-1]
    elif word == 'None':
        return arr
print(asc_des_none([2, 3, 5, 7], 'Des'))
print(asc_des_none([5, 8, 4, 6], 'Asc'))
print(asc_des_none([5, 8, 4, 6], 'None'))
