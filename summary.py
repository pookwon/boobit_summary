from xmlrpc.client import DateTime
from numpy import NaN, double, float64, int64
import pandas as pd
import operator


def get_coin_price(source, cointype, date):
    market = cointype + "USD"
    user_trades = source[ (source['거래'] == market) & (source['날짜'] >= date) & (source['체결 코인 수량'] == cointype) & (source['거래 평균가'] > 0)]
    #print(user_trades)
    return user_trades["거래 평균가"].values[0]

def summary_voulme(source_path, target_path):
    source_frames = pd.read_csv(source_path, dtype={'날짜':str, '종류':str, '거래':str, '유저ID':str, '체결 수량':float64, '체결 코인 수량':str, '거래 평균가':float64, '수수료':float64})

    #source_path = './sample.xlsx'
    #source_frames = pd.read_excel(source_path)

    #source_path = './real_sample.csv'
    #source_frames = pd.read_csv(source_path, dtype={'날짜':str, '유저ID':str, '체결 수량':float64, '거래 평균가':float64})
    #target_path = './sort_sample.xlsx'

    #print(source_frames['유저ID'])
    #print(source_frames.keys())

    uid_list = set(source_frames['유저ID'].values.tolist())
    if NaN in uid_list:
        uid_list.remove(NaN)
    #print(uid_list)

    uid_datas = []
    for uid in uid_list:
        if uid is None or uid is NaN:
            continue

        user_trades = source_frames[source_frames['유저ID'] == uid]
        
        #print(user_trades)

        uid_total = 0
        uid_fee_total = 0.0
        for index, item in user_trades.iterrows():
            #print(item)

            trade_date = item['날짜']
            avg_price = float(item['거래 평균가'])
            qty = float(item['체결 수량'])
            fees = float(item['수수료'])
            coin_type = item['체결 코인 수량']
            market = item["종류"]
            trade_market = item['거래']
            if fees != 0:
                if coin_type == 'USDT':
                    uid_fee_total += fees
                else:
                    if market == 'COIN 선물':
                        market_determine = coin_type + 'USD'
                        if market_determine == trade_market:
                            if avg_price > 0: 
                                uid_fee_total += avg_price * fees
                                #print(trade_market, coin_type, avg_price, fees)
                            else:
                                avg_price = get_coin_price(source_frames, coin_type, trade_date)
                                uid_fee_total += avg_price * fees
                                #print(trade_market, coin_type, avg_price, fees)
                        else:
                            avg_price = get_coin_price(source_frames, coin_type, trade_date)
                            uid_fee_total += avg_price * fees
                            #print(trade_market, coin_type, avg_price, fees)
                    else:
                        uid_fee_total += fees                            
                                
        uid_datas.append({'UID':str(uid), '수수료':-uid_fee_total})

    uid_datas.sort(key=operator.itemgetter('수수료'), reverse=True)

    #print(uid_datas)
    sort_userdata = pd.DataFrame(uid_datas)
    sort_userdata.to_excel(target_path)