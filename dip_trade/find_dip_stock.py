from pykiwoom.kiwoom import *
import numpy as np
import pandas as pd

# 로그인
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 조건식을 가져오기
kiwoom.GetConditionLoad()

# 전체 조건식 리스트 얻기
conditions = kiwoom.GetConditionNameList()

# 0번 조건식에 해당하는 종목 리스트 출력
condition_index = conditions[0][0]
condition_name = conditions[0][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(codes)
