"""
特殊引数について
　　位置引数(a, b, c):(1, 2, 3)
　　キーワード引数(a='エー', b='ビー')
　　デフォルト引数(キーワード引数)と位置引数を併用する場合、
    位置引数の後に記述しないとエラー
　　*args: 複数の引数を「タプル」として受け取る
　　**kwargs: 複数の「キーワード引数」として受け取る
　　慣例として*args, **kwargsという名前が使われることが多いが、*と**が頭についていれば他の名前でも問題ない。
"""


# 標準型
def standard_arg(arg):
    print(arg)


print('標準型')
standard_arg(2)

print('標準型2')
standard_arg(arg=2)


# 引数に/が入る場合、位置引数「しか」使えない
def pos_only_arg(arg, /):
    print(arg)


print('位置引数限定')
pos_only_arg(1)

# トレースバック出力例
# キーワード引数の使用
# pos_only_args(args=1)
"""
Traceback (most recent call last):
  File '"C:\\Users\\masat\\Documents\\python_programming\\special_argument.py", line 26, in <module>'
    pos_only_arg(arg= 1)
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
訳：TypeError: pos_only_arg() は、キーワード引数として渡されたいくつかの位置のみの引数を取得しました: 'arg'
"""


# 複数の引数の場合、/より左側が位置引数のみ、それより右側はキーワード引数も使える
def pos_only_arg2(arg, b, c, /, d):
    print(arg, b, c)


pos_only_arg2(1, 2, 3, d=4)


# キーワード引数しか受け取れない
def kwd_only_arg(*, arg):
    print('(*, arg)', arg)


kwd_only_arg(arg=3)
# トレースバック出力例
# 位置引数での呼び出し
# kwd_only_arg(3)
"""
  File "C:\\Users\\masat\\Documents\\python_programming\\special_argument.py", line 33
       ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 46-47: truncated \\UXXXXXXXX escape
"""


# 複合型
# /より左側は位置引数、*より右側はキーワード引数のみを許容する
def combinated_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# (位置引数, /, 位置引数, *, キーワード引数)
combinated_example(1, 2, kwd_only=3)
# (位置引数, /, キーワード引数, *, キーワード引数)
combinated_example(1, standard=2, kwd_only=3)

# トレースバック出力例(位置引数のみでの呼び出し)
# combinated_example(1, 2, 3)
"""
Traceback (most recent call last):
  File "C:\\Users\\masat\\Documents\\python_programming\\special_argument.py", line 43, in <module>
    combinated_example(1, 2, 3)
TypeError: combinated_example() takes 2 positional arguments but 3 were given

"""

# トレースバック出力例(キーワード引数のみでの呼び出し)
# combinated_example(pos_only=1, standard=2, kwd_only=3)
"""
Traceback (most recent call last):
  File "C:\\Users\\masat\\Documents\\python_programming\\special_argument.py", line 55, in <module>
    combinated_example(pos_only=1, standard=2, kwd_only=3)
TypeError: combinated_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
"""


# kwdsのタプルを出力
# 「**kwargs」のデータ型は可変長の辞書型（dictionary）になる
def foo(name, **kwds):
    print('kwargs:', kwds)
    print('kwargs:', type(kwds))
    for i in kwds:
        result = i
        print(i)
    return 'name' in kwds


foo('aaaa', bbb='bbb', ccc='ccc')
