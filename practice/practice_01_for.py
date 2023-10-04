# 문제1) 사용자가 입력한 단수를 출력하는 코드
# dan = int(input("단수: "))
# for i in range(1, 10):
#     print(f"{dan}x{i} = {dan*i}")

#  문제2) 2단에서 9단까지 출력(중첩 for문)
# for i in range(2, 10):                 # 단
#     for j in range(1, 10):             # 단수
#         print(f"{i} X {j} = {i*j}")

# 문제3) list a의 평균값을 계산하시오
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# a길이 => len(a)
print(len(a))
total = 0
for num in a:
    total += num #tortal = tortal + num
result = total/len(a)
# round(값, 자리수) : 자리수만큼 반올림
print(round(result, 2))

# 문제4) list b에서 최소값 찾기
b = [22, 1, 4, 7, 98]

print(num_min) # 1 출력