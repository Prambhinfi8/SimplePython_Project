print("Welcome to the Prime Number Checker")



def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False

    if is_prime==True:
        print("It's Prime Number.")
    else:
        print("It's not prime Number.")


n=int(input("Choose a Number:"))
prime_checker(n)