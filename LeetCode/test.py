a = ['0', '1', '1', '0']

for ind  in range(len(a)): 
    a[3-ind] = 'x'
    print(a[ind])
