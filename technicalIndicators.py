from datetime import date

import akshare as ak
import numpy as np
import pandas as pd

from log import log

FORMAT = lambda x: '%.4f' % x
class technicalIndicators:
    def MA(DF, N):
        return pd.Series.rolling(DF, N).mean()
    # 均线指标
    def stock_ma(symbol='',start_date='',end_date='',ma=[]):
        data = ak.stock_zh_a_hist(symbol=symbol,period="daily",start_date=start_date,end_date=end_date).sort_index(ascending=False)
        if ma is not None and len(ma) > 0:
            for a in ma:
                if isinstance(a, int):
                    data['ma%s' % a] = technicalIndicators.MA(data['收盘'], a).map(FORMAT).shift(-(a - 1))
                    data['ma%s' % a] = data['ma%s' % a].astype(float)
                    data['ma_v_%s' % a] = technicalIndicators.MA(data['成交量'], a).map(FORMAT).shift(-(a - 1))
                    data['ma_v_%s' % a] = data['ma_v_%s' % a].astype(float)
        return data

    #基金指标：获取前topNum规模的基金股票，有nNum家基金都选了该股票，返回股票列表
    def fund_df(topNum,nNum):
        fund_scale_open_sina_df = ak.fund_scale_open_sina(symbol='股票型基金')
        fund_scale_open_sina_df_top_ten = fund_scale_open_sina_df.sort_values('总募集规模', ascending=False).head(topNum)['基金代码'].values
        list_code = []
        for i in fund_scale_open_sina_df_top_ten:
            try:
                ak_code = ak.fund_portfolio_hold_em(symbol=i, date=str(date.today().year))['股票代码'].values
                code = ','.join(ak_code)
                list_code.append(code)
            except:
                continue
        codetest = ','.join(list_code)
        list2 = codetest.split(',')
        dup = pd.value_counts(list2)
        count = pd.DataFrame(dup, columns=['sum'])
        code_big = count[count['sum'] > nNum].index.values
        log.logger.info("完成基金选股阶段:" + str(code_big))
        return code_big

