# B.py
dices = [list(map(int,input().split(" "))) for _ in range(3)]

ans = 0.0
dice_per_4 = list()
dice_per_5 = list()
dice_per_6 = list()

for i in range(3):
    dice = dices[i]
    dice_median_count_4 = 0
    dice_median_count_5 = 0
    dice_median_count_6 = 0
    for j in range(6):
        if dice[j] == 4:
            dice_median_count_4 += 1
        elif dice[j] == 5:
            dice_median_count_5 += 1
        elif dice[j] == 6:
            dice_median_count_6 += 1
    dice_per_4.append(dice_median_count_4 / 6)
    dice_per_5.append(dice_median_count_5 / 6)
    dice_per_6.append(dice_median_count_6 / 6)

for j in range(3):
    ans += dice_per_4[j] * dice_per_5[j % 2] * dice_per_6[j % 3]
    ans += dice_per_4[j] * dice_per_5[j % 3] * dice_per_6[j % 2]

ans = round(ans, 6)
print(ans)