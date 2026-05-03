class CaseVariation:
    """
    Case Variation Class
    """
    def __init__(self, variation_id, case_id, correct_choice):
        """
        Initializes Case Variation object
        :param variation_id: ID of variation
        :type variation_id: str
        :param case_id: ID of case
        :type case_id: str
        :param correct_choice: ID of correct choice
        :type correct_choice: str
        """
        self.__variation_id = variation_id
        self.__case_id = case_id
        self.__correct_choice = correct_choice

    def get_variation_id(self):
        """
        Get variation ID
        :return: variation ID
        """
        return self.__variation_id

    def get_case_id(self):
        """
        Get case ID
        :return: case ID
        """
        return self.__case_id

    def get_correct_choice(self):
        """
        Get correct choice
        :return: correct choice
        """
        return self.__correct_choice
