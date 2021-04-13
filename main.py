#Liam Etcheto, StudentID:417459

import time
import random

#Static entities
inventory = ['canteen']
groundItems = {'openMeadow': ['red flower'], 'forest': [], 'riverBridge': [], 'recedingMeadow': ['some grass'], 'spiralrock': ['small red rock'], 'lakeFront': [], 'farm': [], 'farmHouse': ['old painting'], 'shack': ['rusty helmet'], 'insideHouse': []}
location = ''
searching = ''
fill = ''
eggCount = 0
health = 100
climbCount = 0
sword = False
consumables = ['canteen', 'full canteen', 'steak', 'old painting', 'red flower', 'small red rock', 'some grass']
cyclopesCount = 0

rockGoblinHealth = 40
cellarOrcHealth = 100
cyclopesHealth = 925





def startgame():  
  print("Type \"start\" to begin")
  while True:
    start = input().lower()
    if start == 'start':
      break 
  #Initial text
  print("\nYou have entered the world of L.O.R.K.!")
  print("L.O.R.K.'s creation is inspired by the text adventure game \"Zork I\" made by Infocom in 1980")
  print("\nYou are standing in an open meadow with an empty canteen. Better find something to drink and a weapon to defend yourself with. (type \"help\" to see actions you can take)")
  #Enter game
  openMeadow()

def actions():
  global inventory
  global location
  global eggCount
  global searching
  global health

  if health <= 0:
    print("\nYour health has reached zero!\n\n*********\nGAME OVER\n*********\n\nTry again.\n")
    return lostGame()

  x = input(">")

  #=====HELP
  if x.lower() == 'help':
      print("\n~ go [direction: North, East, South, West]\n~ look\n~ inventory\n~ health\n~ consume\n~ search\n~ drop\n~ take\n~ etc.. (try stuff)")
 
  #=====GO
  if x.lower() == 'go':
    print("Specify the direction.")

  #=====INVENTORY
  if x.lower() == 'inventory' or x.lower() == 'backpack':
    print(inventory)

  #=====HEALTH 
  if x.lower() == 'health':
    if health == 100:
      print(f"Your health is: {health}/100 MAX")
    else:
      print(f"Your health is: {health}/100")
 
  #=====TAKE
  if x.lower() == 'take' or x.lower() == 'grab' or x.lower() == 'pick up':
    if len(groundItems[str(location)]) == 0:
      print("There's nothing to take.")
    else:
      itemtake = input(f"What would you like to take? {groundItems[str(location)]}\ntake>")
      if itemtake in groundItems[str(location)]:
        inventory.append(str(itemtake))
        groundItems[str(location)].remove(str(itemtake))
      if itemtake == 'steak':
        print("Consuming the steak will replenish 80 hp.")


  #=====DROP
  if x.lower() == 'drop':
    itemdrop = input("What would you like to drop?\n " + str(inventory) + "\ndrop>")
    if itemdrop in inventory:
      if itemdrop == 'pickles':
          print("You can't drop the pickles.")
      else:
        inventory.remove(str(itemdrop))
        groundItems[str(location)].append(str(itemdrop))
        print(f"You have dropped {itemdrop} onto the ground.")
    elif itemdrop == 'pickles':
      groundItems[str(location)].append(str(itemdrop))
 
  #=====SEARCH
  if x.lower() == 'search':
    searching = input("What would you like to search?\nsearch>")
    if searching == 'ground' or searching == 'floor':
      if len(groundItems[str(location)]) == 0:
        print("You find nothing.")
      else:
        print(f"You find {groundItems[str(location)]}\n")
    if searching.lower() == 'chest':
      if location == 'insideHouse':
        groundItems['insideHouse'].append('oil lantern')
        print("You search the chest and find an oil lantern.")
    else:
      return(x)
 
  #=====FILL
  if x.lower() == 'fill':
    fill = input(f"What would you like to fill? \n {inventory}\nfill>")
    if fill == 'canteen' or fill == 'full canteen':
      if 'canteen' in inventory:
        if location == 'riverBridge' or location == 'lakeFront' or location == "forest":
          inventory.remove('canteen')
          inventory.append('full canteen')
          print("You fill your canteen. Full canteen's replenish 20 hp.")
        else:
          print("There's no nearby water source to fill your canteen.")
      elif 'full canteen' in inventory:
        print("Your canteen is full.")
    else:
      print("That item cannot be filled.")
  
  #=====CONSUME
  if x.lower() == 'consume' or x.lower() == 'eat' or x.lower() == 'drink':
    drink = input("What would you like to consume?\n " + str(inventory) + "\nconsume>")
    if drink == 'canteen' or drink == 'full canteen':
      if drink == 'canteen':
        if 'canteen' in inventory:
          print("You can't drink from a canteen that is empty.")
        else:
          print("You don't have an empty canteen, but you do have a full one.")
      if drink == 'full canteen':
        if 'canteen' in inventory:
          print("You have an empty canteen not a full one.")
        else: 
          inventory.remove('full canteen')
          inventory.append('canteen')
          if health < 100:
            if health + 20 > 100:
              health = 100
              print("Refreshing! That topped off your hp.")
            else:
              print("Refreshing! (+20 hp)")
              health += 20
          else:
            print("Refreshing!")
    elif drink.lower() == 'steak':
      if 'steak' in inventory:
        inventory.remove('steak')
        if health < 100:
          if health + 80 > 100:
            health = 100
            print("Quite the hearty slab of meat. That topped off your hp.")
          else:
            health += 80
            print("Quite the hearty slab of meat. (+80 hp)")
        else:
          print("Quite the hearty slab of meat. Time to take a nap.")
    elif drink.lower() in consumables:
      print(f"You eat the {drink}")
    if drink not in consumables:
      print("You can't consume that.")
    
    

  #=====Easter Eggs
  if x.lower() == 'hi' or x.lower() == 'hello':
    print("Oh hey!")
  if x.lower() == 'zork':
    if eggCount == 1:
      print("I already told you! This is L.O.R.K.!")
    elif eggCount == 2:
      print("I already told you! This is L.O.R.K.! Stop Asking!")
    elif eggCount == 3:
      print("No")
    elif eggCount >= 4:
      print("")
    else:
      print("This is L.O.R.K.!")
    eggCount += 1
  return(x)
  
