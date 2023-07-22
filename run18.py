t1 = (4,5,6,7,8,9,0)
print(type(t1))
print("t1[2]=" , t1[2])
print("t1[2:5]=" , t1[2:5])
t2 = ('a','b','c')
t3= t1+t2
print("t3=",t3)
print("len:",len(t3))
print("max(t1)=",max(t1))
print("min(t1)=",min(t1))
for i in t3:
    if i== 0:
        print("0 is availabe")