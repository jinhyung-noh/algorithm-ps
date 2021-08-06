import sys

year = int(sys.stdin.readline())


if year % 400 == 0:
    print(1)
elif year % 100 == 0:
    print(0)
elif year % 4 == 0:
    print(1)
else:
    print(0)



# another way

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:     # 윤년 (400 배수)
#             print(1)
#         else:                   # 윤년 아님 (100 배수)
#             print(0)

#     else:   # 윤년 (4배수이면서 100배수 아님)
#         print(1)

# else:       # 윤년 아님 (4배수 아님)
#     print(0)