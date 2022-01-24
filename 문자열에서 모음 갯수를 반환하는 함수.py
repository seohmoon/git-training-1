#문자열에서 모음 갯수를 반환하는 함수
from itertools import count
from unittest import result


def count_vowels(x):
    a = x.count('a')
    e = x.count('e')
    i = x.count('i')
    o = x.count('o')
    u = x.count('u')
    sum_vowels = a + e + i + o + u
    
    return(sum_vowels)

print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3



#평균점수 구하기
def get_dict_avg(x):
    score = x.values()
    sum_scores = 0
    cnt_subject = 0
    for i in score:
        sum_scores += i
        cnt_subject += 1
    return(sum_scores/cnt_subject)
    

get_dict_avg({
'python': 80,
'algorithm': 90,
'django': 89,
'web': 83,
}) #=> 85.5


#####
#혈액형 분류하기
def count_blood(x):
    a = x.count('A')
    b = x.count('B')
    o = x.count('O')
    ab = x.count('AB')
    
    result = {
        'A': a, 'B': b, 'O': o, 'AB': ab
    }
    
    return(result)

count_blood([
'A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB',
]) #=> {'A': 3, 'B': 3, 'O': 3, 'AB': 3 }



"""
#정사각형만 만들기

def only_square_area(a, b):
    
    result = []
    for i in a:
        for j in b:
            if i == j:
                result.append(i * j)

    print(result)
    return(result)

    only_square_area([32, 55, 63], [13, 32, 40, 55])
#=> [1024, 3025]
"""

def only_square_area(*x):
    print(x)
    result = []
    for i in x[0]:
        for j in x[1]:
            if i == j:
                result.append(i * j)
    print(result)
    return(result)

only_square_area([32, 55, 63], [13, 32, 40, 55])
#=> [1024, 3025]