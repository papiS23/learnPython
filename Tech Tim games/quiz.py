print("Welcome to my quiz!")
playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()
print("Okay, lets play!")

correct_answers = 0
answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("Correct!")
    correct_answers += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    print("Correct!")
    correct_answers += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print("Correct!")
    correct_answers += 1
else:
    print("Incorrect!")

print(f"You have got {correct_answers} correct answers, which is {round((correct_answers/3)*100, 1)}%")