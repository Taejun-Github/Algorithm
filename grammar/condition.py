# testnum = 10

# if testnum < 10:
#     print('less than 10')
# elif testnum < 10:
#     print('more than 10')
# else:
#     print('testnum is 10')

# import datetime
# now = datetime.datetime.now();
# print("{:d}년{:d}월{:d}일{:d}시{:d}분{:d}초".format(now.year,now.month,now.day, now.hour, now.minute, now.second))

# # python에서 false로 변환되는 값은? None, 0, 0.0, 빈 컨테이너 등이다.

# number = input("정수 입력> ")
# number = int(number)

# if number > 0:
#     pass
#     raise NotImplementedError
# else:
#     pass
# 여기에서 pass를 써주지 않으면 들여쓰기 때문에 오류가 발생한다. 반드시 써주어야 한다.
# 그런데 pass만 써주면 그대로 넘어가 버리는 실수가 발생하므로 에러를 일부러 발생시킨다.

# 파이썬에서는 배열을 그냥 + 로 써주면 배열이 연결되고 배열에 * n 을 하면 배열이 n개만큼 연결된다.

# for i in range(100):
#     print('test')

import time
number = 0

target_tick = time.time() + 5

while time.time() < target_tick:
    number += 1

print("{:d}".format(number))

array = [i * i for i in range(10)]
# python에서는 이런 식으로 배열을 만들 수 있다.

array2 = ['1','2','3']
output = [number for number in array if number != '1']
# 이렇게 조건식도 넣을 수 있다.