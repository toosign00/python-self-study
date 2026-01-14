# 2.1 숫자 자료형
print(5)

print(-10)
print(3.14)
print(1000)

# 간단한 사칙연산
print(5 + 3)
print(2 * 8)
print(6 / 3)
print(3 * (3 + 1))

# 2.2 문자열 자료형
print('풍선')
print("나비")
print("abcdefg")
print("10")
print("파이썬" * 3)

# 2.3 boolean 자료형
print(5 > 10)
print(5 < 10)

print(True)
print(False)

print(not True)
print(not False)

print(not (5 > 10))

# 2.4 변수
name = "해피" # 이름
animal = "고양이" # 동물 종류
age = 4 # 나이
hobby = "낮잠" # 취미

"""
# print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.") # 종류, 이름
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.") # 나이, 취미
"""
print(int("3"))

print(int(3.5))

print(float("3.5"))
print(float(3))

print(str(3) + "입니다.")
print(str(3.5) + "입니다.")

print(type(3)) # 정수(int)
print(type("3")) # 문자열(str)
print(type(3.5)) # 실수(float)
print(type(str(3))) # 정수(int)를 문자열(str)로 변환

# 실습문제: 역 이름 출력하기
"""
변수를 사용해 다음 문장을 출력하세요.

1. 변수명은 station으로 한다.
2. 값은 변수에 '사당', '신도림', '인천공항' 순으로 저장한다.
3. 실행결과는 다음과 같은 형태로 나와야 한다.

# 변수에 "사당"을 넣었을 때
사당행 열차가 들어오고 있습니다.

# 변수에 "신도림"을 넣었을 때
신도림행 열차가 들어오고 있습니다.

# 변수에 "인천공항"을 넣었을 때
인천공항행 열차가 들어오고 있습니다.
"""

station = "사당"
# station = "신도림"
# station = "인천공항"

print(station + "행 열차가 들어오고 있습니다.")