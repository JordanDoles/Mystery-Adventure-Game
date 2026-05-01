class Alibi:
    def __init__(self, suspect_id, text, case_id, variation_id, culprit_id):
        self.__suspect_id = suspect_id
        self.__text = text
        self.__case_id = case_id
        self.__variation_id = variation_id
        self.__culprit_id = culprit_id

    def get_suspect_id(self):
        return self.__suspect_id

    def get_text(self):
        return self.__text

    def get_case_id(self):
        return self.__case_id

    def get_variation_id(self):
        return self.__variation_id

    def get_culprit_id(self):
        return self.__culprit_id
