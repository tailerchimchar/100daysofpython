# file = open("day24-filesanddirectories\learning\my_file.txt")
# content = file.read()
# print(content)
# file.close()

# above is same thing as: but with is a lot more convenient because it closes for me
# with open("day24-filesanddirectories\learning\my_file.txt") as file:
#   content = file.read()
#   print(content)
  
  
# how to write
with open("./my_file.txt", mode="a") as file:
  file.write("\nNew text")
  
# w is write, a is append! 