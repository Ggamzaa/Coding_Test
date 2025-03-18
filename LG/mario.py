raw_input = """
        8
        7 2 1 8 4 3 5 6
        """

n = int(input())
print(n)

numbers = list(map(int, input().split()))
print(numbers)

eat = 0
# 언제 안먹을지 어떻게 결정??
# 일단 첫번째는 먹어야 하나?


for i in numbers:
    print(i)