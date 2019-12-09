def s1(n):
    output = 0
    for y in range(1, n+1):
        output += y
    return output
def s2(n):
    output = 0
    for y in range(1, n+1):
        output += (y * y)
    return output
def s3(n):
    numerator = 3 * s2(n)
    denominator = s1(n)
    return numerator//denominator
for x in range(1, 21):
    print('{0:3d} {1:6d} {2:9d} {3:12d}'.format(x, s1(x), s2(x), s3(x)))
