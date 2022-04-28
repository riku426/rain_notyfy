from selenium import webdriver
import time
import csv
import pandas as pd

#ガス橋のコート不良を確認するclass
class Get_Gas_Ground():
    def __init__(self, driver, yoyaku_ground):
        self.driver = driver
        self.yoyaku_ground = yoyaku_ground
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
        #ガス橋グラウンドをクリック
        self.driver.find_element_by_xpath("/html/body/form[2]/div/table/tbody/tr[4]/td/table[1]/tbody/tr[4]/td[2]/table/tbody/tr[2]/td[2]/input").click()
        time.sleep(1)
        #本日のグラウンド名を取得
        self.grounds = []

        #ガス橋は全てで7つある
        for i in range(29, 36):
            self.grounds.append(self.driver.find_element_by_xpath("/html/body/form[2]/div/table[{}]/tbody/tr[2]/td[1]".format(i)).text.replace("\n", ""))
            self.text = []
            self.day = []
            
        #print("self.yoyaku_grounds=", self.yoyaku_ground)
        #print("self.grounds=", self.grounds)

        #7つのグランドがあるため、checkに時間がかかる
        for i in range(7):
            if self.yoyaku_ground in self.grounds[i]:
                self.ground = self.grounds[i]
            else:pass

        for j in range(7):
            if self.ground == self.grounds[j]:
                for i in range(1,8):
                    try:
                        self.text.append(self.driver.find_element_by_xpath("/html/body/form[2]/div/table[{}]/tbody/tr[2]/td[{}]".format(j+29, i+2)).text)
                        self.day.append(self.driver.find_element_by_xpath("/html/body/form[2]/div/table[{}]/tbody/tr[1]/td[{}]".format(j+29, i+2)).text)
                    except:
                        break
                break
            else:
                pass


        self.driver.quit()

        #雨天中止があるかの確認
    def rain_check(self):
        self.message = []
        """ここでテキストを自由に変更できます
        self.text[0] = "コート不良"
        self.text[1] = "コート不良" """
        for i in range(len(self.text)):
            if self.text[i] == "コート不良":
                self.message.append('{}, は、{}でコート不良です。'.format(self.ground, self.day[i]))
            else:
                pass
        #csvファイルにコート状況を保存
        with open("csv/state_of_gas.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.text)

        #前回保存したコート状態と同じなら通知しない仕組み
        alltxt = pd.read_csv("csv/state_of_gas.csv","r", encoding="cp932").values.tolist()
        last_gyou = len(alltxt)
        if last_gyou >= 1:
            #print("alltxt=",alltxt)
            #print("last gyou=",last_gyou)
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
        print("check0",self.ground)
        print("check1",self.message)

        return self.ground, self.message