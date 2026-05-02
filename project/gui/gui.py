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

        self.cases_df = load_all_cases()
        case_names = self.cases_df["case_name"].tolist()

        self.selected_case_name = tk.StringVar()
        self.selected_case_name.set(case_names[0])

        case_dropdown = tk.OptionMenu(
            self.start_frame,
            self.selected_case_name,
            *case_names,
            command=self.update_case_preview
        )
        case_dropdown.config(width=35)
        case_dropdown.pack(pady=5)

        self.case_preview_text = tk.Text(
            self.start_frame,
            width=70,
            height=8,
            wrap="word",
            font=("Arial", 11)
        )
        self.case_preview_text.pack(pady=15)

        self.update_case_preview(case_names[0])

        tk.Button(
            self.start_frame,
            text="Confirm Case",
            width=20,
            command=self.confirm_case_selection
        ).pack(pady=10)

    def update_case_preview(self, selected_case_name):
        """
        Updates the preview box when the player selects a case.
        :param selected_case_name:
        """
        selected_row = self.cases_df[
            self.cases_df["case_name"] == selected_case_name
        ].iloc[0]

        self.case_preview_text.delete("1.0", tk.END)
        self.case_preview_text.insert(tk.END, selected_row["case_opening"])

    def confirm_case_selection(self):
        """
        Starts the game after the player confirms their selected case.
        """
        selected_case_name = self.selected_case_name.get()

        selected_row = self.cases_df[
            self.cases_df["case_name"] == selected_case_name
        ].iloc[0]

        selected_case_id = selected_row["case_id"]

        self.start_game(selected_case_id)

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
        self.found_alibis = {}
        self.room_shapes = {}

        self.culprit_name = next(
            suspect.get_name()
            for suspect in self.suspects
            if suspect.get_suspect_id() == self.culprit_id
        )

        self.current_room = next(
            (location.get_name() for location in self.locations
             if location.get_name().strip().lower() == "main entry"),
            self.locations[0].get_name() if self.locations[0] else "No Room"
        )

        self.start_frame.destroy()
        self.build_gui()
        self.draw_map()
        self.update_output(
            f"{self.current_case.get_opening()}\n\n"
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
        self.title_label.pack(pady=5
                              )

        # Current case
        self.current_case_label = tk.Label(
            self.main_frame,
            text=f"Current Case: {self.selected_case_name.get()}",
            font=("Arial", 14, "bold"),
            bg="lightgrey"
        )
        self.current_case_label.pack(pady=2)

        # Current room
        self.current_room_label = tk.Label(
            self.main_frame,
            text=f"Current Room: {self.current_room.title()}",
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
            text="View Case File",
            width=20,
            command=self.show_case_file
        )
        self.view_suspects_button.pack(pady=5)

        self.ask_alibi_button = tk.Button(
            self.left_panel,
            text="Talk To Suspects",
            width=20,
            command=self.ask_suspect_alibi
        )
        self.ask_alibi_button.pack(pady=5)

        self.view_alibis_button = tk.Button(
            self.left_panel,
            text="View Collected Alibis",
            width=20,
            command=self.show_found_alibi
        )
        self.view_alibis_button.pack(pady=5)

        self.search_room_button = tk.Button(
            self.left_panel,
            text="Search Room",
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
        self.quit_button.pack(side="bottom", anchor="sw", padx=10, pady=10)

        self.instructions_label = tk.Label(
            self.left_panel,
            text="Travel:\nClick a room on the map",
            bg="lightgrey",
            justify="left"
        )
        self.instructions_label.pack(pady=20)

        # Map container
        self.map_container = tk.Frame(self.right_panel, bg="lightgrey")
        self.map_container.pack(fill="x", pady=(0, 10))

        # Map canvas
        self.map_canvas = tk.Canvas(
            self.map_container,
            bg="lightgreen",
            width=700,
            height=380
        )
        self.map_canvas.pack(anchor="center")

        # Output area
        self.output_text = tk.Text(
            self.right_panel,
            bg="white",
            wrap="word",
            font=("Arial", 11)
        )
        self.output_text.pack(fill="both", expand=True)
        self.output_text.config(state="disabled")

    def update_output(self, text):
        """
        updates the output on the screen
        :param text: text to display
        """
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state="disabled")

    def draw_map(self):
        """
        Creates the map
        :return: none
        """
        self.map_canvas.delete("all")
        self.room_shapes.clear()

        # Basic layout for the first few rooms
        room_positions = {
            "main entry": (260, 30, 440, 120),
            "study": (60, 30, 240, 120),
            "master bedroom": (460, 30, 640, 120),
            "bedroom": (60, 140, 240, 230),
            "living room": (260, 140, 440, 230),
            "dining room": (260, 250, 440, 340),
            "kitchen": (460, 140, 640, 230),
            "garden": (460, 250, 640, 340),
        }

        # Fall back if CSV names differ from these
        location_names = [loc.get_name().strip() for loc in self.locations]

        for i, location_name in enumerate(location_names):
            key = location_name.strip().lower()

            if key in room_positions:
                x1, y1, x2, y2 = room_positions[key]
            else:
                # Simple overflow layout
                row = i // 3
                col = i % 3
                x1 = 30 + col * 190
                y1 = 30 + row * 120
                x2 = x1 + 180
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
                text=location_name.title(),
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
            clue_location = clue.get_item_location()

            if not isinstance(clue_location, str):
                continue

            if (
                clue_location.strip().lower() == room_name.strip().lower()
                and clue not in self.found_clues
            ):
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
            current_location = next(
                location for location in self.locations
                if location.get_name().strip().lower() == self.current_room.strip().lower()
            )
            self.update_output(
                f"You travel to the {self.current_room.title()}.\n\n"
                f"{current_location.get_description()}\n"
            )

    def show_case_file(self):
        """
        Displays the suspect list and case description.
        :return: none
        """
        lines = [
            "Case Description:\n",
            f"{self.current_case.get_opening()}\n\n",
            "Suspects:\n"
        ]

        for suspect in self.suspects:
            lines.append(
                f"{suspect.get_role()}\n"
                f"{suspect.get_name()}: {suspect.get_description()}\n"
            )
        self.update_output("\n".join(lines))

    def show_locations(self):
        """
        Displays the locations on the screen
        :return: none
        """
        lines = ["Locations:\n"]
        for i, location in enumerate(self.locations, 1):
            lines.append(f"{i}. {location.get_name()}")
        self.update_output("\n".join(lines))

    # SECTION: GAME FUNCTIONS
    def search_current_room(self):
        """
        Out puts Searches to the current room.
        """

        lines = [
            f"You enter the {self.current_room} and search for clues...\n"
        ]
        found_any = False

        for clue in self.clues:
            clue_location = clue.get_item_location()

            if (isinstance(clue_location, str)
                and clue_location.strip().lower() == self.current_room.strip().lower()
            ):
                found_any = True
                if clue not in self.found_clues:
                    self.found_clues.append(clue)
                    lines.append(
                        f"Found clue: \n{clue.get_item_name()}\n"
                        f"{clue.get_item_description()}\n"
                    )
                else:
                    lines.append(f"You already found: {clue.get_item_name()}\n")

        if not found_any:
            lines.append("There are no clues to be found here.")

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
            lines.append(f"{i}. {clue.get_item_name()} - {clue.get_item_description()}")
        self.update_output("\n".join(lines))

# TODO: tracking for unique responses for asking suspect for an alibi again or if certain pieces of evidence are found prior
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

            matching_alibi = next(
                (
                    alibi for alibi in self.alibis
                    if alibi.get_suspect_id() == suspect.get_suspect_id()
                ),
                None
            )

            if matching_alibi:
                alibi_text = matching_alibi.get_text()
            else:
                alibi_text = "This suspect does not have an alibi."

            self.found_alibis[suspect.get_name()] = alibi_text
            self.update_output(f"{suspect.get_name()}'s alibi:\n\n{alibi_text}")

            window.destroy()

        tk.Button(window, text="Show Alibi", command=submit).pack(pady=10)

    def show_found_alibi(self):
        if not self.found_alibis:
            self.update_output("Collected Alibis:\n\nYou have not collected any alibis yet. Go talk to suspects to find out more about this case.")
            return

        lines = ["Collected Alibis:\n"]

        for suspect_name, alibi_text in self.found_alibis.items():
            lines.append(f"{suspect_name}:\n{alibi_text}\n")

        self.update_output("\n".join(lines))

    # SECTION: GAME END
    def make_accusation(self):
        """
        Creates window that displays the option for user to make an accusation about both:
        1. what happened
        2. who did it
        """
        window = tk.Toplevel(self.root)
        window.title("Make an Accusation")
        window.geometry("575x250")

        tk.Label(
            window,
            text="Make your accusation:",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        accusation_frame = tk.Frame(window)
        accusation_frame.pack(pady=10)

        what_choices = [
            self.current_case.get_what_choice_1(),
            self.current_case.get_what_choice_2(),
            self.current_case.get_what_choice_3()
        ]

        selected_happening = tk.StringVar()
        selected_happening.set(what_choices[0])

        selected_suspect = tk.StringVar()
        suspect_names = [suspect.get_name() for suspect in self.suspects]
        selected_suspect.set(suspect_names[0])

        tk.Label(
            accusation_frame,
            text="I've figured it out!"
        ).grid(row=0, column=0, padx=5, pady=10)

        happening_dropdown = tk.OptionMenu(
            accusation_frame,
            selected_happening,
            *what_choices
        )
        happening_dropdown.config(width=50)
        happening_dropdown.grid(row=0, column=1, padx=5, pady=10)

        tk.Label(
            accusation_frame,
            text="And it was"
        ).grid(row=1, column=0, padx=5, pady=5)

        suspect_dropdown = tk.OptionMenu(
            accusation_frame,
            selected_suspect,
            *suspect_names
        )
        suspect_dropdown.config(width=20)
        suspect_dropdown.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(
            accusation_frame,
            text="who did it!"
        ).grid(row=1, column=2, padx=5, pady=5)

        def submit():
            """
            Displays player's accusation results.
            """
            guessed_happening = selected_happening.get().strip()
            guessed_suspect = selected_suspect.get().strip()

            correct_happening = self.current_variation.get_correct_choice().strip()
            correct_suspect = self.culprit_name.strip()

            happening_correct = guessed_happening == correct_happening
            culprit_correct = guessed_suspect == correct_suspect

            if happening_correct and culprit_correct:
                result = (
                    "You solved the mystery!\n\nEverything about your accusation checks out, nice job!"
                )
            elif happening_correct and not culprit_correct:
                result = (
                    f"You're partially right, but {guessed_suspect} doesn't seem to be the culprit.\n\n"
                    "Maybe take another look around for more information?"
                )
            elif culprit_correct and not happening_correct:
                result = (
                    f"{guessed_suspect} definitely didn't pass the vibe check, and you're right about that.\n\n"
                    "But something about what happened doesn't quite add up.\n\n"
                    "Maybe take another look around for more clues?"
                )
            else:
                result = (
                    "That accusation is incorrect.\n\n"
                    "Neither part of your accusation matches the evidence."
                )
            messagebox.showinfo("Result", result)
            window.destroy()

        tk.Button(
            window,
            text="Submit Accusation",
            command=submit
        ).pack(pady=15)