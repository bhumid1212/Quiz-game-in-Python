print("welcome to my computer Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("okay! let's play :)")
score = 0

answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    
answer = input("what does CSS stands for? ")
if answer.lower() == "cascading style sheet":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    
answer = input("which language is a markup language? ")
if answer.lower() == "html":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    
answer = input("what does API stands for? ")
if answer.lower() == "application programming interface":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    
print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 5)* 100) + "%.")
    