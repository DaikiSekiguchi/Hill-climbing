# coding: utf-8

import random

"""
y = 3x^4 − 5^3 + 2^2 の最小値を求める
"""


def hill_climbing(max_count, step):
    x = random.uniform(-1, 1)
    print("start_x: {0}".format(x))

    count = 0
    cost = calc_cost(x)

    while count < max_count:

        # x軸の+方向か-方向どちらに移動するかを選択する
        direction = random.randint(0, 1)  # 0であれば-方向、1であれば+方向にstepの値だけ移動する

        if direction == 0:
            direction = - step
        else:
            direction = step

        # 移動後のxの値を求める
        new_x = x + direction

        # 移動後のコストを計算する
        new_cost = calc_cost(new_x)

        # 移動前と移動後のコスト(yの値)を比較し、コストが低ければ更新する
        if new_cost < cost:
            x = new_x

        # 変数を更新
        count += 1

    print("final_x: {0}".format(round(x, 1)))
    print("y: {0}".format(calc_cost(x)))


def calc_cost(x):
    return (3 * (x ** 4)) - (5 * (x ** 3)) + (2 * (x ** 2))


# main
if __name__ == "__main__":
    hill_climbing(5000, 0.01)
