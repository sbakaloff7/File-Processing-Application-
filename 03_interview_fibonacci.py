def FibNSeq(n):
    if type(n) != int:
        raise TypeError('n must be a positive int')
    if n == 1:
        return 1
    elif n > 2:
        return FibNSeq(n - 1) + FibNSeq(n - 2)


for n in range(1, 10):
    print(FibNSeq(n))
