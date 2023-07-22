#تابعی ایجاد کنید که لیستی از اعداد صحیح و رشته های غیر منفی را بگیرد و یک لیست جدید بدون رشته برگرداند
def filter_list (arr):
    a = []
    for i in arr:
        if type (i) is int:
            a.append(i)
    return a
print(filter_list([1, 2, "a", "b"]))
print(filter_list(["s", 5, "shima", "5", 12]))
