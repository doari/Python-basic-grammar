# Functions , Lambda(함수와 람다 표현식)

# 함수(Function)란 특정한 작업을 하나의 단위로 묶는 것을 말합니다.
# 함수를 사용하면 불필요한 소스코드의 반복을 중일 수 있습니다.
# 함수는 코드를 재사용할 수 있도록 만들어 놓은 것입니다.

# 함수의 종류
# 내장함수: 파이썬이 제공하는 기본 함수
# 사용자 정의 함수: 프로그램에 직접 정의한 함수


# 함수 정의하기
# def 함수명(매개변수):
#   실행할 소스코드
#   return 반환값

# 함수 호출하기
def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

#global 키워드
#함수 바깥에 선언된 변수를 바로 참조

a= 0

def func():
  global a
  a += 1

for i in range(10):
  func()

print(a)
