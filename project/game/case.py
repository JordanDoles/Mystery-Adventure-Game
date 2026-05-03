class Case:
    """
    Case Class
    """
    def __init__(self, case_id, case_name, case_opening, what_choice_1, what_choice_2, what_choice_3):
        """
        Provides case for given case_id and case_name - case object initialization
        :param case_id: case id
        :type case_id: str
        :param case_name: case name
        :type case_name: str
        :param case_opening: case opening
        :type case_opening: str
        :param what_choice_1: choice possible
        :type what_choice_1: str
        :param what_choice_2: 2nd choice possible
        :type what_choice_2: str
        :param what_choice_3: 3rd choice possible
        :type what_choice_3: str
        :return: None
        """
        self.__case_id = case_id
        self.__case_name = case_name
        self.__case_opening = case_opening
        self.__what_choice_1 = what_choice_1
        self.__what_choice_2 = what_choice_2
        self.__what_choice_3 = what_choice_3

    def get_case_id(self):
        """
        Gets case id
        :return: case id
        """
        return self.__case_id

    def get_name(self):
        """
        Gets case name
        :return: case name
        """
        return self.__case_name

    def get_opening(self):
        """
        Gets case opening
        :return: case opening
        """
        return self.__case_opening

    def get_what_choice_1(self):
        """
        Gets choice possible
        :return: choice 1
        """
        return self.__what_choice_1

    def get_what_choice_2(self):
        """
        Gets 2nd choice possible
        :return: choice 2
        """
        return self.__what_choice_2

    def get_what_choice_3(self):
        """
        Gets 3rd choice possible
        :return: choice 3
        """
        return self.__what_choice_3

