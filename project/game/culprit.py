class Culprit:
    def __init__(self, culprit_id, case_id, variation_id):
        self.__culprit_id = culprit_id
        self.__case_id = case_id
        self.__variation_id = variation_id

    # Getters
    def get_culprit_id(self):
        return self.__culprit_id

    #def get_suspect_id(self):
        #return self.__suspect_id

    def get_case_id(self):
        return self.__case_id

    def get_variation_id(self):
        return self.__variation_id
