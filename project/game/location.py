class Location:
    def __init__(self, location_id, location_name, location_description, case_id):
        self.__location_id = location_id
        self.__location_name = location_name
        self.__location_description = location_description
        self.__case_id = case_id

    # Getters
    def get_location_id(self):
        return self.__location_id

    def get_name(self):
        return self.__location_name

    def get_description(self):
        return self.__location_description

    def get_case_id(self):
        return self.__case_id

