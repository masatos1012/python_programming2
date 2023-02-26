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


"""
 関数内関数(inner function) 関数の中での呼び出しが局所的(限定的)な場合に有効
 クロージャ　関数内関数の高度版　関数終了後もローカル変数を参照できる特徴。これによって同様の記載でグローバル関数の現象、計算量の削減が可能
 デコレーターについて


"""


# 2.innner_function呼び出し
def innner_function(a, b):
    print('#################↓関数内関数↓################')

    # 4.plus実行。returnにて結果を返却
    def vd_plus(c, d):
        return c + d

    # 3.vd_plus呼び出し。ここでinnner_functionで読み込んだ引数をplusに引き渡し
    i = vd_plus(a, b)
    i2 = vd_plus(b, a)
    print('i + i2 ={}'.format(i + i2))
    print('#################↑関数内関数↑################')


def closuer(e, f):
    print('#################↓クロージャ1↓################')

    def inner():
        return e + f

    # ()をつけずにreturnすることで実行されずオブジェクトの情報を引き渡しする(待機）的な
    return inner


# 1.呼び出し。返り値としてinnnerのオブジェクト情報を返す
#   innner_functionに渡した値はまだinnerへ渡されていない。
g = closuer(1, 3)
print("returnでオブジェクト返却されているので実行されず\n"
      "オブジェクト情報のみが返却される\n", g)

# 2.gに代入したinnner_functionを()をつけることで実行できる。

h = g()
print("呼び出し１回目", h)
print("呼び出し2回目", g())

j = closuer(2, 2)
print(j())
print('#################↑クロージャ1↑################')

# クロージャの使用例
# 円周率の計算、πの定義について複数定義し、呼び出された際に使用する値を変更できる。


# 2.circle_area_func呼び出し
print('#################↓クロージャ2↓################')


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    # 3.circle_areaオブジェクトの返還
    return circle_area


# 1.呼び出し
cal = circle_area_func(3.14)
cal2 = circle_area_func(3)
print('calの利用円周率は3.14\n', cal(10))
print('calの利用円周率は3\n', cal2(10))
print('#################↑クロージャ2↑################')

print('#################↓デコレーター↓################')


# 4.デコレータ2番目の呼び出し
def print_more(func):
    def wrapper(*args, **kwargs):
        print('-----オブジェクトの情報を出力------')
        print('func:', func)  # ・・・2
        print('args:', args)
        print('kwargs:', kwargs)
        print('-----オブジェクト出力ここまで------')
        # 4-1.resultに
        result = func(*args, **kwargs)
        print('result:', result)
        return result

    return wrapper


# 3.デコレータ最初の呼び出し
def print_info(func):
    def wrapper(*args, **kwargs):
        print('-----print_info内のオブジェクト情報------')
        print('func:', func)
        print('args:', args)
        print('kwargs:', kwargs)
        print('start')
        print('-----print_info内のオブジェクト情報ここまで------')
        # 3-1.↑ここまで実行、resultに入ると次のデコレータへ
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper


# @をつけた順に関数の中に入っていく
# add_numをデコレートしている為呼び出し直後、
# 上から順番に処理される
@print_info
@print_more
def add_num(a, b):
    return a + b


# 1.関数呼び出し
k = add_num(10, 20)
print(k)
print('#################↑デコレータ↑################')
# デバッグ用
# vd_call()
# innner_function(1, 5)
# closuer()
