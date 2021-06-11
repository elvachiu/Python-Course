import requests
import json
import datetime

# Task: 透過紫外線即時監測資料，找出近三個小時中， UVI 指數前三高的地方。


def within_3hrs(rec):
    now = datetime.datetime.now()
    record_time = rec['PublishTime'].replace('-', ' ').replace(':', ' ')
    year, month, day, hour, minute = [int(x) for x in record_time.split()]
    record_time = datetime.datetime(year, month, day, hour, minute)
    time_diff = (now - record_time).seconds
    return time_diff < 10800


res = requests.get('https://data.epa.gov.tw/api/v1/uv_s_01?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&format=json')
uvi_data = json.loads(res.text)['records']
for record in uvi_data:
    try:
        record['UVI'] = float(record['UVI'])
    except:
        record['UVI'] = 0.0

uvi_data.sort(key=lambda x: -x['UVI'])  # 由大到小排序UVI值
uvi_data = [record for record in uvi_data if within_3hrs(record)]
for record in uvi_data[:3]:
    # print(record['County'])
    print(record['SiteName'], record['UVI'])

# Task: 找出新竹市屋齡五年以下，格局至少三房，總價666萬以下的交易紀錄共有多少筆？
# Task: 符合前項規範下，依照門牌分類，找出交易量前10多的門牌。


def within_5yrs(house):
    try:
        now = datetime.datetime.now()
        five_yrs_ago = datetime.datetime(now.year-5, now.month, now.day)
        record_time = datetime.datetime(house['year'], house['month'], house['day'])
        return five_yrs_ago < record_time
    except:
        return False


res = requests.get('https://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/297/ea78465a-38e5-4b7e-9275-491b0ac966a3.json')
house_data = json.loads(res.text)
# print(house_data[0])
# 需要的keys: 鄉鎮市區 建築完成年月 建物現況格局-房 總價元
for houses in house_data:
    try:
        year = int(houses['建築完成年月'][:3])+1911
        month = int(houses['建築完成年月'][3:5])
        day = int(houses['建築完成年月'][5:])
    except:
        year, month, day = 1911, 1, 1
    room = int(houses['建物現況格局-房'])
    price = int(houses['總價元'])
    houses['year'] = year
    houses['month'] = month
    houses['day'] = day
    houses['room'] = room
    houses['price'] = price
'''
for i, houses in enumerate(house_data):
    try:
        if not within_5yrs(houses): continue
    except:
        pass
    print(houses['year'], houses['month'], houses['day'], houses['room'], houses['price'])
'''
house_data = [house for house in house_data if within_5yrs(house) and house['room'] >= 3 and house['price'] <= 6660000]
print(len(house_data))
cnt = {}
for rec in house_data:
    # print(rec['土地區段位置建物區段門牌'])
    cnt.setdefault(rec['土地區段位置建物區段門牌'], 0)
    cnt[rec['土地區段位置建物區段門牌']] += 1
# print(list(cnt.items()))
result = list(cnt.items())
result.sort(key=lambda x: -x[1])  # 由大到小排列
for addr, count in result[:10]:
    print('門牌:', addr, '門牌交易量:', count)

# Task: 透過公開資料，找出最稀有的待領養動物以及毛色前十名。

res = requests.get('https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL')
animal_data = json.loads(res.text)
# print(animal_data[0])

# keys needed: animal_kind, animal_colour
for animals in animal_data:
    try:
        kind = animals['animal_kind']
        color = animals['animal_colour']
    except:
        kind, color = '其他', '其他'
    animals['kind'] = kind
    animals['color'] = color
    # print(animals['kind'], animals['color'])

kind_cnt = {}
for rec in animal_data:
    kind_cnt.setdefault(rec['animal_kind'], 0)
    kind_cnt[rec['animal_kind']] += 1
# print(list(kind_cnt.items()))
kind_list = list(kind_cnt.items())
kind_list.sort(key=lambda x: -x[1])  # 由小到大排列
print(kind_list)

color_cnt = {}
for rec in animal_data:
    color_cnt.setdefault(rec['animal_colour'], 0)
    color_cnt[rec['animal_colour']] += 1
# print(list(color_cnt.items()))
color_list = list(color_cnt.items())
color_list.sort(key=lambda x: -x[1])  # 由大到小排列
# print(color_list)
for color, count in color_list[:10]:
    print(color, count)
'''
下載csv檔的資料處理方法
import csv
import webbrowser

with open('COA_OpenData.csv', 'r', encoding='utf8') as FILE:
    rd = csv.DictReader(FILE)
    rows = [row for row in rd]

kind_cnt = {}
for row in rows:
    kind_cnt.setdefault(row['animal_kind'], 0)
    kind_cnt[row['animal_kind']] += 1

print(kind_cnt)

colour_cnt = {}
for row in rows:
    colour_cnt.setdefault(row['animal_colour'], 0)
    colour_cnt[row['animal_colour']] += 1

colour_list = list(colour_cnt.items())
colour_list.sort(key=lambda x: -x[1])
for colour, count in colour_list[:10]:
    print(colour, count)
'''
