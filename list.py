# 리스트(list)

# mbti = ['INFP','ENFP','ISTJ','ISFP']

# print(mbti)
# print(mbti[0])

# mbti[0]='INFJ'

# print(mbti)
# print(mbti[0])

# my_list = [123, 'apple']
# print(my_list)

# color = ['red', 'blue', 'green']

# 리스트 element 수정
# color[2] = 'black'

# print(color)

# #추가
# color.append('purple')  #맨 마지막에 요소 추가
# print(color)

# #추가 2

# color.insert(2,'yellow')    #2번 인덱스에 넣고 나머지는 뒤로 밀어낸다
# print(color)

# 제거

# del color[0]
# print(color)

 # 제거 2

# colors = color.pop(0)    # del 은 아예 삭제 pop 은 데이터 반환 가능
# print(color)
# print(colors)

# 제거 3
# color.remove('purple')    # 값을 아예 집어넣어버리기
# print(color)


#리스트 정렬
# print("리스트정렬")
# color = ['blue', 'red', 'black', 'gray','yellow', 'orange']

# 정렬 1

# color.sort()    #알파벳 순으로 정렬
# print(color)

# color.sort(reverse=True)    # 알바펫 역순 정렬
# print(color)

#정렬 2

# sorted(color)   # xx
# print(sorted(color))    # sorted는 괄호안에 변수를 넣어줘야함

# #길이 - 요소의 갯수

# print(len(color))   #리스트의 갯수 파악

# print(color[-1])    #마지막 인덱스는 -1

#리스트 슬라이싱

# color = ['blue', 'red', 'black', 'gray','yellow', 'orange']

# color2 = color[:]


# print(color2)
# print(color[1:5])   # [슬라이싱 시작 : 끝부분 (마지막은 x)]
# print(color[:4])
# print(color[2:])

# print(color[-5:])   #-1은 맨 마지막 그 앞으로 -2 -3 -4


scores = [88,100,90,39,43,53]

# max_val=max(scores)
# min_val=min(scores)
# sum_val=sum(scores)
sum_val = sum(scores)
avg_val = sum(scores)/len(scores)
print(avg_val)

# sum_values = 0
# for score in scores:
#     sums = sum_values + scores
# print(sum_values)


# scores.sort(reverse=True)
# print(scores)


# for score in scores:
#     if score>=80:
#         print(score)
#     else:
#         print("Fail")
