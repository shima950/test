def removeABC (txt):
    result = ""
    for x in txt:
        if x != "a" and x != "b" and x != "c":
            result += x
    if result == txt:
        return None
    return result

print (removeABC("hello shima"))
print (removeABC("hello world"))