#=====Open Meadow
def openMeadow():
  global inventory
  global location
  global searching
  location = "openMeadow"
  print("\n\nOpen Meadow\nThere are so many flowers!")

  while True:
    searching = ''
    x = actions()
    if x.lower() == 'look':
      print("The meadow is filled with countless numbers of red, purple and yellow, flowers,you can't even see your feet! To the north you see a heavily wooded forest. To the east there is a wide raging river that you can see neither the start or end of, but there's a long rickety wooden bridge to cross it. To the south you see more meadow, and even more flowers. To the west you spot a large wooden farm house that appears to be abondoned.")
    if searching.lower() == 'flowers':
      print("The flowers are pretty and that's it.")
    if x.lower() == 'go north':
      return forest()
    if x.lower() == 'go east':
      return riverBridge()
    if x.lower() == 'go south':
      return recedingMeadow()
    if x.lower() == 'go west':
      return farm()



#=====Forest
def forest():
  global inventory
  global location
  location = "forest"
  print("\n\nForest")
  print("The forest is even more dense on the inside than the outside.")
  
  while True:
    x = actions()
    if x == 'look':
      print("The forest has moss growing on the tree bark and the sun barely manages to shine through the heavy foliage. It is so dense you can barely grasp your sense of direction. To the north, you see a gargantuan mountain range. Southward you see the lush open meadow. Looking east, you see the edge of a lake. To the west, you are perplex by a grand opening of a cave.")

    if x.lower() == 'go west' or x.lower() == 'enter' or x.lower() == 'enter cave':
      if 'oil lantern' in inventory:
        print("You turn on your oil lantern and enter the unknown.")
        time.sleep(3)
        return cyclopes()
      else:
        print("You won't be able to see anything if you go in the cave, you need to find a light source first.")
    if x.lower() == 'go north':
      print("Can't go there, the mountains are insurmountable")
    if x.lower() == 'go east':
      print("Can't go there, there's no time for a swim, but you can fill your canteen.")
    if x.lower() == 'go south':
      return openMeadow()

    
