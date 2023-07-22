
def validatePIN (pin):
    if pin.isdigit()  and (len(pin) == "4" or len(pin) == 6) :
        return True
    return False
print(validatePIN("123567"))
print(validatePIN("01"))