#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pandas as pd
import datetime
import baostock as bs

lg = bs.login()

print('login respond error_code:' + lg.error_code)
print('login respond error_msg :' + lg.error_msg)

END_DATE = datetime.datetime.now().strftime('%Y-%m-%d')

START_DATE = (datetime.datetime.now() + datetime.timedelta(days = -22)).strftime('%Y-%m-%d')

LAST_DATE = ''

rs = bs.query_trade_dates(start_date = START_DATE, end_date = END_DATE)

date_list = []

while rs.error_code == '0' and rs.next():
    row_data = rs.get_row_data()
    date_list.append(row_data)

date_size = len(date_list) - 1

for i in range(0, date_size):
    if date_list[date_size - 1 - i][1] == '1':
        LAST_DATE = date_list[date_size - 1 -i][0]
        print(LAST_DATE)
        break

rs = bs.query_all_stock(day = str(LAST_DATE))

print('query_all_stock respond error_code:' + rs.error_code)
print('query_all_stock respond error_msg :' + rs.error_msg)

code_list = []

while rs.error_code == '0' and rs.next():
    row_data = rs.get_row_data()[0]
    code_list.append(row_data)

#print(code_list)

df = pd.DataFrame()

stock_list = []

for code in code_list:
    rs = bs.query_history_k_data(code, 'date, code, pbMRQ',
                                 start_date = LAST_DATE,
                                 end_date = LAST_DATE,
                                 frequency = 'd',
                                 adjustflag = '3')
    if rs.error_code == '0':
        result = rs.get_row_data()
        if float(result[2]) <= float(0):
            print('pass')
            continue
        if float(result[2]) > 2.5:
            continue
        print('append')
        stock_list.append(result)

print(stock_list)
