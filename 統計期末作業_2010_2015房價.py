# -*-coding=utf-8-*-
import csv

house_list = []
house_adress = []  #房屋地址
house_tr_year = []  #房屋交易年月
house_total_price = []  #房屋總價
house_unit_price = []  #房屋單位面積價格
house_unit = []  #房屋面積
house_category = []  #房屋種類
house_year = []  #房屋年紀
j_total = []  # 記錄所有j 之後要寫入檔案
with open(file = "101_1-12.csv", mode = 'r', encoding='utf-8-*-') as f:  # 讀取檔案
    line_1 = f.readlines()
for i in line_1:
    i = i.replace('\n', '')
    i = i.strip()
    j = i.split(',')
    # print(j[7])
    if j[7] == 1 or j[7] == '' or j[7] == '1 ':
        house_adress.append(j[0])
        house_tr_year.append(j[1])
        house_total_price.append(j[2])
        house_unit_price.append(j[3])
        house_unit.append(j[4])
        house_category.append(j[6])
        house_year.append(j[7])
        j_total.append(j)
    else:
        pass

# printing test
# i = 71
# print(house_adress[i], house_tr_year[i], house_total_price[i], house_unit_price[i], house_unit[i], house_category[i], house_year[i])
# print(type(house_year[i]))
# print(j_total[i])

statisitic_lens = len(house_adress)

# printing test
# for i in range(statisitic_lens):
    # print(house_adress[i], house_tr_year[i], house_total_price[i], house_unit_price[i], house_unit[i], house_category[i], house_year[i])


for i in range(statisitic_lens):
    with open('101_1-12新屋.csv', 'a', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        # 寫入一列資料
        writer.writerow(j_total[i])


# 統計期末作業_2010_2015房價