#=====Cyclopes Battle
def cyclopes():
  cyclopesCount = 0
  print("You step deeper into the expansive cave. You start hearing earth shaking foot steps. You look behind you to see a 20 foot tall cyclopes blocking the exit of the cave. In a deep gravely voice the cyclopes mutters, \"Hello there puny human, you've made a very bad decision today.\" Time to fight! \n\n**************************************************\n")
  def myTurn():
    global cyclopesHealth
    global inventory
    global health
    global cyclopesCount
    while True:
      if health <= 0:
        print("\nYour health has reached zero!\n\n*********\nGAME OVER\n*********\n\nTry again.\n")
        lostGame()
      myAttack = random.randint(1,4)
      myDamage = random.randint(10,20)
      attackOrHeal = input(f"Attack or heal? (hp: {health}) (cyclopes hp: {cyclopesHealth})\n>")
      if attackOrHeal.lower() == 'attack' or attackOrHeal.lower() == 'heal':
        if attackOrHeal.lower() == 'attack':
          if myAttack == 1:
            cyclopesHealth -= myDamage
            print(f"You charge at the cyclopes and stab his achillies tendon. (-{myDamage} cyclopes hp)")
            time.sleep(2)
            cyclopesTurn()
          if myAttack == 2:
            cyclopesHealth -= myDamage
            print(f"You run and jump off the side of the wall and stab into the cyclopes chest, and the blade down as you fall. (-{myDamage} cyclopes hp)")
            time.sleep(2)
            cyclopesTurn()
          if myAttack == 3:
            cyclopesHealth -= myDamage
            print(f"The cyclopes swings for an attack but you evade it and counterattack. (-{myDamage} cyclopes hp)")
            time.sleep(2)
            cyclopesTurn()
          if myAttack == 4:
            cyclopesHealth -= (myDamage*3)
            print(f"You climb up the cyclopes back and stab him in his only eye! (-{myDamage*3} cyclopes hp)")
            time.sleep(2)
            cyclopesTurn()



        if attackOrHeal.lower() == 'heal':
          healing = input(f"Inventory: {inventory}. What would you like to heal with? (or type \"cancel\")\nheal>")
          if healing.lower() == 'cancel':
            pass
          if healing == 'steak':
            if 'steak' in inventory:
              inventory.remove('steak')
              if health < 100:
                if health + 80 > 100:
                  health = 100
                  print("Quite the hearty slab of meat. That topped off your hp.")
                  cyclopesTurn()
                else:
                  health += 80
                  print("Quite the hearty slab of meat. (+80 hp)")
                  cyclopesTurn()
              else:
                print("Quite the hearty slab of meat. Time to take a nap.")
                cyclopesTurn()
              if healing != 'cancel' or healing != 'steak':
                if healing in inventory:
                  print("You can't consume that.")
                else:
                  print("That's not in your inventory.")  
          if healing == 'oil lantern':
            if 'oil lantern' in inventory:
               print("AHHHHHHHHH! GLUG GLUG GLUG (-30 hp)")
               health -= 30
          if 'full canteen' in inventory:
            if healing.lower() == 'full canteen':
              inventory.remove('full canteen')
              inventory.append('canteen')
              if health < 100:
                if health + 20 > 100:
                  health = 100
                  print("Refreshing! That topped off your hp!")
                  time.sleep(2)
                  cyclopesTurn()
                else:
                  print("Refreshing! (+20 hp)")
                  health += 20
                  time.sleep(2)
                  cyclopesTurn()
              else:
                print("Refreshing!")
                time.sleep(2)
                cyclopesTurn()
            else:
              if healing.lower() == 'cancel':
                pass
              else:
                print("You can't consume that.")
            if healing.lower() not in inventory:
              if healing.lower() == 'cancel':
                pass
              else:                
                print("That's not in your inventory.")
        else:
          print("You have nothing to heal with.")
      if attackOrHeal.lower() == 'odysseus':
        if cyclopesCount == 0:
          cyclopesCount += 1
          cyclopesHealth -= 750
          print("The cyclopes begins trembling with fear")
        elif cyclopesCount > 0:
          print("The cyclopes heard the first time.")

  def cyclopesTurn():
    global health
    if cyclopesHealth <= 0:
        print("You have defeated the cyclopes!\n\n**************************************************\n\n")
        return endGame()
    while True:
      cyclopesAttack = random.randint(1,4)
      cyclopesDamage = random.randint(14,28)
      if cyclopesAttack == 1:
        health -= cyclopesDamage
        print(f"The cyclopes slams you with his massive club. (-{cyclopesDamage} hp)")
        time.sleep(2)
        return myTurn()
      if cyclopesAttack == 2:
        health -= cyclopesDamage
        print(f"The cyclopes tears a large stalactite off the roof and chucks it at you. (-{cyclopesDamage} hp)")
        time.sleep(2)
        return myTurn()
      if cyclopesAttack == 3:
        health -= cyclopesDamage
        print(f"The cyclopes picks you up with one hand and throws you to the ground. (-{cyclopesDamage} hp)")
        time.sleep(2)
        return myTurn()
      if cyclopesAttack == 4:
        print("The cyclopes swings his mace in a fury of bloodlust! You dodge out of the way just in time.")
        time.sleep(2)
        return myTurn()
  myTurn()


