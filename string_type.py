"""
文字列のまとめ
    文字列に関して
    文字列はimmutable(不変体)であり、インデックス指定での変更ができない
    書き換えをおこなう場合は、スライスを使用し新しい文字列の結合によって表現する
"""


def string_type():
    print(""" \
    ################　↓文字列↓　##################   
    """)
    print("'シングルクォートを出力する場合はダブルクォートで囲む'\n"
          "print('シングルクォート')\n"
          '"逆も叱り"')

    # エスケープ \
    print('dosen\'t')
    # もしくはダブクォートを使用
    print("doesn't")
    # 逆も叱り。シングルクォート囲み、ダブルクォート出力
    print('"Yes," They said.')
    # エスケープも使える
    print("\"Yes\", They said.")
    # 複合型　まとめ
    print('"Isn\'t,"They said.')
    # 文字列の書き換え
    word = 'Python'
    print(word)
    print('a' + word[1:2] + 'h' + word[2:4] + 'ooo' + word[4:5])
    print(''' \
    ################　↑文字列↑　##################   
    ''')


def string_new_line():
    """
    改行
    """
    print(""" \
    ################↓改行について↓##################   
    """)

    print(r'\nを使用することで改行として扱いになる。')
    print(r"記載方法→'First line.\nSecond line.↓出力'")
    s = 'First line.\nSecond line.'
    print(s)
    # 改行扱いになってしまう↓
    print('改行扱いになってしまう↓')
    print('C:\some\name')
    # こちらで解決(RAW文字列)
    print(r'C:some\name')
    # もしくは\\で記述
    print('C:some\\name')
    # 出力を複数行に分けたい場合
    print("""\
        Usage: thingy [options]
            -h          Display this usage message
            -H hostname Hostname to connect to
            """)

    # 文字列を繰り返し出力する
    print(3 * 'un' + 'ium')
    print('Py' 'thon')

    # 文字が長くなるとき
    s = 'aaaaaaaaaaaaaaa' \
        + 'bbbbbbbbbbbb'
    print(s)
    print('hoge\n' 
          'fuga')
    print(""" \
        ################↑改行について↑##################   
        """)


def stirng_slice():
    """
    文字列のインデックスとスライス
    []指定によって指定範囲、指定インデックスの文字列を取得できる
    """
    word = 'Python'
    # 通常
    print(word[0])
    # 終端からの指定
    print(word[-5])
    # インデックス範囲指定
    print(word[0:4])
    print(word[2:5])
    print(word[2:-1])
