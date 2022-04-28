
import time
import csv
import pandas as pd

#東調布のコート不良を確認するclass
class Get_Chohu_Ground():
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.yoyaku.city.ota.tokyo.jp/")
        time.sleep(1)

    #グラウンド名とコート状態を得る関数
    def get_ground(self):
        #施設の検索をクリック
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[1]/div[5]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/a').click()
        time.sleep(1)
        #野球場をクリック
        self.driver.find_element_by_xpath("/html/body/form[2]/div/table/tbody/tr[3]/td/table/tbody/tr[3]/td[3]/input").click()
        time.sleep(1)
        #東調布グラウンドをクリック
        self.driver.find_element_by_xpath("/html/body/form[2]/div/table/tbody/tr[4]/td/table[1]/tbody/tr[4]/td[2]/table/tbody/tr[1]/td[3]/input").click()
        time.sleep(1)
        #本日のグラウンド名を取得
        self.ground = self.driver.find_element_by_xpath("/html/body/form[2]/div/table[6]/tbody/tr[2]/td[1]").text
        self.text = []
        self.day = []
        for i in range(1,8):
            try:
                self.text.append(self.driver.find_element_by_xpath("/html/body/form[2]/div/table[6]/tbody/tr[2]/td[{}]".format(i+2)).text)
                self.day.append(self.driver.find_element_by_xpath("/html/body/form[2]/div/table[6]/tbody/tr[1]/td[{}]".format(i+2)).text)
            except:
                break
        self.driver.quit()

        #print("text=", text)
        #print("day=", day)

        #雨天中止があるかの確認
    def rain_check(self):
        self.message = []
        """ここでテキストを自由に変更できます。
        self.text[0] = "happy"
        self.text[3] = "コート不良 " """
        for i in range(len(self.text)):
            if self.text[i] == "コート不良":
                self.message.append('{}, は、{}でコート不良です。'.format(self.ground, self.day[i]))
            else:
                pass
        with open("csv/state_of_chohu.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.text)

        alltxt = pd.read_csv("csv/state_of_chohu.csv", "r", encoding="cp932").values.tolist()
        last_gyou = len(alltxt)
        if last_gyou >= 1:
            last_weather = alltxt[last_gyou-2]
            now_weather = alltxt[last_gyou-1]

            #print("last_wether=", last_weather)
            #print("now_weather=",now_weather)

            if last_weather == now_weather:
                self.ground = "0"

    #実行関数
    def main(self):

        self.get_ground()
        self.rain_check()

        return self.ground, self.message