class Culprit:
    """
    Culprit Class
    """
    def __init__(self, culprit_id, case_id, variation_id):
        """
        Initialize Culprit object connected to case id and variation id
        :param culprit_id:
        :param case_id:
        :param variation_id:
        """
        self.__culprit_id = culprit_id
        self.__case_id = case_id
        self.__variation_id = variation_id

    def get_culprit_id(self):
        """
        Get culprit id 
        :return: culprit id
        """
        return self.__culprit_id

    def get_case_id(self):
        """
        Get case id 
        :return: case id
        """
        return self.__case_id

    def get_variation_id(self):
        """
        Get variation id 
        :return: variation id
        """
        return self.__variation_id
