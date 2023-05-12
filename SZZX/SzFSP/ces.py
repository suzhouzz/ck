# import datetime
# import random,string
# from data import parm
# from lib import login, product, position
# from selenium.webdriver.common.by import By
# #显式等待模块
# from selenium.webdriver.support.ui import WebDriverWait
# #显式等待条件
# from selenium.webdriver.support import expected_conditions as EC
import re
from locale import *

setlocale(LC_NUMERIC, 'English_US')

i = atof('123,45.6')    # 123456.0
i = int(i)
print(i)
from re import sub
q = 1000.1
money = '1,000.1'
val = sub(r'[^\d.]', '', money)
val = str(q)
if q == val:
    print(val)
else:
    print(1)


































































