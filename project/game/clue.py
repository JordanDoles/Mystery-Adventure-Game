class Clue:
    def __init__(self, name, location, description, clue_type):
        self.name = name
        self.location = location
        self.description = description
        self.clue_type = clue_type

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_description(self):
        return self.description

    def get_clue_type(self):
        return self.clue_type

    def __str__(self):
        return f" {self.name} found in the {self.location}"
