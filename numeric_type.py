"""
 数値
"""


def numeric_type():
    print('#################↓数値↓###################')
    # 簡単な乗除
    a = 2 + 2
    print(a)

    # 変数と数字の組み合わせ
    b = a + 4
    print(b)

    # 変数と変数の組み合わせ
    c = a + b
    print(c)

    # 商 除算は常に浮動点少数を返す
    # Typeはfloatとなる
    d = 15 / 3
    print(d, type(d))

    # 式の評価順は乗除>足し引き
    e = (50 - 5 * 6)
    print(e)

    # 変数と数値の組み合わせ
    f = e / 4
    print(f)

    # 商の整数部のみを出力
    g = 20 // 3
    print(g)

    # 割ったあまり(剰余)を求めたい場合
    h = 17 % 3
    print(h)

    # べき乗5を2回かける
    i = 5 ** 2
    print(i)

    # 変数同士の計算
    j = a + b + (c + d) * e + f * g
    print(j, type(j))

    # ラウンド関数(丸め)
    pie = 3.1415926
    print(round(pie, 2))

    import math

    # 平方根を求める
    result = math.sqrt(25)
    print(result)

    # print(help(math))

    print('#################↑数値↑#####################')


# デバッグ用
numeric_type()
