from Data.main import Main
from sys import exit
from os import stat

m = Main()

textArray = [line.strip() for line in open('Data/text')]
questionArray = [line.strip() for line in open('Data/questions')]
answerArray = [line.strip() for line in open('Data/answers')]

m.setDebugMode(False)

m.intro()

m.displayText(textArray[1:5])
question1 = m.answers(questionArray[0], answerArray[0:2])
if question1 == 'reachforthepipe':
    m.displayText(textArray[7:10])

m.displayText(textArray[11:14])
if m.answers(questionArray[2], answerArray[3:5]) == 'godowntherightpath':
    m.displayText(textArray[15:20])
    m.endGame(50)

m.displayText(textArray[21:28])
answer = m.answers(questionArray[4], answerArray[6:9])
if answer == 'opentherightdoor':
    m.displayText(textArray[29:33])
    m.endGame(100)
elif answer == 'iknowwhatitsays':
    try:
        if raw_input("What does it mean? ").replace(' ', '').lower() != 'youmustgointotheleftdoor':
            print("All of a sudden, you hear a voice in your head saying INCORRECT")
            print("You feel faint, dizzy...")
            print("You pass out")
            m.endGame(150)
        else:
            print("All of a sudden, you hear a voice in your head saying CORRECT!")
    except NameError:
        if input("What does it mean? ").replace(' ', '').lower() != 'youmustgointotheleftdoor':
            print("All of a sudden, you hear a voice in your head saying INCORRECT")
            print("You feel faint, dizzy...")
            print("You pass out")
            m.endGame(150)
        else:
            print("All of a sudden, you hear a voice in your head saying CORRECT!")
        
m.displayText(textArray[34:42])
answer = m.answers(questionArray[6], answersArray[10:12])
if answer == 'gototheabandonedhouse':
    m.displayText(textArray[43:48])
    m.endGame(200)

m.displayText(textArray[49:57])
if m.answers(questionArray[8], answersArray[13:15]) == 'pullthelever':
    print("You pull the lever, but nothing happens")
else:
    print("You push the button, but nothing happens")
    
m.displayText(textArray[58:64])
if m.answers(questionArray[10], answesArray[13:15]) == 'gointothebuilding':
    