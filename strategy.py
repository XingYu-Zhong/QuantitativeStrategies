from log import *
from technicalIndicators import technicalIndicators
import akshare as ak
from datetime import date, timedelta

class strategy:
    #红包策略：
    def strategy01(self):
        target = technicalIndicators.fund_df(100,10)
        stock_rank_lxxd_ths_df = ak.stock_rank_lxxd_ths()[ak.stock_rank_lxxd_ths()['连涨天数'] >= 5]['股票代码'].values
        list_code = list(set(target).intersection(set(stock_rank_lxxd_ths_df)))
        log.logger.info("完成连续下跌5天选股阶段:" + str(list_code))
        target_code = []
        for strCode in list_code:
            tmp_df = technicalIndicators.stock_ma(symbol=strCode,start_date=str(date.today() + timedelta(days=-70)).replace("-", ""), end_date=str(date.today() + timedelta(days=-1)).replace("-", ""),
                                ma=[5, 60])[:1]
            if tmp_df['ma5'].values[0] < tmp_df['ma60'].values[0]:
                stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()[ak.stock_zh_a_spot_em()['代码'] == strCode]
                vol = stock_zh_a_spot_em_df['成交量'].values
                uplowRate = stock_zh_a_spot_em_df['涨跌幅'].values
                if tmp_df['ma_v_5'].values[0] < vol:
                    if uplowRate >= 3 and uplowRate <= 5:
                        target_code.append(strCode)
        if len(target_code) < 1:
            log.logger.info("没有满足条件的股票")
        else:
            log.logger.info("满足条件的股票:" + str(target_code))
        return target_code

    def strategy02(self):
        stock_hot_tgb_df = ak.stock_hot_tgb()['个股代码'].values
        target_code = []
        target = []
        for stock in stock_hot_tgb_df:
            target.append(stock[2:])
        stock_rank_lxsz_ths = ak.stock_rank_lxsz_ths()[ak.stock_rank_lxsz_ths()['连涨天数'] >= 2]['股票代码'].values
        list_code = list(set(target).intersection(set(stock_rank_lxsz_ths)))
        log.logger.info("大于两天上涨的股票："+str(list_code))
        for stock in list_code:
            tmp_df = technicalIndicators.stock_ma(symbol=stock,
                                                  start_date=str(date.today() + timedelta(days=-70)).replace("-", ""),
                                                  end_date=str(date.today() + timedelta(days=-1)).replace("-", ""),
                                                  ma=[5, 60])[:1]
            if tmp_df['ma5'].values[0] < tmp_df['ma60'].values[0]:
                stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()[ak.stock_zh_a_spot_em()['代码'] == stock]
                vol = stock_zh_a_spot_em_df['成交量'].values
                uplowRate = stock_zh_a_spot_em_df['涨跌幅'].values
                if tmp_df['ma_v_5'].values[0] < vol:
                    if uplowRate >= 3 and uplowRate <= 5:
                        target_code.append(stock)
        if len(target_code) < 1:
            log.logger.info("没有满足条件的股票")
        else:
            log.logger.info("满足条件的股票:" + str(target_code))
        return target_code

if __name__ == '__main__':
    strategy().strategy02()

