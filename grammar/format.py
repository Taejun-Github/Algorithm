# format() 함수로 숫자를 문자열로 변환하기
# string_a = "{}".format(10)

# print(string_a)
# print(type(string_a))

# format_a = "{}만 원".format(5000)
# format_b = "다른 형식으로 {} 구하기".format(5.123)
# format_c = "숫자를 각각 입력하기: {}, {}, {}".format(1, 2, 3)
# format_d = "숫자: {},문자: {},논리값: {}".format(1, 'a', True)

# print(format_a, ' ', format_b, ' ',format_c, ' ',format_d)

output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print(output_a)
print(output_b) # 5칸의 공백을 만든다
print(output_c) # 10칸의 공백을 만든다
print(output_d) # 빈자리를 0으로 채워서 5칸을 만든다
print(output_e) # 맨 앞자리를 부호로 채우고 나머지 빈 곳을 0으로 채운다.

output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52) # +를 붙이지 않으면 양수를 출력할 때 기호 부분이 공백이 된다.
output_i = "{: d}".format(-52)

output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(-52) # 이렇게 =를 써주면 기호를 맨 앞으로 밀 수 있다.
output_k = "{:=+5d}".format(52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52) # 이렇게 하면 맨 앞자리에 부호가 나오고 나머지를 0으로 채울 수 있다.
# 기호와 공백을 조합할 때는 = 기호를 앞에 붙일 수 있다. 그리고 반드시 조합 형태를 지켜야 한다.

output_f_a = "{:f}".format(1.234)
# 이렇게 실수를 출력할 때는 f를 붙여준다.

output_f_b = "{:g}".format(1.234000)
# :g를 사용하면 의미 없는 뒷부분의 0을 제거하고 출력할 수 있다.

# 문자열의 구성 파악하기
"""
isalnum(): 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인한다.
isalpha(): 문자열이 알파벳으로만 구성되어 있는지 확인한다.
isidentifier(): 문자열이 식별자로 사용할 수 있는 것인지 확인한다.
isdecimal(): 문자열이 정수 형태인지 확인한다.
isdigit(): 문자열이 숫자로 인식될 수 있는 것인지 확인한다.
isspace(): 문자열이 공백으로만 구성되어 있는지 확인한다.
islower(): 문자열이 소문자로만 구성되어 있는지 확인한다.
issupper(): 문자열이 대문자로만 구성되어 있는지 확인한다.

"""

output_find_a = "hihihihihallohihihihi".find("hallo")
# 왼쪽부터 찾아서 처음 등장하는 위치를 찾는 것이 find()

output_find_b = "hihihihihiciaohihihihihi".rfind("ciao")
# 오른쪽부터 찾아서 처음 등장하는 위치의 인덱스를 반납

print(output_find_a in 'hi')
# 이렇게 하면 True나 False를 반납한다.

