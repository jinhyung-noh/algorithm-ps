def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    new_id = ''.join(char for char in new_id if char in 'abcdefghijklmnopqrstuvwxyz0123456789-_.')
    # 3
    while ('..' in new_id):
        new_id = new_id.replace('..','.')
    # 4
    while new_id !='' and new_id[0] == '.':
        new_id = new_id.lstrip('.')
    while new_id != '' and new_id[-1] == '.':
        new_id = new_id.rstrip('.')
    # 5
    if new_id == '':
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]          
        while (new_id != '' and new_id[-1] == '.'):
            new_id = new_id.rstrip('.')
    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id
