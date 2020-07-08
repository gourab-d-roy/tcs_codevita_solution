flag=0
i=1
count=dict()
res=''
alpha=dict()
lst=list()
ls=list()
for idx in range(97, 97 +26):
   res = res + chr(idx)

for le in res:
    alpha[le]=alpha.get(le,0)+i
    i=i+1
nos=input('numbers of strings  ')
for j in range(1,int(nos)+1):
    sen=input('string input  ')
    lst.append(sen)
print(lst)

def check(word):
    ls=list()

    for letter in word:
        count[letter]=count.get(letter,0)+1#found each char count in word
    #ls=list()
    for letter in word:
        if alpha[letter]==count[letter]:
            ls.append(True)
        else:
            ls.append(False)
    if all (ls)==True:
        print('yes')
    else:
        print('no')

for item in lst:
    check(item)
