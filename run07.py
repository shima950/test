def simpleEncoder (txt):
    b = []
    c = txt.lower()
    for i in c:
        a = c.count(i)
        b.append(i)
        if a == 1:
            i = '['
        elif a >= 2:
            i = ']'
        print("".join(i), end='')

print (simpleEncoder("ahmadi"))
print (simpleEncoder("shima"))