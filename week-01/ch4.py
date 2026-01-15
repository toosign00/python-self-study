#4.1 문자열이란
sentence1 = '나는 소년입니다.'
print(sentence1, type(sentence1))
sentence2 = "파이썬은 쉬워요."
print(sentence2, type(sentence2))
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)

#4.2 원하는 만큼 문자열 자르기: 슬라이싱
jumin= "990229-1234567"
print("성별 식별번호 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4]) # 2부터 4 직전까지 (2,3)
print("일 : " + jumin[4:6]) # 4부터 6 직전까지 (4,5)
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 -> jumin[0:6] == jumin[:6]
print("주민등록번호 뒷자리 : " + jumin[7:]) # 7부터 끝까지 -> jumin[7:14] == jumin[7:]
print("주민등록번호 뒷자리(뒤에서부터 : " + jumin[-7:]) # 뒤에서 7번째 위치부터 끝까지

#4.3 함수로 문자열 처리하기
python = "Python is Amazing"

print(python.lower()) # 모두 소문자로 변환
print(python.upper()) # 모두 대문자로 변환
print(python[0].isupper()) # 인덱스 0에 있는 값이 대문자인지 확인
print(python[1:3].islower()) # 인덱스 1~2에 있는 값이 소문자인지 확인
print(python.replace("Python", "JavaScript")) # Python을 JavaScript로 변경

find = python.index("n") # 처음 발견한 n의 인덱스
print(find) # 'Python'에서 n(인덱스 5)
find = python.index("n", find + 1) # 두 번째 n의 인덱스
print(find) # 'Amazing'에서 n(인덱스 15)
find = python.find("JavaScript") # JaVaScript가 없으면 -1을 반환(출력)한 후 프로그램 계속 수행
print(find)

index = python.index("n") # 처음 발견한 n의 인덱스
print(index) # 'Python'에서 n(인덱스 5)
index = python.index("n", index + 1) # 두 번째 n의 인덱스
print(index) # 'Amazing'에서 n(인덱스 15)
index = python.index("n", 2, 6) # 2~5 인덱스 범위 내에서 n을 찾음
print(index)
index = python.index("JavaScript") # JavaScript가 없으면 오류 발생 후 프로그램 종료
print(index)

print(python.count("n")) # 문자열 내 n의 개수 세기
print(python.count("v")) # 문자열 내 v의 개수 세기
print(len(python)) # 문자열의 길이 구하기
