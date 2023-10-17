# looping through dictionaries

student_dict = {
  "student": ["Angela", "James", "Lily"],
  "Score": [56, 76, 98]
}

for (key,value) in student_dict.items():
  print(value)
  
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a data frame
for (key,value) in student_data_frame.items():
  print(key) # prints student and score
  print(value) # prints data in each of the columns
  
  # loops through rows of a data f rame
  for(index, row) in student_data_frame.iterrows():
    print(index) # prints one of the students scores
    print(row) # this is the one we want though
    print(row.student)
    if row.student == "Angela":
      print(row.Score)