# 문자열(Strings) = 문자의 나열

city = "seoul" #Seoul, SEOUL, SEOul

print(city)

city.upper()    #대문자로 바꿈
print(city.upper())

city = city.upper()

print(city)

city.lower() #소문자로 바꿈
print(city.lower())
city = city.lower()

occupation = "  developer  "
print(occupation)
occupation.lstrip() #공백 제거 명령어   rstrip 오른쪽 공백 lstrip 왼쪽 공백
print(occupation.lstrip())

occupation.rstrip()
occupation.strip() #전체 공백 제거
print(occupation.strip())

print("infp\nenfp\nistj\nestj") # \n 줄바꿈   \t  개행문자

score ="점수 : 90"
print(score.removeprefix("점수 : "))

score_2 = "75점"
print(score_2.removesuffix("점"))

city = "서울 중구"
print(city.replace("서울","서울시"))

si_1 = "용인"

si_2 = "인천"

gu_1 = "기흥"

gu_2 = "종로"

#서울시 종로구
#용인시 기흥구
#(시의이름)시 (구의이름)구
print(f"{si_1}시 {gu_1}구")

print(f"{si_2}시 {gu_2}구")