#=====River Bridge
def riverBridge():
  global inventory
  global location
  location = "riverBridge"
  print("\n\nThe River and the Bridge")
  print("The river rages southward, and the wooden rickety bridge's integrity is certainly to be questioned.")
  
  while True:
    x = actions()
    if x == 'look':
      print("Crossing this bridge is asking for trouble, but across from it (east) you see a somewhat tall rock formation that's shaped like a cone, it appears to be man made. To the north you see more lake. To the south you see the eastern rim of the meadow beginning to fade and grass takes its place, but there's an out of place depression in the ground. To the west is the open meadow.")
    if x.lower() == 'go north':
      print("You can't go north from here, the river makes the surrounding ground moist, it's too risky!")
    if x.lower() == 'cross' or x.lower() == 'cross bridge' or x.lower() == 'go east':
      return bridgeSequence()
    if x.lower() == 'go south':
      print("You can't go south from here, the river makes the surrounding ground moist, it's too risky!")
    if x.lower() == 'go west':
      return openMeadow()


#=====Bridge Sequence
def bridgeSequence():
  global location
  print("You begin crossing the rickety bridge.")
  time.sleep(2)
  print("The creaking of the bridge is so loud you can hear it over the river!")
  time.sleep(3)
  n = random.randint(1,50)
  if n == 1:
    print("UH OH!\nThe bridge suddenly collapses and there's no where near enough time to scramble off of it! You fall into the raging river and get thrown to the bottom of the canyon.\n*********\nGAME OVER\n*********\n\nTry again.\n")
    lostGame()
  else:
    print("Barely made it across!")
    time.sleep(1)
    if location == 'riverBridge':
      return spiralRock()
    else:
      return riverBridge()

#=====Spiral Rock
def spiralRock():
  global inventory
  global location
  global climbCount
  global sword

  location = "spiralRock"
  print("\n\nSpiral Rock")
  print("You stand at the base of an amazing rock \"sculpture\" so to say. You see footprints in the grass surrounding the rock.")

  while True:
    x = actions()
    if x == 'look':
      print("It must have took a longtime to chisel this thing! This basalt rock spirals upwards for quite a ways and flatens out on top. Until the top, the spiral is at a good angle to climb up it. To the north you see the lake, and something whimsical? To the east is this massive rock right in front of me, spiral rock, but behind it is an expansive canyon that wraps up and towards the spiral rock and the lake, but then divergeses east endlessly. To the south is the canyon. To the west is the rickety bridge.")
    if x.lower() == 'go north':
      return lakeFront()
    if x.lower() == 'go east':
      print("Can't go east, spiral rock is in the way.")
    if x.lower() == 'go south':
      print("Can't go south, you'll fall into the canyon.")
    if x.lower() == 'cross' or x.lower() == 'cross bridge' or x.lower() == 'go west':
      return bridgeSequence()
    if x.lower() == 'climb' or x.lower() == 'climb rock' or x.lower() == 'climb spiral rock':
      if sword == True:
        print("There's no need to climb spiral rock, you already took the longsword.")
      else:
        return climbingSequence()


