ans = []
while True:
    input_str = input().rstrip()  # 문자열의 끝에서 공백을 제거
    if input_str == ".":
        break  # 마지막에 단독 온점이 입력되면 종료
    elif input_str.endswith("."):  # 마지막 문자가 온점인 경우
        input_str = input_str[:-1].rstrip()  # 온점 제거 및 끝의 공백 제거
        stack = []
        mapping = {')': '(', ']': '['}
        balanced = True
        
        for char in input_str:
            if char in mapping.values():  # 여는 괄호
                stack.append(char)
            elif char in mapping.keys():  # 닫는 괄호
                if not stack or stack.pop() != mapping[char]:
                    balanced = False
                    break
        
        if balanced and not stack:  # 괄호가 균형 잡혀있고 스택이 비어있어야 함
            ans.append('yes')
        else:
            ans.append('no')
    else:
        ans.append('no')

for result in ans:
    print(result)
