def calc_sum(x, y): #매개변수에 인자값 전달 
    return x + y #calc_sum() 함수를 호출한 위치에 반환 값이 전달 됨

a, b = 2,3

c = calc_sum(a, b) #반환값 5가 변수 c에 저장
d = calc_sum(a, c) #반환값 7가 변수 c에 저장

print("사용자 정의 함수 calc_sum() 호출을 이용한 c의 결과: {0}".format(c))
print("사용자 정의 함수 calc_sum() 호출을 이용한 c의 결과: {0}".format(d))

#언팩 연산자를 사용하는 튜플 형식의 가변 매개변수
def calc_sum(*params): #매개변수에 인자값들이 튜플 형식으로 전달 
    total = 0
    for val in parmas:
        total += val #개별 인자값 누적
    return total #변수 total의 값이 calc_sum() 함수를 호출한 위치에 반환 값으로 전달 됨

ret_val = calc_sum(1, 2) # 1,2가 인자로 전달되어 for문이 2번 반복, calc_sum() 함수는 수행 결과로 3 반환
print("calc_sum(1, 2) 함수가 반환한 값: {0}".format(ret_val))
#"calc_sum(1, 2) 함수가 반환한 값: 3 출력

ret_val = calc_sum(1, 2, 3)  # 1,2, 3이 인자로 전달되어 for문이 3번 반복, 결과로 6 반환
print("calc_sum(1, 2, 3) 함수가 반환한 값: {0}".format(ret_val))

"""
[결과]
calc_sum(1, 2) 함수가 반환한 값: 3
calc_sum(1, 2, 3) 함수가 반환한 값: 6
"""

#명시적 매개변수와 가변 매개변수의 혼합 사용
def calc_sum(precision, *params):#함수 호출시 첫 번째 매개변수 precision에 인자 값이 가장 먼저 전달되고
    #나머지 인자 값들이 params 매개변수에 튜플 형식으로 전달
    if precision == 0:
        total = 0 #정수 0으로 초기화
    elif 0 < precision < 1:
        total = 0.0 #부동 소수점 0.0으로 초기화

    for val in parmas: # 매개변수 params가 1과 2를 가진 튜플이므로 for문이 2번 반복
        total += val #개별 인자값 누적
    return total #변수 total의 값이 calc_sum() 함수를 호출한 위치에 반환 값으로 전달 됨

ret_val = calc_sum(0, 1, 2)  # 결과로 3 반환
print("calc_sum(0, 1, 2) 함수가 반환한 값: {0}".format(ret_val))

ret_val = calc_sum(0.1, 1, 2)  #정수 0.0으로 초기화 됨, 결과로 3.0 반환
print("calc_sum(0.1, 1, 2) 함수가 반환한 값: {0}".format(ret_val))

"""
calc_sum(0, 1, 2) 함수가 반환한 값: 3
calc_sum(0.1, 1, 2) 함수가 반환한 값: 3.0
"""

#언팩 연산자를 사용하는 튜플 형식의 반환값
def calc_sum(precision1, precision2, *params):
    if precision1 == 0:
        total1 = 0 #정수 0으로 초기화
    elif 0 < precision1 < 1:
        total1 = 0.0 #부동 소수점 0.0으로 초기화

    if precision2 == 0:
        total2 = 0 #정수 0으로 초기화
    elif 0 < precision2 < 1:
        total2 = 0.0 #부동 소수점 0.0으로 초기화
    
    for val in parmas: 
        total1 += val #개별 인자값 누적
        total2 += val
    return total1, total2 #튜플을 반환해서 하나 이상의 값을 반환할 수 있음
ret_val = calc_sum(0, 0.1, 1, 2)  #매개변수 precision1,precision2, params순서 튜플 (3, 3.0) 반환
print("calc_sum(0, 0.1, 1, 2) 함수가 반환한 값: {0}, {1}".format(*ret_val)) 
#인자의 값은 여러 인자로 분리하기 위해 언팩연산자 사용함
print("calc_sum(0, 0.1, 1, 2) 함수가 반환한 값: {0}, {1}".format(ret_val[0], ret_val[1]))
#튜플의 개별 원소를 인덱스로 접근해 처리
""""
[결과]
calc_sum(0, 0.1, 1, 2) 함수가 반환한 값: 3, 3.0
calc_sum(0, 0.1, 1, 2) 함수가 반환한 값: 3, 3.0
"""

d



