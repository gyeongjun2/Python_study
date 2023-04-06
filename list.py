# 리스트(list)

mbti = ['INFP','ENFP','ISTJ','ISFP']

print(mbti)
print(mbti[0])

mbti[0]='INFJ'

print(mbti)
print(mbti[0])

my_list = [123, 'apple']
print(my_list)

color = ['red', 'blue', 'green']

# 리스트 element 수정
color[2] = 'black'

print(color)

#추가
color.append('purple')  #맨 마지막에 요소 추가
print(color)

#추가 2

color.insert(2,'yellow')    #2번 인덱스에 넣고 나머지는 뒤로 밀어낸다
print(color)

# 제거

del color[0]
print(color)

# 제거 2

colors = color.pop(0)    # del 은 아예 삭제 pop 은 데이터 반환 가능
print(color)
print(colors)

# 제거 3
color.remove('purple')    # 값을 아예 집어넣어버리기
print(color)
