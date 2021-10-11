from mysql import connector

mydb = connector.connect(
            host = "localhost",
            username = "root",
            password = "admin",
            database = "pythontemp"
        )

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS customers(customer_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30))")

mycursor.execute("SHOW TABLES")

print(*[x for x in mycursor])

try:
    mycursor.execute("ALTER TABLE customers ADD address VARCHAR(255)")
except:
    print("Column already exist")

mycursor.execute("DESC customers")

print(*[x for x in mycursor])

sql = "INSERT INTO customers(name,address) values(%s,%s)"

val = [
    ("Levi Ackermann","Wall Rose"),
    ("Eren Jaeger","Wall Maria"),
    ("Lalatinna","Konosuba"),
    ("Kaneki Kun","Re"),
    ("Rias Gremory","DxD"),
]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount," was inserted")

mycursor.execute("SELECT * FROM customers ORDER BY name")

result = mycursor.fetchall()

for x in result:
    print(x)

