# 반복문(loops)

i = 0
text= ""
sum = 0
for i in range(1, 101):
    print(i)


for i in range(1, 101):
    sum +=i

print(sum)

progress = 0

while progress <100:
    progress += 1
    print(f"{progress}% completed")