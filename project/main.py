# TODO: Entry point of the program

# TODO: initialize game data / engine (from backend)
# TODO: initialize GUI
# TODO: connect GUI to game logic
# TODO: start main loop (GUI loop)

# Later:
# - call functions to get_suspects(), get_locations(), get_objects()
# - pass that data into GUI to display

import tkinter as tk
from gui.gui import MysteryGUI

def main():
    root = tk.Tk()
    app = MysteryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()