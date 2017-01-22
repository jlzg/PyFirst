import random
import sys
import os

random_num = random.randrange(0,100)

x= 0
while(random_num != 12):
    print("line ", x, " ", random_num)
    x+=1
    random_num = random.randrange(0,100)


print ("what's your name")

#name = input()
#name = sys.stdin.readline()
#print ("Hello", name)


test_file = open("test.txt","wb")

print (test_file.mode)
print (test_file.name)

test_file.write(bytes("first line of the file\n","utf8"))

test_file.close()

test_file = open("test.txt", "r+")

text = test_file.read()
print(text)

test_file.close()


##OOP
class Animal:
    __name = ""
    __sound = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self, name):
        return self.__name

    def __init__(self, name, sound):
        self.__name = name
        self.__sound = sound

    def toString(self):
        return "{} is making a sound {}".format(self.__name, self.__sound)

cat = Animal("King", "Phew")

print(cat.toString())

cat.set_name("Queen")
print(cat.toString())

class Dog(Animal):
    __owner = ""
    __sound = "Won"
    def __init__(self, name):
        self.__name = name
        super(Dog, self).__init__(name= self.__name, sound = self.__sound)


dog = Dog("Bot")
print (dog.toString())


os.remove("test.txt")

