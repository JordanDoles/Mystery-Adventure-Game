class Alibi:
    def __init__(self, suspect_id, alibi_text, case_id, variation_id, culprit_id):
        """
        Provides alibi for given suspect id, case id and variation id and culprit id
        :param suspect_id: ID of suspect
        :type suspect_id: str
        :param alibi_text: alibi text
        :type alibi_text: str
        :param case_id: ID of case
        :type case_id: str
        :param variation_id: ID of variation
        :type variation_id: str
        :param culprit_id: ID of culprit
        :type culprit_id: str
        :return: None
        """
        self.__suspect_id = suspect_id
        self.__alibi_text = alibi_text
        self.__case_id = case_id
        self.__variation_id = variation_id
        self.__culprit_id = culprit_id

    def get_suspect_id(self):
        """
        Returns suspect ID
        :return: suspect ID
        """
        return self.__suspect_id

    def get_alibi_text(self):
        """
        Returns alibi text
        :return: alibi text
        """
        return self.__alibi_text

    def get_case_id(self):
        """
        Returns case ID
        :return: case ID
        """
        return self.__case_id

    def get_variation_id(self):
        """
        Returns variation ID
        :return: variation ID
        """
        return self.__variation_id

    def get_culprit_id(self):
        """
        Returns culprit ID
        :return: culprit ID
        """
        return self.__culprit_id
