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