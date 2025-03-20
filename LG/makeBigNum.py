
number ="1924"
k = "2"
result=""

# num_list = [map(int,number.split())]
num_list = list(map(int, number))

num_list.sort(reverse=True)

for i in range(int(k)):
    result += str(num_list[i])

print(result)

