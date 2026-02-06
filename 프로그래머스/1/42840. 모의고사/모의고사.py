def solution(answers):
    #수포자들의 점수
    p1 = 0
    p2 = 0
    p3 = 0
    #정답넣을 배열
    answer = []
    #수포자들이 찍는 규칙 배열
    p1List = [1,2,3,4,5]
    p2List = [2,1,2,3,2,4,2,5]
    p3List = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)): # 문제의 길이 만큼 반복
        if answers[i] == p1List[i%len(p1List)]: # i를 배열의 길이로 나눈 나머지를 이용해서 문제번호와 알맞은 찍는 곳을 찾음
            p1 +=1
        
        if answers[i] == p2List[i%len(p2List)]:
            p2 +=1
        
        if answers[i] == p3List[i%len(p3List)]:
            p3 +=1    
    
    max_score = max(p1, p2, p3)  # 같은 점수일 경우 오름차순 정렬 해야하기 때문에 최고점수찾기
    # 최고점수랑 같으면 p1부터 넣어서 오름차순으로 넣어지게 하기
    if p1 == max_score: answer.append(1) 
    if p2 == max_score: answer.append(2)
    if p3 == max_score: answer.append(3)
    
    return answer