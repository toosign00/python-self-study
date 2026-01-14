# 3.1 연산자의 종류

# 3.1.1 산술 연산자
print( 1 + 1 )
print( 3 - 2 )
print( 5 * 2 )
print( 6 / 3 )

print( 2 ** 3 ) # 2의 3승
print( 10 % 3) # 나머지 구하기
print( 10 // 3 ) # 몫 구하기

# 3.1.2 비교 연산자
print( 10 > 3 )
print( 4 >= 7 )
print( 10 < 3 )
print( 5 <= 5 )

print( 3 == 3 )
print (4 == 2 )
print(3 + 4 == 7)
print( 1 != 3)

# 3.1.3 논리 연산자
print( (3 > 0) and (3 > 5) ) # false
print( (3 > 0) or (3 > 5) ) # true
print(not(1 != 3)) # false

# 3.2 연산자의 우선순위
print( 2 + 3 * 4 ) # 14
print( (2 + 3) * 4 ) # 20

# 3.3 변수로 연산하기
number = 2 + 3 * 4
print( number ) # 14

# number = number + 2 # (2 + 3 * 4) + 2
# print( number ) # 16

number += 2 # number = number + 2 와 동일
print( number ) # 16

number -=2 # number = number - 2 와 동일
print( number ) # 14
number *=2 # number = number * 2 와 동일
print( number ) # 28
number /=2 # number = number / 2 와 동일
print( number ) # 14.0
number **=2 # number = number ** 2 와 동일
print( number ) # 196.0
number %=2 # number = number % 2 와 동일
print( number ) # 0.0

# 3.4 함수로 연산하기
print( abs(-5) ) # -5의 절댓값
print( pow(4, 2) ) # 4를 제곱한 값
print( max(5, 12) ) # 둘 중 큰 값
print( min(5, 12) ) # 둘 중 작은 값
print( round(3.14) ) # 3.14를 소수점 이하 첫째 자리에서 반올림한 정수
print(round(4.6789, 2)) # 4.6789를 소수점 이하 셋째 자리에서 반올림한 값

# 3.4.2 math 모듈
from math import * # math 모듈의 모든 기능을 가져옴

result = floor(4.99)
print(result) # 4.99의 내림
result = ceil(3.14)
print(result) # 3.14의 올림
result = sqrt(16)
print(result) # 16의 제곱근

# 3.4.3 random 모듈
from random import * # random 모듈의 모든 기능을 가져옴
print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
print(random())
print(random())
print(random()*10) # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 0 이상 10 미만 정수에서 난수 생성(random() 결과를 int()로 감싸서 정수로 변환)
print(int(random()*10)+1) # 1 이상 11 미만 정수에서 난수 생성(random() 결과를 정수로 변환해 1을 더함)

# 예 1부터 45까지의 정수 범위 안에서 로또 번호 생성
print(int(random()*45)+1)

# 예2 randrange() 함수 이용
print( randrange(1, 46) ) # 1 이상 46 미만
print( randrange(1, 45) ) # 1 이상 45 미만

# 3.5 실습문제: 스터디 날짜 정하기

"""
문제: 코딩 스터디 모임을 만들었습니다. 월 4번 모이는데, 3번은 온라인으로, 1번은 오프라인으로 모이기로 했습니다.
조건에 맞는 오프라인 모임 날짜를 정하는 프로그램을 작성하세요.

조건:
1. 날짜를 무작위로 뽑는다.
2. 월별 일수가 다르므로 최소 일수인 28일 이내로 정한다(28일까지만 날짜 선정).
3. 매월 1~3일은 스터디 준비를 해야 하므로 제외한다.
4. 실행 결과는 다음과 같은 형태로 나와야 한다. 단, 날짜는 무작위므로 책과 결과가 다를 수 있다.

실행결과: 오프라인 스터디 모임 날짜는 매월 18일로 선정됐습니다.
"""

date = int(random() * 28) + 4 # 4일 ~ 31일
print(f"오프라인 스터디 모임 날짜는 매월 {date}일로 선정됐습니다.")

# 셀프체크 문제
"""
문제: 연산자를 이용해 온도 단위를 변환하는 프로그램을 만들어 보세요.

조건:
1. 섭씨 온도를 저장하기 위한 변수를 만든다.
2. 다음 공식을 이용해 섭씨 온도를 화씨 온도로 변환하고 새로운 변수에 저장한다.
화씨온도 = (섭씨온도 * 9/5) + 32
3. 썹씨 온도와 화씨 온도를 다음과 같이 출력한다.

실행결과:
# 섭씨 온도가 30도 일 때
섭씨온도 : 30
화씨 온도 : 86.0

# 섭씨 온도가 10도일 때
섭씨 온도 : 10
화씨 온도 : 50.0
"""

temp_c = 30
temp_f = temp_c * 9/5 + 32

print(f"섭씨 온도 : {temp_c}")
print(f"화씨 온도 : {temp_f}")

temp_c = 10
temp_f = temp_c * 9/5 + 32

print(f"섭씨 온도 : {temp_c}")
print(f"화씨 온도 : {temp_f}")

