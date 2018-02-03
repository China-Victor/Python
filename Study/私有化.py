class Personal(object):

    def __init__(self, name, age, foo):
        self.name = name
        self._age = age
        self.__foo = foo

    def say_personal(self):
        print("personal info :")
        print("name = %s" % self.name)
        print("age = %s" % self._age)
        print("foo = %s" % self.__foo)


class Student(Personal):

    def __init__(self, name, age, foo):
        super().__init__(name, age, foo)
        self.name = name
        self._age = age
        self.__foo = foo

    def say_student(self):
        print("personal info :")
        print("name = %s" % self.name)
        print("age = %s" % self._age)
        print("foo = %s" % self.__foo)

    def set_age(self, age):
        self._age = age

    def set_foo(self, foo):
        self.__foo = foo

p = Student("张三", 18, "Bar")

p.say_personal()
p.say_student()

# __x 双下画线开头属性，为私有属性， 不可被之类继承，
# 虽然属性名相同，但是各有一份，固此处只能修改personal对象的"__foo"，而不会修改父类的属性"_foo"
p.set_foo("basket")

# _x 单下划线开头属性 可被之类继承， 所以 "_age" 为继承父类的属性
p.set_age(20)

p.say_student()
p.say_personal()

# ['_Personal__foo', '_Student__foo', '__class__', ...]
# 可以看到双下划线私有属性会被重命名为 _所在类名 + 私有属性名
print(dir(p))
# 强制修改
p._Personal__foo = "basket"

p.say_student()
p.say_personal()
