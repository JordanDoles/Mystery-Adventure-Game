class Clue:
    """
    Clue Class
    """
    def __init__(self, clue_id, item_name, item_description, item_location, case_id, variation_id, culprit_id):
        """
        Initialize the Clue object. Each are tied to specific case, variation, and culprit
        :param clue_id: ID of the clue
        :type clue_id: int
        :param item_name: name of the item
        :type item_name: str
        :param item_description: description of the item
        :type item_description: str
        :param item_location: location of the item
        :type item_location: str
        :param case_id: case id
        :type case_id: int
        :param variation_id: ID of the variation
        :type variation_id: int
        :param culprit_id: culprit id
        :type culprit_id: int
        """
        self.__clue_id = clue_id
        self.__item_name = item_name
        self.__item_description = item_description
        self.__item_location = item_location
        self.__case_id = case_id
        self.__variation_id = variation_id
        self.__culprit_id = culprit_id

    def get_clue_id(self):
        """
        Get the ID of the clue
        :return: clue id
        """
        return self.__clue_id

    def get_item_name(self):
        """
        Get the name of the item
        :return: item name
        """
        return self.__item_name

    def get_item_description(self):
        """
        Get the description of the item
        :return: item description
        """
        return self.__item_description

    def get_item_location(self):
        """
        Get the location of the item
        :return: item location
        """
        return self.__item_location

    def get_case_id(self):
        """
        Get the ID of the case
        :return: case id
        """
        return self.__case_id

    def get_variation_id(self):
        """
        Get the ID of the variation
        :return: variation id
        """
        return self.__variation_id

    def get_culprit_id(self):
        """
        Get the ID of the culprit
        :return: culprit id
        """
        return self.__culprit_id
