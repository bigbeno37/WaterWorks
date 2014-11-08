from time import sleep
from sys import exit

class Main(object):
    debugMode = False
    
    def setDebugMode(self, debug):
        self.debugMode = debug
    
    def intro(self):      
        print("Welcome to WaterWorks v0.1!")
        try:
            name = raw_input("What is your name? ")
        except NameError:
            name = input("What is your name? ")
        print("Hello, " + name + ". Time to begin!")
        sleep(2) if self.debugMode == False else sleep(0)
    
    def displayText(self, text):
        if self.debugMode == False:
            for element in text:
                print(element)
                sleep(2)
                
    def answers(self, question, answer):
        try:
            inputAnswer = raw_input("What do you do?\n" + question + " ").replace(' ', '').lower()
        except NameError:
            inputAnswer = input("What do you do?\n" + question + " ").replace(' ', '').lower()
        
        if inputAnswer in answer:
            return inputAnswer
        else:
            self.redoAnswers(question, answer)
        
    def redoAnswers(self, x, y):
        print("Command not recognised!")
        self.answers(x, y)
        
    def endGame(self, points):
        print("Unfortunately, you did not make it to the end of the game")
        print("You reached a score of " + str(points) + "!")
        exit()