#===== Climbing Sequence
def climbingSequence():
  global inventory
  global sword
  pullCount = 0
  global health
  print("You begin climbing spiral rock.")
  time.sleep(2)
  print("The rocks crumbling beneath your feet!")
  n = random.randint(1,3)
  if n == 1:
    print("You lose your footing and fall to the ground. (-10 hp)")
    health -= 10
    time.sleep(2)
    return spiralRock()
  print("you've reached the top! There's a sword dug into the center of the rock.")
  while True:
    pull = input("Try to retrieve the sword.\n>")
    if pull.lower() == "pull" or pull == 'pull sword' or pull == 'take' or pull == 'take sword':
      pullCount += 1
      if pullCount == 1:
        print("You attempt pulling the sword out of the rock, it seems there's no luck.")
      if pullCount == 2:
        print("The sword actually budged this time, it's begging to wiggle loose!")
      if pullCount == 3:
        sword = True
        inventory.append("longsword")
        print("It's free! You unleash the sword from the rock and sheath it on your hip.")
        time.sleep(3)
        print("You begin climbing back down the rock.")
        time.sleep(2)
        print("You made it to the bottom of the rock. THERE\'S A GOBLIN DEFENDING THE SWORD!")
        time.sleep(3)
        return rockGoblinFight()
  

#=====Spiral Rock Goblin Fight
def rockGoblinFight():
  print("The goblin utters complete non-sense and goes beserk! Time to fight!\n\n**************************************************\n")
  def myTurn():
    global rockGoblinHealth
    global inventory
    global health
    while True:
      if health <= 0:
        print("\nYour health has reached zero!\n\n*********\nGAME OVER\n*********\n\nTry again.\n")
        return lostGame()
      myAttack = random.randint(1,4)
      myDamage = random.randint(10,20)
      attackOrHeal = input(f"Attack or heal? (hp: {health}) (goblin hp: {rockGoblinHealth})\n>")
      if attackOrHeal.lower() == 'attack' or attackOrHeal.lower() == 'heal':
        if attackOrHeal.lower() == 'attack':
          if myAttack == 1:
            rockGoblinHealth -= myDamage
            print(f"You ruthlessly jab your sword at the goblin and he shrieks! (-{myDamage} goblin hp)")
            time.sleep(2)
            goblinTurn()
          if myAttack == 2:
            rockGoblinHealth -= myDamage
            print(f"You slash the goblin, giving him a wicked gash. (-{myDamage} goblin hp)")
            time.sleep(2)
            goblinTurn()
          if myAttack == 3:
            rockGoblinHealth -= myDamage
            print(f"With a quick blow from your blade, you dismember one of the goblins limbs. (-{myDamage} goblin hp)")
            time.sleep(2)
            goblinTurn()
          if myAttack == 4:
            rockGoblinHealth -= myDamage
            print(f"You deliver a powerful round house kick to the goblin's cranium. (-{myDamage} goblin hp)")
            time.sleep(2)
            goblinTurn()
        if attackOrHeal.lower() == 'heal':
          if 'full canteen' in inventory:
            healing = input(f"Inventory: {inventory}. What would you like to heal with? (or type \"cancel\")\nheal>")
            if healing.lower() == 'cancel':
              pass
            if healing.lower() == 'full canteen':
              inventory.remove('full canteen')
              inventory.append('canteen')
              if health < 100:
                if health + 20 > 100:
                  health = 100
                  print("Refreshing! That topped off your hp!")
                  time.sleep(2)
                  goblinTurn()
                else:
                  print("Refreshing! (+20 hp)")
                  health += 20
                  time.sleep(2)
                  goblinTurn()
              else:
                print("Refreshing!")
                time.sleep(2)
                goblinTurn()
            else:
              if healing.lower() == 'cancel':
                pass
              else:
                print("You can't consume that.")
            if healing.lower() not in inventory:
              if healing.lower() == 'cancel':
                pass
              else:                
                print("That's not in your inventory.")
          else:
            print("You have nothing to heal with.")


  def goblinTurn():
    global health
    if rockGoblinHealth <= 0:
        print("You have defeated the goblin!\n\n**************************************************")
        return spiralRock()
    while True:
      goblinAttack = random.randint(1,4)
      goblinDamage = random.randint(5,12)
      if goblinAttack == 1:
        health -= goblinDamage
        print(f"The goblin slashes you with his rusty dagger! (-{goblinDamage} hp)")
        time.sleep(2)
        return myTurn()
      if goblinAttack == 2:
        health -= goblinDamage
        print(f"The goblin ferociously bites you! (-{goblinDamage} hp)")
        time.sleep(2)
        return myTurn()
      if goblinAttack == 3:
        health -= goblinDamage
        print(f"The goblin fakes you out, causing you stumble to the ground and he gets a cheap shot. (-{goblinDamage} hp)")
        time.sleep(2)
        return myTurn()
      if goblinAttack == 4:
        health -= goblinDamage
        print(f"The goblin flying-goblin-kicks you in the head! (-{goblinDamage} hp)")
        time.sleep(2)
        return myTurn()
  myTurn()


  

