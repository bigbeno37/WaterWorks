from time import sleep

textArray = [line.strip() for line in open('text')]

class Main(object):    
    def intro(self, debugMode):      
        print("Welcome to WaterWorks v0.1!")
        name = input("What is your name? ")
        print("Hello, " + name + ". Time to begin!")
        sleep(2) if debugMode == False else sleep(0)
    
    def displayText(self, text, rangeBegin, rangeEnd, debugMode):
        if debugMode == False:
            for i in range(rangeBegin, rangeEnd):
                print(text[i])
                sleep(2)
            
    def part1Answering(self):
        inputAnswer = input("What do you do?\n(Reach for the pipe / Follow the cave exit): ").replace(' ', '').lower()
        
        return 1 if inputAnswer == 'reachforthepipe' else None
        return 2 if inputAnswer == 'followthecaveexit' else None
        print("Command not recognised!")
        self.part1Answering()
        
    def part2Answering(self):
        inputAnswer = input("What do you do?\n(Go down the right path / Go up the left path): ").replace(' ', '').lower()
        
        return 1 if inputAnswer == 'godowntherightpath' else None
        return 2 if inputAnswer == 'gouptheleftpath' else None
        print("Command not recognised!")
        self.part2Answering()
        
Main().intro(True)
Main().displayText(textArray, 1, 6, False)
part1Answer = Main().part1Answering()
if part1Answer == 1:
    Main().displayText(textArray, 7, 10, False)
Main().displayText(textArray, 11, 14, False)