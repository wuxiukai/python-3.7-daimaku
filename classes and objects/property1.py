class Person11:
    def __init__(self,name):
        self.__name = name
        print(self.__name)
    @property
    def name(self):
        """I'm the 'x' property."""
        return self.__name
#检测代码
p = Person11('王五')
print(p.name)
