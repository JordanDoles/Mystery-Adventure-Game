class Suspect:
    def __init__(self, suspect_id, name, role, description):
        self.__suspect_id = suspect_id
        self.__name = name
        self.__role = role
        self.__description = description

    # Getters
    def get_suspect_id(self):
        return self.__suspect_id

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def get_description(self):
        return self.__description
