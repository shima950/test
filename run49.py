def countdown(x , y):
    a = []
    for i in range(x , 0, -1):
        a.append(f"{i}. ")
    a.append(y.upper()+"!")

    return "".join(a)
print(countdown(10, "go"))