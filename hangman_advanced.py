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


def main():
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
  # überprüft ob das Wort noch nicht erraten ist
  while userGuess.replace(" ", "") != secretWord:
    print(HANGMANPICS[0] + "\n")
    print(userGuess)
    # fragt nach Buchstabe
    guess = input("Guess a letter:\n")
    guess = guess.upper()
    # überprüft ob der guess den richtigen Datentyp hat und nicht ein bereits geratener Buchstabe ist
    while guess in alreadyGuessed:
      print("You already tried this letter or your input is invalid")
      guess = input("Guess a letter:\n")
      guess = guess.upper()
    alreadyGuessed.append(guess)
    # überprüft ob guess richtig ist
    if guess in secretWord:
      # fügt guess dem userGuess guess hinzu und zeigt dann die Überschrift
      positionGuess = secretWord.index(guess)
      userGuess = list(userGuess)
      userGuess = userGuess.insert(positionGuess*2, guess)
      userGuess = "".join(userGuess)
      print(HANGMANPICS[life] + "\n")
      print(userGuess + "\n")
      print("Already guessed letters:\n" + " ".join(alreadyGuessed))
    else: 
      # printed das entsprechende Menü + überprüft ob noch Versuche vorhanden sind
      life = life + 1
      print(HANGMANPICS[life])
      print("Already guessed letters:\n" + " ".join(alreadyGuessed))
      if life == 6:
        print("YOU LOST!")
        break
  # winscreen
  print("YOU WON!")

    


main()