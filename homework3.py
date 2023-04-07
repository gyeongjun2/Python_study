#세준이가 기말을 망쳤습니다 
n = int(input())    # 과목의 갯수

score = list(map(int, input().split())) # 각 과목 점수 입력 받기

score_max = max(score)      #최댓값 저장

new_sum = 0
for i in score:
    new_score=i/score_max*100      #새로운 점수 조작
    new_sum = new_sum + new_score

avg = new_sum/len(score)    # 조작된 평균 구하기

print(avg)    # 조작된 평균 값 출력!!










