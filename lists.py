import time,os
#Note: This is a work in progress, and is not finished.Also, when you try to put a space sometimes in the name, it will not work.Quite odd...
exitYN = ""


toDoList = []
RemoveEdit = ""
list_number = 0
choice = ""
name = input("What will be this list's name? ")
#name = name.replace(" ", " ")  
print(f"When you edit to change,the first thing in the {name} is classified as 0 by the computer.")
time.sleep(5.5)
os.system("clear")

def printList():
  print()
  for item in toDoList:
    print(item)
    print("\n")

while True:
  choice = input(f"Do you want to view, add or edit your {name}?\n")
  if choice == "view" or choice == "View":
    printList()
  elif choice == "add" or choice == "Add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif choice == "edit" or choice == "Edit":
    RemoveEdit = input("Do you want to remove or change your to do list?\n")
    if RemoveEdit == "Remove" or RemoveEdit == "remove":
      item = input("What do you want to remove?\n")
      if item in toDoList:
        toDoList.remove(item)
      else:
        print(f"{item} was not in the list\n")
    elif RemoveEdit == "Change" or RemoveEdit == "change":
      printList()
      list_number = int(input("What number in your to do list do you want to change?"))
      item = toDoList[list_number]
      if toDoList[list_number] != item:
          print("That is not in your list.\n")
      else:
        toDoList[list_number] = input("What do you want to change it to?")
        
  else:
    exitYN = input("Do you want to exit?")
    if exitYN == "Yes" or exitYN == "yes":
      print("Okay,goodbye!👋")
      break
    else:
      print("Please pick one of the options")
  time.sleep(3)
  os.system("clear")
time.sleep(3)
os.system("clear")
exit()
