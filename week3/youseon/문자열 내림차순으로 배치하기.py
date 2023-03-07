# 해당 파일은 구조를 위한 예시 파일입니다.
def solution(s):
    answer = ''
    upperArr = []
    lowerArr = []
    for alpha in s:
        print(alpha)
        if alpha.isupper(): 
            upperArr.append(alpha)
        else:
            lowerArr.append(alpha)
    lowerArr.sort(reverse=True)
    upperArr.sort(reverse=True)
    return ''.join(lowerArr)+''.join(upperArr)