# クラス完了

class Human(object):
    """
    基底クラスの宣言
    クラス変数：名前　性別　年齢　タプル
    """
    name = None
    sex = None
    age = None
    human_info = ()

    # コンストラクタ
    # 引数から取得した情報を各変数へ代入
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.human_info = (name, self.sex, self.age)
        # self.human_info = (name, sex, age)

    def say_something(self):
        # フォーマット関数を使い、For文にてタプルを出力する
        for i in self.human_info:
            if i is not None:
                print('for文の中は{}'.format(i))
                pass
            else:
                # 引数が足りない場合はその旨を出力し、終了する。
                print('iが{}なので出力できません。'.format(i))
                pass


# 　上記を継承したクラスを作成し、別メソッドを作成する。
class JapaneseHuman(Human):
    def __init__(self, name=None, sex=None, age=None):
        self.age = '54'
        super().__init__(name, sex, age)


# コンストラクタ前、初期変数はNoneが入っているためTypeはNone型になる
print('print(Human.name)', type(Human.name))
print('########################################')
# インスタンス化の際に引数として上記3つを渡し
# メソッドの呼び出しでそれらを出力する。
human = Human('Masato', 'men', '32')
human.say_something()
# コンストラクタ生成後のNameはHumanは引数に値が入っているためTypeが変わる
print('print(human.name)', type(human.name))

print('########################################')
japanese_human = JapaneseHuman('Seki', 'meen')
JapaneseHuman.say_something(self)
