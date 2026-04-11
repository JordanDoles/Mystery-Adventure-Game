class Suspect:
    """
    Suspect class
    """
    def __init__(self, name, role, alibi):
        """
        Constructor
        :param name: name of the suspect
        :param role: role of the suspect
        :param alibi: alibi of the suspect
        :return: none
        """
        self.name = name
        self.role = role
        self.alibi = alibi

    def get_name(self):
        """
        get name of the suspect
        :return: name of the suspect
        """
        return self.name

    def get_role(self):
        """
        get role of the suspect
        :return: role of the suspect
        """
        return self.role

    def get_alibi(self):
        """
        get alibi of the suspect
        :return: alibi of the suspect
        """
        return self.alibi

    def __str__(self):
        """
        string representation of the suspect
        :return: string representation of the suspect
        """
        return f"{self.name} - Role: {self.role}"
