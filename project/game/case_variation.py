class CaseVariation:
    def __init__(self, variation_id, case_id, correct_choice):
        self.__variation_id = variation_id
        self.__case_id = case_id
        self.__correct_choice = correct_choice

    def get_variation_id(self):
        return self.__variation_id

    def get_case_id(self):
        return self.__case_id

    def get_description(self):
        return self.__description

    def get_correct_choice(self):
        return self.__correct_choice
