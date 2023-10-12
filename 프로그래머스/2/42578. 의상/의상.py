from math import prod
def solution(clothes):
    answer = 1
    cloth_dict = {}
    for i in clothes:
        if i[1] not in cloth_dict.keys():
            cloth_dict[i[1]] = 1
        else:
            cloth_dict[i[1]] += 1
    cloth_list = list(cloth_dict.values())
    for i,j in enumerate(cloth_list):
        cloth_list[i] = j+1
    if len(cloth_list) == 1 :
        answer = cloth_list[0] - 1
    else:
        answer = prod(cloth_list) - 1
    return answer