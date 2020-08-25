ls=[]
count=dict()
ct=dict()
mer=''
main=input('original.........')
for letter in main:
    count[letter]=count.get(letter,0)+1
no=int(input('nos.......'))
for  i in range(no):
    mer=mer+input('strs........')

#print(mer)
for l in mer:
    ct[l]=ct.get(l,0)+1

print(count)#for my use
print(ct)#for my use

for j in count:
    print (count[j])
    print(ct[j])

    #'''try:#for my use
    if (count[j]==ct[j]):
        ls.append(1)
    else:
        ls.append(False)
    #except:#for my use
    #    continue#for my use
print(ls)
if all(ls)==True:
    print('YES')
else:
    print('NO')
