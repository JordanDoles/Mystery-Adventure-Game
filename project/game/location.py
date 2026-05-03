class Location:
    """
    Location Class
    """
    def __init__(self, location_id, location_name, location_description, case_id):
        """
        Initialize a Location object
        :param location_id: location_id
        :type location_id: str
        :param location_name: location_name
        :type location_name: str
        :param location_description:location_description
        :type location_description: str
        :param case_id: case_id
        :type case_id: str
        """
        self.__location_id = location_id
        self.__location_name = location_name
        self.__location_description = location_description
        self.__case_id = case_id

    def get_location_id(self):
        """
        Return the Location ID
        :return: location_id
        """
        return self.__location_id

    def get_name(self):
        """
        Return the Location Name
        :return: location name
        """
        return self.__location_name

    def get_description(self):
        """
        Return the Location Description
        :return: location_description
        """
        return self.__location_description

    def get_case_id(self):
        """
        Return the Location Case ID
        :return: location id 
        """
        return self.__case_id

