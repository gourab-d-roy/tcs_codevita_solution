def convert(n):
    lst=list()
    sum=0
    mul=1
    while(n!=0):
        lst.append(int(n%2))
        n=int(n/2)



    lst.reverse()
    return lst

num=int(input('num'))
print(convert(num))
