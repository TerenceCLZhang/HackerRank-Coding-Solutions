def find_second_lowest(arr):
    sorted_array = sorted(arr)
    return sorted_array[1]


if __name__ == '__main__':
    score_name_dict = {}
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in score_name_dict:
            score_name_dict[score].append(name)
        else:
            score_name_dict[score] = [name]
            scores.append(score)
    
    second_lowest_grade = find_second_lowest(scores)
    second_lowest_grades_names = sorted(score_name_dict[second_lowest_grade])
    for name in second_lowest_grades_names:
        print(name)
