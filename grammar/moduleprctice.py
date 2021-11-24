import math
from ssl import enum_certificates
# math.sin(1)
print(math.sin(1))
print(math.tan(1))

print(math.floor(2.5))# 내림

print(math.ceil(2.5)) # 올림

from math import sin, cos, tan, floor, ceil
# 이렇게 원하는 함수만 가져올 수도 있다.

import math as m
# 이렇게 하면 m으로 모듈을 사용할 수 있다.
import random
print(random.random())
print(random.uniform(10, 20))
# 지정한 범위 사이의 float를 리턴한다.
print(random.choice([1,2,3,4,5]))
# 리스트 내부에 있는 요소를 랜덤하게 선택한다.

import sys
print(sys.argv)
print(sys.getwindowsversion())
print(sys.copyright)

import os
print(os.name)
os.mkdir("hi")
os.rmdir("hi")

with open("original.txt", "w") as file:
    file.write("hi")

os.rename("original.txt", "new.txt")
# 파일을 생성하고 파일 이름을 변경한다.

import datetime
now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

output_b = "{}년{}월{}일{}시{}분{}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
output_a = now.strftime("%Y .%m. %d %H:%M:%S")
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
# 문자열, 리스트 등 앞에 *를 붙이면 요소 하나하나가 매개변수로 지정된다.

from urllib import request

target = request.urlopen("https://www.pornhub.com")
output = target.read()

print(output)

def test(function):
    def wrapper():
        print('aaa')
        function()
        print('bbb')
    return wrapper
#이런식으로 함수를 감싸는 데코레이터를 작성할 수 있다.

@test
def hello():
    print('hi')

hello()

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def __del__(self):
        print('소멸자')


    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.sum() / 4

    @classmethod
    def classmethod1(cls):
        print('클래스메서드')

    def __str__(self):
        return "{}{}{}".format(self.name, self.get_sum, self.get_average)

class Parent:
    def __init__(self):
        print('parent')

    def test(self):
        print('test')

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)