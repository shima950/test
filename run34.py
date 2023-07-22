#تابعی بنویسید که لیستی از دو عدد را بگیرد و مشخص کند که مجموع ارقام دو عدد با یکدیگر برابر است یا خیر
def is_equal(nlist):
    s1 = 0
    s2 = 0
    for i in str(nlist[0]):
        s1 += int(i)
    for j in str (nlist[1]):
        s2 += int(j)
    return (True if s1 == s2 else False)

print(is_equal([21,35]))
print(is_equal([1,1]))
print(is_equal([0,0]))
print(is_equal([104,41]))