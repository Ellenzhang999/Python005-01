from abc import ABCMeta, abstractmethod

SIZES = {'小': 1, '中等': 2, '大': 3}

# 动物类不允许被实例化->使用抽象类
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性
# 是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
class Animal(object):    
    is_ferocious = False
    @abstractmethod
    def __init__(self, name, eat, size, character):
        self.name = name
        self.eat = eat
        self.size = SIZES[size]
        self.character = character
        # 是否属于凶猛动物
        if (self.size >= 2 and self.eat == '食肉' and self.character == '凶猛'):
            self.is_ferocious = True
        else:
            self.is_ferocious = False

# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，
# 其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
class Cat(Animal):
    #类属性
    sound = "喵~"    

    def __init__(self, name, eat, size, character):      
        super().__init__(name, eat, size, character)
        self.able_pet = not self.is_ferocious

class Dog(Animal):
    #类属性
    sound = "汪~"

    def __init__(self, name, eat, size, character):    
        super().__init__(name, eat, size, character)
        self.able_pet = not is_ferocious

# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
class Zoo(object):

    def __init__(self, name):
        self.name = name
        self.animals = dict()

    # 增加动物到动物园
    def add_animal(self, animal):        
        # 先判断动物在不在
        if self.animals.get(animal.name):   
            print(f"{animal.name} has been added and won't be added again")
        else:
            self.animals[animal.name] = animal           
            print(f"{animal.name} is added")

    def has_animal_type(self, animal_type):
        for v in self.animals.values():
            if v.__class__.__name__ == animal_type:
                return True
        return False

def hasattr(zoo,animal_type):
    return zoo.has_animal_type(animal_type)

# 调试输出：
# 大花猫 1 is added
# 大花猫 2 is added
# 大花猫 1 has been added and won't be added again
# 动物园里有猫吗？True
# 动物园里有狗吗？False
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化三只Cat测试添加重复
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    z.add_animal(cat1)
    cat2 = Cat('大花猫 2', '食肉', '小', '温顺')
    z.add_animal(cat2)
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(f"动物园里有猫吗？{have_cat}")
    print(f"动物园里有狗吗？{hasattr(z,'Dog')}")

    

