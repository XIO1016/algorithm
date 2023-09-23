import re
import sys

# 입력값 받기
inputCase, name = sys.stdin.readline().strip().split()

# 입력값을 처리하기 위한 변수 초기화
firstWord = [name[0]]  # 첫 번째 단어
rootWords = []  # 분리된 단어

# 입력값에 따라 처리 방법이 달라짐
if inputCase == '1':
    # 대문자, 소문자 순서로 패턴 기준으로 문자 분리
    rootWords = re.findall('[A-Z][a-z]*', name)

    # 소문자로 이뤄진 단어 하나 분리
    for i in range(1, len(name)):
        if name[i].isupper():
            break
        else:
            firstWord[-1] += name[i]
    rootWords = firstWord + rootWords

elif inputCase == '2':
    # 언더스코어 기준으로 단어 분리
    rootWords = name.split('_')

elif inputCase == '3':
    # 대문자, 소문자 순서로 패턴 기준으로 문자 분리
    rootWords = re.findall('[A-Z][a-z]*', name)

# 단어의 첫 글자를 대문자로, 나머지 글자를 소문자로 변환하여 붙이기
for i in range(len(rootWords)):
    rootWords[i] = rootWords[i].title()
result3 = "".join(rootWords)

# 첫 번째 단어는 소문자, 나머지 단어는 소문자로 변환하여 붙이기
rootWords[0] = rootWords[0].lower()
result1 = "".join(rootWords)

# 두 번째 단어부터 언더스코어로 붙이기
for i in range(1, len(rootWords)):
    rootWords[i] = rootWords[i].lower()
result2 = "_".join(rootWords)

# 결과값 출력
print(result1)
print(result2)
print(result3)
