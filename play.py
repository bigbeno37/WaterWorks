from Data.main import Main
from sys import exit
from os import stat
from time import sleep

m = Main()

textArray = [line.strip() for line in open('Data/text')]
questionArray = [line.strip() for line in open('Data/questions')]
answerArray = [line.strip() for line in open('Data/answers')]

m.setDebugMode(True)

m.intro()

def game():
    m.displayText(textArray[1:5])
    question1 = m.answers(questionArray[0], answerArray[0:2])
    if question1 == 'reachforthepipe':
        m.displayText(textArray[7:10])

    m.displayText(textArray[11:14])
    if m.answers(questionArray[2], answerArray[3:5]) == 'godowntherightpath':
        m.displayText(textArray[15:20])
        m.endGame(50)
        replay()

    m.displayText(textArray[21:28])
    answer = m.answers(questionArray[4], answerArray[6:9])
    if answer == 'opentherightdoor':
        m.displayText(textArray[29:33])
        m.endGame(100)
        replay()
    elif answer == 'iknowwhatitsays':
        try:
            if raw_input("What does it mean? ").replace(' ', '').lower() != 'youmustgointotheleftdoor':
                print("All of a sudden, you hear a voice in your head saying INCORRECT")
                sleep(2)
                print("You feel faint, dizzy...")
                sleep(2)
                print("You pass out")
                sleep(2)
                m.endGame(150)
                replay()
            else:
                print("All of a sudden, you hear a voice in your head saying CORRECT!")
        except NameError:
            if input("What does it mean? ").replace(' ', '').lower() != 'youmustgointotheleftdoor':
                print("All of a sudden, you hear a voice in your head saying INCORRECT")
                sleep(2)
                print("You feel faint, dizzy...")
                sleep(2)
                print("You pass out")
                sleep(2)
                m.endGame(150)
                replay()
            else:
                print("All of a sudden, you hear a voice in your head saying CORRECT!")
        
    m.displayText(textArray[34:42])
    answer = m.answers(questionArray[6], answerArray[10:12])
    if answer == 'gototheabandonedhouse':
        m.displayText(textArray[43:48])
        m.endGame(200)
        replay()

    m.displayText(textArray[49:57])
    if m.answers(questionArray[8], answerArray[13:15]) == 'pullthelever':
        print("You pull the lever, but nothing happens")
    else:
        print("You push the button, but nothing happens")
    
    m.displayText(textArray[58:64])
    if m.answers(questionArray[10], answerArray[19:21]) == 'gointothebuilding':
        m.displayText(textArray[65:72])
        m.endGame(250)
        replay()

    m.displayText(textArray[73:79])
    if m.answers(questionArray[12], answerArray[16:18]) == 'gototheplains':
        m.displayText(textArray[80:91])
        m.endGame(300)
        replay()
    
    m.displayText(textArray[92:104], 3)
    if m.answers(questionArray[14], answerArray[22:24]) == 'preparetoliveinthewild':
        m.displayText(textArray[105:115])
        m.endGame(350, True)
        replay()
        
    m.displayText(textArray[116:126])
    m.endGame(400, False, True)
    replay()
        
def replay():
    try:
        if raw_input("Do you want to play again? (Yes / No) ").lower() == 'yes':
            game()
        else:
            exit()
    except NameError:
        if input("Do you want to play again? (Yes / No) ").lower() == 'yes':
            game()
        else:
            exit()

game()