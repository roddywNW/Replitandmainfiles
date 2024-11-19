import random,time,os

list_of_words = ["grapes", "banana", "apple", "orange", "pear","roblox","godot","swift","python","java","c++","c#","html","css","javascript","php","ruby","kotlin","caia","dynasti"]

word = random.choice(list_of_words)

lives = 6
#You found a letter, and you won, and you loss,etc.
#Show how many letters there are in the word with spaces

attempts = 6-lives
#Make it so it copies the last amount of lives and if it doesn't change then it adds a stick.

print("Welcome to hangman,just for you to know,all the words will be lowercase.Therefore,please guess in lowercase :).Also,sometimes the word won't have letters ,but numbers or stuff like that.\n")


def lives_counter():
  if lives <= 0:
    time.sleep(2)
    os.system("clear")
    print("You lost,the word was",word)
    exit()
  else:
    print(f"So far your results look like this:\n {spaces_list}")
    print(f"You guessed these letters :{letter_guessed}.So, in total you guessed {len(letter_guessed)} letters.")
    print("Try again!You currently have ",lives,"lives left.")


spaces = range(len(word))
spaces_list = ["_" for _ in range(len(word))]
#Find out how to show letters and not spaces
letter_guessed = []



while True: 
  guess = input("Guess a letter:\n ")
  guess = guess.strip().lower() 
  time.sleep(1.5)
  os.system("clear")

  if guess in letter_guessed:
    print("You already guessed that.")
    continue
  else:
    letter_guessed.append(guess)
    if guess in word:
      print("You have found a letter!")
      #This still counts from 0 
      for i in range(len(word)):
        if word[i] == guess:
          spaces_list[i] = guess
          spaces = str(spaces_list)
          print(spaces)
          if spaces_list == list(word):
            print("You won!")
            time.sleep(2)
            exit()
          else:
            print("")
            continue
        else:
          continue
    else:
      lives -= 1
      lives_counter()
      continue
