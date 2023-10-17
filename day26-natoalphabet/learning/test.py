# list comprehension is specific to python

# creating a list from previous lists

list = [1,2,3]
new_list = [item+1 for item in list]

print(new_list)

name = "Angela"

letters_list = [letter for letter in name]
print(letters_list)

# no need for this. just do range(1,5)
# range_list = []
# for i in range(1,5):
#   range_list.append(i)
  
range_list_test = [num*2 for num in range(1,5)]
print(range_list_test)

names = ["Alex", "Beth", "Caroline", "dave", "Eleanor", "freddie"]
short_names = [item for item in names if len(item) < 5]

long_names = [item.upper() for item in names if len(item) > 4]

print(short_names)
print(long_names)