if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    all = []
    number_of_subjects = 0
    for a in student_marks[query_name]:
        number_of_subjects += 1
        all.append(a)
        total = sum(all)

    average = total/number_of_subjects
    print(format(average, '.2f'))
