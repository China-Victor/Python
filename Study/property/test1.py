class Personal(object):
    """通过get、set方式控制属性的获取和设置"""
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("name is not isinstance str.")


p = Personal("Victor")
print(p.get_name())

p.set_name("Victor Wu")
print(p.get_name())

p.set_name(18)
