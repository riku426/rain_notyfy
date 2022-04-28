import datetime

def csv_drop():

    time = datetime.datetime.now()
    hour = time.hour
    
    """ここでテストのために現在時刻を変えられます。
    hour = 15 """
    #hour = 19
    if hour == 19:
        with open("csv/state_of_chohu.csv", "w") as f:
            pass
        with open("csv/state_of_hagi.csv", "w") as f:
            pass
        with open("csv/state_of_gas.csv", "w") as f:
            pass
    else:
        pass