def read(name):
    file = open(name,"r")
    word_arr = []
    for line in file:
        for word in line.split():
            word_arr.append(word)
    return word_arr


def BubbleSort(words):
    k = len(words)

    for i in range(k):
        for z in range(0, k - i - 1):
            if (words[z + 1].upper() < words[z].upper()):
                words[z], words[z + 1] = words[z + 1], words[z]
    return words


def FrequencyFind(Sorted_arr,word):
    k=0
    a=len(Sorted_arr)
    for i in range(a):
        if(word in Sorted_arr[i] and len(word)== len(Sorted_arr[i])):
           k=k+1
    return k




name = input("Enter the file name: ")
word=[]
word = read(name)
sort =[]
sort = BubbleSort(word)
print(sort)

search = input("\nEnter words :")
Freq = FrequencyFind(sort, search)
if (Freq == 0):
    print("The words that you are searching does not exist in the text file")
else:
    print("\n")
    print(search, "Repeats", Freq, "Times")
