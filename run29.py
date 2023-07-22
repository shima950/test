#تابعی بنویسید که مقدار دقیقه را به عنوان آرگومان ورودی بگیرد، آن را به ثانیه تبدیل کرده و در خروجی برگرداند
def convert(minutes):
    time = (minutes * 60)
    return time
print (convert(40))
print (convert(2))