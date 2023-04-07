print("정수 3개 입력")

a = input("1: ")
b = input("2: ")
c = input("3: ")

max = a

if b>max:
    max = b

if c>max:
    max = c

print("가장 큰 정수 값은",max,"입니다")