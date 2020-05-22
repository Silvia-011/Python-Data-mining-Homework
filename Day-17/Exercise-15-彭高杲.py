import pymysql

conn = pymysql.Connect(
    host="rm-m5e63zf8ii67j7uq1zo.mysql.rds.aliyuncs.com",
    port=3306,
    user="huabang_learning",
    passwd="huabang_201904",
    db="huabang_learning",
    charset='utf8'
)
cursor = conn.cursor()
sql = "SELECT 那个好吃的叫啥, 多少钱, 在哪里吃 FROM penggaogao_tastyfood;"
cursor.execute(sql)
context = cursor.fetchall()
fp = open(r"E:\大学\项目\华榜\培训\Exercise\tasty_food.txt",'w')
loan_count = 0
for i in context:
    fp.write(str(i))
    fp.write('\n')
    loan_count += 1
fp.write("一共读取了%d条数据"%loan_count)
fp.close()
cursor.close()
conn.close()