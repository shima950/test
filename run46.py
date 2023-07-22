#تابعی ایجاد کنید که تعداد بردها، تساوی ها و باخت های یک تیم فوتبال را می گیرد
# و تعداد امتیازاتی را که آن تیم تا کنون به دست آورده است محاسبه می کند

def football_points(win, draw, lost):
    return win * 3 + draw

print(football_points(3, 4, 2))
print(football_points(5, 0, 2))
print(football_points(0, 0, 1))