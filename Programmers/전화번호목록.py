def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for idx in range(len(phone_book)-1):
        if phone_book[idx+1].startswith(phone_book[idx]):
            answer = False
        
    return answer