def get_map(arr1, map_1): 
    for num in arr1:
        bin_list = list(str(bin(num))[2:])
        map_1.append([0 for _ in range(len(arr1) - len(bin_list))] + bin_list)


def solution(n, arr1, arr2):
    answer = []
    map_1 = []
    map_2 = []
    get_map(arr1, map_1)
    get_map(arr2, map_2)
    for i in range(len(arr1)):
        wall = ''
        for j in range(len(arr1)):
            wall += '#' if (map_1[i][j] == '1' or map_2[i][j] == '1') else ' '
        answer.append(wall) 
    return answer
