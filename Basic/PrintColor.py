# Colorize output: https://www.devdungeon.com/content/colorize-terminal-output-python
# Restart kernel in Python Interactive window if it does not colorize output in Python Interactive and Terminal
# Color printing is not working in Anaconda PowerShell prompt

import colorama
from colorama import Fore, Back, Style
# If using Windows, init() will cause anything sent to stdout or stderr
# will have ANSI color codes converted to the Windows versions. Hooray!
# If you are already using an ANSI compliant shell, it won't do anything
# colorama.init()
# colorama.init(autoreset=True)

# Set the color semi-permanently
print(Fore.CYAN)
print("Text will continue to be cyan")
print("until it is reset or changed")
print(Style.RESET_ALL)

# Colorize a single line and then reset
print(Fore.RED + 'You can colorize a single line.' + Style.RESET_ALL)

# Colorize a single word in the output
print('Or a single ' + Back.GREEN + 'words' + Style.RESET_ALL + ' can be highlighted')

# Combine foreground and background color
print(Fore.BLUE + Back.WHITE)
print('Foreground, background, and styles can be combined')
print("==========            ")

print(Style.RESET_ALL)
print('If unsure, reset everything back to normal.')