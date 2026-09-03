# 반복문 : while문, for문

# while문
# 1 ~ 10까지의 반복 출력
i = 1
while i<=10:
    print(i)
    i += 1

    if i == 5:
        break
else:
    print("end")

nums = [1,3,5,7,9]
target = 2

while i < len(nums):
    if (i == target):
        print("found")
        break
else:
    print("not found")

for i in nums:
    if (i == target):
        print("found")
        break
else:
    print("not found")

# 1 ~ 10 까지의 합
i = 0
tot = 0

for i in range(1,11):
    if i % 2 != 0:
        continue
    tot += i
print(tot)