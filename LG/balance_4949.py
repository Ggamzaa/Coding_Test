import sys

while True:
    # input
    string = input()
    if string == "." :
        break

    # 초기화
    stack = []
    no = False
    # print(string)

    # 글자 하나 하나 보기
    for s in string:
        if s == "[" or s == "(":
            stack.append(s)
        elif s == "]":
            if len(stack) == 0:
                no = True
                break
            a = stack.pop()
            if a != "[":
                no = True
                break
        elif s == ")":
            if len(stack) == 0:
                no = True
                break
            a = stack.pop()
            if a != "(":
                no = True
                break

    if len(stack) != 0 or no:
        print("no")
    else:
        print("yes")