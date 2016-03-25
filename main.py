import os

print("Loading List")
f = open("List.txt" , "r")
print("Done Loading List")
itemList= f.read().split("\n")
# itemList = ["OO9162-13","OO9183-08","24-417"]

for each in itemList:
  try:
    each = each.split("|")
    os.rename("Input/"+each[0], "Finished/"+each[1])
    print("/" + each[1]+ " ---- Finished/" + each[0])
  except:
    pass
