#code by gourab-d-roy for string merge question tcs codevita season 9 zone 2
#author:GDR/gourab-d-roy
ls=[]
count=dict()
ct=dict()
mer=''
main=input('original string input.........')
for letter in main:
    count[letter]=count.get(letter,0)+1
no=int(input('nos.......'))
for  i in range(no):
    mer=mer+input('input strs to be merged........')


for l in mer:
    ct[l]=ct.get(l,0)+1



for j in count:
    print (count[j])
    print(ct[j])

   
    if (count[j]==ct[j]):
        ls.append(1)
    else:
        ls.append(False)
    

if all(ls)==True:
    print('YES')
else:
    print('NO')
