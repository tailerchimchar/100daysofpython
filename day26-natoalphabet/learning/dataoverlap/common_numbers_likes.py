with open("./file1.txt", mode="r") as file:
  intlist1 = [int(num) for num in file.read().split()]
  
with open("./file2.txt", mode="r") as file:
  intlist2 = [int(num) for num in file.read().split()]
  
result = [num for num in intlist1 if num in intlist2]

print(result)