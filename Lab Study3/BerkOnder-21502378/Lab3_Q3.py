def Count_Compare(x,y):
    list1 = [0]*26
    list2 = [0]*26

    for i in range(len(x)):
        position = ord(x[i])-ord('a')
        list1[position] = list1[position] + 1

    for i in range(len(y)):
        position = ord(y[i])-ord('a')
        list2[position] = list2[position] + 1

    k = 0
    status = True
    while k<26 and status:
        if list1[k]==list2[k]:
            k = k + 1
        else:
            status=False

    return status

x=input('Enter first word:')
y=input('Enter second word:')
res=Count_Compare(list(x),list(y))
if(res):
    print(x, '&', y, 'are anagram words')
else:
    print(x, '&', y, 'are not anagram words')
