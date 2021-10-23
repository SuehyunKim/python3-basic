li = []

for i in range(7):
    num = int(input("정수를 입력해주세요.:"))
    li.append(num) #리스트 값 순차적으로 추가

avg = sum(li)/len(li)
print("평균:",avg)li = []