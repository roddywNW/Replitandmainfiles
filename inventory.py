import os,time

try:
  f=open('inventory.txt','r')
  inventory = eval(f.read())
  f.close()
except:
  print("New inventory being made")

inventory = []

def add():
  time.sleep(1)
  os.system('clear')
  name = input("Enter name of item: ").capitalize()
  while True:
    try:
      qty = int(input("Enter quantity of item: "))
      break
    except:
      print("Item quantity has to be a whole number")
    #Try works with this and if theres an error then it'll run the except code  
  row = [name,qty]
  inventory.append(row)
  f = open('inventory.txt','w')
  f.write(str(inventory))
  f.write("\n")
  f.close()
  #Adds inventory to inventory.txt

def view():
  h1 = "Name"
  h2 = "Quantity"
  print(f"{h1:10} {h2:10}")
  for row in inventory:
    print(f"{row[0]:10} | {row[1]:10}")
    time.sleep(0.5)
  print("Press 5 to return to main menu")
  done = input("")
  if done == "5":
    print("Returning to main menu")
    time.sleep(0.5)
  else:
    print("That is not a valid choice,please try again")
    time.sleep(0.5)
    os.system('clear')
    return
  #Shows inventory from inventory.txt and return to main menu



def remove():
  time.sleep(1)
  os.system('clear')
  name = input("Enter name of item to remove: ").capitalize()
  delete = input("Are you sure you want to delete this item? Y/N").capitalize()
  if delete == "Y":
    for row in inventory:
      if row[0] == name:
        #First value in row is name so it looks for name in inventory by first value in row
        inventory.remove(row)
        print(f"{name} has been removed")
        time.sleep(2)
        break
  elif delete == "N":
    print(f"{name} will not be removed")
    time.sleep(.25)
    print("Returning to main menu")
    time.sleep(1)
  else:
    print("That is not a valid choice,please try again")
    time.sleep(1)
    os.system('clear')
    return
  #Add confirmation to delete item

#Could add a delete all option but idk


def auto_save():
  time.sleep(0.75)
  os.system('clear')
  try:
    print("Saving inventory...")
    f = open('inventory.txt','w')
    f.write(str(inventory)+'\n')
    f.close()
    time.sleep(0.25)
    print("Inventory saved")
    time.sleep(1)
    os.system('clear')
  except:
    print("No value to be saved,continue on!")
    time.sleep(.25)
    #Saves inventory to inventory.txt automatically

def auto_load():
  global inventory
  time.sleep(0.75)
  os.system('clear')
  try:
    print("Loading inventory...")
    with open('inventory.txt','r') as f:
      #with open automatically closes file
      inventory=eval(f.read())
    time.sleep(0.25)
    print("Inventory loaded")
    time.sleep(0.25)
    os.system('clear')
  except:
    print("No inventory to load,continue on!")
    time.sleep(.5)
    os.system('clear')
    #Loads inventory from inventory.txt automatically

while True:
  time.sleep(0.75)
  os.system('clear')
  auto_load()
  choices = input("Enter inventory: 1.Add 2.View 3.Remove 4.Exit").capitalize()
  if choices == "1" or choices=="Add":
    add()
  elif choices == "2" or choices == "View":
    view()
  elif choices == "3" or choices == "Remove":
    remove()
  elif choices == "4" or choices == "Exit":
    exit()
  else:
    print("That is not a valid choice,please try again")
    time.sleep(1)
    os.system('clear')
    continue
  auto_save()
#Find out how to load values from inventory.txt into inventory list to show in view function
