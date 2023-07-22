#باتوجه به یک چندضلعی منتظم ان وجهی؛مجموع زوایای داخلی را برحسب درجه برگردانید

def sum_polygon(num):
    x = 180*(num-2)
    return x

print(sum_polygon(3))
print(sum_polygon(4))
print(sum_polygon(6))