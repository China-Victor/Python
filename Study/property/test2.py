class Personal(object):
    """通过property类为公开属性绑定get、set方法，通过get、set方法获取和设置私有属性值"""
    def __init__(self, name=None):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("name is not instance of Type 'str'")

    name = property(get_name, set_name, doc="I'm the 'name' property.")


p = Personal()

# 等同于p.set_name("Victor")
p.name = "Victor"

# 等同于p.get_name()
print(p.name)
