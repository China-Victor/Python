class Personal(object):
    """使用@property为属性绑定get、set函数"""
    def __init__(self, name=None):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("name is not instance of Type 'str'")


p = Personal()

p.name = "Victor"
print(p.name)

p.name = 18
