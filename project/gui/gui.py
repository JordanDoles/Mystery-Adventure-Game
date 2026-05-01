import tkinter as tk
from tkinter import messagebox

from project.game.load_data import (
    load_all_cases,
    load_specific_case_id,
    load_random_variation,
    load_random_culprit,
    load_suspects,
    load_locations,
    load_clues,
    load_alibis)

# TODO: find out how to make it so that you can't type in the output box
# TODO: "start" screen with basic game goal description & player ability to choose case
class MysteryGUI:
    """
    Class for Mystery Investigation Game GUI
    """
    # SECTION: INITIALIZATION
    def __init__(self, root):
        """
        initialization function
        :param root: tkinter root window
        :return: None
        """
        self.root = root
        self.root.title("Mystery Investigation Game")
        self.root.geometry("900x600")

        self.show_start_screen()

# TODO: "start" screen with basic game goal description
    # SECTION: START SCREEN
    def show_start_screen(self):
        """
        Displays the opening case selection screen.
        """
        self.start_frame = tk.Frame(self.root, bg="lightgrey")
        self.start_frame.pack(fill="both", expand=True)

        tk.Label(
            self.start_frame,
            text="Welcome to the Mystery Investigation Game.",
            font=("Arial", 18, "bold"),
            bg="lightgrey"
        ).pack(pady=20)

        tk.Label(
            self.start_frame,
            text="Choose a case to investigate:",
            font=("Arial", 14),
            bg="lightgrey"
        ).pack(pady=10)

        cases_df = load_all_cases()

        for _, row in cases_df.iterrows():
            case_id = row["case_id"]
            case_name = row["case_name"]

            tk.Button(
                self.start_frame,
                text=case_name,
                width=35,
                command=lambda selected_case_id=case_id: self.start_game(selected_case_id)
            ).pack(pady=5)

    def start_game(self, case_id):
        """
        Loads the selected case, chooses a random variation and culprit,
        then starts the main game GUI.
        :param case_id:
        """
        self.case_id = case_id

        self.current_case = load_specific_case_id(self.case_id)

        self.current_variation = load_random_variation(self.case_id)
        self.variation_id = self.current_variation.get_variation_id()

        self.current_culprit = load_random_culprit(self.case_id, self.variation_id)
        self.culprit_id = self.current_culprit.get_culprit_id()

        self.suspects = load_suspects(self.case_id)
        self.locations = load_locations(self.case_id)
        self.clues = load_clues(self.case_id, self.variation_id, self.culprit_id)
        self.alibis = load_alibis(self.case_id, self.variation_id, self.culprit_id)

        self.found_clues = []
        self.room_shapes = {}

        self.culprit_name = next(
            suspect.get_name()
            for suspect in self.suspects
            if suspect.get_suspect_id() == self.culprit_id
        )

        self.current_room = self.locations[0].get_name() if self.locations else "No Room"

        # Canvas room click tracking
        self.room_shapes = {}

        self.start_frame.destroy()
        self.build_gui()
        self.draw_map()
        self.update_output(
            "Welcome to the Mystery Investigation Game.\n"
            "Click a room on the map to travel there."
        )


    # SECTION: GUI BUILDING
    def build_gui(self):
        """
        Build GUI function
        :return: none
        """
        # Main container
        self.main_frame = tk.Frame(self.root, bg="lightgrey")
        self.main_frame.pack(fill="both", expand=True)

        # Title
        self.title_label = tk.Label(
            self.main_frame,
            text="Mystery Investigation Game",
            font=("Arial", 18, "bold"),
            bg="lightgrey"
        )
        self.title_label.pack(pady=10)

        # Current room
        self.current_room_label = tk.Label(
            self.main_frame,
            text=f"Current Room: {self.current_room}",
            font=("Arial", 12, "bold"),
            bg="lightgrey"
        )
        self.current_room_label.pack(pady=5)

        # Main content
        self.content_frame = tk.Frame(self.main_frame, bg="lightgrey")
        self.content_frame.pack(fill="both", expand=True)

        # Left panel for controls
        self.left_panel = tk.Frame(self.content_frame, bg="lightgrey")
        self.left_panel.pack(side="left", fill="y", padx=10, pady=10)

        # Right panel for map + output
        self.right_panel = tk.Frame(self.content_frame, bg="lightgrey")
        self.right_panel.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Buttons
        self.view_suspects_button = tk.Button(
            self.left_panel,
            text="View Suspects",
            width=20,
            command=self.show_suspects
        )
        self.view_suspects_button.pack(pady=5)

        self.ask_alibi_button = tk.Button(
            self.left_panel,
            text="Ask for Alibi",
            width=20,
            command=self.ask_suspect_alibi
        )
        self.ask_alibi_button.pack(pady=5)

        self.view_locations_button = tk.Button(
            self.left_panel,
            text="View Locations",
            width=20,
            command=self.show_locations
        )
        self.view_locations_button.pack(pady=5)

        self.search_room_button = tk.Button(
            self.left_panel,
            text="Search Current Room",
            width=20,
            command=self.search_current_room
        )
        self.search_room_button.pack(pady=5)

        self.view_clues_button = tk.Button(
            self.left_panel,
            text="View Found Clues",
            width=20,
            command=self.show_found_clues
        )
        self.view_clues_button.pack(pady=5)

        self.accuse_button = tk.Button(
            self.left_panel,
            text="Make Accusation",
            width=20,
            command=self.make_accusation
        )
        self.accuse_button.pack(pady=5)

        self.quit_button = tk.Button(
            self.left_panel,
            text="Quit",
            width=20,
            command=self.root.quit
        )
        self.quit_button.pack(pady=5)

        self.instructions_label = tk.Label(
            self.left_panel,
            text="Travel:\nClick a room on the map",
            bg="lightgrey",
            justify="left"
        )
        self.instructions_label.pack(pady=20)

        # Map canvas
        self.map_canvas = tk.Canvas(
            self.right_panel,
            bg="white",
            height=300
        )
        self.map_canvas.pack(fill="x", pady=(0, 10))

        # Output area
        self.output_text = tk.Text(
            self.right_panel,
            bg="white",
            wrap="word",
            font=("Arial", 11)
        )
        self.output_text.pack(fill="both", expand=True)

    def update_output(self, text):
        """
        updates the output on the screen
        :param text: text to display
        :return: None
        """
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)

