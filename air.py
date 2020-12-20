#!usr/bin/env python
# _*_ coding:utf-8 _*_
from config import *
careinfo = [
    # 上海 => 西双版纳
    {
        'flightNo': [],
        'flightNoCheck': {},
        'data': getParams("2021-01-15", "上海", "西双版纳")
    },
    {
        'flightNo': [],
        'flightNoCheck':{},
        'data': getParams("2021-01-17", "西双版纳", "上海")
    }
]

if __name__ == '__main__':
    pool = ThreadPool(1)  # 降速
    # n = 1
    try:
        for m in range(0, 65 * 24 * 365):
            print('\n====================> ' + str(m) + "\n")
            results = pool.map(get_date, careinfo)
            time.sleep(120)
    except Exception as e:
        print(e)
    pool.close()
    pool.join()