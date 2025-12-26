N, K = map(int, input().split()) ## N 과 K를 받기 위한 변수 
people = list(range(1, N+1)) ## N 사람수에 맞춰 배열 요소 세팅
result = [] ## 결과를 집어 넣기 위한 배열 선언
idx = 0 ## 제거 해야 되는 위치를 계산하는 변수

while people: ## 이 배열이 거짓이될때까지(빌때까지)반복
    idx = (idx + (K-1))%len(people) ## k-1 이 첫번째 원하는 번째, 제거하고 나서 배열의 길이가 변함,이후 idx에 저장해서 그 이후 길이 계산,  %연산자로 나머지를 계산해서 배열의 길이를 초과하는 만큼을 계산 할 수 있음
    result.append(str(people.pop(idx))) ## 제거한 사람을 넣어주는 역할 str로 저장해야 join함수에서 사용가능
    
print("<"+", ".join(result)+ ">") ## join함수를 사용해서 깔끔하게 출력 for문을 사용해서 하나하나 검사해서 마지막은 ,를 안넣게 할 수 있는데 시간초과 날꺼 같아서