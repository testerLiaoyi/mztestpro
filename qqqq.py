class Dog():
    """模拟狗类蹲下和打滚"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟狗坐下"""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """模拟狗打滚"""
        print(self.name.title() + " rolled over!")

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("this car has " + str(self.odometer_reading) + " miels on it")

    def updata_odometer(self,mileage):
        """将里程表的读书设置为指定的值
        并禁止把里程表往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cat't roll back an odometer ")

    def incremente_odometer(self,miles):
        """将里程表读数增加指定的值"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类属性"""
        super().__init__(make,model,year)


# my_dog = Dog('willie',6)
# print("my dog's name is " + my_dog.name.title() + '.')
# print("my dog's age is " + str(my_dog.age) + ' years old.')
# my_dog.sit()
# my_dog.roll_over()
my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
#直接修改属性值
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#通过方法修改属性的值
my_new_car.updata_odometer(22)
my_new_car.read_odometer()
#通过方法对属性的值进行递增
my_new_car.incremente_odometer(100)
my_new_car.read_odometer()
