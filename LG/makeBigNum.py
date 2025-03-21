from itertools import combinations

number ="1924"
k = "2"
result=""

# num_list = [map(int,number.split())]
num_list = list(map(int, number))

num_list.sort(reverse=True)

# 어떻게 k개씩 빼는 것을 구현할 수 있을까??
# for i in range(int(k)):
#     result += str(num_list[i])
result_list=[]
for remove_indices in combinations(range(len(num_list)), int(k)):
    result = ''.join(str(num_list[i]) for i in range(len(num_list)) if i not in remove_indices)
    result_list.append(result)
result_list.sort(reverse=True)

print(result_list)

