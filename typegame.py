from getkey import getkey, keys
import time
import re
import sys

from colors import *

def clear():
  print("\033c",end="")

start_screen = f'''{Blue}
▒█▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀█ █▀▀▄ 　 ▀▀█▀▀ █░░█ █▀▀█ █▀▀ 
▒█▄▄█ █▄▄█ ░░█░░ █▀▀█ █░░█ █░░█ 　 ░▒█░░ █▄▄█ █░░█ █▀▀ 
▒█░░░ ▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀▀ ▀░░▀ 　 ░▒█░░ ▄▄▄█ █▀▀▀ ▀▀▀{reset}'''

level_screen = f'''{bright_magenta}               ▒█░░░ █▀▀ ▀█░█▀ █▀▀ █░░ █▀▀ ▄ 
               ▒█░░░ █▀▀ ░█▄█░ █▀▀ █░░ ▀▀█ ░ 
               ▒█▄▄█ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀▀▀ ▀{bright_green}

        Beginner:         {Blue}Intermediate:         {bright_blue}Settings{reset}
     1: Hello World!      7: For Loops         c: {bright_cyan}Cursor{reset}
    2: Adding            8: More Loops
     3: Variables       9: Even More Loops
      4: Lists           10: Comprehension
     5: Tuples            11: List Methods
    6: Dictionaries        12: Coolness
'''

levels = {
  1:'''print("Hello World!")''',
  2:'''print(1+1)''',
  3:'''age = 12

print(age)''',
  4:'''languages = ["Python", "Java", "C"]

print(languages)''',
  5:'''location = (3,5)

print(location)''',
  6:'''groceries = {"apples":3, "milk":2, "bread":3, "eggs":2}

print(groceries)''',
  7:'''for i in range(3):
\tprint(i)''',
  8:'''cities = ["New York", "Paris", "Shanghai", "Tokyo"]

for i in cities:
\tprint(i)''',
  9:'''letters = "abcde"

for i in list(letters):
\tprint(i)''',
  10:'''odd_numbers = [i for i in range(10) if i % 2 != 0]

print(odd_numbers)''',
  11:'''countries = ["United States", "Japan", "China"]

countries.remove("China")

countries.append("New Zealand")

print(countries)''',
  12:'''numbers = list(map(lambda i: i*10, [i for i in range(1,6)]))

print(numbers)''',
  13:'''primes = [x for x in range(2,20) if all(x % y != 0 for y in range(2,x))]

print(primes)'''
}

line_cursor = True

def find_func(string):
  string = string.replace("for ",f"{Blue}for{reset} ")
  
  string = string.replace("in ",f"{Blue}in{reset} ")

  string = string.replace("if ",f"{Blue}if{reset} ")

  string = string.replace("lambda ",f"{Blue}lambda{reset} ")

  string = string.replace("+",f"{bright_blue}+{reset}")

  string = string.replace("-",f"{bright_blue}-{reset}")

  string = string.replace("=",f"{bright_blue}={reset}")
  
  for i in re.findall('\".*?\"',string):
    string = string[:string.find(i)] + bright_yellow + i[0:-1] + string[string.find(i[1:-1]) + len(i[1:-1])] + reset + string[string.find(i[1:-1]) + len(i[1:-1]) + 1:]

  for i in re.findall('\..*?\(',string):
    string = string[:string.find(i)] + bright_blue + i[0:-1] + string[string.find(i[1:-1]) + len(i[1:-1])] + reset + string[string.find(i[1:-1]) + len(i[1:-1]) + 1:]
  
  return string

