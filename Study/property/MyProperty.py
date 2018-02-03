
def my_property(func):
    def add_attr(obj):
        """@x"""
        setattr(obj, func.__name__, None)
    return add_attr



class Personal(object):

    def __init__(self, name=None):
        self.__name = name

    @my_property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

