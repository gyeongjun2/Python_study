# 튜플 (Tuples)

# 튜플은 소괄호 사용

tup = (1, 20, 40) #각각의 요소의 값을 변경 x
# print(tup[0])
# tup[0]=100 x 변경불가

# tup = (100, 11, 22) #튜플 전체의 값은 변경 가능
# print(tup)

for x in tup:
    print(x)

# 리스트 변환 1

list_1 = list(tup)
print(list_1)
#리스트 변환 2
list_2 = [x for x in tup]
print(list_2)