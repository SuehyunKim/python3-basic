t1 = float(input("첫 번째 과목의 점수를 입력하세요.:"))
t2 = float(input("두 번째 과목의 점수를 입력하세요.:"))
t3 = float(input("세 번째 과목의 점수를 입력하세요.:"))

total = t1 + t2 + t3
avg = total/3

if avg >= 50:
    print("평균점수는", round(avg,3), "점으로 합격입니다.", sep="")
else:
    print("평균점수는", round(avg,3), "점으로 불합격입니다.", sep="")