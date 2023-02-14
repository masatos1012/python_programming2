import data_structure as ds
import numeric_type as nt
import special_argument as sa
import string_type as st
import variable_declaration as vd

# import closuer_type as ct

# TODO　インプットによって呼び出すメソッドを選択し索引のような動きを実装

# 変数宣言と出力
vd.vd_call()
# 数値型
nt.numeric_type()
# 文字列
st.string_type()
# 改行パターン
st.string_new_line()
# スライスの使用法
st.stirng_slice()
# データ構造
ds.data_structure_list()
# 関数内関数
# vd.innner_function()
# クロージャー
# vd.closuer()
# デコレーター
# vd.decolator()


sa.standard_arg(arg=2)
sa.pos_only_arg(2)
sa.pos_only_arg2(1, 2, 3, d=4)
sa.kwd_only_arg(arg=2)
sa.combinated_example(1, 2, kwd_only=3)
sa.foo('aaaa', bbb='bbb', ccc='ccc', ddd='ddd')
