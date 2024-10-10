import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

secretWords = [
    "Byte",
    "Code",
    "Data",
    "Disk",
    "Edit",
    "File",
    "Game",
    "Hack",
    "Icon",
    "Java",
    "Keys",
    "Link",
    "Mail",
    "Menu",
    "Node",
    "Port",
    "Rank",
    "Ruby",
    "Scan",
    "Site",
    "Sort",
    "Tech",
    "Type",
    "Unix",
    "User",
    "View",
    "Wave",
    "Web",
    "Wiki",
    "Zip",
    "Access",
    "Action",
    "Array",
    "Audio",
    "Binary",
    "Border",
    "Buffer",
    "Canvas",
    "Cipher",
    "Client",
    "Clouds",
    "Cluster",
    "Coding",
    "Column",
    "Config",
    "Console",
    "Control",
    "Cookie",
    "Cursor",
    "Daemon",
    "Debug",
    "Decode",
    "Domain",
    "Encode",
    "Engine",
    "Folder",
    "Format",
    "Header",
    "Helper",
    "Kernel"
]

def startscreen():
  print("+--------------------+")
  print("¦ WELCOME TO HANGMAN ¦")
  print("¦                    ¦")
  print("¦        +---+       ¦")
  print("¦        |   |       ¦")
  print("¦        O   |       ¦")
  print("¦       /|\  |       ¦")
  print("¦       / \  |       ¦")
  print("¦            |       ¦")
  print("¦     ==========     ¦")
  print("¦   Press R + Enter  ¦")
  print("+--------------------+")
  ready = input("")
  while ready != "R":
    ready = input("")

def mainOnePlayer():
  # anzahl versuche
  life = 0
  # wählt ein random Wort von der Liste
  secretWord = secretWords[random.randint(0,59)]
  secretWord = secretWord.upper()
  secretWord = list(secretWord)
  # erstellt die userguess Liste
  userGuess = ("_ ") * len(secretWord)
  #Liste mit den bereits falsch geratenen Buchstaben
  alreadyGuessed = []
  print(HANGMANPICS[life] + "\n")
  print(userGuess + "\n")
  # überprüft ob das Wort noch nicht erraten ist
  while "_" in userGuess:
    # fragt nach Buchstabe
    guess = input("Guess a letter:\n")
    guess = guess.upper()
    # überprüft ob der guess den richtigen Datentyp hat und nicht ein bereits geratener Buchstabe ist
    while guess in alreadyGuessed or len(guess) > 1:
      print("\nYou already tried this letter or your input is invalid")
      print("Already guessed letters:\n" + " ".join(alreadyGuessed))
      guess = input("\nGuess a letter:\n")
      guess = guess.upper()
    alreadyGuessed.append(guess)
    # überprüft ob guess richtig ist
    if guess in secretWord:
      # fügt guess dem userGuess guess hinzu und zeigt dann die Überschrift
      for i in range(secretWord.count(guess)):
        positionGuess = secretWord.index(guess)
        userGuess = list(userGuess)
        userGuess[positionGuess*2] = guess
        userGuess = "".join(userGuess)
        secretWord[positionGuess] = "+"
      secretWord = "".join(secretWord)
      secretWord = secretWord.replace("+", guess)
      secretWord = list(secretWord)
      print("Your guess was correct!\n")
      print(HANGMANPICS[life], "\n")
      print(userGuess + "\n")
      if "_" in userGuess:
        print("Already guessed letters:\n" + " ".join(alreadyGuessed))
    elif guess not in secretWord: 
      # printed das entsprechende Menü + überprüft ob noch Versuche vorhanden sind
      life = life + 1
      print("Your guess was incorrect!\n")
      print(HANGMANPICS[life])
      print("\n" + userGuess + "\n")
      print("Already guessed letters:\n" + " ".join(alreadyGuessed) + "\n")
      # wenn keine versuche vorhanden sind Lossscreen
      if life == 6:
        print("The word was: " + "".join(secretWord))
        print("\nYOU LOST!\n")
        break
  # winscreen
  if life < 6:
    print("YOU WON!\n")

def winscreen():
  print("+--------------------+")
  print("¦  YOU GOT IT RIGHT! ¦")
  print("¦      YOU  WON!     ¦")
  print("¦                    ¦")
  print("¦             +---+  ¦")
  print("¦             |   |  ¦")
  print("¦                 |  ¦")
  print("¦      O          |  ¦")
  print("¦     /|\         |  ¦")
  print("¦     / \         |  ¦")
  print("¦ ================== ¦")
  print("¦  WANNA PLAY AGAIN? ¦")
  print("+--------------------+")
  again = input("")
  again = again.lower()
  while again != "yes" and again != "no":
    print("(yes or no)")
    again = input("")
    again = again.lower()
  return again

winscreen()
#startscreen()
#mainOnePlayer()
exit(0)