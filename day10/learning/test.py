#functions with outputs
# using doc string for formatting functions
def format_name(f_name, l_name):
  '''
  Take a first and last name and format it to return the Title case version of the name
  '''
  if f_name == "" or l_name == "":
    return
  return f"Formatted Name: {f_name.title()} {l_name.title()}"
  
print(format_name("tailer", "nguyen"))

#desired output: Tailer, not taILER

#functions with more than 1 return statements
print(format_name(input("What is your first name? "), input("What is yoru last name? ")))
