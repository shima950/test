#کدی بنویسید که مقادیر دو متغیر را با هم عوض کند
def valuechanger(num1,num2):
    num1,num2 = num2,num1
    return num1,num2
print(valuechanger(2,6))
print(valuechanger(-3,0))