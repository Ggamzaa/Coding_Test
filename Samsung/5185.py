answer = {
    "0" : "0000", "1" : "0001", "2" :  "0010", "3" : "0011", "4" : "0100", "5" : "0101", "6" : "0110", "7" : "0111", "8" : "1000",
    "9" : "1001", "A" : "1010", "B" : "1011", "C" : "1100", "D" : "1101", "E" : "1110", "F" : "1111"}
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    n , oxg= map(str,input().split())
    ans = f"#{test_case} "

    # range는 0 부터 n-1까지 순환 n 포함X
    for i in range(0,(int(n))):
        ans += answer[oxg[i]]
        
    print(ans)