from os import environ
#find out if i should change some lists to tuples by the networkchuck video

#Should I just put the stats in a dictionary?



# the shell also works on bash
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
#This environ thing is to hide the pygame window
#Don't forget to add music and when you do also find out how to get the files of music or if it's given online,also watch a video on how to do it.
###To be honest i don't understand why pygame dont work.
import random,os,time,pygame as py
#import pygame as py makes it so you only have to type py to use the functions

#For a sec I thought it was not randomizing because it was doing Ender alot but it is as it showed by a draw
#pygame is gray because iit isn't being used.

#pygame.mixer.init()

#pygame.mixer.music.load('song1.mp3')
#pygame.mixer.music.unload()
#Get's rid

#pygame.mixer.music.play(loops=-1, start=10, fade_ms=2000)

#pygame.mixer.music.rewind()
#pygame.mixer.music.stop()
#pygame,mixer.music.pause()
#pygame.mixer.music.unpause()

#pygame.mixer.music.fadeout(1000)

#pygame.mixer.music.get_volume()
#pygame.mixer.music.set_volume(0.5)

#pygame.mixer.music.get_pos()
#What time it is in the song

#pygame.mixer.music.set_pos(10)

#pygame.mixer.music.get_busy()

#Hashtaged all the python code for later reference and because I can't find out how to import sound like the mp.3

#pygame.mixer.music.queuq('song2.mp3')
#The basics

#List goes here for the agility things

agility_list = ["Orc = 0.5","Human = 1","Elf = 1.25","Mink = 1.5","Human = 1"]


#List goes here for the strength things

strength_list = ["Human = 1","Wizard = 1.25","Orc = 1.5","Elf = 0.75","Mink = 0.5"]

#This list is for moves

move_list = ["Slash","Stab","Punch","Kick","Bash","Fireball","Ice","Still thinking bout it"]

#this list is for race abilities

race_ability_list = ["Overbearing strength", "Overbearing agility", "Overbearing intelligence", "Overbearing force","Overbearing charisma(Has a chance to lower damage)"]

#This list states how im gonna do that like ask what move next and showing it.

strength_ability_list = ["Slash = 1","Stab = 2","Punch = 3","Kick = 4","Bash = 5","etc, and I'll have to ask after every thingy,then change dmg to ability times multiplier and etc,then I have to also do agility","This gon take a minute and it sucks."]
magic_ability_list = ["Mana ball","mana pool","Regeneration","Mana blade"]
#Change these abilities to dictionary for the name to have a : which is the damage or multiplier or smth
if "Mana ball" in magic_ability_list:
  print("Hi")
  #Just to test basically.I also have to do something about all these comments.Also create only max 3 ability lists.
#Not using it yet,pretty much just to store ideas, and also to late maybe use the ideas from the list,and create more like add if it's effective,non-effective,super non-effective,super-effective,etc.
#Also like you can only use abilities a certain amount of time so county that by "abilitynameuses = 10 so you  uses_left = "abilitynameuses" - "timesused".So you have used {abilityname} {uses_left} times.

in_battle = "No"
chars_made = 0
race_buff = 0
race_buff2 = 0
player_2_hp_left = 0
player_1_hp_left = 0
draw_dmg = 0
damage = 0
battle_commence = "No"

#Add it so off of race it changes to roll to have a higher chance to attack like agility.So add  agility

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(25)*rollDice(25))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(8)*rollDice(8))/2)+12
  return strengthStat

while True:
  if chars_made == 0:
    print("⚔️ CHARACTER BUILDER ⚔️")
    print()
    name1 = input("Name your Legend:\n")
    type = input("Character Type (Human, Elf, Wizard, Orc,Mink):\n")
    print()
    print(name1)
    health1 = health()
    strength1 = strength()
    print("HEALTH:", health1)
    print("STRENGTH:", strength1)
    print()
    print("May your name go down in Legend…")
    print()
  if chars_made == 1:
    print("⚔️ CHARACTER BUILDER ⚔️")
    print()
    name2 = input("Name your Legend:\n")
    type2 = input("Character Type (Human, Elf, Wizard, Orc,Mink):\n")
    print()
    print(name2)
    health2 = health()
    strength2 = strength()
    print("HEALTH:", health2)
    print("STRENGTH:", strength2)
    print()
    print("May your name go down in Legend…")
    print()
  chars_made += 1
  again = input("Again?By the way, you can't battle if you haven't made two characters.And the battles for now are only 1 on 1,so it's advised to create two characters.\n")
  if chars_made == 1:
    print("You have made", chars_made, "character.")
  elif chars_made > 1:
    print("You have made", chars_made, "characters.")
  
  if chars_made == 2:
    break
  if again=="No" or again=="no":
    break
  time.sleep(3)
  os.system("clear")
if chars_made == 2:
  print(f"{name1} has a health of {health1} and a strength of {strength1}.{name2} has a health of {health2} and a strength of {strength2}\n")
  battle_commence = "Yes"
