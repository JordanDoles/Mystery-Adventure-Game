class Case:
    def __init__(self, case_id, name, opening):
        self.__case_id = case_id
        self.__name = name
        self.__opening = opening

    def get_case_id(self):
        return self.__case_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_opening(self):
        return self.__opening
