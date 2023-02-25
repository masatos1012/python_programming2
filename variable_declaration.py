"""
変数宣言と出力
変数を宣言する方法を記述する
関数変数命名規則はスネークケース
小文字_小文字
"""


def vd_call():
    print('#################↓変数宣言↓################')
    num = 2
    print(num, type(num))
    name = 'Mike'
    print(name)
    print('Hi', name)
    # 区切り文字を指定
    print('Hi', name, sep=',')
    # 終端文字を指定
    print('Hi', name, sep=',', end='\n')
    print('Hi', name, sep=',', end='.\n')

    print('#################↑変数宣言↑################')

# デバッグ用
# vd_call()
