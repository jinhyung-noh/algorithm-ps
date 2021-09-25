# def solution(w, h):
#     from math import ceil, gcd

#     w, h = min(w, h), max(w, h)
#     _gcd = gcd(w, h)
#     m = ceil(h / w)
    
#     return w * h - _gcd * (m * int(w / _gcd))


def solution(w, h):
    from math import gcd
    return w * h - (w + h - gcd(w, h))

print(solution(8, 12))