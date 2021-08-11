import sys




pos = [0] * 8           # pos[i]: position of queen of i-th column (0..i..7)
flags = [False] * 8     # flags[j]: whether queen is in j-th row (0..j..7)
flags_b = [False] * 15  # whether queen is in /// way
flags_c = [False] * 15  # whether queen is in \\\ way

def put() -> None:
    """print position of all queens"""
    for i in range(8):
        print(f"{pos[i]:2}", end="")
    print()

def set(i: int) -> None:
    """set i-th column"""
    for j in range(8):
        if not flags[j]          \
            and not flags_b[i+j] \
            and not flags_c[i-j+7]:
            pos[i] = j      # place a queen in j-th row
            if i == 7:      # last element --> print all queens
                put()
            else:
                flags[j] = flags_b[i+j] = flags_c[i-j+7] = True    # mark that queen is in j-th row
                set(i+1)
                flags[j] = flags_b[i+j] = flags_c[i-j+7] = False    # mark that queen is in j-th row

set(0)
