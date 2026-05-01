class Case:
    def __init__(self, case_id, name):
        self.__case_id = case_id
        self.__name = name

    def get_case_id(self):
        return self.__case_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
