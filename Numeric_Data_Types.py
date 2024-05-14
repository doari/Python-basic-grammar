#수 자료형

# 정수형(Integer) 양,음,0
# 코딩 테스트에서는 주로 정수형

# 양의정수
a = 1000
a = a + 5
print(a)

# 음의정수
a = -1000
a = a - 5
print(a)

# 0
a = 0
print(a)

#---------------------------------------------------
# 실수형(Real Number) 소수점 아래의 데이터를 포함하는 수 자료형

# 양의실수
a = 157.93
print(a)

# 음의실수
a = 157.93
print(a)

# 양의실수
a = 5.
print(a)

# 양의실수
a = -.7
print(a)

#지수 표현 방식
#유효숫자e지수 = 유효숫자 * 10지수
#도달할 수 없는 노드에 대하여 무한(INF) 설정하곤 한다.
#10억 미만이라면 무한(INF)의 값으로 1e9를 이용할 수 있습니다.

# 1,000,000,000 의 지수 표현 방식(기본적으로 실수형이다.)
a = 1e9
b = int(1e9)
print(a) 
print(b) 

#752.5
a = 75.25e1
print(a)

#3.954
a = 3954e-3
print(a)

#컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 가집니다.(4byte,8byte)

a = 0.3 + 0.6
print(a)

if a == 0.9:
  print(True)
else:
  print(False)

#round 함수를 이용하여 반올림
a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
  print(True)
else:
  print(False)

  # 사칙연산
# 나누기 연산자(/) 실수형으로 반환
# 나머지 연산자(%)
# 몫 연산자(//)
# 거듭 제곱 연산자(**)

a = 7
b = 3

# 나누기
print(a / b)

# 나머지
print(a % b)

# 몫
print(a // b)

a = 5
b = 3

# 거듭 제곱
print(a ** b)

# 제곱근
print(a ** 0.5)