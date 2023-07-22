#تابعی ایجاد کنید که یک رشته را به عنوان آرگومان دریافت کند و یک لیست مرتب حاوی ایندکس تمام حروف بزرگ در رشته را برگرداند
def index_of_caps(string):
    lis = []
    for i in range(0, len(string)):
        if string[i].isupper():
            lis.append(i)
    return lis
print (index_of_caps('sHImA'))
print (index_of_caps('DeleTE'))
print (index_of_caps('shift'))
