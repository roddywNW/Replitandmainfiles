
#os.rename("myname.txt", "NEW.o")
#os.mkdir("Hello") # Creates a folder called 'Hello'
#print(os.listdir())

#Idea of how to do challenge:make file,use random function for random name then input,use os to make the file,then save the data to the file then auto save by input backup to main probably

# | Name | Date | Priority
import os, time,random
todo = []

lengthfilename=random.randint(2,12)
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

letterschoices=""
for i in range(lengthfilename):
  letterschoices+=random.choice(alphabet)

letterschoices+=".txt"



# Only create backup folder if it doesn't exist
if not os.path.exists("Backup folder"):
    os.mkdir("Backup folder")

# Check if backup file exists before trying to read it
backup_file_path = "Backup folder/" + letterschoices
#The / after backup folder tells the system to put the file into that folder

if os.path.exists(backup_file_path):
    f = open(backup_file_path, "r")
    backup = eval(f.read())
    f.close()
else:
    # Create empty backup file if it doesn't exist
    f = open(backup_file_path, "w")
    f.write("[]")  # Empty list
    f.close()
    backup = []



def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")
  #Adds to the list
  time.sleep(1.5)
  os.system("clear")
  
def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
    print()
  time.sleep(1.5)
  doneview = input("If you're done viewing,press v")
  if doneview.lower().strip() == "v":
    os.system("clear")
  else:
    print("Ok, just so you know, you can stop viewing by pressing 'v' when prompted.")
    time.sleep(1)
    input=("")
    time.sleep(1)
    os.system("clear")
  #Allows you to view the list

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")
  time.sleep(1)
  os.system("clear")
  #Allows you to edit the list

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)
  print("Removed")
  time.sleep(1.5)
  os.system("clear")
  #Allows you to remove from the list

def save_todo():
  global todo
  global letterschoices
  
  # Save to the backup file
  backup_file_path = "Backup folder/" + letterschoices
  with open(backup_file_path, "w") as f:
    f.write(str(todo))

  # Save to todo.txt
  f = open("todo.txt", "w")
  for row in todo:
    for item in row:
      f.write(str(item) + ",")
    f.write("\n")
  f.close()
  print("Saved")
  time.sleep(1.5)
  os.system("clear")
  #Allows you to auto save the list


def load_todo():
  f = open("todo.txt", "r")
  for line in f:
    row = line.split("|")
    row.pop()
    todo.append(row)
    #Allows you to load the list but not automatically,it's optional
  print("Loaded")
  time.sleep(1.5)
  os.system("clear")

def mass_delete():
  view()
  DeleteAll = input("Are you sure you want to delete all of these?")
  time.sleep(3)
  if DeleteAll.lower()== "y" or "yes":
    todo.clear()
    print("All todos have been deleted.")
    time.sleep(1.5)
    os.system("clear")
  else:
    print("Ok, nothing has been deleted.")
    time.sleep(1.5)
    os.system("clear")

  #Allows you to delete every key in the list

 # Consolidate all backup data into inventory.txt
inventory_data = []


def consolidate_and_cleanup_backups():
  global inventory_data
  if os.path.exists("Backup folder"):
    for filename in os.listdir("Backup folder"):
      if filename.endswith(".txt"):
        backup_file_path = "Backup folder/" + filename
        try:
          with open(backup_file_path, "r") as f:
            backup_content = eval(f.read())
            # Only add if backup_content is not empty
            if backup_content:  # This skips empty lists []
              inventory_data.extend(backup_content)
        except:
          print(f"Error reading {filename}")
  
  # Filter out empty lists before saving
  filtered_data = [item for item in inventory_data if item]  # Removes empty lists []
  
  # Save consolidated data to inventory.txt
  with open("inventory.txt", "w") as f:
    f.write(str(filtered_data))
  
  # Delete all backup files
  if os.path.exists("Backup folder"):
    for filename in os.listdir("Backup folder"):
      file_path = "Backup folder/" + filename
      if os.path.isfile(file_path):
        os.remove(file_path)
    
    # Remove the backup folder itself
    os.rmdir("Backup folder")
  
  print("All backup data consolidated to inventory.txt and backup files deleted.")
  time.sleep(2)
load_Y_N = input("Load previous todo list? (y/n) > ").lower().strip()


if load_Y_N == "y":
  # First check if inventory.txt exists (from previous session)
  if os.path.exists("inventory.txt"):
    try:
      with open("inventory.txt", "r") as f:
        todo = eval(f.read())
      print("Loaded data from inventory.txt")
      time.sleep(1)
    except:
      print("Error loading inventory.txt, trying todo.txt instead")
      load_todo()
  else:
    try:
      load_todo()
    except:
      print("Error loading todo.txt,no data found.")
  #Loads the previous todo list
      time.sleep(1.5)
else:
  print("Ok, just so you know, you can load the previous todo list by typing 'y' when prompted.")
  time.sleep(1.5)
  os.system("clear")
  #Allows to load later



while True:
  save_todo()
  load_todo()
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> 5: Mass delete\n> 6: Quit\n>")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  elif menu == "y":
    load_todo()
  elif menu == "5":
    mass_delete()
  elif menu == "6":
    consolidate_and_cleanup_backups()
    exit()
    #Exits the program
  elif menu == "4":
    remove()
  else:
    #Has it run again
    print("Command not recognized.Please try again.")
    time.sleep(1.5)
    os.system("clear")
    continue
