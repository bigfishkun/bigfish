import tushare as ts

#获取连接备用
cons = ts.get_apis()

df = ts.bar('600000', conn=cons, freq='D', start_date='2016-01-01', end_date='')
print(df.head(5))

#带因子的行情

df = ts.bar('600000', conn=cons, start_date='2016-01-01', end_date='', ma=[5, 10, 20], factors=['vr', 'tor'])
print(df.head(5))


#复权行情, adj=qfq(前复权)， hfq（后复权），默认None不复权

df = ts.bar('600000', conn=cons, adj='qfq', start_date='2016-01-01', end_date='')
print(df.head(5))


#分钟数据, 设置freq参数，分别为1min/5min/15min/30min/60min，D(日)/W(周)/M(月)/Q(季)/Y(年)

df = ts.bar('600000', conn=cons, freq='1min', start_date='2016-01-01', end_date='')
print(df.head(5))


#指数日行情, 设置asset='INDEX'

df = ts.bar('000300', conn=cons, asset='INDEX', start_date='2016-01-01', end_date='')
print(df.head(5))


#股票tick,type:买卖方向，0-买入 1-卖出 2-集合竞价成交

df = ts.tick('600000', conn=cons, date='2017-10-26')
print(df.head(20))
#数据里没有增加代码一列，如果有需要可以同多df[‘code’] = code实现。