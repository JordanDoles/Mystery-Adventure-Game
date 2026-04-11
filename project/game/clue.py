class Clue:
    """
    Class representing clues
    """
    def __init__(self, name, location, description, clue_type):
        """
        Constructor
        :param name: name of the clue
        :param location: name of the location
        :param description: description of the clue
        :param clue_type: type of clue
        :return: None
        """
        self.name = name
        self.location = location
        self.description = description
        self.clue_type = clue_type

    def get_name(self):
        """
        get name of the clue
        :return: name of the clue
        """
        return self.name

    def get_location(self):
        """
        get location of the clue
        :return: name of the location
        """
        return self.location

    def get_description(self):
        """
        get description of the clue
        :return: clue description
        """
        return self.description

    def get_clue_type(self):
        """
        get clue type
        :return: clue type
        """
        return self.clue_type

    def __str__(self):
        """
        string representation of the clue
        :return: string representation of the clue
        """
        return f" {self.name} found in the {self.location}"