while battle_commence == "Yes":
  if type == "Human" or type == "human:":
    #Add a option to see a race details table or chart.
    #print(f"{name1} is a human,the basis of races,your strength stat buff is 1.Note get rid of these bc it causes more wordsthanneeded\n") 
    race_buff = 1
  elif type == "Elf" or type == "elf":
    #print(f"{name1} has selected the Elf race,specializing in close combat in groups,being weak on your own grants a strength debuff of 0.75 the regular stat.\n")
    race_buff = 0.75
  elif type == "Wizard" or type == "wizard":
    #print(f"{name1} has selected the wizard class,specializing in powerful magical spells,with a strength buff of 1.25.\n")
    race_buff = 1.25
  elif type == "Orc" or type == "orc":
    #print(f"{name1} has selected the Orc race,specializing in strength over all,with a strength buff of 1.5.\n")
    race_buff = 1.5
  elif type == "Mink" or type == "mink":
    #print(f"{name1} has selected the Mink race,specializing in agility over strength,with a strength debuff of 0.5.\n")
    #print("You have chosen the mink race.You have a 50% chance to deal double damage.")
    
    race_buff = 0.5
  else: 
    race_buff = 1
  if type2 == "Human" or type2 == "human":
    #print(f"{name2} is a human,the basis of races,your strength stat buff is 1.\n")
    race_buff2 = 1
    
  elif type2 == "Elf" or type2 == "elf":
    race_buff2 = 0.75
    #print(f"{name2} has selected the Elf race,specializing in close combat in groups,being weak on your own grants a strength debuff of 0.75 the regular stat.\n")
  
  elif type2 == "Wizard" or type2 == "wizard":
    race_buff2 = 1.25
    #print(f"{name2} has selected the wizard class,specializing in powerful magical spells,with a strength buff of 1.25.\n")
  
  elif type2 == "Orc" or type2 == "orc":
    race_buff2 = 1.5
    #print(f"{name2} has selected the Orc race,specializing in strength over all,with a strength buff of 1.5.\n")
  
  elif type2 == "Mink" or type2 == "mink":
    #print(f"{name2} has selected the Mink race,specializing in agility over strength,with a strength debuff of 0.5.\n")
    race_buff = 0.5
  
  else:
    race_buff = 1

  time.sleep(6)
  print("Battle commence!!!")

  player_one_place = rollDice(6)
  player_two_place = rollDice(6)
    
  if player_one_place > player_two_place:
    print(f"{name1} goes first!")
    playerone_first = "Yes"
    
  elif player_one_place < player_two_place:
    
    print(f"{name2} goes first!")
    playerone_first = "No"
    
  elif player_one_place == player_two_place:
    
    print("Draw,both of you attack.")
    playerone_first = "Draw"  

  if playerone_first == "Yes":
    damage = float(race_buff) * float(strength1)
    
    player_2_hp_left = float(health2) - float(damage)
    
    print(f"{name1} attacks {name2} for {damage} damage, leaving them with {player_2_hp_left} health left.\n")
    
    if player_2_hp_left <= 0:
      print(f"{name2} has died,{name1} wins!\n")
      exit()
    else:
      time.sleep(5)
      health2 = player_2_hp_left
      continue
  elif playerone_first == "No":
    
    damage = float(race_buff2) * float(strength2)
    player_1_hp_left = float(health1) - float(damage)
    print(f"{name2} attacks {name1} for {damage} damage, leaving them with {player_1_hp_left} hp left.\n")
    if player_1_hp_left <= 0:
      print(f"{name1} has died, {name2} wins!\n")
      exit()
    else:
      time.sleep(5)
      health1 = player_1_hp_left
      
      continue
  elif playerone_first == "Draw":
    
    damage = float(race_buff) * float(strength1)
    
    draw_dmg = float(race_buff2) * float(strength2)
    
    player_2_hp_left = float(health2) - float(damage)
    
    player_1_hp_left = float(health1) - float(draw_dmg)
    
    print(f"{name1} attacks {name2} for {damage} damage, leaving them with {player_2_hp_left} hp left.\n")
    
    print(f"While {name2} attacks {name1} for {draw_dmg} damage leaving them with {player_1_hp_left} hp left.\n")
    
    if player_2_hp_left <= 0:
      print("{name2} has died, {name1} wins!\n")
      exit()
    elif player_1_hp_left <= 0:
      print(f"{name1} has died, {name2} wins!\n")
      exit()
    elif player_2_hp_left <= 0 and player_1_hp_left <= 0:
      print("This battle has ended in a draw.\n")
    else:
      health1 = player_1_hp_left
      health2 = player_2_hp_left
      time.sleep(5)
      continue
    #Whole bunch of ifs,elifs,and elses im lucky it aint break, but it does work.
    exit()
      #Note,had a error so I used time sleep so apparently it keeps showing the same text of the same battle.
  #Shorten the time gap,then make moves later on so there can be more damage opportunities.

    
#Add a music choice featurefor the battle.
