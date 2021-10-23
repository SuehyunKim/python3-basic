n = int(input("정수를 입력하세요.:"))

def sum(n):
    """0부터 입력받은 값까지의 합을 계산하는 함수입니다."""
    s = 0
    for x in range (0,n+1):
        s += x
    return s

print(sum(n))
