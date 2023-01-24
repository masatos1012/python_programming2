"""
リストの記述
リストはmutabLe(可変体なのでインデックスにて書き換えが可能)
スライスの使用も可能
# TODO　リスト(完了）　タプル　辞書型　集合
# TODO　内包表記の追記
"""


def data_structure_list():
    print(""" \
      ################　↓リスト↓　##################   
      """)

    # 配列(リスト)作成
    L = [0, 1, 2, 3, 4, 5, 6, 7]
    print('<標準リストの出力> L={}'.format(L))
    print('LのTypeを出力', type(L))
    print('"L[0]:{}"               ・・・インデックスは0から始まる'.format(L[0]))
    print('"L[:4]:{}"   ・・・0≦:<4'.format(L[:4]))
    print('"L[4:]:{}"   ・・・4≦:'.format(L[4:]))
    print('"L[2:6]:{}"  ・・・2≦:<6となる'.format(L[2:6]))
    print('"L[-1]:{}"              ・・・インデックス最後からの指定も可能'.format(L[-1]))

    # 文字列のリスト
    print("\n############################\n"
          "リスト型は文字列に対してもインデックスが使える\n"
          "List(文字列)と記載しリスト型へ変換できる\n"
          "文字列の置換に便利")
    print('############################')
    L2 = list('abcdrfghijk')
    print('<文字列リストの出力>\nL2= {}'.format(L2))
    print('"L2"(Type):', type(L2), '\n')
    print('"L2[3]:{}"           \
                           ・・・インデックスでの指定'.format(L2[3]))
    print('"L2[::2]:{}" ・・・２つ飛ばしで出力'.format(L2[::2]))
    print('"L2[1::2]:{}" \
          ・・・開始位置の変更。２つ飛ばしで出力'.format(L2[1::2]))
    print('"L2[::-2]:{}" ・・・終端から-２ずつ'.format(L2[::-2]))
    print('"L2[-1::-2]:{}" ・・・終端-1から-２ずつ(反転)'.format(L2[-1::-2]))

    # リストの結合
    print("\n############################\n"
          "リスト同士の結合も可能\n"
          '############################')
    L3 = ["a", "b", "c", "d", "e"]
    L4 = [1, 2, 3]
    L5 = [L3, L4]
    print('L3= {}'.format(L3))
    print('L4= {}'.format(L4))
    print('L5= {}'.format(L5))
    print("print(L5):", type(L5))
    print('')
    print('<左リストの出力>\nL5[0]= {}'.format(L5[0]))
    print('<右リストの出力>\nL5[1]= {}'.format(L5[1]))
    print('')
    print('<特定値の出力>\nL5[0][0]= {}'.format(L5[0][0]))
    print('L5[1][0]= {}'.format(L5[1][0]))
    print('L5[0][1]= {}'.format(L5[0][1]))
    print('<特定値,範囲指定の出力>\nL5[0][1:3]= {}'.format(L5[0][1:3]))
    print('L5[1][1:3]= {}'.format(L5[1][1:3]))

    # リストの操作
    print("\n############################\n"
          "リストの操作\n"
          '############################')
    L6 = ["a", "b", "c", "d", "e"]
    print('L6= {}'.format(L6))
    print('')
    L6.append(100)
    print('<値の追加 append>\nL6.append(100)= {}'.format(L6))
    L6.insert(1, 200)
    print('<値の追加 insert>記述：insert(inndex,value)\n'
          'L6.insert(1, 200)= {}'.format(L6))
    print('')
    L6.pop()
    print('<値の取り出し pop>\nL6.pop()= {}'.format(L6))
    L6.pop(0)
    print('<値の取り出し pop>\nL6.pop(0)= {}'.format(L6))
    print('')
    del L6[1]
    print('<値の削除 del>\ndel L6[1]= {}'.format(L6))
    # del L6[2]
    # L7 = L6
    L6.remove('c')
    print('<値の削除 remove>\nL6.remove("c")= {}'.format(L6))
    L6.clear()
    print('<リストの削除 clear>\nL6.clear()= {}'.format(L6))

    # リスト内包表記
    print("\n############################\n"
          "リスト内包表記\n"
          '############################')
    t = [1, 2, 3, 4, 5]
    t2 = []
    for i in t:
        t2.append(i)
    print('<リストの生成>\nt2= {}'.format(t2))
    print(""" 一般的なリストの生成記述↓
      t2 = []
      for i in t:
          t2.append(i)
      """)

    print("リスト内包表記での記載：r = [i for i in t]")
    r = [i for i in t]
    print('<リストの生成>\nr= {}'.format(r))

    print(""" \
      ################　↑リスト↑　##################   
      """)

# デバッグ用
# data_structure_list()
