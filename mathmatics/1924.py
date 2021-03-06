# 문제
# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

# 출력
# 첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

# 예제 입력 1 
# 1 1
# 예제 출력 1 
# MON

# 예제 입력 2 
# 3 14
# 예제 출력 2 
# WED

# 예제 입력 3 
# 9 2
# 예제 출력 3 
# SUN

# day=0                                                   >>임의의 값
# arrlist=[31,28,31,30,31,30,31,31,30,31,30,31]           >>월에 맞는 일 수
# weekday=["SUN","MON","TUE","WED","THU","FRI","SAT"]     >>요일에 맞는 날짜
# x,y=map(int,(input()).split())                          >>x y 값 받고
# for i in range (x-1):                                   >>반복문 돌려서
#     day=day+arrlist[i]                                  >> 일 수를 다 day 에 더해줌
# day=(day+y)%7                                           >> day 에 y 더해서 7로 나눈 나머지
# print(weekday[day])                                     >> 요일리스트에서 인덱싱으로 찾음

        
m,d=map(int,input().split())
mlist=(31,28,31,30,31,30,31,31,30,31,30,31)
weekday=("SUN","MON","TUE","WED","THU","FRI","SAT")
maddtotal=0
for i in range(0,m-1):
    maddtotal+=mlist[i]
print(weekday[(maddtotal+d)%7])
