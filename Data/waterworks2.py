#Created by Oli MacPherson and Ben O'Sullivan!
#For use with only Python 2 at the moment cause i cant be bothered changing all the raw_inputs.
import sys, os, random
import time

intro_phrases = ["The world is changing. \n",
                   "Humanity's voracious appetite for and consumption of electricity born of burning coal and oil is releasing harmful gas into the atmosphere. \n",
                   "You will now experience the effects of this upon the world's climate. \n",
                   "Your objective is to survive for as long as you can, in a world of violent climate change. \n",
                   "Good luck. \n"]
def intro ():
  for phrase in intro_phrases:
    print(phrase)
    time.sleep(4)
  extreme_rain_1()

def enterdaspace ():
  answerrr = raw_input()
  if answerrr == '1':
    print("You enter the airlock, and enter a brand new world. The spacecraft rockets away into space, and you live happily ever after.")
    print("Well done! You finished! Keep your eyes open for the second game, coming out in December 2014!")
    print("Of course, none of this would have been neccessary if we just looked after the planet a bit more.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  if answerrr == '2':
    print("You turn away from the airlock, unwilling to trust fate. You die of suffocation, many lonely days later.")
    print("You have died. You have failed. Your score is 1000 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  else:
    print("Invalid answer. Please type either 1 or 2.")
    enterdaspace()
  
def spacecraftflying ():
  print("The spacecraft is soaring overhead. Your head looks up at it's ceiling. You wonder whether you should go explore.")
  answerr = raw_input("Quick! Do you remember. Did you open a window (1) or not (2)? No lying please.") 
  if answerr == '1':
    print("You run out of air, and the vacuum sucks you into space. You manage to grab a spacesuit, and hurredly put it on. You look back at the spacecraft, and realise, Venus is too far away. But just as you begin to despair, a new spacecraft appears. It opens it's airlock. Do you enter (1), or not (2)?")
    enterdaspace()
  if  answerr == '2':
    print("The spacecraft rocks wildly, as it enters Venus's atmosphere. You run, but lose control of the craft. You crash. And. Burn.")
    print("You have died. You have failed. Your score is 950 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  else:
    print("Invalid answer. Please type either 1 or 2.")
    spacecraftflying()
      
def spacecrafttakeoff ():
  print("The spacecraft begins to shake. There are lizards about! Do you take off (1) or not (2)?")
  spacecraft = raw_input()
  if spacecraft == '1':
    print("You strap yourself in, and key the ignition. The spacecraft rockets off into the atmosphere.")
    spacecraftflying()
  if spacecraft == '2':
    print("The spacecraft topples over as the lizards begin to rip up the landing gear. The spacecraft ignites, exploding, melting the flesh from your bones.")
    print("You have died. You have failed.Your score is 900 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  else:
      print("Invalid answer. Please type either 1 or 2.")
      spacecrafttakeoff()
    
def doyuodiewindow ():
  windowopen = raw_input("Do you open a window (1) or not (2)?")
  if windowopen == '1':
    windowisopen = True
    spacecrafttakeoff()
  if windowopen == '2':
    windowisopen = False
    spacecrafttakeoff()
  else:
    print("Invalid answer. Plese type '1' or '2'.")
    doyuodiewindow()
      
def campornot ():
  camppls = raw_input("")
  if camppls == '1':
    print("You and Michael begin to retrieve the camping equipment from your bags, but before you can, the lizard's friends come roaring out of the desert, and ravage your camp. You are picked up and slowly ripped in two.")
    time.sleep(2)
    print("You have died. You have failed. Your score is 850 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  if camppls == '2':
    print("You and Michael hustle up the ramp. Once inside, you realise it is extremely humid and hot. You are sweating very much.")
    time.sleep(2)
    doyuodiewindow()
  else:
    print("Invalid answer. Please type either '1' or '2'.")
    campornot()
      
def whichway ():
  theway = (raw_input("Do you go towards the spacecraft to leave immediately (1), or to the next settlement, for food and water (2)?").upper()).replace(" ", "")
  if theway == '1':
    print("You point at the very far off spacecraft, and beckon Michael towards you. The two of you begin to walk.")
    time.sleep(2)
    print("After two hours in the desert, you are hopelessly lost. You fall to the ground, weakened. Michael has already given up, and died. You crawl towards the ship, determined to make it. You don't even realise it when you slip into death.")
    time.sleep(2)
    print("You have died. You have failed. Your score is 800 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  if theway == '2':
    print("You set off towards the settlement, and within the hour, you arrive, and replenish your supplies. By he time you eventually reach the spacecraft, it is nightfall. Do you set up camp (1) or do you go inside immediately (2)?")
    campornot()
  else:
    print("Invalid answer. Please type either '1' or '2'.")
    whichway()
  
def backatthehousetrekstart ():
  print("Back at the house, you ready yourself and the team for the journey. Your team runs out of water, and John dies of dehydration, but you and Michael continue on.")
  time.sleep(3)
  print("You and Michael leave the house, and Michael asks you which way we should go.")
  whichway()
    
def whatthefdoyoudo ():
  whatdoyoudo = (raw_input("Do you kill him (1), capture him (2), or run (3)?").upper()).replace(" ", "")
  if whatdoyoudo == "1":
    print("You move forwards, and slice down with the sword. The man's head rolls away.")
    time.sleep(2)
    print("There are some bullets on the counter. You grab them, then head back to the house.")
    backatthehousetrekstart()
  if whatdoyoudo == "2":
    print("You lower your sword, and point it at the man. He snarls, and throws himself onto your sword, killing you in the process.")
    time.sleep(2)
    print("You have died. You have failed. Your score is 750 points.")
  if whatdoyoudo == "3":
    print("You turn to run, but are cut down in two strides.")
    print("You have died. You have failed. Your score is 700 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  else:
    print("Invalid answer. Please type '1', '2', or '3'.")
    whatthefdoyoudo()
      
      
def abandonedhouse ():
  print("Still grasping your bloody sword, you stride out towards the house. It does indeed appear empty.")
  time.sleep(2)
  print("You walk to the door, and enter slowly. There is a man inside that you did not hear. He turns, and hisses at you. What do you do?")
  whatthefdoyoudo()
      
def thegun ():
  gunanswer = (raw_input("Do you pick up the gun (1), or the sword that's lying beside it (2)?").upper()).replace(" ", "")
  if gunanswer == "1":
    print("You pick up the gun, load a bullet, and walk outside. The lizard is there, and he charges. You raise the gun and- \n")
    time.sleep(5)
    print("The gun misfires, and explodes in your hands. You are knocked backwards into the door. As you begin to fall unconscious, you witness the lizard begin to eat you.")
    time.sleep(2)
    print("You have died. You have failed. Your score is 650 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  if gunanswer == "2":
    print("You grab the sword and stride outside. ")
    print("The lizard charges, but you raise your sword and cut it's throat as it comes.")
    time.sleep(2)
    print("You skin the beast and take the skin in to Michael. He smiles and tanks you. Now he needs some bullets, he says. he points to an abandoned house ten metres from the door. There should be some in there.")
    time.sleep(3)
    abandonedhouse()
  else:
    print("Invalid answer. Please type either '1' or '2'.")  
    thegun()
  
def doyoustillhelp ():
  doyoustillhelp1 = (raw_input("Do you still want to help? Yes (1) or no (2)").upper()).replace(" ", "")
  if doyoustillhelp1 == "1":
    print("Good. Michael says he needs some reptile skin first. He points to a gun by the door, and says to kill the one outside.")
    thegun()
  if doyoustillhelp1 == "2":
    print("The stranger shakes his head regretfully, and turns away. 'You can leave, then.' he says.")
    time.sleep(2)
    print("You turn, and stalk out, outraged. You walk right into the giant lizard still waiting outside.")
    time.sleep(2)
    print("You are eaten. You have died. You have failed. your score is 600 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  else:
    print("Invalid answer. Please type either '1' or '2'.")
    
def insidethehouse ():
  print("You turn, and take in the room around you. It is a neatly furnished home, complete with two men, sitting frozen at a table, in the midst of an afternoon tea. They are staring at you.")
  time.sleep(3)
  print("They stand, and one walks over. He puts his arm on your shoulder, and says 'You have come at a great moment, stranger. Will you undertake some tasks for me and my friend here?'.")
  time.sleep(3)
  print("Do you undertake these tasks? Yes (1) or no (2)?")
  taskchoice = (raw_input().upper()).replace(" ", "")
  if taskchoice == "1":
    print("The stranger smiles, and extends his hand. 'I'm  Michael,' he says, 'and this is my friend, John. We are trying to get to venus.'.")
    time.sleep(3)
    print("John chimes in, says it's the only way to excape the now uncontrollable climate change threatening Earth. He says there's a spacecraft in the north, they only have to reach it.")
    time.sleep(3)
    print("They say they need you to find one or two things for them, then they can leave for the spacecraft.")
    time.sleep(3)
    doyoustillhelp()
  if taskchoice == "2":
    print("The stranger shakes his head regretfully, and turns away. 'You can leave, then.' he says.")
    time.sleep(2)
    print("You turn, and stalk out, outraged. You walk right into the giant lizard still waiting outside.")
    time.sleep(2)
    print("You are eaten. You have died. You have failed. your score is 600 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  else:
    print("Invalid answer. Please type either '1' or '2'.")
    insidethehouse()

def housedoorchoice1 ():
  housedoorchoice = raw_input("Do you run around the side of the house (1), or do you open the door and enter (2)?").replace(" ","").upper()
  if housedoorchoice == "1":
    print("You attempt to run, but the lizard catches you before you go three steps. It eats you alive.")
    time.sleep(3)
    print("You have died. You have failed. Your score is 550 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  if housedoorchoice == "2":
    print("You grab the handle and turn it, running in and slamming the door behind you.")
    time.sleep(2)
    insidethehouse()
  else:
    print("Invalid answer. Please type either '1' or '2'.")
    housedoorchoice1()   
      
      
def route_choice_1 ():
  answer_routechoice1 = (raw_input("Which way do you go? To the house (1) or to the oasis (2)?").replace(" ","")).upper()
  if answer_routechoice1 == "T2":
    print("You run towards the glorious sight, splashing water from the bucket in your haste to reach it. Once you arrive, however, it fades. It was a mirage.")
    time.sleep(3)
    print("You gaze at your now empty bucket, then sit, and weep.")
    print("You die of thirst. You have failed. Your score is 500 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  if answer_routechoice1 == "1":
    print("You stroll towards the house, drinking leisurely from the bucket as you do. You have made it to the door when you hear thundering feet behind you. You turn, and see a massive lizard thundering towards you.")
    time.sleep(4)
    housedoorchoice1()
  else:
    print("Invalid answer. Please type either '1' or '2'.")
    route_choice_1()
    
def stuck_in_room_2 ():
  print("It seems you only have a few seconds until the door collapses. Do you leave the house through the back window (1), or climb through the trapdoor in the ceiling (2)?")
  answer_stuckinroom = (raw_input().upper()).replace(" ", "")
  if answer_stuckinroom == "2":
    print("You scramble up to the trapdoor, and climb through. The roof, weakened by the downpour, cannot withstand your weight. You fall, and die in pain. You have failed. Your score is 450 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
       sys.exit()
  if answer_stuckinroom == "1":
    print("You leap out of the window.")
    print("The sun shines down upon you. Suddenly thirsty, you drink from the bucket.")
    time.sleep(2)
    print("You begin to walk, and are faced with two routes. In the distance, their looms a beautiful oasis. To the left, however, their is a small house that seems uninhabited.")
    time.sleep(3)
    route_choice_1()  
  else:
    print("Invalid answer. Please type either '1' or '2'.")
    stuck_in_room_2()  

  
def extreme_rain_choice_bucket ():
  stuck_in_room_2
  
def extreme_rain_2 ():
  print("Your door is blown off it's hinges with the force of the gale, and water pours in the door. Do you stay where you are (1), or barricade yourself in the other room (2)?")
  extreme_rain_2_answer = (raw_input().replace(" ","")).upper()
  if extreme_rain_2_answer == "1":
    print("You stay in your chair, watching as the water floods the room.")
    time.sleep(2)
    print("You doze off, peacefully.")
    time.sleep(2)
    print("You do not wake up. You have drowned. You have failed. Your score is 400 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  if extreme_rain_2_answer == "2":
    print("You run to the door, and dive inside, slamming it behind you.")
    stuck_in_room_2()
  else:
    print("That is not a valid answer. Please type either '1' or '2'.")
    extreme_rain_2()

def very_thirsty_rain_big_roof_leak ():
  print("You are extremely thirsty. You stumble over to the stream of water dribbling down from the tiles, and drink until your thirst is sated.")  
  extreme_rain_2()

def rain_1_roof_leak_big ():
  time.sleep(1)
  print("The leak in the roof gets slowly larger. There are some wooden boards to the side of the room, and some tiles. Do you plug the hole, and if so, with what? Do you leave the hole (1), plug the hole with boards (2), or plug the hole with tiles (3)?")
  rain_1_roof_leak_big_answer = (raw_input()).upper()
  if (rain_1_roof_leak_big_answer.replace(" ","")).upper() == "2":
    print("You pick up the boards, and nail them in place. The leak stops completely.")
    time.sleep(2)
    print("An hour later, you are unbearable thirsty. You gaze at the empty bucket longingly, and at the plugged hole in the ceiling.")
    time.sleep(2)
    print("You open the door, and stumble outside, only to find the sun blinding you with it's heat. \n You fall backwards.")
    time.sleep(2)
    print("You stay there until you die of thirst. You have failed. Your score is 350 points.")
    print("Would you like to play again?")  
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  if rain_1_roof_leak_big_answer.replace(" ","") == "3":
    print("You pick up the tiles, and glue them to the roof. Some water still seeps through.")
    very_thirsty_rain_big_roof_leak()
  if rain_1_roof_leak_big_answer.replace(" ","") == "1":
    time.sleep(1)
    print("The roof, weakened by the downpour and the hole, collapses, crushing you. \n" + "You have failed. Your score is 300 points.")
    print("Would you like to play again?")
    answertoques = raw_input().upper()
    if answertoques == "YES":
      extreme_rain_1()
    else:
      sys.exit()
  else:
    print("Invalid answer. Please type '1', 'Plug the hole with tiles', or 'Leave the hole'.")
    rain_1_roof_leak_big()

def rain_1_answer_function ():
  rainanswer = raw_input("Do you fetch a bucket and catch the water (1), or do you let it drip(2)?").replace(" ","").upper()
  if rainanswer == "1":
    print("You get a bucket and place it under the dripping ceiling. Water begins to collect in the bottom of the bucket.")
    time.sleep(2)
    extreme_rain_2()
  if rainanswer == "2":
    print("You sit back in your chair, content to let the rain drip. It's only a small leak after all.")
    time.sleep(2)
    rain_1_roof_leak_big()
  else:
    print("Invalid response. Please type either '1' or '2'.")
    rain_1_answer_function()

def extreme_rain_1 ():
  print("The rain is bucketing down around you. You are sitting at home, snug inside your small, two-room house. The roof begins to leak, just a little. What do you do?")
  rain_1_answer_function()
  
def introfunction ():
  haveyouplayed = raw_input("Have you played this game before?").upper()
  if haveyouplayed == "YES":
    extreme_rain_1()
  if haveyouplayed == "NO":
    intro()
  else:
    print("Invalid answer. Please type either 'yes' or 'no'.")
    introfunction()
    
introfunction()