student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-1.5: Create function that converts students' grades
def convert_grade(grade):
  if grade > 90 and grade <=100:
    return "Outstanding"
  elif grade > 80 and grade <= 90:
    return "Exceeds Expectations"
  elif grade > 70 and grade <= 80:
    return "Acceptable"
  else:
    return "Fail"

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  student_grades[key] = convert_grade(student_scores[key])
    

# 🚨 Don't change the code below 👇
print(student_grades)