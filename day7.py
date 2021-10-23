#1부터 100까지의 수 중에서 짝수이면서 7의 배수는 아닌 수 찾기

count = 0
for i in range(1,101):
    if i % 2 == 0:
        if i % 7 != 0:
            count += 1
print('1부터 100까지의 수 중에서 짝수이면서 7의 배수가 아닌 수의 개수:', count, '개', sep='')

print('')
#0이 입력될 때까지 숫자를 계속 입력받아 입력받은 숫자들의 합 구하기

sum = 0

while True:
    n = int(input('숫자를 입력하세요:'))

    if n != 0:
        sum += n
    else:
        break
print('total:', sum)