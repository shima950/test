def hackerSpeak(text):
    coded = ''
    for i in text:
        if i == 'a':
            coded += '4'
        elif i == 'e':
            coded += '3'
        elif i == 'i':
            coded += '1'
        elif i == 'o':
            coded += '0'
        elif i == 's':
            coded += '5'
        else:
            coded += i
    return coded
print(hackerSpeak("python is cool"))
print(hackerSpeak("programming is fun"))
print(hackerSpeak("become a coder"))
        