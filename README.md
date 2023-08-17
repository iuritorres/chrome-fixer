# Chrome Fixer

## Problem

This program is a simple script designed to identify and address a Google Chrome bug.

This bug occurs for an unknown reason, but essentially, the chrome.exe executor fails to open Google Chrome correctly until it is renamed. Furthermore, each small update to Chrome creates a new chrome.exe in the root Chrome folder, which disrupts the functionality of the chrome.lnk shortcut on the desktop.

To resolve this issue, the script is integrated with the Windows Task Scheduler, triggered at every login. It checks for the creation of a new chrome.exe file in the root folder. If such a file exists, the script deletes the corrupted files (the .exe file in the root folder and the .lnk file on the desktop), and then implements the necessary modifications to restore proper functionality.

## Solution

This project only have 2 main files:

-  ChromeFixer.py
-  environment.py

### enviroment.py

In the Environment file we store the constants that will be consumed in the fixer, it stores `CHROME_PATH` and `CHROME_NAME`, the chrome name is just a new different name of the default, just to fix the bug, but the `CHROME_PATH` stores litteraly the chrome path in the computer that it is being executed.

### ChromeFixer.py

This file have a simple class `ChromeFixer` that will store some helpful methods to resolve it.

The class is not really necessary here, but knowing that we have some environment and instance based stuffs here, i guess work with classes make a little bit easier.

Essenciatly, we have 3 properties and 3 methods.

#### Properties:

-  `self.desktop_path`
-  `self.chrome_path`
-  `self.chrome_name`

The `desktop_path` will not need external intervention, it gets its own value by a especific method of the os' pyhton vanilla library.

The `chrome_path` and `chrome_name` will be determined in the `environment.py` file.

#### Methods:

-  `__has_file()`
-  `__create_shortcut()`
-  `execute()`

Note: `__has_file()` and `__create_shortcut()` methods is just helpfull functions to be used in `execute()`.

`__has_file()` uses `os.listdir()` to get the names of files in some folder based on `file_name`(str), `root_path`(str) parameters.

`__create_shortcut()` uses a shell instance created with `win32com.client`'s pyhton library to create a shortcut using `path_from`(str) and `path_to`(str) parameters.

The `execute()` method just use `__has_file()` to verify the has some new chrome.exe in the root folder, and if exists, use `os.rename` and `os.remove` to make the necessary changes and then use `__create_shortcut()` method to update the .lnk in desktop.
