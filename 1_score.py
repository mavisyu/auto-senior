score = ['35', 46, '57', 91, '29']
correct_score_list = []

for index, x in enumerate(score):
  correct_score = str(score[index])[::-1]
  correct_score_list.append(correct_score)
print(correct_score_list)