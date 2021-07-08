def Checking_Off(x,y):

    list1=list(y)
    if(len(x)!=len(y)):
        return False
    
    for k in x:
        i=0
        flag=False
        
        while (flag==False) & (i<len(list1)):
            if(k==list1[i]):
                flag=True
            i=i+1   
        if(flag==False):
            return False
    return True

x=input('Enter first word:')
y=input('Enter second word:')
res=Checking_Off(list(x),list(y))

if(res):
    print(x, '&', y, 'are anagram words')
else:
    print(x, '&', y, 'are not anagram words')
