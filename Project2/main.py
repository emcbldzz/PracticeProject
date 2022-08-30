# This is a sample Python script.
from Student import Student
# https://www.pythontutorial.net/python-basics/python-read-text-file/
if __name__ == '__main__':
    # with open('scores.txt', 'r') as f:
    #     print('---------using read, all content, one string-------------')
    #     contents = f.read()
    #     print(contents)
    #
    # with open('scores.txt', 'r') as f:
    #     print ('---------using readlines, returns the file contents as a list of strings:-------------')
    #     [print(line) for line in f.readlines()]
    #
    counter = 1
    student_list = []
    with open('scores.txt', 'r') as f:
        print('---------using readline, read the file line by line -------------')
        while True:
            # student_x = Student()
            line = f.readline()
            if not line:
                break
            s = line.strip().split(',')
            student_list.append(Student(s[0], int(s[1]), s[2]))

    # with open('scores.txt', 'r') as f:
    #     print('---------concise way,reading the file object, which is an iterable object, looks similar to readlines-------------')
    #     for line in f:
    #         print(line.strip())

    total_score = 0
    avg_score = 0
    max_score = 0
    min_score = 100
    median_score = 0
    student_cnt = 0
    for s in student_list:
        total_score += s.score
        student_cnt += 1
        max_score = max(s.score, max_score)
        min_score = min(s.score, min_score)

    if student_cnt > 0:
        avg_score = total_score/student_cnt

    if student_cnt % 2 == 0:
        median_score = (student_list[student_cnt//2 - 1].score + student_list[student_cnt//2].score)/2
    elif student_cnt % 2 == 1:
        median_score = student_list[student_cnt//2].score


    print("----student report----")
    print(f'''\ttotal_score={total_score}
    max_score={max_score}
    min_score={min_score}
    avg_score={round(avg_score,1)}
    median_score={median_score}''')


    with open("score_report.txt", "w") as o:
        o.write('\t----student report----')
        o.write(f'''
        total_score={total_score}
        max_score={max_score}
        min_score={min_score}
        avg_score={round(avg_score,1)}
        median_score={median_score}''')