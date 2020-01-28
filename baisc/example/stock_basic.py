import baostock as bs
import pandas as pd

lg = bs.login()

print('login respond error_code:' + lg.error_code)
print('login respond error_msg :' + lg.error_msg)

rs = bs.query_stock_basic(code = 'sh.600000')

print('query_stock_basic error_code:' + rs.error_code)

stock_data_list = []

while rs.error_code == '0' and rs.next():
    row_data = rs.get_row_data()
    stock_data_list.append(row_data)

result = pd.DataFrame(stock_data_list, columns = rs.fields)

result.to_csv('./stock_basic.csv', encoding = 'utf8', index = False)

print(result)

bs.logout()
    
