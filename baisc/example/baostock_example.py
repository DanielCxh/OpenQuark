#!/bin/python3

import baostock as bs
import pandas as pd

import datetime

#### Login System ####
lg = bs.login()

print('login respond error_code : ' + lg.error_code)
print('login respond error_msg : '  + lg.error_msg)

# date : 交易所行情日期
# code : 证券代码
# open : 开盘价格
# high : 最高价
# low  : 最低价
# close: 收盘价
# preclose : 前收盘价格
# volume : 成交量(单位：股)
# amount : 成交额(单位：人民币元)
# adjustflag: 复权状态(1, 后复权；2，前复权；3，不复权)
# turn : 换手率
# tradestatus : 交易状态(1, 正常交易; 0, 停牌)
# pctChg : 涨跌幅（百分比）
# peTTM : 滚动市盈率
# pbMRQ : 市净率
# psTTM : 滚动市销率
# pcfNcfTTM : 滚动市现率
# isST : 是否ST股（1, 是; 2, 否）
SOCKET_INFO = 'date, code, open, high, low, close, preclose, volume, pctChg, amount, adjustflag, turn, tradestatus, pctChg, isST'

END_DATE = datetime.datetime.now().strftime('%Y-%m-%d')

print(SOCKET_INFO)
#### 获取沪深A股历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。
# 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
rs = bs.query_history_k_data_plus('sh.600000',
                                  SOCKET_INFO,
				  start_date='2020-01-01',
			          end_date=END_DATE,
				  frequency="d",
				  adjustflag="3")

print('query_history_k_data_plus respond error_code: '+rs.error_code)
print('query_history_k_data_plus respond error_msg : '+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####
result.to_csv("./history_A_stock_k_data.csv", index=False)
print(result)

bs.logout()

print(datetime.datetime.now().strftime('%Y-%m-%d'))
print(datetime.datetime.now().weekday())
print(datetime.datetime.strptime('20200121', '%Y%m%d').weekday())

