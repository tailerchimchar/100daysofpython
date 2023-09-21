#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    counter = 2
    while(is_prime and counter < (number/2)):
        if number % counter == 0:
            print("It's not a prime number.")
            is_prime = False
        counter+=1

    if is_prime:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
