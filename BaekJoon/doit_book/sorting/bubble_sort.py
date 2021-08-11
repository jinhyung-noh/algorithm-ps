def bubble_sort(seq):

    n = len(seq)
    for i in range(n-1):
        exchng = 0
        for j in range(n-1, i, -1):
            if seq[j-1] > seq[j]:
                seq[j-1], seq[j] = seq[j], seq[j-1]
                exchng += 1
        # no exchange in some "pass" --> sort completed!
        if exchng == 0:
            break

a = [1, 5,2,3,32,34,5,23,6,9]

bubble_sort(a)
print(a)