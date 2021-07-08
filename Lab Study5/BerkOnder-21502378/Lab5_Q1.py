def mintree(arr):
    print ("Tree:")
    for i in arr:
        print (i)
    temp = [None] * len(arr) 
    n = len(arr) - 1
    for i in range(len(arr[n])):  
        temp[i] = arr[n][i]  
    for i in range(len(arr) - 2, -1,-1):  
        for j in range( len(arr[i + 1]) - 1):  
            temp[j] = arr[i][j] + min(temp[j], temp[j + 1]);
    return temp[0] 
  

arr = [[2],[5, 4],[1, 4, 7],[8, 6, 9, 6]]
print(mintree(arr))
arr = [[2],[5, 4],[7, 4, 1],[8, 2, 9, 6],[11, 3, 8, 8, 6]]
print(mintree(arr))
arr = [[3],[7, 3],[5, 4, 9],[2, 8, 3, 6],[7, 13, 4, 6, 5]]
print(mintree(arr))
arr = [[3],[7, 3],[5, 4, 9],[2, 8, 3, 6],[7, 13, 4, 6, 5],[5, 11, 9, 1, 2, 7]]
print(mintree(arr))
