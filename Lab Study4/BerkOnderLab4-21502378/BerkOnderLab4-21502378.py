def mors(arr, word):
    write = ""
    way = word.split()
    for k in way:
        i = 1
        for ch in k:
            if ch == ".":
                i = i * 2
            elif ch == "-":
                i = (i * 2) + 1
            else:
                print('Invalid Morse Code at the ' + str(i) + 'th position')
                
        write += arr[i] + " "
    print(write)

arr = ['', 'start', 'E', 'T', 'I', 'A', 'N', 'M', 'S', 'U', 'R', 'W', 'D', 'K', 'G', 'O', 'H', 'V', 'F', 'Ü', 'L', '', 'P', 'J', 'B', 'X', 'C', 'Y', 'Z', 'Q', 'Ç', 'İ', '5', '4', '$', '3', '?', '-', '.', '2', ',', ':', '+', ';', '*', '%', '#', '1', '6', '=', '/', 'ş', 'ğ', 'ö', '&', '8', '7', '9', '0', '', '', '', '', '']
word=input("Please enter a mors code:")
mors(arr,word)
