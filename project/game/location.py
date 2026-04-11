class Location:
    """
    This class represents a location
    """
    def __init__(self, name, description):
        """
        constructor for Location class
        :param name: name of the location
        :param description: description of the location
        :return: none
        """
        self.name = name
        self.description = description

    def get_name(self):
        """
        gets the name of the location
        :return: name of the location
        """
        return self.name

    def get_description(self):
        """
        gets the description of the location
        :return: description of the location
        """
        return self.description

    def __str__(self):
        """
        string representation of the location
        :return: string representation of the location
        """
        return f"{self.name} - {self.description}"
