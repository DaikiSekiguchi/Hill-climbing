# coding: utf-8

import random
import copy

"""
y = 3x^4 − 5^3 + 2^2 の最小値を求める
"""


def hill_climbing(max_count, step):
    current_x = random.uniform(-1, 1)
    print("start_x: {0}".format(current_x))

    count = 0
    current_value = calc_value(current_x)

    while count < max_count:
        new_x1 = current_x - step  # x軸の－方向に進む
        new_x2 = current_x + step  # x軸の＋方向に進む

        temp_value1 = calc_value(new_x1)  # yの値(－に進んだ場合)
        temp_value2 = calc_value(new_x2)  # yの値(＋に進んだ場合)

        if temp_value1 < temp_value2:
            new_x = new_x1
            new_value = temp_value1
        else:
            new_x = new_x2
            new_value = temp_value2

        # 移動前と移動後のyの値を比較し、new_valueの値が現在の値(current_value)より低ければ値を更新する
        if new_value < current_value:
            current_x = new_x
            current_value = new_value

        # 変数を更新
        count += 1

    print("final_x: {0}".format(round(current_x, 2)))
    print("y: {0}".format(calc_value(round(current_x, 2))))


def calc_value(x):
    return (3 * (x ** 4)) - (5 * (x ** 3)) + (2 * (x ** 2))


# main
if __name__ == "__main__":
    hill_climbing(5000, 0.01)
