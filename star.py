def calc_sum(x, y): #매개변수에 인자값 전달 
    return x + y #calc_sum() 함수를 호출한 위치에 반환 값이 전달 됨

a, b = 2,3

c = calc_sum(a, b) #반환값 5가 변수 c에 저장
d = calc_sum(a, c) #반환값 7가 변수 c에 저장

print("사용자 정의 함수 calc_sum() 호출을 이용한 c의 결과: {0}".format(c))
print("사용자 정의 함수 calc_sum() 호출을 이용한 c의 결과: {0}".format(d))