def level_select():
  global line_cursor
  
  print(start_screen)
  time.sleep(0.7)
  print(f"\n{darken}{italic}Inspired by {reset}{Orange}coder100{reset}{darken}'s {reset}{bright_yellow}Standard Type{reset}{darken}...{reset}")
  time.sleep(0.7)
  input(f"\n{darken}Press {bright_blue}[{Blue}ENTER{bright_blue}]{reset} {darken}To Start{reset} ")
  clear()
  
  while True:
    print(level_screen)
    
    time.sleep(0.2)
    
    selected_level = input(f"{bright_blue}>{Blue} ").strip()
    
    print(reset)

    if selected_level == "c" or selected_level == "C":
      clear()
      
      cursor_screen()
      
      time.sleep(1)
      
      selected_cursor = input(f"\n{bright_blue}Select a {bright_cyan}Cursor{bright_blue}:{Blue} ")

      if selected_cursor == "2" or selected_cursor == "cursor 2" or selected_cursor == "Cursor 2":
        line_cursor = False
      else:
        line_cursor = True

      clear()
    
    else:
      try:
        clear()
        
        stats = start_level(levels[int(selected_level)])
  
        clear()
        
        display_stats(stats)
  
        clear()
      
      except ValueError:
        time.sleep(0.3)
        
        print(f"{darken}Invalid input, try again.")
        
        time.sleep(1.5)
  
        clear()

def start_level(level):
  mistakes = 0
  speeds = []
  count = round(len(level)/20)
  
  type_string = ""
  full_string = ""

  print(f"{darken}Press {bright_blue}[{Blue}ENTER{bright_blue}]{reset} {darken}To Start{reset} ")

  getkey()

  clear()

  start_time = time.time()

  mistake = False
  
  while True:
    wpm = round(len(type_string.replace("("," ").replace(":"," ").split()) / (time.time() - start_time) * 60)

    accuracy = round(100 - ((mistakes / (len(type_string)+1)) * 100), 2)
    if count < 1:
      speeds.append(round(wpm))
      count = round(len(level)/20)
    else:
      count -= 1

    if line_cursor == True:
      full_string = find_func(type_string) + f"{bright_blue}|{reset}" + reset + darken + level[len(type_string):]
    else:
      full_string = find_func(type_string) + darken + underline + level[len(type_string):len(type_string)+1] + reset + darken + level[len(type_string)+1:]
    
    print(f"{wpm} {bright_yellow}WPM{reset} {darken}|{reset} {accuracy}% {bright_cyan}Accuracy{reset}", "\n\n" + full_string, "\n")
    
    key = getkey()
    
    if key == keys.BACKSPACE:
      type_string = type_string[:-1]
    else:
      if key == level[len(type_string)]:
        type_string += key
        mistake = False
      else:
        if mistake == False:
          mistakes += 1
          mistake = True
    
    clear()
    
    if type_string == level:
      full_string = find_func(type_string)

      print(f"{wpm} {bright_yellow}WPM{reset} {darken}|{reset} {accuracy}% {bright_cyan}Accuracy{reset}","\n")
      
      print(full_string)
      
      time_passed = time.time() - start_time

      words = len(type_string.replace("("," ").replace(":"," ").split())

      chars = len(type_string)
      
      print(f"\n{Blue}Program Success!\n\n{reset}")

      time.sleep(1)
      
      lines = type_string.count("\n") + 1

      time.sleep(0.5)

      input(f"\n{darken}Press {bright_blue}[{Blue}ENTER{bright_blue}]{reset} {darken}To View Stats{reset} ")
      
      return lines, mistakes, time_passed, words, chars, speeds

def display_stats(stats):
  lpm = round((stats[0] / stats[2]) * 60)
  
  accuracy = round(100 - ((stats[1] / stats[4]) * 100), 2)

  wpm = round((stats[3] / stats[2]) * 60)

  print(f"{round(stats[2])} {Blue}Seconds{reset} {darken}|{reset} {stats[3]} {Orange}Words{reset}")

  time.sleep(1)
  
  graph(stats[5])

  time.sleep(1)
  
  print(f"\n{stats[1]} {bright_red}Mistakes{reset} {darken}|{reset} {accuracy}% {bright_cyan}Accuracy{reset} {darken}|{reset} {lpm} {bright_blue}Lines of Code/Minute{reset} {darken}|{reset} {wpm} {bright_yellow}WPM{reset}")

  time.sleep(1)

  input(f"\n{darken}Press {bright_blue}[{Blue}ENTER{bright_blue}]{reset} {darken}To Continue{reset} ")

