# Dictionary, Set Data Types(사전, 집합 자료형)

# 딕셔너리 자료형(딕셔너리)
# 딕셔너리는 키와 값의 쌍을 데이터로 가지는 자료형
# 딕셔너리는 중괄호({})를 이용합니다.
# 변경 불가능한 자료형 을 키로 사용할수있다.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다.")

#---------------------------------

# 키 데이터만 뽑아서 리스트로 이용할 때는 keys() 함수를 이용합니다.
# 값 데이터만 뽑아서 리스트로 이용할 때는 values() 함수를 이용합니다.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])

a = dict()
a['홍길동'] = 97
a['이순신'] = 98

print(a)

b = {'홍길동': 97, '이순신': 98}
print(b)

key_list = list(b.keys())
print(key_list)

# 집합 자료형(집합)
# 집합은 중괄호({})를 이용합니다.
# 중괄호 안에 데이터를 나열하여 초기화 할 수 있습니다.
# 데이터의 중복을 허용하지 않습니다.
# 순서가 없습니다.
# 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리 가능

# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 합집합: A or B
# 교집합: A and B
# 차집합: A-B

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)
# 교집합
print(a & b)
# 차집합
print(a - b)

# 집합 자료형 관련 함수
# add() : 집합에 원소 추가
# update() : 집합에 원소 여러개추가
# remove() : 집합에서 원소 삭제
# pop() : 집합에서 원소 삭제

data = set([1, 2, 3])
print(data)

# 집합에 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 집합에서 원소 삭제
data.remove(3)
print(data)

# 리스트나 튜플은 순서가 있기 때문에 인덱싱으로 데이터를 얻을수 있다.
# 사전 자료형과 집합자료형은 순서가 없기 때문에 인덱싱으로 데이터를 얻을수 없다.