#=====Lake Front
def lakeFront():
  global inventory
  global location
  location = "lakeFront"
  print("\n\nLake Front")
  print("This is a fine place to fill your canteen. You see a fairy, which can be assumed is the guardian of this lake.")
  while True:
    x = actions()
    if x == 'look':
      print("The lake sparkles with enchantment, the water is a beautiful transparent blue. The fairy flys close and speaks to you saying \"Tell him \'Odysseus\'\". To the north is the lake. To the east is excess sagebrush and desolation. To the south is spiral rock. To the west is the raging river.")
    if x.lower() == 'go north':
      print("There's no time for a swim")
    if x.lower() == 'go east':
      print("You are stopped by an invisible barrier, the fairy says to you \"I wouldn't go that direction, mortals havn't seemed to make it that far\".")
    if x.lower() == "go south":
      return spiralRock()
    if x.lower() == 'go west':
      print("Can't go there, you'll fall into the river.")


#=====Receding Meadow
def recedingMeadow():
  global inventory
  global location
  location = "recedingMeadow"
  print("\n\nReceding Meadow")
  print("The meadow's vegetation begins to thin and an outter edge of a canyon makes an appearance.")

  while True:
    x = actions()
    if x == 'look':
      print("A seemingly bottomless canyon unveiled itself as you got closer to it. The formation stretches southbound for countless miles, and you can't see the start or end of it. Besides a beautiful waterfall created by the river to the left, nothing but void remains in the canyon. To the north is the open meadow which is as graceful as ever. To the east is the raging river. To the west, there is a tiny worn down shack.")
    if x == 'go north':
      return openMeadow()
    if x == 'go east':
      print("Can't go east, the river is even more intense further down.")
    if x == 'go south':
      print("Can't go south, you'll fall into the canyon.")
    if x == 'go west':
      return shack()