def graph(speeds):
  graph_height = 10
  
  incre = round(max(speeds)/graph_height)
  
  graph = [[i]*len(speeds) for i in ["  "] * round((max(speeds)/incre)+2)]
  
  for idx, val in enumerate(speeds):
  	height = round(val/incre)
  	graph[height][idx] = f" {bright_yellow}⬤{reset}"

  for idx, val in enumerate(graph):
    num = str(idx*incre)
    if len(num) == 2:
      num += " "
    elif len(num) == 1:
      num += "  "
    val[0] = f"{bright_blue}{underline}{num} {reset} "
  
  graph.reverse()

  graph[-1] = graph[-1] + [bright_blue, underline] + list(" " * (len(graph[-1]) * 2 + 5)) + [reset]

  graph[-1] = [i for i in graph[-1] if i != "  "]
  
  for i in graph:
  	print("".join(i))

def cursor_screen():
  print(f'''              {bright_blue}▒█▀▀█ █░░█ █▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀ 
              ▒█░░░ █░░█ █▄▄▀ ▀▀█ █░░█ █▄▄▀ ▀▀█ 
              ▒█▄▄█ ░▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀▀ ▀░▀▀ ▀▀▀{reset}
''')

  time.sleep(1)

  print(f"            {Blue}Cursor {bright_yellow}1{reset}:                    {bright_cyan}Cursor {bright_red}2{reset}:")

  time.sleep(0.85)
  print(f"    {bright_blue}|{reset}{darken}A fox jumps over a dog.{reset}         {darken}{underline}A{reset}{darken} fox jumps over a dog.{reset}")
  time.sleep(1)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A{bright_blue}|{reset}{darken} fox jumps over a dog.{reset}         A{darken}{underline} {reset}{darken}fox jumps over a dog.{reset}")
  time.sleep(0.31)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A {bright_blue}|{reset}{darken}fox jumps over a dog.{reset}         A {darken}{underline}f{reset}{darken}ox jumps over a dog.{reset}")
  time.sleep(0.39)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A f{bright_blue}|{reset}{darken}ox jumps over a dog.{reset}         A f{darken}{underline}o{reset}{darken}x jumps over a dog.{reset}")
  time.sleep(0.32)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A fo{bright_blue}|{reset}{darken}x jumps over a dog.{reset}         A fo{darken}{underline}x{reset}{darken} jumps over a dog.{reset}")
  time.sleep(0.29)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A fox{bright_blue}|{reset}{darken} jumps over a dog.{reset}         A fox{darken}{underline} {reset}{darken}jumps over a dog.{reset}")
  time.sleep(0.33)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A fox {bright_blue}|{reset}{darken}jumps over a dog.{reset}         A fox {darken}{underline}j{reset}{darken}umps over a dog.{reset}")
  time.sleep(0.28)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A fox j{bright_blue}|{reset}{darken}umps over a dog.{reset}         A fox j{darken}{underline}u{reset}{darken}mps over a dog.{reset}")
  time.sleep(0.35)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A fox ju{bright_blue}|{reset}{darken}mps over a dog.{reset}         A fox ju{darken}{underline}m{reset}{darken}ps over a dog.{reset}")
  time.sleep(0.30)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A fox jum{bright_blue}|{reset}{darken}ps over a dog.{reset}         A fox jum{darken}{underline}p{reset}{darken}s over a dog.{reset}")
  time.sleep(0.36)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A fox jump{bright_blue}|{reset}{darken}s over a dog.{reset}         A fox jump{darken}{underline}s{reset}{darken} over a dog.{reset}")
  time.sleep(0.30)
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  print(f"    A fox jumps{bright_blue}|{reset}{darken} over a dog.{reset}         A fox jumps{darken}{underline} {reset}{darken}over a dog.{reset}")
  time.sleep(0.5)


level_select()
