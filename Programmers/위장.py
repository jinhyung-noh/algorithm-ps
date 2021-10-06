def solution(clothes):
    from collections import defaultdict

    spi_clothes = defaultdict(list)

    for cloth, category in clothes:
        spi_clothes[category].append(cloth)


    answer = 1
    for category in spi_clothes:
        answer *= len(spi_clothes[category]) + 1

    return answer - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)
