import tushare as ts
import load.sqlitelib as sqlitelib

class TsLoad(object):
    def __init__(self):
        # 获取连接备用
        self.__cons__ = ts.get_apis()

    def loadStockBasics(self):

        stocks = ts.get_stock_basics('2016-08-29')
        print(stocks)

        db = sqlitelib.Database()

    def test(self):

        df = ts.bar('600000', conn=self.__cons__, freq='D', start_date='2016-01-01', end_date='')
        print(df.head(5))

        #带因子的行情

        df = ts.bar('600000', conn=self.__cons__, start_date='2016-01-01', end_date='', ma=[5, 10, 20], factors=['vr', 'tor'])
        print(df.head(5))


        #复权行情, adj=qfq(前复权)， hfq（后复权），默认None不复权

        df = ts.bar('600000', conn=self.__cons__, adj='qfq', start_date='2016-01-01', end_date='')
        print(df.head(5))


        #分钟数据, 设置freq参数，分别为1min/5min/15min/30min/60min，D(日)/W(周)/M(月)/Q(季)/Y(年)

        df = ts.bar('600000', conn=self.__cons__, freq='1min', start_date='2016-01-01', end_date='')
        print(df.head(5))


        #指数日行情, 设置asset='INDEX'

        df = ts.bar('000300', conn=self.__cons__, asset='INDEX', start_date='2016-01-01', end_date='')
        print(df.head(5))


        #股票tick,type:买卖方向，0-买入 1-卖出 2-集合竞价成交

        df = ts.tick('600000', conn=self.__cons__, date='2017-10-26')
        print(df.head(20))
        #数据里没有增加代码一列，如果有需要可以同多df[‘code’] = code实现。


if __name__=='__main__':
    loader = TsLoad()
    loader.getStockBasics()


