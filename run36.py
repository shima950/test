#تابعی بسازید که عددی را به عنوان آرگومان بگیرد و "Fizz" یا "Buzz" یا  "FizzBuzz" را در خروجی برگرداند

def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return "FizzBuzz"
    elif num%3==0:
        return "Fizz"
    elif num%5==0:
        return "Buzz"
    else:
        return str(num)

print(fizz_buzz(15))
print(fizz_buzz(9))
print(fizz_buzz(20))
print(fizz_buzz(4))
print(fizz_buzz(21))