# TODO: draw the rest of the rooms on the map
    def draw_map(self):
        """
        Creates the map
        :return: none
        """
        self.map_canvas.delete("all")
        self.room_shapes.clear()

        # Basic layout for the first few rooms
        room_positions = [
            ("Kitchen", 30, 30, 180, 120),
            ("Living Room", 220, 30, 370, 120),
            ("Bedroom", 410, 30, 560, 120),
            ("Study", 125, 150, 275, 240),
            ("Garden", 315, 150, 465, 240),
        ]

        # Fall back if CSV names differ from these
        location_names = [loc.get_name().strip() for loc in self.locations]

        for i, location_name in enumerate(location_names):
            if i < len(room_positions):
                _, x1, y1, x2, y2 = room_positions[i]
            else:
                # Simple overflow layout
                row = i // 3
                col = i % 3
                x1 = 30 + col * 190
                y1 = 30 + row * 120
                x2 = x1 + 150
                y2 = y1 + 90

            fill_color = "lightblue" if location_name == self.current_room else "lightgray"

            # This draws the box for the room
            rect_id = self.map_canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=fill_color,
                outline="black",
                width=2
            )
            text_id = self.map_canvas.create_text(
                (x1 + x2) / 2,
                (y1 + y2) / 2,
                text=location_name,
                font=("Arial", 12, "bold")
            )

            if self.room_has_unfound_clues(location_name):
                exclamation_id = self.map_canvas.create_text(
                    x2 - 15,
                    y1 + 15,
                    text="!",
                    fill="red",
                    font=("Arial", 18, "bold")
                )
                self.room_shapes[exclamation_id] = location_name

            self.room_shapes[rect_id] = location_name
            self.room_shapes[text_id] = location_name

        self.map_canvas.bind("<Button-1>", self.on_map_click)

    def room_has_unfound_clues(self, room_name):
        """
        Informs user that there are clues to be found in unsearched room
        :param room_name: name of the room
        :return: True or False
        """
        for clue in self.clues:
            if clue.get_location().strip().lower() == room_name.strip().lower() and clue not in self.found_clues:
                return True
        return False

    def on_map_click(self, event):
        """
        Allows used to selecting items on map and directs them to search the current room
        :param event: enters room of closest click on GUI
        :return: none
        """
        clicked_item = self.map_canvas.find_closest(event.x, event.y)
        if not clicked_item:
            return

        item_id = clicked_item[0]
        if item_id in self.room_shapes:
            self.current_room = self.room_shapes[item_id]
            self.current_room_label.config(text=f"Current Room: {self.current_room}")
            self.draw_map()
            self.update_output(f"You travel to the {self.current_room}, select 'Search Current Room' to look for clues.")

