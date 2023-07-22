
def greeting (name):

    GUEST_LIST = {
"Randy": "Germany",
"Karla": "France" ,
"Wendy": "Japan" ,
"Norman": "England" ,
"Sam": "Argentina"
}
    if name  in GUEST_LIST:
        return f"Hi! I'm {name}, and I'm from {GUEST_LIST.get(name)}."
    else:
        return "Hi! I'm a guest."
print(greeting("Karla"))
print(greeting("Shima"))
print(greeting("Sam"))