def extract(n):
    lst=list()
    mul=1
    sum=0
    while(n!=0):
        #after iterated divisions quotient will turn 0
        lst.append(n%10)
        n=int(n/10)
#extracted digit list inreverse order
    print('doing...')#checkpoint
    print('digits...')

    for i in lst:
        sum=sum+(i*mul)
        mul=mul*10

    lst.reverse()
    print(lst)
    print('reconstructing the num from list of digits...')

    return sum
num=int(input('number'))
print(extract(num))
