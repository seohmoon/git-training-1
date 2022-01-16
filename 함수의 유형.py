#함수의 유형
# 1) 매개변수와 반환 값이 있는 함수
def func_parameters_return(x, y, z): #이 함수 호출 시 매개변수(x, y, z)에 인자 값 전달
    print("매개변수로 전달된 값은{0}, {1},{2} 입니다.".format(x, y, z))
    print("매개변수와 반환값이 있는 함수입니다.")
    return "Hello, Python!" #func_parameters_return()함수를 호출한 위치에 반환 값으로 전달

ret_val = func_parameters_return(1, 2, 3)
print("func_parameters_return() 함수가 반환한 값: {0}".format(ret_val))

"""
[결과]
매개변수로 전달된 값은 1, 2, 3 입니다.
매개변수와 반환값이 있는 함수입니다.
func_parameters_return() 함수가 반환한 값: Hello Python!
"""

# 2) 매개변수는 없고, 반환 값이 있는 함수
def func_noparameters_return(): #매개변수가 없어서 괄호만 입력
    print("매개변수가 없는 함수입니다.") #문자열 출력
    return "Hello, Python!" #func_noparameters_return()함수를 호출한 위치에 반환 값으로 전달

ret_val = func_noparameters_return()
print("func_noparameters_return() 함수가 반환한 값: {0}".format(ret_val))

"""
[결과]
매개변수가 없는 함수입니다.
func_noparameters_return() 함수가 반환한 값: Hello Python!
"""

# 3) 매개변수는 있고 반환 값이 없는 함수
def func_parameters_noreturn(x, y, z): #이 함수 호출 시 매개변수(x, y, z)에 인자 값 전달
    print("매개변수로 전달된 값은{0}, {1}, {2} 입니다.".format(x, y, z))
    print("반환값이 없는 함수입니다.")

func_parameters_noreturn(1, 2, 3)

"""
[결과]
매개변수로 전달된 값은 1, 2, 3 입니다.
반환값이 없는 함수입니다.
"""

# 4) 매개변수와 반환 값이 없는 함수
def func_noparameters_noreturn(): #매개변수가 없어서 괄호만 입력
    print("매개변수가 없는 함수입니다.") #문자열 출력

func_noparameters_noreturn()

"""
[결과]
매개변수와 반환 값이 없는 함수입니다.
"""