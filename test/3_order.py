n = int(input('請輸入n值(0-100):'))
num = []
for i in range(n):
    num.append(i + 1)

i = 0
k = 0
m = 0

while m < n - 1:
    if num[i] != 0:
        # print(f'{num[i]} != 0')
        k += 1
    if k == 3:
        # print(f'{num[i]} -> 3')
        num[i] = 0
        k = 0
        m += 1
        # print(f'm = {m}')
    i += 1
    if i == n:
        i = 0

i = 0

if n == 0:
    print(f'沒有人')
else:
    while num[i] == 0:
        i += 1
    print(f'第 {num[i]} 順位')