#=====Farm and Farm House
def farm():
  global inventory
  global location
  location = "farm"
  frontDoor = True
  doorLock = True
  doorCount = 0

  print("\n\nFarm and Farm House")
  print("You're standing at the entrance of the farm house. The farm land is dry and desolate.")


  while True:
    x = actions()
    if x == 'look':
      print("Besides the farm house, there's nothing but dirt and some broken fence. What stands out is there are foot prints coming back and forth from southward to the farm house. To the north is the side of a cave, but no opening. To the east is the open meadow. To the south is a tiny worn down shack. To the west, behind the farm house, is stacks of rocks along with a drop-off being a canyon.")
    
    if x =='go north':
      print("There's no purpose in approaching the cave from the side.")
    if x == 'go east':
      return openMeadow()
    if x == 'go south':
      return shack()
    if x == 'go west':
      print("Can't go there, behind the hosue is the canyon and that would be quite the tumble.")
    
    
    if x == 'open door' or x == 'open' or x == 'open front door':
      if frontDoor == True:
        print("The front door is locked.")
      if doorLock == False:
        if doorCount == 0:
          frontDoor = False
          doorCount += 1
          print("As you open the front door, it falls off its hinges and causes a flury of dust to erupt into the air.")
        else:
          print("The door is already open, in fact, it's off its hinges.")
    if x.lower() == 'unlock' or x.lower() =='unlock door' or x.lower() == 'use key':
      if 'key' in inventory:
        doorLock = False
        print("You unlock the door.")
      else:
        print("You'll need to find the key that unlocks this door.")
    if x.lower() == 'go in house' or x == 'enter' or x == 'enter house' or x == 'go inside':
      if frontDoor == False:
        return insideHouse()
      else:
        print("You'll need to open the door first.")

#=====Inside House
def insideHouse():
  print("\n\nInside House")
  print("This house is certainly due for serious maintenence!")
  global location
  location = 'insideHouse'
  searching = ''
  while True:
    x = actions()
    if x == 'look':
      print("You step inside the single level abondoned farm house. Dust bunnies are plentiful. It's hard to see but you can make out everything in the room. You see a table and two chairs, and on top of the table appears to be a interrupted game of cards, which are also dusty. In the corner of the room you see a chest.")
    if x.lower() == 'exit' or x.lower() == 'exit house' or x.lower() == 'leave house' or x.lower() == 'go back' or x.lower() == 'leave' or x.lower() == 'go east':
      return farm()
    if x.lower() == 'go north' or x.lower() == 'go south' or x.lower() == 'go west':
      print("You have to leave the house first")
    


#=====Worn Down Shack
def shack():
  global inventory
  global location
  location = "shack"
  cellarDoor = True

  print("\n\nWorn Down Shack")
  print("There are many wooden boards scattered around the shack, the door is missing, and the inside is exposed.")

  while True:
    x = actions()
    if x == 'look':
      print("Looking closer into the shack reveals a cellar door that appears to be connected to a basement, you hear russling... To the north you see the abondoned wooden farm house, and a trail of footprints leading from the trapdoor towards the farm. To the east is the meadow and its outskirts, by the canyon. To the south is the boundless canyon that spans as far as the eye can see. To the west is a path that leads to the edge of the canyon, the canyon wraps around the whole southern part of the land.")
    if x.lower() == 'go north':
      return farm()
    if x.lower() == 'go east':
      return recedingMeadow()
    if x.lower() == 'go south':
      print("Can't go south, you'll fall into the canyon.")
    if x.lower() == 'go west':
      print("Can't go west, the canyon has wrapped around the corner here.")
    
    if x.lower() == 'open' or x.lower() == 'open cellar' or x.lower() == 'open cellar door' or x.lower() == 'open door':
      if cellarDoor == False:
        print("The cellar door is already open.")
      if cellarDoor == True:
        cellarDoor = False
        print("You open the cellar door. You hear a groan and a kackle, and your longsword shines bright blue.")
    if x.lower() == 'close' or x.lower() == 'close cellar' or x.lower() == 'close cellar door' or x.lower() == 'close door':
      if cellarDoor == True:
        print("The cellar door is already closed.")
      if cellarDoor == False:
        cellarDoor = True
        print("You close the cellar door.")
    if x.lower() == 'go down' or x.lower() == 'enter cellar' or x.lower() == 'go down cellar' or x.lower() == 'down':
      if cellarDoor == True:
        print("You have to open the door first.")
      if cellarDoor == False:
        if sword == True:
          return orcBattle()
        else:
          print("You should find a weapon before you go down there.")


