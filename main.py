#!usr/bin/env python3
from art.hallway_straight import hallwayStraight
from art.corner_left import cornerLeft
from art.corner_right import cornerRight
from art.crossroad import crossRoad
from art.t_straight import tStraight
from art.t_left import tLeft
from art.t_right import tRight
from art.dead_end import deadEnd
from art.locked_door import lockedDoor
from art.logo import logo
from art.empty_room import emptyRoom
from art.skeleton import skeleton
from art.skelhead_pre_hit import skelHeadPreHit
from art.skelhead_post_hit import skelHeadPostHit
from art.empty_staircase import emptyStaircase

import os,platform,time,sys

currentPlatform = platform.system()
def clearScreen():
  if currentPlatform == "Windows":
    os.system('cls')
  elif currentPlatform == "Linux":
    os.system('clear')

def newParagraph():
  time.sleep(1)
  print()

OFFSET = 0
def tw(text, sleep=.05):
  for char in text:
    print(char, end='', flush=True)
    if char != '\a':
      time.sleep((sleep + OFFSET)  * (2 if char == ',' else 1))
  print('')
  time.sleep(1)

#input tables
straight = ['straight', 'ahead', 'forward', 'up']
back = ['back', 'return', 'down', 'run', 'run away']
interact = ['take', 'steal', 'yoink', 'use', 'pick', 'pick up', 'interact', 'investigate', 'search' 'yeet', 'push']
kill = ['kill', 'slaugher', 'murder', 'stab', 'decapitate']


print("WARNING: Please do not enter anything into the terminal while text is being displayed. \nIt may interfere with choice making functions. \nI am way too lazy to do anything about that.")
time.sleep(5)
clearScreen()
time.sleep(1)
#INTRODUCTION
logo()
time.sleep(1)
tw("A text-based adventure made by an inexperienced 17 year old IT student")
print()
tw("Press enter to start")
adventureBegin = input("")
print("Set the text speed you want. [slow/medium/fast] Default is medium.")
txtSpeed = input("> ")
if txtSpeed.lower() == "slow":
  OFFSET = 0.1
elif txtSpeed.lower() == "medium":
  OFFSET = 0
elif txtSpeed.lower() == "fast":
  OFFSET = -0.03
elif txtSpeed.lower() == "instant":
  OFFSET = -0.05
