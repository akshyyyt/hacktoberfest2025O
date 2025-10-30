# Your code here
n, m, a = map(int, input().split())

if n%a == 0 and m%a == 0:
    print((n//a)*(m//a))
elif n%a !=0 and m%a == 0:
    tileHor = n/a
    tileHor = int(tileHor)+1

    print(tileHor*(m//a))
elif n%a == 0 and m%a != 0:
    tileVer = m/a
    tileVer = int(tileVer)+1

    print((n//a)*tileVer)
else:
    tileHor = n/a
    tileHor = int(tileHor)+1

    tileVer = m/a
    tileVer = int(tileVer)+1

    print(tileHor*tileVer)
