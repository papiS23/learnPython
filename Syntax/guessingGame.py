secret_word = 'marysia'
guess = input("Your guess: ")
tries = 0

while guess != secret_word:
    tries += 1
    if tries < 3:
        print(f"You have {3-tries} tries.", end=' ')
        guess = input("Try again: ")
    else:
        break

if guess == secret_word:
    print("You win!")
else:
    print("You have no more tries. You lost!")