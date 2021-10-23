def FindMax(a):
    max = 0
    for i in range(1,len(a)):
        if a[i] > a[max]:
            max = i
    return max

my_lst = [8,15,4,23,7,11,2,19,6,10]
print("Max =", FindMax(my_lst))
