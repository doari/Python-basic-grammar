# Conditional Statements(조건문)

# 조건문
# 조건문은 프로그램의 흐름을 제어하는 문법으로, 조건문을 이용해 조건에 따라서 프로그램의 로직을 설정할 수 있습니다.

x = 15

if x >= 10:
  print("x >= 10")

if x >= 0:
  print("x >= 0")

if x >= 30:
  print("x >= 30")

# 들여쓰기
# 파이썬에서는 코드의 블록(Block)을 들여쓰기(Indent)로 지정한다.
# 탭과 공백문자 방법이 있는데 파이썬 스타일 가이드라인에서는 4개의 공백 문자를 사용하는것을 표준으로 설정

score = 85
if score >= 70:
  print('성적이 70점 이상입니다.')
  if score >= 90:
    print('우수한 성적입니다.')
else:
  print('성적이 70점 미만입니다.')
  print('조금 더 분발하세요.')

print('프로그램을 종료합니다.')

# 조건문의 기본 형태
# 조건문의 기본적인 형태은 if ~ elif ~ else 입니다.
# 조건물을 사용할 때 elif 혹은 else 부분은 경우에 따라서 사용하지 않아도 됩니다.

a = 5

if a >= 0:
  print("a >= 0")
elif a >= -10:
  print("0 > a >= -10")
else:
  print("-10 > a")

# 성적 구간에 따른 학점 출력 예제

score = 85
if score >= 90:
  print("학점: A")
elif score >= 80:
  print("학점: B")
elif score >= 70:
  print("학점: C")
else:
  print("학점: F")

#----------------------------------------------------

# 비교 연산자

# 대입 연산자(=)와 같음 연산자(==)의 차이점에 유의하세요.

# X==Y : X와 Y가 같을때 참(True)이다..
# X!=Y : X와 Y가 다를때 참(True)이다..
# X>Y : X가 Y보다 클을때 참(True)이다.
# X<Y : X가 Y보다 작을때 참(True)이다.
# X>=Y : X가 Y보다 크거나 같을때 참(True)이다.
# X<=Y : X가 Y보다 작거나 같을때 참(True)이다.

# 논리 연산자
# and : 두 개의 조건이 모두 참일때 참(True)이다.
# or : 두 개의 조건 중 하나라도 참일때 참(True)이다
# not : 조건의 부정을 나타내는 연산자

a = 15

if a <= 20 and a >= 0:
  print("Yes")

# 파이썬의 기타 연산자
# x in 리스트 : 리스트 안에 x가 들어있을때 참(True)
# x not in 문자열 : 문자열 안에 x가 들어있지 않을때 참(True)

# pass 키워드
# 조건문의 블록을 비워두는 키워드, 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용

score = 85

if score >= 80:
  pass # 나중에 작성할 소스코드
else:
  print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# 조건문의 간소화
# 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있습니다.

score = 85
if score >= 80: result = "Success"
else: result = "Fail"

print(result)
# 조건부 표현식(Conditional Expression)은 if ~ else문을 한 줄에 작성할 수 있도록 해줍니다.
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)


#-----------------------------------------------------------------------

# 파이썬 조건문 내에서의 부등식

# 다른 프로그래밍 언어와 다르게 파이썬은 조건문 내에서의 수학의 부등식을 지원합니다.
# 예를 들어 x > 0 and x < 20과 0 < x < 20과 같은 결과를 반환합니다.

#코드 스타일 1
x = 15
if x > 0 and x < 20:
  print("x는 0이상 20미만의 수입니다.")

# 코드 스타일 2
x = 15
if 0 < x < 20:
  print("x는 0이상 20미만의 수입니다.")













  