sıra =int(input(" Please enter rows for two dim array:"))
List=[]
print("Enter ",sıra,"list of int:")
for k in range(sıra):
    List.append([int(x) for x in input().split()])
print(List)

while(1==1):
  print("Enter a list please")
  search=[int(x) for x in input().split()]
  if search in List:
      print("List is in the two dim list")
  else:
      print("List is not in the two dim list")
