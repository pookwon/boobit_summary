from xmlrpc.client import DateTime
from numpy import NaN, double, float64, int64
import pandas as pd
import operator


def summary_voulme(source_path, target_path):
    source_frames = pd.read_csv(source_path, dtype={'날짜':str, '유저ID':str, '체결 수량':float64, '거래 평균가':float64})

    #source_path = './sample.xlsx'
    #source_frames = pd.read_excel(source_path)

    #source_path = './real_sample.csv'
    #source_frames = pd.read_csv(source_path, dtype={'날짜':str, '유저ID':str, '체결 수량':float64, '거래 평균가':float64})
    #target_path = './sort_sample.xlsx'

    #print(source_frames['유저ID'])
    #print(source_frames.keys())

    uid_list = set(source_frames['유저ID'].values.tolist())
    uid_list.remove(NaN)
    #print(uid_list)

    uid_datas = []
    for uid in uid_list:
        if uid is None or uid is NaN:
            continue

        user_trades = source_frames[source_frames['유저ID'] == uid]
        
        #print(user_trades)

        uid_total = 0
        for index, item in user_trades.iterrows():
            #print(item)
            #print('avg', item[13], 'qty', item[11])

            avg_price = float(item['거래 평균가'])
            qty = float(item['체결 수량'])

            if qty > 0 and avg_price > 0:
                uid_total += avg_price * qty
        
        uid_datas.append({'UID':str(uid), '거래량':int(uid_total)})

    uid_datas.sort(key=operator.itemgetter('UID'))

    #print(uid_datas)
    sort_userdata = pd.DataFrame(uid_datas)
    sort_userdata.to_excel(target_path)