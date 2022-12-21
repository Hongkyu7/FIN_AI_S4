from pykiwoom.kiwoom import *
import numpy as np
import pandas as pd
import time
from datetime import datetime


def get_first_condition_info(api):
    # 조건식을 가져오기
    api.GetConditionLoad()

    # 전체 조건식 리스트 얻기
    condition_list = api.GetConditionNameList()

    # 0번 조건식 index와 이름 가져오기
    first_condition_index = condition_list[0][0]
    first_condition_name = condition_list[0][1]

    return first_condition_index, first_condition_name


# 로그인
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 0번 조건식 info 가져오기
condition_index, condition_name = get_first_condition_info(kiwoom)


while True:
    if kiwoom.GetConnectState():
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        print(f"현재 시간 : {hour}시 {minute}분")
    else:
        # Login
        kiwoom.CommConnect(block=True)

        # 0번 조건식 info 가져오기
        condition_index, condition_name = get_first_condition_info(kiwoom)

        continue

    if hour >= 9:
        result = []
        while True:
            now_local = datetime.now()
            hour_local = now_local.hour
            minute_local = now_local.minute
            if hour_local >= 15 and minute_local > 30:
                break

            tickers = kiwoom.SendCondition("0101", condition_name, condition_index, 0)
            data = (hour_local, minute_local, tickers)
            print(data)
            result.append(data)
            time.sleep(180)
        break
    else:
        time.sleep(60)
        continue
