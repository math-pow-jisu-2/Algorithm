# boj-2839: 설탕 배달
## 설탕을 정확하게 n킬로그램 배달
## 3/5 두가지 봉지
## 최대한 적은 봉지 가져가기

n = int(input())
temp = 0

while n>=0:
    if n%5==0:
        temp += (n//5)
        print(temp)
        break
    n -= 3
    temp += 1
else:
    print(-1)
