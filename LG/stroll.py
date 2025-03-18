import psutil
raw_input = """5 3
0 1
1 2
2 3
3 2
6 1"""

first_line = list(map(int, raw_input.splitlines()[0].split()))

# 나머지 줄들은 공백으로 나누어 숫자로 변환
remaining_lines = [list(map(int, line.split())) for line in raw_input.splitlines()[1:]]


result = []
split = 0
# 입력된 데이터를 출력
t=3
result.append(remaining_lines[0][0]+remaining_lines[0][1]*t)
for item in remaining_lines[1:]:
    num1 = int(item[0])  # 첫 번째 값
    num2 = int(item[1])  # 두 번째 값
    print(num1, num2)
    print(result[-1])
    if result[-1] >num1 + (num2 * t):
        result[-1] = num1 + (num2 * t)
        result.append(num1 + (num2 * t))
    else:
        result.append(num1 + (num2 * t))
        split += 1
    
# result.sort()
print(result)
print(split)

# 메모리 사용량 체크
process = psutil.Process()
memory_info = process.memory_info()
print(f"\n메모리 사용량: {memory_info.rss / 1024 / 1024:.2f} MB")
    