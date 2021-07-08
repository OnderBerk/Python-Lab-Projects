def Sort_Compare(x,y):
    x.sort()
    y.sort()
    if(len(x)!=len(y)):
        return False
    else:
        k=0
        while(x[k]==y[k] and k<len(y)-1):
            if(x[k]!=y[k]):
                return False
            else:
                k+=1
    return True

x=input('Enter first word:')
y=input('Enter second word:')

res=Sort_Compare(list(x),list(y))

if(res):
    print(x, '&', y, 'are anagram words')
else:
    print(x, '&', y, 'are not anagram words')
