import random
secret_number = random.randint(1 , 10)
while True:
    user_guess = int(input("What is the number I am thinking of?"))
    if user_guess == secret_number:
        print ("YOU GOT IT!")
        break
    elif user_guess > secret_number:
        print ("That's TOO high")
    else:
        print ("That's TOO low")