class Case:
    def __init__(self, case_id, name, what_choice_1, what_choice_2, what_choice_3):
        self.__case_id = case_id
        self.__name = name
        self.__what_choice_1 = what_choice_1
        self.__what_choice_2 = what_choice_2
        self.__what_choice_3 = what_choice_3

    def get_case_id(self):
        return self.__case_id

    def get_name(self):
        return self.__name
        
    def get_what_choice_1(self):
        self.__what_choice_1 = what_choice_1
        
    def get_what_choice_2(self):
        self.__what_choice_1 = what_choice_2
        
    def get_what_choice_3(self):
        self.__what_choice_3= what_choice_3
