# 딕셔너리
# 딕셔너리는 중괄호 {}
student = {
    "student_no": "20191807",
    "major": "information",
    "grade": 3
}

print(student["student_no"])

student["student_no"] = "20221807"

print(student)
print(student["student_no"])

# 추가

student["gpa"] = 4.5
print(student)

#수정
student["gpa"] = 4.3
print(student)

#삭제
del student["grade"]
print(student)

# 데이터 접근 함수 get

print(student.get("major"))
print(student.get("none", "해당 키-값 쌍이 없습니다"))  #없다면 뒤에 ("키","없을 시 출력할 문자")

#딕셔너리의 키를 반환
print (list(student.keys()))  #.keys() << 키 반환 list() 반환한 키를 리스트로 만듦

#딕셔너리의 값을 반환

print(list(student.values()))

#딕셔너리와 반복문
tech = {
    "HTML": "Advanced",
    "JS": "Intermediate",
    "Python": "Expert",
    "Go": "Novice"
}

for key, value in tech.items():
    print(f'{key}-{value}')

print("------------------")
for k in tech.keys():
    print(k)

print("------------------")
for v in tech.values():
    print(v)

# 중첩(Nesting)

children_1 = {
    "human_no": "1",
    "gpa": "4.3"
}

children_2 = {
    "human_no": "2",
    "gpa": "2.9"
}


childrens = [children_1, children_2] # 딕셔너리의 중첩 리스트로

for children in childrens:
    print(children['human_no'])
    children['졸업'] = False
    print(children)

student = {
    "subjects": ["회계원리", "중국어회화"]
}

print(student["subjects"])

subjects_list = student["subjects"]

for subject in subjects_list:
    print(subject)

# 딕셔너리 안에 딕셔너리 ?

market = {
    "coffeshop":{
    "starbucks": "7",
    "twosome": "10"
    }
}

print(market)

for k in market.keys():
    print(k)

for v in market.values():
    print(v)

    for v in market.values():
        for v2 in v.values():
            print(v2)
