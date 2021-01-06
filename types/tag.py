from uuid import uuid4

class tag :
    #    fields 
    __id = ""
    __name = ""
    __is_active = True
    ################################3
    
    
    #    constructor 
    def __init__(self, name) : 
        self.__id = uuid4()
        self.__name = name
        self.__is_active = True
    ##############################################
    
    
    def remove(self) : 
        self.__is_active = False

    def get_id(self) : 
        return self.__id

    def get_name(self) : 
        return self.__name

    def get_is_active(self) : 
        return self.__is_active
        
    def set_id(self, id) : 
        self.__id = id

    def set_name(self, name) : 
        self.__name = name

    def set_is_active(self, is_active) : 
        self.__is_active = is_active
    
        
    