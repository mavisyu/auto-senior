# score = ['35', 46, '57', 91, '29']
correct_score_list = []

print('Enter your score: ')
enter_score = input()
score = list(map(int,enter_score.lstrip('[').rstrip(']').split(',')))
print(f'wrong score is : {score}')

for index, x in enumerate(score):
    correct_score = str(score[index])[::-1]
    correct_score_list.append(correct_score)
print(f'correct score is : {correct_score_list}')