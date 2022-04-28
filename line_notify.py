import requests
import result
import drop

def main():
    #東調布グラウンドで練習を行いかつ、グラウンドのコート不良を確かめる。
    ground, message = result.main()
    #print("ground=",ground)
    #print("message=",message)
    #print(place)
    #print("ok2")
    #message = ["東調布グラウンドは雨天中止です。", "雨が降っている"]
    url = "https://notify-api.line.me/api/notify"
    token = "IIxv7cdaArbLqlLuva8XM8vChZYTlvhxap2ryJVkSTV"
    headers = {"Authorization":"Bearer "+token}

    if ("東調布" in ground or "萩中" in ground or "ガス橋" in ground) and message != []:
        payload = {"message": message}

        r = requests.post(url, headers = headers, params = payload)
    
    else:
        pass

    drop.csv_drop()

if __name__ == "__main__":
    main()