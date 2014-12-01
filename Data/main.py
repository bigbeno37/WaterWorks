from time import sleep
from sys import exit
from os import system

class Main(object):
    debugMode = False
    name = ""
    
    def setDebugMode(self, debug):
        self.debugMode = debug
    
    def intro(self):      
        print("Welcome to WaterWorks v1.7b!")
        try:
            self.name = raw_input("What is your name? ")
        except NameError:
            self.name = input("What is your name? ")
        print("Hello, " + self.name + ". Time to begin!")
        sleep(2) if self.debugMode == False else sleep(0)
    
    def displayText(self, text, time=2):
        if self.debugMode == False:
            for element in text:
                print(element)
                sleep(time)
                
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
        
    def endGame(self, points, bad_end=False, good_end=False):
        if bad_end == False and good_end == False:
            print("Unfortunately, you did not make it to the end of the game")
            print("You reached a score of " + str(points) + "!")
        elif bad_end == True:
            print("BAD END")
            self.credits(True)
        elif good_end == True:
            print("GOOD END")
            self.credits()

    def credits(self, ending=False):
        self.displayText(["WaterWorks", "Created and debugged by Ben O'Sullivan", "Inspiration from the works of Oliver MacPherson", "Thanks for playing " + self.name + "!"], 4)
        if ending == True:
            print("Now play WaterWorks part 2!")
            system("python Data/waterworks2.py")
        exit()