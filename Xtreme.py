x = input("")
y = input("")
z = input("")
a = y.split()
s = z.split()
for m in s:
    i = 0
    flag = 0
    for n in a:
        if m < n and flag == 0:
            a.insert(i,m)
            flag = 1
        else:
            i = i + 1
for n in a:
    print(n, end = " ")
            
        
            
            