print("welcome to my game")

playing = input("Do you want to play? ")
#prompt asking user to play game or not
if playing.lower() != "yes":
    quit()

print("Okay lets play")
#adding score with correct answers
score = 0
#.lower() makes all input whether its capital or not in samll case

answer = input("WHat does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("WHat does APU stand for? ")
if answer.lower() == "accelator processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

    answer = input("WHat does GPU stand for? ").lower() #applying here .lower() makes already converted your answer in lower case
if answer == "graphic processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")
#+str(score) using this because score is in number format and undefined opertation (adding number in string ) so i am using str(score) 
print("You got " + str(score) + " question correct!")
#using () before score so divide operate first than mltyplication
print("You got " + str((score/3) * 100) + "%")