from selenium import webdriver
import time
import datetime

#Loginするためのクラス
class Login:
    def __init__(self, driver):
        #ログインしてトップにある予約日
        self.yoyaku = "0"
        #google driver
        self.driver = driver
        self.driver.get("https://www.yoyaku.city.ota.tokyo.jp")
        time.sleep(1)
        self.count = 0
        self.ground = "0"

    
    def login(self):
        #予約確認画面に移るまで繰り返す
        while self.yoyaku == "0":
            self.count += 1
            #「予約の確認」ボタンを押す
            self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/div[5]/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/a").click()
            time.sleep(1)
            #idをsendする
            self.login_id = self.driver.find_element_by_xpath("/html/body/form[2]/div/div[2]/table/tbody/tr/td/div/table[2]/tbody/tr/td[1]/input[1]")
            self.login_id.send_keys("00091224")
            time.sleep(1)

            #passwordをsendする
            self.login_pas = self.driver.find_element_by_xpath("/html/body/form[2]/div/div[2]/table/tbody/tr/td/div/table[2]/tbody/tr/td[1]/input[2]")
            self.login_pas.send_keys("111111")
            time.sleep(1)

            #ログインボタンを押す
            self.driver.find_element_by_xpath("/html/body/form[2]/div/div[2]/table/tbody/tr/td/div/table[2]/tbody/tr/td[1]/div/a").click()
            time.sleep(1)
        
            #エラーメッセージが出たら
            try:
                if self.driver.find_element_by_xpath("/html/body/form[2]/div/div/table[1]/tbody/tr/td/div/table/tbody/tr[1]/td").text == "システムエラーが発生しました。":
                    print("システムエラーです。")
                    self.driver.find_element_by_xpath("/html/body/form[2]/div/div/table[2]/tbody/tr/td/a").click()
                elif self.count == 3:
                    self.driver.quit()
                    print("ログインできないバグです。")
                    break


            #エラーメッセージが出なかったら
            except:
                #予約日とグラウンド名を取得
                self.yoyaku = self.driver.find_element_by_xpath("/html/body/form[2]/div/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td[3]").text
                self.ground = self.driver.find_element_by_xpath("/html/body/form[2]/div/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td[4]").text
                break
        self.driver.quit()
        return self.yoyaku, self.ground

    def play(self):
        return self.login()

#予約日と本日が一致しているのかのチェック関数
def day_check():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome("C:\\Users\\riku4\\venv\\myenv\\Lib\\site-packages\\chromedriver_binary\\chromedriver.exe", options=options)

    log_bot = Login(driver)
    yoyaku, ground = log_bot.play()

    Today = "0"
    ground = "0"

    """ここでテストのためのグラウンドを決められます
    ground = "蒲田地域_野球場多摩川ガス橋緑地野球場_５号面"
    print("place_yoyaku1",ground)"""
        
    time.sleep(1)
    dt_now = datetime.datetime.now()
    dt_str = dt_now.strftime('%Y年%m月%d日')


    """ここでテストのための日付を決められます
    test_day = "2022年1月8日"
    if test_day in yoyaku:
        print("予約日です")
        Today = True
        return Today, ground
    
    else:
        print("間違っているよ")
        return Today, "0"   """
    

    if dt_str in yoyaku:
        print("予約日です")
        Today = True
        return Today, ground


