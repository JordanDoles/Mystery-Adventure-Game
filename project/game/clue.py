class Clue:
    def __init__(self, clue_id, item_name, item_description, item_location, case_id, variation_id, culprit_id):
        self.__clue_id = clue_id
        self.__item_name = item_name
        self.__item_description = item_description
        self.__item_location = item_location
        self.__case_id = case_id
        self.__variation_id = variation_id
        self.__culprit_id = culprit_id

    def get_clue_id(self):
        return self.__clue_id

    def get_item_name(self):
        return self.__item_name

    def get_item_description(self):
        return self.__item_description

    def get_item_location(self):
        return self.__item_location

    def get_case_id(self):
        return self.__case_id

    def get_variation_id(self):
        return self.__variation_id

    def get_culprit_id(self):
        return self.__culprit_id
