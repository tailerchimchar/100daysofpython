#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open(r"day24-filesanddirectories/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
  names = file.readlines()

for name in names:
  stripped_name = name.strip()
  with open(r"day24-filesanddirectories/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    content = file.read()
  new_content = content.replace("[name]", stripped_name)
  mailing_address = f"day24-filesanddirectories\Mail Merge Project Start\Output\ReadyToSend\letter_to_ppls.txt"
  with open(mailing_address, mode="w") as output:
    output.write(new_content)
  
