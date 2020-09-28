from cx_Freeze import *

includefiles = ['hangman.ico']
bas = None
if sys.platform == 'win32':
    base = "win32.GUI"

shortcut_table = [
    ("desktopShortcut", #Shortcut
     "desktopfolder", #Directory_
     "Hangman game", #Name
     "TARGETDIR0", #Component_
     "[TARGETDIR]\Hangman.exe", #Target
     None, #Arguments
     None, #Description
     None, #Hotkey
     None, #Icon
     None, #IconIndex
     None, #ShowCmd
     "tARGETDIR", #WKdir
     )
]
msi_data = {"shortcut_table"}

bdist_msi_option = {'data':msi_data}
setup(
     version = "1.0",
     description="Hangman Game developed by Nikita",
     author = "NikitaKumbhare"
     name = "HangMan",
     options = {'build_exe':{'include_files':includefiles},"bdist_msi":bdist_msi_options, },
     executables = [
         Executable(
            script='Hangman.py',
            base=base,
            icon='hangman',
     )
 ]
)
