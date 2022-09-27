main = [1,2,3,4,5,6,7,8,9]
a=[0,1,2,0,4,5,0,7,8]
for i in range(0,9):
    if a[i]==0:
        for j in range(0,9):
            if main[j] in a:
                print("true")
            else:
                print("false")
                a[i]=main[j]
print(main[8])
print(a)
