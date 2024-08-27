print("Welcome to Game")
player=input("Do you Want to play?")
if player.lower() !="yes":
    quit()
print("ok lets play")
score=0

question=input("How Many Days in a Week?")
if question.lower()=="Seven":
 print("Correct")
 score=+1
else:
    print("Incorrect")


question=input("In Which Direction does the sunbrise?")
if question.lower()=="east":
 print("Correct")
 score=+1
else:
    print("Incorrect")


question=input("What is our national bird?")
if question.lower()=="peacock":
 print("Correct")
 score=+1
else:
    print("Incorrect")



question=input("Which is the fastest animal in the land?")
if question.lower()=="Cheetah":
 print("Correct")
 score=+1
else:
    print("Incorrect")

    print("Your score:"+str(score))
            
    
