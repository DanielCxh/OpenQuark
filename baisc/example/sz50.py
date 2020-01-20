import baostock as bs
import pandas as pd

lg = bs.login()

print('login respond error_code:' + lg.error_code)
print('login respond error_msg :' + lg.error_msg)

rs = bs.query_sz50_stocks()

print('query_sz50 error code:' + rs.error_code)
print('query_sz50 error msg :' + rs.error_msg)

sz50_stocks = []

while rs.error_code == '0' and rs.next():
    row_data = rs.get_row_data()
    sz50_stocks.append(row_data)

#print(sz50_stocks)

result = pd.DataFrame(sz50_stocks, columns = rs.fields)

result.to_csv('./sz50_stocks.csv', encoding = 'utf8', index = False)

print(result)

bs.logout()