clearScreen()
tw("You check the time. It's about 2 am, and you're in the forest all alone. You've been looking for that damn mansion since earlier in the afternoon.")
newParagraph()
tw("You finally begin to see a clearing in the path ahead of you. You're out of the forest. You can see a shape in the distance. It's the mansion...")
newParagraph()
while True:
  tw("The house sits on top of a small hill in a large opening surrounded by the thick forest. As you approach it, you begin think about your options.")
  newParagraph()
  print("What do you want to do? \n - Enter the mansion \n - Go around the mansion")
  choice = input("> ")
  clearScreen()
  if "enter" in choice.lower():
    tw("As you approach the entrance, the doors open by themselves, almost as if they were magical. You step through the doors, and suddenly they close shut. You try opening the doors again, but they are firmly stuck in place. You have been trapped in the mansion.")
    while True:
      clearScreen()
      hallwayStraight()
      tw("You find yourself in a hallway right past the entrance.")
      newParagraph()
      print("What do you want to do? \n - Walk straight ahead \n - Turn around")
      choice = input("> ")
      if choice.lower() in straight:
        getKey = 0
        while True:
          clearScreen()
          tLeft()
          tw("You come across a fork in the road.")
          newParagraph()
          print("Which way do you want to go? \n - Straight ahead \n - Left")
          choice = input("> ")
          if choice.lower() == "take fork":
            tw("HAHAHAHAHA aren't you funny")
          elif choice.lower() in straight:
            while True:
              clearScreen()
              lockedDoor()
              tw("You find a locked door.")
              newParagraph()
              if getKey == 0:
                print("What do you want to do? \n - Turn around")
              elif getKey == 1:
                print("What do you want to do? \n - Turn around \n - Use simple key")
              choice = input("> ")
              if choice.lower() in back:
                break
              elif choice.lower() in interact and getKey == 0:
                tw("You do not have the key to open this door.")
              elif choice.lower() in interact and getKey == 1:
                tw("You open the door using the simple key you found, and head on through.")
                getEquip = 0
                getKey = 0
                while True:
                  clearScreen()
                  crossRoad()
                  tw("You approach a crossroad in the hallway.")
                  newParagraph()
                  print("What do you want to do? \n - Turn left \n - Walk straight down \n - Turn right \n - Go back")
                  choice = input("> ")
                  if choice.lower() in back:
                    print()
                    tw("There is literally no point in going back to where you came from.")
                  elif "left" in choice.lower():
                    clearScreen()
                    lockedDoor()
                    tw("It's another locked door...")
                    newParagraph()
                    if getKey == 0:
                      print("What do you want to do? \n - Go back")
                      choice = input("> ")
                      if choice.lower() in back:
                        continue
                    elif getKey == 1:
                      print("What do you want to do? \n - Go back \n \n - Use rotten key")
                      choice = input("> ")
                      if choice.lower() in back:
                        continue
                      elif choice.lower() in interact:
                        tw("You insert the rotten key. The door is rusted and won't unlock so easily, but you manage it, breaking the key in the process. You open the door, climb a flight of stairs, and begin exploring the second floor in your search for freedom.")
                        destroyedWall = 0
                        while True:
                          if destroyedWall == 0:
                            clearScreen()
                            cornerRight()
                            tw("The corridor takes a right turn.")
                            newParagraph()
                            print("What should you do? \n - Walk to the right \n - Go back")
                          elif destroyedWall == 1:
                            clearScreen()
                            tStraight()
                            tw("The rock broke through the wall on the left, revealing another path.")
                            print("WHat should you do? \n - Walk to the right \n - Walk to the left \n - Go back")
                          choice = input("> ")
                          if choice.lower() in back:
                            print()
                            tw("You have already checked everything downstairs. There is no point in going back now.")
                            time.sleep(1)
                          elif "right" in choice.lower():
                            while True:
                              clearScreen()
                              tRight()
                              tw("It's another fork in the road...")
                              newParagraph()
                              print("Which direction do you want to go? \n - Straight \n - Right \n - Go back")
                              choice = input("> ")
                              if choice.lower() == "take fork":
                                tw("Are you kidding me")
                              elif choice.lower() in back:
                                break
                              elif choice.lower() in straight:
                                clearScreen()
                                emptyStaircase()
                                if destroyedWall == 0:
                                  tw("There's a staircase in front of you, but there is seemingly nothing at the top. You decide there's no point in climbing the stairs.")
                                elif destroyedWall == 1:
                                  tw("There's a staircase in front of you, but there is seemingly nothing at the top. There is a large hole in the roof, it could be where that giant rock came from. You decide there's no point in climbing the stairs.")
                                time.sleep(1)
                                continue
                              elif "right" in choice.lower():
                                while True:
                                  clearScreen()
                                  emptyRoom()
                                  tw("The room is completely empty.")
                                  newParagraph()
                                  if destroyedWall == 0:
                                    print("What do you want to do? \n - Search the room further \n - Go back")
                                  elif destroyedWall == 1:
                                    print("What do you want to do? \n - Go back")
                                  choice = input("> ")
                                  if choice.lower() in back:
                                    break
                                  elif choice.lower() in interact and destroyedWall == 0:
                                    while True:
                                      print()
                                      tw("You find it suspicious that the room is so barren, so you decide to search it further.")
                                      newParagraph()
                                      tw("As you search the room, you notice a brick hanging slightly out from the wall.")
                                      newParagraph()
                                      print("What do you want to do with the brick? \n - Push it back in \n - Nothing")
                                      choice = input("> ")
                                      if "nothing" in choice.lower():
                                        print()
                                        tw("You decide to leave the loose brick alone")
                                        time.sleep(1)
                                        break
                                      
                                      elif choice.lower() in interact:
                                        print()
                                        tw("You push the brick back in place. Suddenly you hear a distant rumbling. You look behind you and see a huge rock rolling down the hallway you were just in.")
                                        time.sleep(1)
                                        clearScreen()
                                        time.sleep(1)
                                        cornerRight()
                                        time.sleep(2)
                                        clearScreen()
                                        time.sleep(1)
                                        tStraight()
                                        newParagraph()
                                        tw("The rock hit and broke down a wall on its path. You might want to check that out.")
                                        destroyedWall = 1
                                        time.sleep(1)
                                        break

                                  elif choice.lower() in interact and destroyedWall == 1:
                                    print()
                                    tw("You already searched the room. There is nothing else to find.")

                          elif "left" in choice.lower() and destroyedWall == 0:
                            print()
                            tw("That's a wall.")
                          
                          elif "left" in choice.lower() and destroyedWall == 1:
                            ##########
                            while True:
                              clearScreen()
                              deadEnd()
                              tw("hurr durr come back later wip bois")
                              time.sleep(3)
                              sys.exit()
                            ##########

                    elif getKey == 1:
                      print("What do you want to do? \n - Go back")
                      choice = input("> ")
                      if choice.lower() in back:
                        continue

                  elif choice.lower() in straight:
                    clearScreen()
                    hallwayStraight()
                    tw("You walk down the hallway. It seems a bit longer than the others...")
                    newParagraph()
                    print("Do you keep walking or go back? \n - Keep walking \n - Go back")
                    choice = input("> ")
                    if "walk" in choice.lower():
                      clearScreen()
                      hallwayStraight()
                      tw("You keep walking down the hallway, which seems painfully long. You feel like you've been walking forever, but there just is no end to this corridor.")
                      newParagraph()
                      print("Do you really want to keep walking down this corridor? \n - Yes \n - No")
                      choice = input("> ")
                      if choice.lower() == "yes":
                        clearScreen()
                        hallwayStraight()
                        tw("You keep walking, and walking, and walking down the corridor.")
                        tw("Then you walk some more")
                        tw("Finally, you begine to see an end to the corridor. You breathe a sigh of relief.")
                        while True:
                          clearScreen()
                          emptyRoom()
                          if getEquip == 0:
                            tw("You enter an empty room. On the far side of the room is an armor stand and a weapon rack, with a simple wooden sword and a lousy piece of leather armor on display. The realization falls over you that you might not be alone in this mansion.")
                            newParagraph()
                            print("What do you want to do now? \n - Pick up weapon and armor \n - Go back")
                            choice = input("> ")
                            if choice.lower() in interact:
                              tw("You grab the sword and the worn leather chestplate. Any form of protection might help at this point.")
                              getEquip = 1
                            elif choice.lower() in back:
                              print("Are you really sure you want to go back empty handed after all this time? \n - No")
                              choice = input("> ")
                              if choice.lower() == "no":
                                continue
                          elif getEquip == 1:
                            tw("The room is empty, lest for the armor stand and weapon rack you just looted.")
                            newParagraph()
                            print("What should you do from here? \n - Go back")
                            choice = input("> ")
                            if choice.lower() in back:
                              break
                      elif choice.lower() == "no":
                        tw("You decide it's not worth the effort to walk any further, and you begin walking back to where you started.")
                        continue
                    elif choice.lower() in back:
                      continue
                  elif "right" in choice.lower():
                    while True:
                      clearScreen()
                      skeleton()
                      tw("It's a skeleton! As it spots you, it begins slowly walking towards you...")
                      newParagraph()
                      if getEquip == 1:
                        print("Think fast! What should you do? \n - Run away \n \n - Kill skeleton")
                        choice = input("> ")
                        if choice.lower() in back: ###############
                          tw("You hurry back out of the room and shut the door behind you. The skeleton shouldn't be able to open it.")
                          break
                        elif choice.lower() in kill:
                          clearScreen()
                          time.sleep(1)
                          skelHeadPreHit()
                          time.sleep(2)
                          clearScreen()
                          time.sleep(.5)
                          skelHeadPostHit()
                          time.sleep(1)
                          tw("You stab the wooden sword into the skeleton's skull, killing it instantly. As the skeleton turns to dust, it drops a rotten key. You grab the key and walk out of the room.")
                          getKey = 1
                          break
                      elif getEquip == 0:
                        print("Think fast! What should you do? \n - Run away")
                        choice = input("> ")
                        if choice.lower() in back:
                          tw("You hurry back out of the room and shut the door behind you. The skeleton shouldn't be able to open it.")
                          break
                        elif choice.lower() in kill:
                          tw("You don't have any means to kill it.")
          elif "left" in choice.lower():
            while True:
              clearScreen()
              emptyRoom()
              if getKey == 0:
                tw("You enter an empty bedroom. On the night stand lies a simple key.")
              elif getKey == 1:
                tw("The bedroom is empty")
              newParagraph()
              if getKey == 0:
                print("What do you do? \n - Grab simple key \n - Go back")
              elif getKey == 1:
                print("What do you do? \n - Go back")
              choice = input("> ")
              if choice.lower() in interact:
                tw("You grab the simple key.")
                getKey = 1
              elif choice.lower() in back:
                break

      elif choice.lower() in back:
        while True:
          clearScreen()
          deadEnd()
          tw("The door won't budge...")
          newParagraph()
          print("What do you want to do? \n - Turn around")
          choice = input("> ")
          if choice.lower() in back:
            break

  elif "around" in choice.lower():
    tw("You take a walk around the mansion to check it out. You notice there are no other doors than the main entrance, and all the windows are tightly sealed, making you unable to open any of them.")
    newParagraph()
    tw("You see no other possible option than to return to the main entrance and head inside.")
    clearScreen()
