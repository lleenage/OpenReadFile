import os

def read_to_files(files):
    answer_list = []
    for file in files:
        if file.endswith(".txt"):
            with open(file, encoding='utf-8') as f:
                list_ans = []
                lines = f.readlines()
                lines_count = len(lines)
                ans = [lines_count, file, lines]
                list_ans.append(ans)
                answer_list.append(list_ans[0])
    answer = sorted(answer_list)

    with open('result.rtf', 'w', encoding='utf-8') as res:
        for i in answer:
            res.write(f'{i[1]}\n{i[0]}\n{''.join(i[2])}\n')

files = os.listdir()
read_to_files(files)