import os
from win32com.client import Dispatch
from environment import CHROME_PATH, CHROME_NAME

class ChromeFixer:
   def __init__(self) -> None:
      self.desktop_path = f'{os.environ["USERPROFILE"]}\\Desktop'
      self.chrome_path = CHROME_PATH
      self.chrome_name = CHROME_NAME


   def __has_file(self, file_name: str, root_path: str) -> bool:
      if file_name in os.listdir(root_path):
         return True

      return False


   def __create_shortcut(self, path_from: str, path_to: str):
      shell = Dispatch('WScript.Shell')

      shortcut = shell.CreateShortCut(path_to)
      shortcut.Targetpath = path_from
      shortcut.save()


   def execute(self):
      has_chrome = self.__has_file('chrome.exe', self.chrome_path)

      if has_chrome:
         # Olds
         os.remove(f'{self.chrome_path}\\{self.chrome_name}')

         os.rename(
            f'{self.chrome_path}\\chrome.exe',
            f'{self.chrome_path}\\{self.chrome_name}'
         )

         # Shortcuts
         os.remove(f'{self.desktop_path}\\Chrome.lnk')

         self.__create_shortcut(
            path_from = f'{self.chrome_path}\\{self.chrome_name}',
            path_to = f'{self.desktop_path}.lnk'
         )

# Execute Fix
if __name__ == '__main__':
   ChromeFixer().execute()
