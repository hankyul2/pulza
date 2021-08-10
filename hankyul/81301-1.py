def solution(s):
    digit_code = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(digit_code)):
        s = s.replace(digit_code[i], str(i))

    return int(s)

if __name__ == '__main__':
    print(solution('four4five5'))
