#!/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.request as request
import json


def find_pairs():
    ids = ['rb2007', 'rb2008', 'rb2009', 'rb2010', 'rb2011', 'rb2012']
    url_5m = 'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine5m?symbol='
    result = []

    for id in ids:
        url = url_5m + id
        req = request.Request(url)
        rsp = request.urlopen(req)
        res = rsp.read()
        res_json = json.loads(res)
        result.append(res_json)

    close_result = []

    for instrument in result:
        one_day_list = []
        for one_day in instrument:
            one_day_list.append(float(one_day[-2]))
        close_result.append(np.array(one_day_list))

    close_result = np.array(close_result)
    close_result = close_result.T

    print(close_result)

    df = pd.DataFrame(data = close_result, columns = ids)
    df.plot()
    #sns.heatmap(df.corr(), annot=True, square=True)
    plt.show()

find_pairs()
