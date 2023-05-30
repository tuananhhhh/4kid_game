secret_no = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_no = int(input("Guess the number: "))
    guess_count += 1
    if guess_no == secret_no:
        print("You won!")
        break
else:
    print("You lose!")