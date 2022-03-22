# 2xN 타일링

n=int(input())
dp= [0 for _ in range(1001)] #배열 만들어 주고
dp[1]=1
dp[2]=3 #정답은 [0,1,3,5,11 ... ] 순으로 가기 때문에 0,1,3, 맟춰준다.
for i in range (3, 1001):
    dp[i]=dp[i-1]+2*dp[i-2] # (i-1)의 값과 (i-2)*2 의 값이기 때문에 식을 이렇게 짜준다.
print(dp[n]%10007)  #결과 값 출력
