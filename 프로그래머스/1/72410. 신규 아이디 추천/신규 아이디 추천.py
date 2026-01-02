import re

def solution(new_id):
    # 1단계: 소문자화
    new_id = new_id.lower()
    
    # 2단계: 특수문자 제거
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    
    # 3단계: 연속 마침표 처리
    new_id = re.sub(r'\.{2,}', '.', new_id)
    
    # 4단계: 양 끝 마침표 제거
    new_id = new_id.strip('.')
    
    # 5단계: 빈 문자열 처리
    if len(new_id) == 0:
        new_id = 'a'
        
    # 6단계: 길이 제한
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')
    
    # 7단계: 길이 보충
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
            
    return new_id