# TODO: suspects can only be interacted with in certain rooms
    def show_suspects(self):
        """
        Displays the suspects on the screen
        :return: none
        """
        lines = ["Suspects:\n"]
        for i, suspect in enumerate(self.suspects, 1):
            lines.append(f"{i}. {suspect.get_name()} - {suspect.get_role()}")
        self.update_output("\n".join(lines))

    def show_locations(self):
        """
        Displays the locations on the screen
        :return: none
        """
        lines = ["Locations:\n"]
        for i, location in enumerate(self.locations, 1):
            lines.append(f"{i}. {location.get_name()}: {location.get_description()}")
        self.update_output("\n".join(lines))

# TODO: (maybe) functionality for the player to find each clue in a room individually
    def search_current_room(self):
        """
        Out puts Searches to the current room 
        :return: none
        """
        lines = [f"You are searching {self.current_room}...\n"]
        found_any = False

        for clue in self.clues:
            if clue.get_location().strip().lower() == self.current_room.strip().lower():
                found_any = True
                if clue not in self.found_clues:
                    self.found_clues.append(clue)
                    lines.append(
                        f"Found clue: {clue.get_name()}\n"
                        f"Description: {clue.get_description()}\n"
                    )
                else:
                    lines.append(f"You already found: {clue.get_name()}\n")

        if not found_any:
            lines.append("No clues found here.")

        self.update_output("\n".join(lines))
        self.draw_map()

    def show_found_clues(self):
        """
        Displays the found clues on the screen
        :return: none
        """
        if not self.found_clues:
            self.update_output("Found Clues:\n\nYou have not found any clues yet.")
            return

        lines = ["Found Clues:\n"]
        for i, clue in enumerate(self.found_clues, 1):
            lines.append(f"{i}. {clue.get_name()} - {clue.get_description()}")
        self.update_output("\n".join(lines))

# TODO: tracking for unique responses for asking suspect for an alibi again (this may just be put in when you accuse a suspect)
# TODO: unique responses if certain pieces of evidence are found before talking to suspect
    def ask_suspect_alibi(self):
        """
        Prompts user to ask suspect for their alibi
        :return: none
        """
        window = tk.Toplevel(self.root)
        window.title("Ask for Alibi")
        window.geometry("300x300")

        tk.Label(window, text="Choose a suspect:", font=("Arial", 12, "bold")).pack(pady=10)

        suspect_listbox = tk.Listbox(window)
        suspect_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        for suspect in self.suspects:
            suspect_listbox.insert(tk.END, suspect.get_name())

        def submit():
            """
            Displays suspects alibi to the screen if it is selected
            :return: none
            """
            selection = suspect_listbox.curselection()
            if not selection:
                messagebox.showwarning("No Selection", "Please choose a suspect.")
                return

            suspect = self.suspects[selection[0]]
            self.update_output(
                f"{suspect.get_name()}'s alibi:\n\n{suspect.get_alibi()}"
            )
            window.destroy()

        tk.Button(window, text="Show Alibi", command=submit).pack(pady=10)

    def make_accusation(self):
        """
        Creates window that displays the option for user to make an accusation
        :return: none
        """
        window = tk.Toplevel(self.root)
        window.title("Make an Accusation")
        window.geometry("300x350")

        tk.Label(
            window,
            text="Choose a suspect to accuse:",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        suspect_listbox = tk.Listbox(window, height=10)
        suspect_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        for suspect in self.suspects:
            suspect_listbox.insert(tk.END, suspect.get_name())

        def submit():
            """
            Displays suspects accuse to the screen if it is selected
            :return: none
            """
            selection = suspect_listbox.curselection()
            if not selection:
                messagebox.showwarning("No Selection", "Please choose a suspect.")
                return

            accused_suspect = self.suspects[selection[0]]

            if accused_suspect.get_name() == self.culprit_name:
                messagebox.showinfo(
                    "Result",
                    f"You solved the mystery.\n{self.culprit_name} is the culprit."
                )
            else:
                messagebox.showinfo(
                    "Result",
                    f"That accusation is incorrect.\n"
                    f"{accused_suspect.get_name()} is not the culprit.\n"
                )

            window.destroy()

        tk.Button(
            window,
            text="Submit Accusation",
            command=submit
        ).pack(pady=10)

        # Optional: allow double-click on a suspect to accuse immediately
        suspect_listbox.bind("<Double-Button-1>", lambda event: submit())