#=====Orc Battle
def orcBattle():
  print("Your blade glows so brightly it illuminates the entire cellar. Allowing your eyes to meet those of one of the most menacingly and fearsome beasts you've ever seen. This Orc is hungry for blood. Time to fight!\n\n**************************************************\n")
  def myTurn():
    global cellarOrcHealth
    global inventory
    global health
    if health <= 0:
      print("\nYour health has reached zero!\n\n*********\nGAME OVER\n*********\n\nTry again.\n")
      lostGame()
    while True:
      myAttack = random.randint(1,4)
      myDamage = random.randint(10,20)
      attackOrHeal = input(f"Attack or heal? (hp: {health}) (orc hp: {cellarOrcHealth})\n>")
      if attackOrHeal.lower() == 'attack' or attackOrHeal.lower() == 'heal':
        if attackOrHeal.lower() == 'attack':
          if myAttack == 1:
            cellarOrcHealth -= myDamage
            print(f"You give a nice hack into the orc's shoulder, causing him to shriek in fury. (-{myDamage} orc hp)")
            time.sleep(2)
            goblinTurn()
          if myAttack == 2:
            cellarOrcHealth -= myDamage
            print(f"You go for a killing blow but the orc's speed interupts your move, you opt for a leg chop. (-{myDamage} orc hp)")
            time.sleep(2)
            goblinTurn()
          if myAttack == 3:
            cellarOrcHealth -= myDamage
            print(f"You swing your sword in rapid succession, leaving many slices and cuts on the orc's body. (-{myDamage} orc hp)")
            time.sleep(2)
            goblinTurn()
          if myAttack == 4:
            cellarOrcHealth -= (myDamage)
            print(f"You ram your sword straight into the orc's chest, he doesn't like this. (-{myDamage} orc hp)")
            time.sleep(2)
            goblinTurn()
        if attackOrHeal.lower() == 'heal':
          if 'full canteen' in inventory:
            healing = input(f"Inventory: {inventory}. What would you like to heal with? (or type \"cancel\")\nheal>")
            if healing.lower() == 'cancel':
              pass
            if healing.lower() == 'full canteen':
              inventory.remove('full canteen')
              inventory.append('canteen')
              if health < 100:
                if health + 20 > 100:
                  health = 100
                  print("Refreshing! That topped off your hp!")
                  time.sleep(2)
                  goblinTurn()
                else:
                  print("Refreshing! (+20 hp)")
                  health += 20
                  time.sleep(2)
                  goblinTurn()
              else:
                print("Refreshing!")
                time.sleep(2)
                goblinTurn()
            else:
              if healing.lower() == 'cancel':
                pass
              else:
                print("You can't consume that.")
            if healing.lower() not in inventory:
              if healing.lower() == 'cancel':
                pass
              else:                
                print("That's not in your inventory.")
        else:
          print("You have nothing to heal with.")


  def goblinTurn():
    global health
    if cellarOrcHealth <= 0:
        print("You have defeated the orc! It looks like he dropped some stuff when he died.\n\n**************************************************")
        groundItems['shack'].append('key')
        groundItems['shack'].append('steak')
        return shack()
    while True:
      goblinAttack = random.randint(1,4)
      goblinDamage = random.randint(10,18)
      if goblinAttack == 1:
        health -= goblinDamage
        print(f"The orc punches you square in the jaw. (-{goblinDamage} hp)")
        time.sleep(2)
        return myTurn()
      if goblinAttack == 2:
        health -= goblinDamage
        print(f"The orc fires an arrow into your abdomen, causing serious damage (-{goblinDamage} hp)")
        time.sleep(2)
        return myTurn()
      if goblinAttack == 3:
        health -= (goblinDamage/2)
        print(f"The orc slashes his sword in your direction and clips you. (-{goblinDamage/2}) hp)")
        time.sleep(2)
        return myTurn()
      if goblinAttack == 4:
        health -= goblinDamage
        print(f"The orc shrieks so loud your ears begin to bleed. (-{goblinDamage} hp)")
        time.sleep(2)
        return myTurn()
  myTurn()


def lostGame():
  time.sleep(3)
  exit()

def endGame():
  print("CONGRATULATIONS! YOU DEAFTED THE CYCLOPES! YOU WIN!")
  exit()
  
startgame()