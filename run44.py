#با داشتن شعاع یک دایره و مساحت یک مربع، تابعی بنویسید که اگر محیط دایره بزرگتر از محیط مربع باشد
# مقدار True و اگر محیط مربع بزرگتر از محیط دایره باشد، False را برگرداند

def circle_or_square (radius, side):

    circle_perimeter = 2 * radius * 3.14
    square_perimeter = 4 * side **(1/2)

    if circle_perimeter > square_perimeter:
        return True
    else:
        return False
    
print(circle_or_square(16, 625))
print(circle_or_square(5, 100))
print(circle_or_square(8, 144))