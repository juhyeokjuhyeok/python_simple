# 주석(comment): 메모의 역할. 실행X

#1. 출력함수(print)
#- ()안의 값을 출력
#변수값 확인용도로 많이 사용
print("=" * 200)
print("Hello Python")

#문자열 타입
# - Python: '' or "" -> String
# - C, Java: ''(char), ""(String)
print("=" * 200)
#참고: Escape code
# - 문법: \(역 슬러쉬) + @
# - 문자열(string) 내의 일부 문자의 의미를 달리하여 특정한 효과 주기
# - 예) \n: 한 줄 개행, \t: 탭(8칸 공백)
print("Hello \nPython")
print("Hello \tPython")

# 좋은 개발자!: 누구나 알아보기 쉽게 코드를 작성하는 사람
# 회사: 항상 신기술, 새로나온 기법을 사용하지는 않음
#과거기법, 새로운 기법의 공부가 필요
#영타 250~ 400타


#2. 자료형(type)

# - Python의 모든 자료형은 객체(object)
# - JAVA 정수형: byte, short, int, long
# - Python 정수형: int
# 1) 문자열(string): "Hello", 'Hi'
# 2) 정수형(int): 3, -1, 0
# 3) 실수형(float): 3.14, 0.0, -2.2
# 4) 논리형(boolean): True, False(T, F는 반드시 대문자)

# 설명: 동일한 Type에서 다양한 종류의 자료형을 사용하는 이유?
# - 메모리(저장공간)를 효율적으로 사용하기 위해서!
# - 대부분 만들어진지 오래 된 언어는 다양한 종류의 자료형 사용!
# - 자료형은 저장 할 수 있는 크기의 범위가 지정
# - 가정: int(-10000 ~ 10000)
# - 가정 short(-100 ~ 100)
# - 특정값: 0~9 -> 어떤 Type을 사용하면 효율적일까요? short

# 3. 동적 타이핑 언어(Dynamic Typing Language)
# - JAVA: int num = 4;
# - Python: num = 4(Type 지정 X)
# - 코드가 실행될 때 자동으로 Type을 지정
# - type() 함수: ()안의 값의 type을 확인할 때 사용 - 많이씀
print("=" * 200)
print(type("ABC"))
print(type(3.14))
print(type(5))

# 4.형변환(Type Casting)
# - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능
# - 1) int(): 정수형으로 변환
# - 2) float(): 실수형으로 변환
# - 3) str(): 문자열형으로 변환
print("=" * 200)
# "Hi" -> float(), int() 불가능
# 문자열 실수형"3.14" 가능
# 문자열 정수형 "5" 가능

int_a = 3
float_b = 3.14
str_inc_c = "9"
str_float_d = "9.2"

#큰자료형 -> 작은 자려형으로 변환할 때 주의!
# 정수형(3) -> 실수형(3.0)
print(float(int_a))
#정수형(3) -> 문자열("3");
# 실수형(3.14) -> 정수형(3) # 주의!(파일에 손실 생김)
#실수형(3.14) -> 문자열("3.14");
#문자열 정수형("3") -> 정수형(3)
#문자열 정수형("3") -> 실수형(3.0)
#문자열 실수형("3.14") -> 정수형(Error)
# print(int(str_float_d))
#문자열 실수형("3.14") -> 실수형(3.14)

# 5.None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초기값을 갖지 않게하려고 생성할 때 사용
# - 기타 언어의 NULL과 같은 의미로 사용
print("=" * 200)

# C, JAVA: 변수 생성 -> int num
#Python: 변수 생성 -> num(Error)
# Python: 변수 생성 -> num = None
student_name = None # 절대사용금지
student_name = "" # 적극권장

#"Null Pointer Exception"

# 기본 자료형(Primitive Type): 변수에 값이 그대로 저장
# - int num = 4;
# 객체 자료형(Reference Type): 변수에 값이 위치한 "주소"가 저장
# - String name = "10";

# - JAVA, C: 기본, 객체 둘다 사용
# - Python: 객체만 사용

# 6.변수(Variable)
# - 변수: 하나의 값을 저장할 수 있는 메모리 공간
print("=" * 200)
num = 4
num = 10
print(num) # 출력: 10

# - 변수 생성 및 초기화
# 문법: num = 5
# * num: "num" 변수 생성
# * 대입연산자(=): 우측의 값을 좌측에 저장
# 동등연산자(==): Equal
# * 초기화: 초기 변수를 생성하면 쓰레기 파일들이 존재
           변수에 값을 대입하면 공간이 초기화 되고 값만 저장!