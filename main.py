from time import sleep

class Main(object):
    debugMode = False
    
    def setDebugMode(self, debug):
        self.debugMode = debug
    
    def intro(self):      
        print("Welcome to WaterWorks v0.1!")
        name = input("What is your name? ")
        print("Hello, " + name + ". Time to begin!")
        sleep(2) if self.debugMode == False else sleep(0)
    
    def displayText(self, text):
        if self.debugMode == False:
            for element in text:
                print(element)
                sleep(2)
                
    def answers(self, question, answer):
        inputAnswer = input("What do you do?\n" + question + " ").replace(' ', '').lower()
        
        if inputAnswer in answer:
            return inputAnswer
        else:
            self.redoAnswers(question, answer)
        
    def redoAnswers(self, x, y):
        print("Command not recognised!")
        self.answers(x, y)
        
    def endGame(self, name, leaderboard):
        print("Unfortunately, you did not make it to the end of the game")
        print("You reached a score of " + points "!")
        
        if len(leaderboard) > 0:
            print("The leaderboard is currently: ")
        else:
            print("The leaderboard is currently empty!")
            
    def showLeaderboard(self, name, leaderboard, file):
        answer = input("Do you want to save your score?")
        if answer == 'Y':
            