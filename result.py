from selenium import webdriver
from ground_check.chohu_check import Get_Chohu_Ground
from ground_check.haginaka_check import Get_Hagi_Ground
from ground_check.gas_check import Get_Gas_Ground
import login


#様々な関数を実行する関数
def main():
    ground = "0"
    Today, ground = login.day_check()
    #print("place_yoyaku", ground)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome("C:\\Users\\riku4\\venv\\myenv\\Lib\\site-packages\\chromedriver_binary\\chromedriver.exe", options=options)

    message = []
    if Today == True:
        if "東調布" in ground:
            chohu_bot = Get_Chohu_Ground(driver)
            ground, message = chohu_bot.main()
    
        elif "萩中" in ground :
            hagi_bot = Get_Hagi_Ground(driver)
            ground, message = hagi_bot.main()
            print("check ground", ground)
            print("check_mes", message)

        elif "ガス橋" in ground:
            gas_bot = Get_Gas_Ground(driver, ground)
            ground, message = gas_bot.main()

        else:
            pass

    return ground, message
