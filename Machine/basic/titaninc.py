# -*- coding: utf-8 -*-
import pandas as pd
from tabulate import tabulate
import seaborn as sns
from sklearn import svm
from sklearn import metrics


def convert_dummies(df, key):
    dum = pd.get_dummies(df[key])
    ks = dum.keys()
    dum.columns = [key + "_" + str(k) for k in ks]
    df = pd.concat((df, dum.ix[:, 1:]), axis=1)
    df = df.drop(key, axis=1)
    return df


def convert_to_seizon_list(lis):
    seizon = []
    for element in lis:
        if element == 0:
            seizon.append('死亡')
        else:
            seizon.append('生存')
    return seizon


if __name__ == "__main__":
    sns.set(style="whitegrid", color_codes=True)
    # タイタニック号の乗客リスト
    titanic = sns.load_dataset("titanic")

    headers = [c for c in titanic.columns]
    headers.insert(0, "ID")
    print tabulate(titanic[:5], headers, tablefmt="pipe")

    # 生存したか否かのリストを取得
    deadOrAlive = pd.np.array(titanic.survived)
    seizon_list = convert_to_seizon_list(deadOrAlive)

    # 数値に変換
    titanic = convert_dummies(titanic, "who")
    titanic = convert_dummies(titanic, "class")
    titanic = convert_dummies(titanic, "sex")
    titanic = convert_dummies(titanic, "alone")
    titanic = convert_dummies(titanic, "embark_town")
    titanic = convert_dummies(titanic, "deck")
    titanic = convert_dummies(titanic, "embarked")
    titanic['age'] = titanic.age.fillna(titanic.age.median())
    titanic['adult_male'] = titanic.adult_male.map({True: 1, False: 0}).astype(int)
    titanic['alone'] = titanic.adult_male.map({True: 1, False: 0}).astype(int)

    # 使用しないカラムを削除
    titanic = titanic.drop("alive", axis=1)
    titanic = titanic.drop("pclass", axis=1)
    titanic = titanic.drop("survived", axis=1)

    # SVC.fit(入力データ、答え)で学習。gamma=1.0
    clf = svm.SVC(gamma=0.5)
    clf.fit(titanic[:800], deadOrAlive[:800])

    headers2 = [c for c in titanic.columns]

    # 後半の30データを基に予測 SVC.predict(データ)
    expected = seizon_list[-31:-1]
    predicted = convert_to_seizon_list(clf.predict(titanic[-31:-1]))

    print '\n投入データ\n{}'.format(tabulate(titanic[-31:-1], headers2, tablefmt="pipe"))
    print '\n実際の結果\n{}'.format(str(expected).decode("string-escape"))

    print '\n予想結果\n{}'.format(str(predicted).decode("string-escape"))

    # precision=適合率, recall=再現率, f1-score=平均
    print("\nClassification report for classifier\n%s\n"
      % (metrics.classification_report(expected, predicted)))
