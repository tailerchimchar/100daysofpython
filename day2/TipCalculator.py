#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

party_amount = int(input("How many people were in your party?\n"))
bill_total = float(input("How much was your Bill?\n"))

tip = input("From percentages 0-100, how much would you like to tip? Prefer 10,12,15\n")

if(int(tip) > 100 or int(tip) <= 0):
  print("Please tip from 0-100%")
else:
  tip_total = float("1." + tip)
  amount_each_should_pay = (bill_total / party_amount) * tip_total
  final_amount = "{:.2f}".format(amount_each_should_pay)
  print(f"Each person should pay ${final_amount}")