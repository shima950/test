#تابعی ایجاد کنید که یک رشته را بگیرد و رشته ای را برگرداند که در آن هر کاراکتر یک بار تکرار شود

def double_char(string):
    word =" "
    for i in range(0, len(string)):
        word += string[i] * 2
    return word

print(double_char('shima'))
print(double_char('2407'))
print(double_char('ahmadi76'))
