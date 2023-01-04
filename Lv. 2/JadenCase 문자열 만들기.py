def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
        
    answer = ' '.join(s)
    
    return answer;
    
# https://school.programmers.co.kr/learn/courses/30/lessons/12951
