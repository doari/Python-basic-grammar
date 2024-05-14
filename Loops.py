# Loops(반복문)

# 반복문
# 반복적으로 실행하고자 할 때 사용하는 문법
# 파이썬에서는 while문과 for문이 있습니다. 어떤 것을 사용해도 상관 없습니다.
# 다만 코딩테스트에서의 실제 사용 예시를 확인해 보면, for 문이 더 간결한 경우가 많습니다.
# 반복문은 조건문과 비슷하게 작성되어 있습니다.

# 1부터 9까지 모든 정수의 합 구하기 예제(while 문)
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
  result += i
  i += 1

print(result)

# 1부터 9까지 홀수의 합 구하기 예제 (while 문)
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
  if i % 2 == 1:
    result += i
  i += 1

print(result)

# 반복문에서의 무한 루프
# 무한 루프(infinite loop)란 끊임없이 반복되는 반복 구문을 의미합니다.
# 무한 루프를 끊을 수 있는 방법은 break 키워드를 이용합니다.

#반복문 : for 문
# for문의 구조는 다음과 같은데, 특정한 변수를 이용하여 'in'뒤에 오는 데이터(리스트, 튜플 등)에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문합니다.

array = [9, 8, 7, 6, 5]

for x in array:
  print(x)

# for문에서 연속적인 값을 차례대로 순회할 때는 rnage()를 주로 사용합니다.
# range()는 특정한 범위의 정수를 순회하는 함수입니다.
# range(a, b)는 a부터 b-1까지의 정수를 순회
# 인자를 하나만 넣으면 자동으로 시작 값은 0 이 됩니다.

#1부터 30까지 모든 정수의 합 구하기 예제 (for문)
result = 0

for i in range(1, 31):
  result += i

print(result)

# 파이썬의 continue 키워드
# continue 키워드는 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 continue를 사용

# 1부터 9까지의 자연수 중 홀수의 합 출력하기
result = 0

for i in range(1, 10):
  if i % 2 == 0:
    continue
  result += i

print(result)

# 파이썬의 break 키워드
# break 키워드는 반복문을 끊는 키워드입니다.

# 1부터 5까지의 정수를 차례대로 출력하고자 할 때 다음과 같이 작성할 수 있습니다.

i = 1

while True:
  print("현재 i의 값:", i)
  if i == 5:
    break
  i += 1

# 학생들의 합격 여부 판단 예제 1)점수가 80점만 넘으면 합격
scores = [90, 85, 77, 65, 97]

for i in range(5):
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")

# 학생들의 합격 여부 판단 예제 2)특정 번호의 학생은 제외하기
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
  if i + 1 in cheating_student_list:
    continue
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")

# 중첩된 반복문: 구구단 예제
for i in range(2, 10):
  for j in range(1, 10):
    print(i, "X", j, "=", i * j)
  print()
