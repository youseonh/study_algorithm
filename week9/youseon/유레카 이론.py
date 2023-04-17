tri_nums = []

# 1부터 1000까지의 삼각수 계산
for i in range(1, 46):
    tri_nums.append(i*(i+1)//2)

# 세 개의 삼각수 합으로 이루어진 수 생성
eureka = [0]*1001
for i in range(len(tri_nums)):
    for j in range(i, len(tri_nums)):
        for k in range(j, len(tri_nums)):
            if tri_nums[i]+tri_nums[j]+tri_nums[k] <= 1000:
                eureka[tri_nums[i]+tri_nums[j]+tri_nums[k]] = 1

# 주어진 수가 유레카 수인지 판별
T = int(input())
for _ in range(T):
    n = int(input())
    print(1 if eureka[n] else 0)