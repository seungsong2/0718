class Dog :
    def __init__(self,name,breed):
        self.dog_name = name
        self.dog_breed = breed
        self.dog_sex = "여"

    def bark(self):
        print(self.dog_name + "가 짖습니다.")

# 제제를 추출하는 법
print(Dog("제제","푸들").dog_name)

# self = 너가 만든 객채 가지고 와

Dog("제제","푸들").bark()

my_dog = Dog("제제" ,"푸들")
my_dog.bark()