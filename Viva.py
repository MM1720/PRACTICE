a=int(input("Enter lower limit "))
b=int(input("Enter Upper limit "))
c=0
for i in range(a,b+1):
    if i==2:
        c=c+i
    if i>2:
        f=0
        for j in range(1,int((i+1)/2)+1):
            if i%j==0:
                f=f+1
        if f<2:
            c=c+i
            f=0
print(c)
