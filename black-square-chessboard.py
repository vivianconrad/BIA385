print ("What row is it in?")
row = int(input())
print ("What column is it in?")
column = int(input())

if (row%2 == 0) and (column%2==0):
  print("YES")
 
elif (row%2==1) and (column%2==1):
  print("YES")
else:
  print("NO")
