#Write your code below this row 👇

# if want all the numbers from 1-10, have to do range until 11
# if want numbers from 1 - 100, then need to do range(1,100)
sum = 0
for num in range(1,101):
    if num % 2 == 0:
        sum+=num

print(sum)

# can add a 3rd paramter to range for Step_size
sum = 0
for num in range(2,101,2 ):
    sum+=num

print(sum)