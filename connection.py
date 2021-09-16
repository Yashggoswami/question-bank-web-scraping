import mysql.connector
import third


db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="Quizzitdb"
)

mycursor = db.cursor()




third.find_data(14)
# print(third.data)
for k, v in third.data.items():
    columns = ','.join("`"+str(x).replace('/', '_')+"`" for x in v.keys())
    values = ','.join("'"+str(x).replace('/', '_')+"'" for x in v.values())
    sql = f"Insert Into Questions ({columns}) values ({values});"
    # print(f"inserting {values}")
    try:
        mycursor.execute(sql)
    except:
        print("error aaya")
    # print(sql)
db.commit()
print("done insertion....")