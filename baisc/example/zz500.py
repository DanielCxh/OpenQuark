import baostock as bs
import pandas as pd

lg = bs.login()

rs = bs.query_zz500_stocks()

print('query_zz500 error code:' + rs.error_code)
print('query_zz500 error msg :' + rs.error_msg)

zz500_stocks = []

while rs.error_code == '0' and rs.next():
    zz500_stocks.append(rs.get_row_data())

result = pd.DataFrame(zz500_stocks, columns = rs.fields)

result.to_csv('./zz500_stocks.csv', encoding = 'utf8', index = False)

print(result)

bs.logout()
