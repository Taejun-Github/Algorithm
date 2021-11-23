def print_n_times(value, n):
    for i in range(10):
        print(i)

def print_n_times_args(n=2, *values):
    for i in range(n):
        print(i)

# *가변 매개변수로 받을 수 있다. 가변 매개변수는 반드시 마지막에 와야 한다.
# 매개변수에는 디폴트값을 지정할 수 있다.

counter = 0

def fibonacci(n):
    global counter
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 여기에서 global을 쓰지 않으면 오류가 발생한다. 다른 언어와 달리 python에서는 함수 내부에서 외부 변수 접근이 불가능하다.


dictionary = { 1: 1, 2: 2}

def fibonacciMemo(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacciMemo(n - 1) + fibonacciMemo(n - 2)
        dictionary[n] = output
        return output

#메모가 되어 있으면 메모된 값을 리턴하고 메모가 되어 있지 않으면 값을 구한다.


# 요소를 하나만 가지는 튜플을 선언하기
a = (1,)
# 이렇게 하나만 써줘도 ,를 반드시 써야 한다. 튜플이 리스트와 다른 점은 한번 결정된 요소를 바꿀 수 없다는 것이다.

a, b = 10, 20

a, b = b, a
# 이렇게 튜플을 사용하면 간단하게 값을 교환할 수 있다.

# map과 filter는 제너레이터이기 때문에 한번만 사용가능하다.

#람다식
power = lambda x : x * x
#람다의 형식은 lambda 매개변수: 리턴값이다.


# 제너레이터

def test():
    print("A")
    yield 1
    print("B")
    yield 2
    print("C")


output = test()

print("D")
a = next(output)
print(a)

print("E")
b = next(output)
print(b)

print("F")
c = next(output)
print(c)

# yield 키워드를 사용하면 함수를 호출해도 실행되지 않고 반드시 next() 함수를 사용해서 함수 내부의 코드를 실행한다.

