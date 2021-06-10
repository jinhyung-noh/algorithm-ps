a = range(10)
i=3
n = 1
while True:
    try:
        print(a[i-n], a[i+n])
        n += 1

    except IndexError:
        print("IndexError")
        break