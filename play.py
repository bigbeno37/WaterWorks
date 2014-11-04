from main import Main
from sys import exit
from os import stat

textArray = [line.strip() for line in open('text')]
questionArray = [line.strip() for line in open('questions')]
answerArray = [line.strip() for line in open('answers')]
leaderboardArray = [line.strip() for line in open('leaderboard')]



Main().setDebugMode(True)

Main().intro()

Main().displayText(textArray[1:5])
question1 = Main().answers(questionArray[0], answerArray[0:2])
if question1 == 'reachforthepipe':
    Main().displayText(textArray[7:10])

Main().displayText(textArray[11:14])
if Main().answers(questionArray[2], answerArray[3:5]) == 'godowntheleftpath':
    Main().displayText(textArray[15:20])
    exit()

Main().displayText(textArray[21:28])
answer = Main().answers(questionArray[4:5])
if answer == 'gointotherightdoor':
    print()
elif 

'''gointotherightdoor
gointotheleftdoor
iknowwhatitsays'''