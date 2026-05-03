class Suspect:
    """
    Suspect class
    """
    def __init__(self, suspect_id, suspect_name, suspect_role, suspect_description):
        """
        Initialize a Suspect object
        :param suspect_id: suspect id
        :type suspect_id: str
        :param suspect_name: name of the suspect
        :type suspect_name: str
        :param suspect_role: role of the suspect
        :type suspect_role: str
        :param suspect_description: description of the suspect
        """
        self.__suspect_id = suspect_id
        self.__suspect_name = suspect_name
        self.__suspect_role = suspect_role
        self.__suspect_description = suspect_description

    # Getters
    def get_suspect_id(self):
        """
        Get the suspect id
        :return: suspect id
        """
        return self.__suspect_id

    def get_name(self):
        """
        Get the suspect name
        :return: name of the suspect
        """
        return self.__suspect_name

    def get_role(self):
        """
        Get the role of the suspect
        :return: role of the suspect
        """
        return self.__suspect_role

    def get_description(self):
        """
        get the description of the suspect
        :return: description of the suspect
        """
        return self.__suspect_description
