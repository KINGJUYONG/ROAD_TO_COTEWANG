
def solution(s):
    ans = 0
    
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    #3 4 5
    for i in range(len(s)):
        if s[i].isdigit():
            ans *= 10
            ans += int(s[i])
            continue
        else: #문자일때
            breaks = 0
            for k in range(3, 6): #3 ~ 5자리까지 찾음
                if breaks != 0:
                    break
                for q in range(10):
                    if words[q] == s[i:i+k]:
                        ans *= 10
                        ans += q
                        i += k
                        breaks = 1
                        break

    return ans
