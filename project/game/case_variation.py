class CaseVariation:
    def __init__(self, variation_id, case_id, description):
        self.__variation_id = variation_id
        self.__case_id = case_id
        self.__description = description

    def get_variation_id(self):
        return self.__variation_id

    def get_case_id(self):
        return self.__case_id

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description
