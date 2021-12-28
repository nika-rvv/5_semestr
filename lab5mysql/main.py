import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="first_db"
)

c=db.cursor()
c.execute("INSERT INTO faculties (name, description) VALUES (%s, %s);", ('Faculty', 'Description'))
db.commit()
c.close()
db.close()