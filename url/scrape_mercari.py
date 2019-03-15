from selenium import webdriver
from selenium.webdriver.support.ui import Select

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chromeを起動させる(phantomjsだとNG)
# browser = webdriver.PhantomJS("phantomjs.exe")
browser = webdriver.Chrome('/home/yuki/PycharmProjects/pyStudy/url/chromedriver')

# 文字コード(UTF-8)関連
import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def check_price(keyword, maxpage):
    text = ""
    priceList = {}
    df_main = pd.DataFrame(columns=['SOLD', 'PRICE'])

    # 各ページから価格を取得する
    for num in range(1, maxpage):
        # 検索用URL
        res = browser.get("https://www.mercari.com/jp/search/?page=" + str(num) + "&keyword=" + keyword)
        print("https://www.mercari.com/jp/search/?page=" + str(num) + "&keyword=" + keyword)

        # items-boxが一つもなければ終了
        item_box_list = browser.find_elements_by_css_selector(".items-box")
        if len(item_box_list) == 0:
            break

        for item_box in item_box_list:
            # SOLD or NOT SOLD
            if len(item_box.find_elements_by_css_selector(".item-sold-out-badge")) > 0:
                sold = "SOLD"
                item_price = item_box.find_element_by_css_selector(".items-box-price")
                # ,と円は削除しておく
                price_text = item_price.text
                price_text = re.sub(r",", "", price_text)
                price_text = re.sub(r"¥ ", "", price_text)
                price_text_int = int(price_text)

                se_temp = pd.Series([sold, price_text_int], index=df_main.columns)
                df_main = df_main.append(se_temp, ignore_index=True)
            # else:
            #     sold = "NOT SOLD"

    print(df_main)
    sns.stripplot(x='SOLD', y='PRICE', data=df_main)
    plt.show()
    sns.pairplot(df_main, hue="SOLD")
    plt.show()


def main():
    argvs = sys.argv
    # check_price(SearchWord,最大ページ数)
    check_price("Nintendo switch", 200)


if __name__ == "__main__":
    main()
