
import baostock as bs
import pandas as pd
import datetime

lg = bs.login()

print('bs.login error_code:' + lg.error_code)
print('bs.login error_msg: ' + lg.error_msg)

# 获取指数(综合指数、规模指数、一级行业指数、二级行业指数、策略指数、成长指数、价值指数、主题指数)K线数据
# 综合指数，例如：sh.000001 上证指数，sz.399106 深证综指 等；
# 规模指数，例如：sh.000016 上证50，sh.000300 沪深300，sh.000905 中证500，sz.399001 深证成指等；
# 一级行业指数，例如：sh.000037 上证医药，sz.399433 国证交运 等；
# 二级行业指数，例如：sh.000952 300地产，sz.399951 300银行 等；
# 策略指数，例如：sh.000050 50等权，sh.000982 500等权 等；
# 成长指数，例如：sz.399376 小盘成长 等；
# 价值指数，例如：sh.000029 180价值 等；
# 主题指数，例如：sh.000015 红利指数，sh.000063 上证周期 等；

STOCK_INFO = 'date, code, open, high, low, close, volume, amount, pctChg'

DATE_START = '2019-09-01'
DATE_END   = '2020-01-01'

rs = bs.query_history_k_data_plus('sh.000300',
                                  STOCK_INFO,
                                  start_date = DATE_START,
                                  end_date = DATE_END,
                                  frequency = 'd')

print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

data_list = []

while (rs.error_code == '0' and rs.next()):
    row_data = rs.get_row_data()
    data_list.append(row_data)

result = pd.DataFrame(data_list, columns=rs.fields)

print(result)


print(datetime.datetime.now().strftime('%Y-%m-%d'))
print(datetime.datetime.now().weekday())
print(datetime.datetime.strptime('20200121', '%Y%m%d').weekday())
