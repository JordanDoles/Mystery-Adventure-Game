# Starts the game

import tkinter as tk
from gui.gui import MysteryGUI

def main():
    root = tk.Tk()
    app = MysteryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
