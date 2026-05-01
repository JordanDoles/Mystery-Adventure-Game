class Location:
    def __init__(self, location_id, name, case_id, variation_id):
        self.__location_id = location_id
        self.__name = name
        self.__case_id = case_id
        self.__variation_id = variation_id

    # Getters
    def get_location_id(self):
        return self.__location_id

    def get_name(self):
        return self.__name

    def get_case_id(self):
        return self.__case_id

    def get_variation_id(self):
        return self.__variation_id
