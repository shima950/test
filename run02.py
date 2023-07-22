#تابعی بنویسید که لیستی از اعداد را می گیرد و لیستی با دو عنصر را برمی گرداند:

def sum_odd_and_even(lst):
    result = []
    evens_sum = 0
    odds_sum = 0
    for i in lst:
        if i % 2 == 0:
            evens_sum += i
        else:
            odds_sum += i
    result.append(evens_sum)
    result.append(odds_sum)
    return result

print(sum_odd_and_even([1, 2, 3, 4, 5, 6, 7, 8]))