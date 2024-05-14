# Basic Input and Output(기본 입출력)

# 기본 입출력
# 프로그램 동작의 첫 단계는 데이터를 입력 받거나 생성하는 것이다.
# input() 함수는 한 줄의 문자열을 입력을 받는 함수이다.
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

#***
# 입력을 위한 전형적인 소스코드 1)
# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 입력을 위한 전형적인 소스코드 2)
# n, m, k를 공백을 기준으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

# ------------------------------------
# 빠르게 입력 받기

# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
# 파이썬의 경우 sys라이브러리에 정의된 sys.stdin.readline() 메서드를 이용한다.
# 단, 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용한다.

import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)

# 자주 사용되는 표준 출력 방법
# print() : 한 줄에 여러 개의 데이터를 출력
# 각 변수를 콤마(,)로 구분하여 띄어쓰기로 구분하여 출력 할수 있다.
# print()는 기본적으로 출력 후에 줄 바꿈(line feed)을 수행한다.
# 아래와 같이 줄 바꿈을 원치 않는 경우, end 속성을 이용할수있다.

# 출력을 위한 전형적인 소스코드
# 출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

# 출력할 변수
answer = 7
print("정답은 " + str(answer) + "입니다.")

# f-string
# 문자열 앞에 접두사 f를 붙여 사용한다.
# 중괄호 안에 변수명을 깅비하여 간단히 문자열과 정수를 함께 넣을 수 있습니다.

answer = 7
print(f"정답은 {answer}입니다.")
