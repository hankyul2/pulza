def solution(s):
    answer = ''
    digit_code = [
        ('zero', 0), ('one', 1), ('two', 2),
        ('three', 3), ('four', 4), ('five', 5),
        ('six', 6), ('seven', 7), ('eight', 8),
        ('nine', 9)
    ]

    s_len = len(s)
    idx = 0
    
    while idx < s_len:
        if s[idx].isdigit():
            answer += s[idx]
            idx += 1
        else:
            for code, num in digit_code:
                if s[idx:idx+len(code)] == code:
                    answer += str(num)
                    idx += len(code)
                    break

    return int(answer)



