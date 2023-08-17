# Hangman ASCII art source: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

hang_stages = [
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

hangmantitle = """ 
 _                                             
| |                                                +---+    
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __      |   |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \     O   |
| | | | (_| | | | | (_| | | | | | | (_| | | | |   /|\  |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|   / \  |
                    __/ |                              |
                   |___/                         ========="""       