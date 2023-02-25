"""
リストの記述
リストはmutable(可変体なのでインデックスにて書き換えが可能)
スライスの使用も可能
# TODO　リスト(完了）　タプル　辞書型　集合
# TODO　内包表記の追記
"""


def data_structure_list():
    print(""" \
      ################　↓リスト↓　##################   
      """)

    # 配列(リスト)作成
    l = [0, 1, 2, 3, 4, 5, 6, 7]
    print('<標準リストの出力> l={}'.format(l))
    print('lのTypeを出力', type(l))
    print('"l[0]:{}"               ・・・インデックスは0から始まる'.format(l[0]))
    print('"l[:4]:{}"   ・・・0≦:<4'.format(l[:4]))
    print('"l[4:]:{}"   ・・・4≦:'.format(l[4:]))
    print('"l[2:6]:{}"  ・・・2≦:<6となる'.format(l[2:6]))
    print('"l[-1]:{}"              ・・・インデックス最後からの指定も可能'.format(l[-1]))

    # 文字列のリスト
    print("\n############################\n"
          "リスト型は文字列に対してもインデックスが使える\n"
          "list(文字列)と記載しリスト型へ変換できる\n"
          "文字列の置換に便利")
    print('############################')
    l2 = list('abcdrfghijk')
    print('<文字列リストの出力>\nl2= {}'.format(l2))
    print('"l2"(Type):', type(l2), '\n')
    print('"l2[3]:{}"           \
                           ・・・インデックスでの指定'.format(l2[3]))
    print('"l2[::2]:{}" ・・・２つ飛ばしで出力'.format(l2[::2]))
    print('"l2[1::2]:{}" \
          ・・・開始位置の変更。２つ飛ばしで出力'.format(l2[1::2]))
    print('"l2[::-2]:{}" ・・・終端から-２ずつ'.format(l2[::-2]))
    print('"l2[-1::-2]:{}" ・・・終端-1から-２ずつ(反転)'.format(l2[-1::-2]))

    # リストの結合
    print("\n############################\n"
          "リスト同士の結合も可能\n"
          '############################')
    l3 = ["a", "b", "c", "d", "e"]
    l4 = [1, 2, 3]
    l5 = [l3, l4]
    print('l3= {}'.format(l3))
    print('l4= {}'.format(l4))
    print('l5= {}'.format(l5))
    print("print(l5):", type(l5))
    print('')
    print('<左リストの出力>\nl5[0]= {}'.format(l5[0]))
    print('<右リストの出力>\nl5[1]= {}'.format(l5[1]))
    print('')
    print('<特定値の出力>\nl5[0][0]= {}'.format(l5[0][0]))
    print('l5[1][0]= {}'.format(l5[1][0]))
    print('l5[0][1]= {}'.format(l5[0][1]))
    print('<特定値,範囲指定の出力>\nl5[0][1:3]= {}'.format(l5[0][1:3]))
    print('l5[1][1:3]= {}'.format(l5[1][1:3]))

    # リストの操作
    print("\n############################\n"
          "リストの操作\n"
          '############################')
    l6 = ["a", "b", "c", "d", "e"]
    print('l6= {}'.format(l6))
    print('')
    l6.append(100)
    print('<値の追加 append>\nl6.append(100)= {}'.format(l6))
    l6.insert(1, 200)
    print('<値の追加 insert>記述：insert(inndex,value)\n'
          'l6.insert(1, 200)= {}'.format(l6))
    print('')
    l6.pop()
    print('<値の取り出し pop>\nl6.pop()= {}'.format(l6))
    l6.pop(0)
    print('<値の取り出し pop>\nl6.pop(0)= {}'.format(l6))
    print('')
    del l6[1]
    print('<値の削除 del>\ndel l6[1]= {}'.format(l6))
    # del l6[2]
    # l7 = l6
    l6.remove('c')
    print('<値の削除 remove>\nl6.remove("c")= {}'.format(l6))
    l6.clear()
    print('<リストの削除 clear>\nl6.clear()= {}'.format(l6))

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
