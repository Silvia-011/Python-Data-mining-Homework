import json

#尝试request包但是解析不了本地url
'''url = "file:///E:/大学/项目/华榜/培训/Python-Data-mining-Tutorial/Week-03/中国地名表.json"
res = request.GET(url)
file = res.decode("utf-8")
file = eval(file)'''
with open("E:\\大学\\项目\\华榜\\培训\\Python-Data-mining-Tutorial\\Week-03\\中国地名表.json") as fp:
    file = json.load(fp)
city_dict = {}
i = 0

while file["root"]["name"]["province"][i]:
    pro = file["root"]["name"]["province"][i]["name"]
    city_dict[pro] = []
    q = 0
    while file["root"]["name"]["province"][i]["city"][q]:
        city_dict[pro].append(file["root"]["name"]["province"][i]["city"][q]["name"])
        q +=1
    i += 1

real_city = input("请输入想要查询的城市地名（xx市）：")

for key, value in city_dict():
    key_list.append(key)
    value_list.append(value)

real_pro = 0
for y in value_list:
    if real_city in y:
        real_pro = value_list.index(y)

if real_pro == 0:
    print("对不起，没有这个城市。")
else:
    print("上级省份为：")
    print(real_pro)
    check = 0
    print("下级地区为：")
    while file["root"]["name"]["province"][check]["name"] == real_pro:
        for q in file["root"]["name"]["province"][check]["city"]:
            if file["root"]["name"]["province"][check]["city"][q]["name"] == real_city:
                print(file["root"]["name"]["province"][check]["city"][q]["area"])